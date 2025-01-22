import os
from backend.sim_wrapper import SimWrapper
from backend.sim_api import *
from backend.dtypes import *
from backend.trap import *

## Base report class (show a report file, show a wx.Window, etc.)
class Report:
    def Show(self):
        pass

## Simple file report.
class FileReport(Report):
    def __init__(self, filename):
        self.filename = filename

    def Show(self):
        os.system('notepad.exe {}'.format(self.filename))

## Base observer class.
class Observer:
    def BreakOnPreExecute(self):
        return True

    def BreakOnPreException(self):
        return True

    def BreakOnPostExecute(self):
        return True

    def OnPreSimulation(self, endpoint):
        pass

    def OnPreExecute(self, endpoint):
        pass

    def OnPreException(self, endpoint):
        pass

    def OnPostExecute(self, endpoint):
        pass

    def OnInfiniteLoop(self, endpoint):
        pass

    def OnSimFinished(self, endpoint):
        pass

    def OnSimulationDead(self, pc):
        pass

    def CreateReport(self):
        return None

## Simple observer which does not overwrite any AtlasState / AtlasInst values.
class SanityCheckObserver(Observer):
    def __init__(self, logfile):
        self.fout = open(logfile, 'w')
        self.logfile = logfile
        self.prev_rd_vals_by_inst_uid = {}
        self.csrs_before_exception_handling = None

    def OnPreSimulation(self, endpoint):
        starting_pc = '0x{:08x}'.format(atlas_pc(endpoint))
        self.fout.write('BEGIN SIMULATION (starting pc: {})\n'.format(starting_pc))

    def OnPreExecute(self, endpoint):
        pc = '0x{:08x}'.format(atlas_pc(endpoint))
        inst = atlas_current_inst(endpoint)
        dasm = inst.dasmString()
        kvpairs = [('pc', pc), ('dasm', dasm)]

        rs1 = inst.getRs1()
        if rs1:
            # rs1(x7):0xff
            key = 'rs1({})'.format(rs1.getName())
            val = '0x{:08x}'.format(rs1.read())
            kvpairs.append((key, val))

        rs2 = inst.getRs2()
        if rs2:
            # rs2(x7):0xff
            key = 'rs2({})'.format(rs2.getName())
            val = '0x{:08x}'.format(rs2.read())
            kvpairs.append((key, val))

        rd = inst.getRd()
        if rd:
            # rd(x7):0xff
            key = 'rd({})'.format(rd.getName())
            val = '0x{:08x}'.format(rd.read())
            kvpairs.append((key, val))

        imm = inst.getImmediate()
        if imm is not None:
            # imm:0xff
            key = 'imm'
            val = '0x{:08x}'.format(imm)
            kvpairs.append((key, val))

        # OnPreExecute (pc: 0xff, dasm: add x0, x0, x0, rs1(x0):0xff, rs2(x0):0xff, rd(x0):0xff)
        kvpairs_str = ', '.join(['{}:{}'.format(k, v) for k, v in kvpairs])
        self.fout.write('--> OnPreExecute ({})\n'.format(kvpairs_str))
        self.csrs_before_exception_handling = None

    def OnPreException(self, endpoint):
        trap_cause = atlas_inst_active_exception(endpoint)
        assert trap_cause >= 0
        cause = TRAP_CAUSES[trap_cause]

        # ----> OnPreException (cause: ILLEGAL_INSTRUCTION)
        self.fout.write('----> OnPreException (cause: {})\n'.format(cause))

        # Track CSR values before/after exception handling.
        inst = atlas_current_inst(endpoint)
        state = inst.getAtlasState()
        csr_rset = state.getCsrRegisterSet()

        self.csrs_before_exception_handling = {}
        for reg_id in range(csr_rset.getNumRegisters()):
            reg = csr_rset.getRegister(reg_id)
            if reg:
                reg_name = reg.getName()
                reg_value = reg.read()
                self.csrs_before_exception_handling[reg_name] = reg_value

    def OnPostExecute(self, endpoint):
        inst = atlas_current_inst(endpoint)
        uid = inst.getUid()

        kvpairs = []
        if uid in self.prev_rd_vals_by_inst_uid:
            rd_before = self.prev_rd_vals_by_inst_uid[uid]
            rd_after = inst.getRd().read()
            rd_before_hex = '0x{:08x}'.format(rd_before)
            rd_after_hex = '0x{:08x}'.format(rd_after)
            rd_name = inst.getRd().getName()

            # rd(x7):0xff -> 0x100
            key = 'rd({})'.format(rd_name)
            val = '{} -> {}'.format(rd_before_hex, rd_after_hex)
            kvpairs.append((key, val))

        if self.csrs_before_exception_handling is not None:
            for csr_name, before_val in self.csrs_before_exception_handling.items():
                after_val = atlas_reg_value(endpoint, csr_name)
                if before_val != after_val:
                    # mstatus:0x00000000 -> 0x00000008
                    key = csr_name
                    val = '0x{:08x} -> 0x{:08x}'.format(before_val, after_val)
                    kvpairs.append((key, val))

        # ----> OnPostExecute (rd(x7):0xff -> 0x100, mstatus:0x00000000 -> 0x00000008)
        kvpairs_str = ', '.join(['{}:{}'.format(k, v) for k, v in kvpairs])
        self.fout.write('----> OnPostExecute ({})\n'.format(kvpairs_str))
        self.csrs_before_exception_handling = None

    def OnInfiniteLoop(self, endpoint):
        pc = atlas_pc(endpoint)
        self.fout.write('----> Infinite loop detected at pc: 0x{:08x}\n'.format(pc))

    def OnSimFinished(self, endpoint):
        workload_exit_code = atlas_exit_code(endpoint)
        test_passed = atlas_test_passed(endpoint)
        inst_count = atlas_inst_count(endpoint)

        # END SIMULATION RESULTS:
        # ----> workload_exit_code: 0
        # ----> test_passed: True
        # ----> inst_count: 100
        self.fout.write('END SIMULATION RESULTS:\n')
        self.fout.write('----> workload_exit_code: {}\n'.format(workload_exit_code))
        self.fout.write('----> test_passed: {}\n'.format(test_passed))
        self.fout.write('----> inst_count: {}\n'.format(inst_count))

    def OnSimulationDead(self, pc):
        self.fout.write('----> Simulation dead at pc: 0x{:08x}\n'.format(pc))

    def CreateReport(self):
        self.close()
        return FileReport(self.logfile)

    def close(self):
        if self.fout:
            self.fout.close()
            self.fout = None

    def __del__(self):
        self.close()

## Example observer that tries to implement an instruction in Python (even though
## there is a C++ implementation, we will go around it and update register values
## in Python).
class PythonInstRewriter(Observer):
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic

    # We only want to reroute the "mul" instruction. This will be done in pre_execute only.
    def BreakOnPreException(self):
        return False

    def BreakOnPostExecute(self):
        return False

    def OnPreExecute(self, endpoint):
        insn = atlas_current_inst(endpoint)
        if insn.getMnemonic() == self.mnemonic:
            #ActionGroup* RvmInsts::mul_64_handler(atlas::AtlasState* state)
            #{
            #    const AtlasInstPtr & insn = state->getCurrentInst();
            #
            #    const uint64_t rs1_val = insn->getRs1()->dmiRead<uint64_t>();
            #    const uint64_t rs2_val = insn->getRs2()->dmiRead<uint64_t>();
            #    const uint64_t rd_val = rs1_val * rs2_val;
            #    insn->getRd()->dmiWrite(rd_val);
            #
            #    return nullptr;
            #}

            rs1_val = insn.getRs1().read()
            rs2_val = insn.getRs2().read()
            rd_val = rs1_val * rs2_val
            insn.getRd().dmiWrite(rd_val)

            # Tell Atlas to skip the C++ inst implementation.
            atlas_finish_execute(endpoint)

    def OnSimFinished(self, endpoint):
        workload_exit_code = atlas_exit_code(endpoint)
        test_passed = atlas_test_passed(endpoint)
        inst_count = atlas_inst_count(endpoint)

        print ('END SIMULATION RESULTS:')
        print ('----> workload_exit_code: {}'.format(workload_exit_code))
        print ('----> test_passed: {}'.format(test_passed))
        print ('----> inst_count: {}'.format(inst_count))

## Utility class which runs an observer on an Atlas simulation running in the background.
class ObserverSim:
    def __init__(self, riscv_tests_dir, sim_exe_path, test_name):
        self.riscv_tests_dir = riscv_tests_dir
        self.sim_exe_path = sim_exe_path
        self.test_name = test_name

    def RunObserver(self, obs):
        # You can ping the simulation as long as the SimWrapper is in scope.
        # See all the available APIs in IDE.backend.sim_api
        with SimWrapper(self.riscv_tests_dir, self.sim_exe_path, self.test_name) as sim:
            obs.OnPreSimulation(sim.endpoint)

            # Always put a pre_execute breakpoint so we can skip an instruction and
            # go right to simulation finish in the event of an infinite loop.
            atlas_break_action(sim.endpoint, 'pre_execute')

            if obs.BreakOnPreException():
                atlas_break_action(sim.endpoint, 'pre_exception')

            if obs.BreakOnPostExecute():
                atlas_break_action(sim.endpoint, 'post_execute')

            # Give the observer a chance to do something at the end of simulation.
            atlas_break_action(sim.endpoint, 'sim_finish')

            # Look at the pre_execute PC and skip the instruction to terminate
            # the simulation if the same PC is executing twice (about to go into
            # an infinite loop).
            last_pre_execute_pc = -1

            while True:
                current_action = atlas_continue(sim.endpoint)

                if current_action == 'pre_execute':
                    curr_pre_execute_pc = atlas_pc(sim.endpoint)
                    if curr_pre_execute_pc == last_pre_execute_pc:
                        obs.OnInfiniteLoop(sim.endpoint)
                        break
                    else:
                        last_pre_execute_pc = curr_pre_execute_pc

                if current_action == 'pre_execute' and obs.BreakOnPreExecute():
                    obs.OnPreExecute(sim.endpoint)
                elif current_action == 'pre_exception' and obs.BreakOnPreException():
                    obs.OnPreException(sim.endpoint)
                elif current_action == 'post_execute' and obs.BreakOnPostExecute():
                    obs.OnPostExecute(sim.endpoint)
                elif current_action == 'sim_finished':
                    obs.OnSimFinished(sim.endpoint)
                elif current_action == 'sim_dead':
                    obs.OnSimulationDead(curr_pre_execute_pc)

                if current_action in ('sim_dead', 'sim_finished'):
                    break

        return obs.CreateReport()
