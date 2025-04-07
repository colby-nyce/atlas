import os, subprocess, sys
from backend.atlas_dtypes import JsonConverter
from backend.sim_api import BrokenPipeResponse

# This class is to be used as follows:
#
#   with SimWrapper(riscv_tests_dir, sim_exe_path, test_name) as sim:
#       ...
#
# The sim object will be used to interact with the simulator, and the
# C++ simulation is running for as long as the 'with' block is active.
# See IDE.backend.sim_api for the available Python <--> C++ APIs.
class SimWrapper:
    def __init__(self, riscv_tests_dir, sim_exe_path, test_name):
        self.riscv_tests_dir = riscv_tests_dir
        self.sim_exe_path = sim_exe_path
        self.test_name = test_name
        self.return_dir = os.getcwd()
        self.endpoint = SimEndpoint()

    def UnscopedEnter(self):
        riscv_tests_dir = os.path.abspath(self.riscv_tests_dir)
        os.chdir(os.path.dirname(self.sim_exe_path))
        program_path = "./atlas"

        program_args = ["--interactive"]
        if self.test_name.startswith('rv32'):
            program_args.extend(["-p", "top.core0.params.isa_string", "rv32g_zicsr_zifencei"])
        else:
            program_args.extend(["-p", "top.core0.params.isa_string", "rv64g_zicsr_zifencei"])

        program_args.append(f"{riscv_tests_dir}/{self.test_name}")
        return self if self.endpoint.start_server(program_path, *program_args) else None

    def UnscopedExit(self):
        if self.endpoint.process:
            self.endpoint.close()
        os.chdir(self.return_dir)

    def __enter__(self):
        return self.UnscopedEnter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.UnscopedExit()

# This class runs an Atlas simulation in the background and provides basic
# low-level communication with the simulator.
class SimEndpoint:
    def __init__(self):
        self.process = None

    def start_server(self, program_path, *program_args):
        self.process = subprocess.Popen(
            [program_path, *program_args],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )

        ide_ready = False
        while not ide_ready:
            response = self.__receive().strip()
            if response == 'ATLAS_IDE_READY':
                ide_ready = True

        if not ide_ready:
            self.close()

        if self.process:
            print ('Started simulator with PID ' + str(self.process.pid))

        return self.process is not None

    def request(self, request, broken_pipe_return=None):
        try:
            self.__send(request)
        except BrokenPipeError:
            return BrokenPipeResponse() if broken_pipe_return is None else broken_pipe_return

        response = None
        while response is None:
            recvd = self.__receive()
            if recvd == '':
                return ''

            # To parse the response to the request we just asked, get the last ATLAS_IDE_RESPONSE
            # that we see from the C++ simulator's stdout.
            #
            #        Preparing to run...
            #        Meta-Parameters:
            #        architecture: NONE
            #        is_final_config: false
            #        Non-default model parameters: 1
            #        Running...
            #        Running Complete
            #        Simulation Performance      : wall(0.0260), system(0.0000), user(0.0200)
            #        Scheduler Tick Rate  (KTPS): 1976.45  (1k ticks per second)
            #        Scheduler Event Rate (KEPS): 13608.8 KEPS (1k events per second)
            #        Scheduler Events Fired: 272176
            #        Run Successful!
            #   |--> ATLAS_IDE_RESPONSE: {"response_code":"ok","response_payload":null}
            #   |
            #   |--- This is all we care about.
            if recvd.find('ATLAS_IDE_RESPONSE: ') != -1:
                response = recvd.split('ATLAS_IDE_RESPONSE: ')[1].strip()

        return JsonConverter.ConvertResponse(response)

    def close(self):
        if self.process:
            print ('Closing simulator with PID ' + str(self.process.pid))
            self.process.terminate()
            self.process.wait()
            self.process = None

    def __send(self, message):
        self.process.stdin.write(message.strip() + '\n')
        self.process.stdin.flush()

    def __receive(self):
        return self.process.stdout.readline().strip()
