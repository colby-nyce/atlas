RV32I_INST = [
    {'mnemonic': 'sll', 'handler': 'sll_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srl', 'handler': 'srl_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sra', 'handler': 'sra_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slli', 'handler': 'slli_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srli', 'handler': 'srli_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srai', 'handler': 'srai_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'add', 'handler': 'add_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sub', 'handler': 'sub_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'and', 'handler': 'and_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'or', 'handler': 'or_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'xor', 'handler': 'xor_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mv', 'handler': 'addi_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'addi', 'handler': 'addi_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'li', 'handler': 'li_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'andi', 'handler': 'andi_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ori', 'handler': 'ori_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'xori', 'handler': 'xori_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lui', 'handler': 'lui_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'auipc', 'handler': 'auipc_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slt', 'handler': 'slt_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sltu', 'handler': 'sltu_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slti', 'handler': 'slti_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sltiu', 'handler': 'sltiu_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'beq', 'handler': 'beq_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bne', 'handler': 'bne_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'blt', 'handler': 'blt_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bltu', 'handler': 'bltu_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bge', 'handler': 'bge_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bgeu', 'handler': 'bgeu_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'jal', 'handler': 'jal_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'jalr', 'handler': 'jalr_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lb', 'handler': 'lb_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lbu', 'handler': 'lbu_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lh', 'handler': 'lh_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lhu', 'handler': 'lhu_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lw', 'handler': 'lw_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sb', 'handler': 'sb_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sh', 'handler': 'sh_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sw', 'handler': 'sw_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'nop', 'handler': 'nop', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'fence', 'handler': 'nop', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ecall', 'handler': 'ecall', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ebreak', 'handler': 'ebreak', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mret', 'handler': 'mret_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sret', 'handler': 'sret_32', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sfence.vma', 'handler': 'sfence_vma', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'wfi', 'handler': 'wfi', 'cost': 1, 'tags': 'BASE_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sllw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srlw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sraw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slliw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srliw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sraiw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'addw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'subw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'addiw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ld', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lwu', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sd', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'divw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'divuw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'remw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'remuw', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lr.d', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': True, 'crypto': False},
    {'mnemonic': 'sc.d', 'handler': 'invalid', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': True, 'crypto': False},
]

RV64I_INST = [
    {'mnemonic': 'sll', 'handler': 'sll_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sllw', 'handler': 'sll_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srl', 'handler': 'srl_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srlw', 'handler': 'srl_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sra', 'handler': 'sra_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sraw', 'handler': 'sra_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slli', 'handler': 'slli_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slliw', 'handler': 'slli_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srli', 'handler': 'srli_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srliw', 'handler': 'srli_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'srai', 'handler': 'srai_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sraiw', 'handler': 'srai_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'add', 'handler': 'add_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mv', 'handler': 'addi_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'addw', 'handler': 'add_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sub', 'handler': 'sub_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'subw', 'handler': 'sub_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'and', 'handler': 'and_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'or', 'handler': 'or_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'xor', 'handler': 'xor_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'addi', 'handler': 'addi_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'li', 'handler': 'li_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'addiw', 'handler': 'addi_32', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'andi', 'handler': 'andi_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ori', 'handler': 'ori_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'xori', 'handler': 'xori_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lui', 'handler': 'lui_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'auipc', 'handler': 'auipc_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slt', 'handler': 'slt_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sltu', 'handler': 'sltu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'slti', 'handler': 'slti_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sltiu', 'handler': 'sltiu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'beq', 'handler': 'beq_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bne', 'handler': 'bne_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'blt', 'handler': 'blt_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bltu', 'handler': 'bltu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bge', 'handler': 'bge_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'bgeu', 'handler': 'bgeu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'jal', 'handler': 'jal_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'jalr', 'handler': 'jalr_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lb', 'handler': 'lb_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lbu', 'handler': 'lbu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lh', 'handler': 'lh_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lhu', 'handler': 'lhu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lw', 'handler': 'lw_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'lwu', 'handler': 'lwu_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ld', 'handler': 'ld_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sb', 'handler': 'sb_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sh', 'handler': 'sh_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sw', 'handler': 'sw_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sd', 'handler': 'sd_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': True, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'fence', 'handler': 'nop', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ecall', 'handler': 'ecall', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'ebreak', 'handler': 'ebreak', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mret', 'handler': 'mret_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sret', 'handler': 'sret_64', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': True, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'sfence.vma', 'handler': 'sfence_vma', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'wfi', 'handler': 'wfi', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'nop', 'handler': 'nop', 'cost': 1, 'tags': 'BASE_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
]
