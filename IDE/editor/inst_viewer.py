import wx
from backend.sim_api import *
from backend.atlas_dtypes import *
from backend.observers import *

class InstViewer(wx.Panel):
    def __init__(self, parent, frame, workspace):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('green')
        self.frame = frame
        self.workspace = workspace
        self.inst_editor = workspace.inst_editor

        mono10 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, 'Consolas')
        self.inst_list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.inst_list_ctrl.SetFont(mono10)
        self.insts_by_pc = {}

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.inst_list_ctrl, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()

    def LoadTest(self, test):
        self.inst_list_ctrl.ClearAll()
        self.inst_list_ctrl.InsertColumn(0, "PC")
        self.inst_list_ctrl.InsertColumn(1, "Disasm")
        self.insts_by_pc = {}

        class InstSnooper(Observer):
            def __init__(self, insts_by_pc):
                Observer.__init__(self)
                self.insts = []
                self.insts_by_pc = insts_by_pc
                self.infinite_loop_pc = None

            def OnPreExecute(self, endpoint):
                pc = atlas_pc(endpoint)
                inst = atlas_current_inst(endpoint)
                dasm = inst.dasmString()
                self.insts.append((hex(pc), dasm))
                self.insts_by_pc[hex(pc)] = inst.deepCopy()

            def OnSimulationStuck(self, endpoint):
                self.infinite_loop_pc = atlas_pc(endpoint)

        riscv_tests_dir = self.frame.riscv_tests_dir
        sim_exe_path = self.frame.sim_exe_path
        obs_sim = ObserverSim(riscv_tests_dir, sim_exe_path, test)

        obs = InstSnooper(self.insts_by_pc)
        obs_sim.RunObserver(obs)

        for pc, dasm in obs.insts:
            i = self.inst_list_ctrl.GetItemCount()
            self.inst_list_ctrl.InsertItem(i, pc)
            self.inst_list_ctrl.SetItem(i, 1, dasm)

        if obs.infinite_loop_pc:
            i = self.inst_list_ctrl.GetItemCount()
            self.inst_list_ctrl.InsertItem(i, hex(obs.infinite_loop_pc))
            self.inst_list_ctrl.SetItem(i, 1, "Infinite loop detected")

        self.inst_list_ctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.inst_list_ctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)

        # Set our size to be the minimum size needed to show all items
        colwidth0 = self.inst_list_ctrl.GetColumnWidth(0)
        colwidth1 = self.inst_list_ctrl.GetColumnWidth(1)
        minwidth = colwidth0 + colwidth1 + 10
        self.inst_list_ctrl.SetSize((minwidth, wx.DisplaySize()[1]))

        self.inst_list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.__OnItemSelected)
        self.Layout()

        # Select the first item
        self.inst_list_ctrl.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

    def __OnItemSelected(self, event):
        row = event.GetIndex()
        pc = self.inst_list_ctrl.GetItemText(row, 0)
        if pc not in self.insts_by_pc:
            return

        inst = self.insts_by_pc[pc]
        self.inst_editor.LoadInst(pc, inst)
