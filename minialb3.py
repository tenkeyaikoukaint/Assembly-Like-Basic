
"""Assembly-Like Basic minimum implementation"""

import sys

class VM:

    def __init__(self):
        self.program = []
        self.memory = [0 for i in range(0,256)]
        self.acc = 0
        self.counter = 0
        self.pc = 0
        self.print_buffer = ""
        self.input_buffer = ""
        self.symbols = []

class Line:
    def __init__(self):
        self.label = ""
        self.opcode = ""
        self.operand = ""

def lexer(stmt):
    ptr = 0
    """string into label opcode operand"""
    label = ""
    opcode = ""
    operand = ""
    if stmt and stmt[0].startswith("&"):
        label = stmt.pop(0).replace("&", "")
    if stmt:
        opcode = stmt.pop(0)
    if stmt:
        operand = stmt.pop(0)
    return label, opcode, operand

def parse(vm):
    op = vm.program[vm.pc].opcode
    arg = vm.program[vm.pc].operand
    if op == "print" or op == "print*":
        # vm.print_buffer += vm.program[vm.pc].operand.replace("_"," ")
        print(f"{vm.acc}")
    elif op == "prints" or op == "prints*+":
        vm.print_buffer = ""
        for i in range(vm.acc):
            vm.print_buffer += chr(vm.memory[vm.counter])
            count(vm, 1)
        print(vm.print_buffer)
    elif op == "input" or op == "input*":
        # vm.input_buffer = input(vm.print_buffer)
        num = input()
        vm.acc = int(num)
    elif op == "inputs" or op == "inputs*+":
        string = input()
        length = min(vm.acc, len(string))
        for i in range(length):
            vm.memory[vm.counter] = ord(string[i])
            count(vm, 1)
    elif op == "store" or op == "store+":
        vm.memory[vm.counter] = int(arg)
    elif op == "stores" or op == "stores*+":
        length = min(vm.acc, len(arg))
        for i in range(length):
            vm.memory[vm.counter] = ord(arg[i])
            count(vm, 1)
    elif op == "load" or op == "load*":
         vm.acc = int(arg)
    elif op == "set" or op == "set+":
         vm.counter = int(arg) % 256
    elif op == "add" or op == "add*+":
        vm.acc += vm.memory[vm.counter]
    elif op == "sub" or op == "sub*+":
        vm.acc -= vm.memory[vm.counter]
    elif op == "inc" or op == "inc+":
        count(vm, 1)
    elif op == "dec" or op == "dec+":
        count(vm, -1)
    elif op == "cinc" or op == "cinc*+":
        if vm.acc == int(arg):
            count(vm, 1)
    elif op == "cdec" or op == "cdec*+":
        if vm.acc == int(arg):
            count(vm, -1)
    elif op == "jpnz" or op == "jpnz+":
        if vm.counter != 0:
            vm.pc = labeltolinenum(vm, arg)-1
    elif op == "call" or op == "call+":
         vm.memory[vm.counter] = vm.pc
         count(vm, 1)
         vm.pc = labeltolinenum(vm, arg)-1
    elif op == "ret" or op == "ret+":
         count(vm, -1)
         vm.pc = vm.memory[vm.counter]

def count(vm, arg):
    vm.counter = max(0, min(255, vm.counter + arg))

def labeltolinenum(vm, label):
    code = vm.program
    linenum = 0
    for i in range(0, len(code)):
        if code[i].label == label:
            linenum = i
    return linenum

def main():
    vm = VM()
    file = open(sys.argv[1])
    source = file.readlines()
    for current_line in source:
        stmt = current_line.replace("'"," ").replace(","," ").replace("..",",").replace(":"," ").split()
        line = Line()
        if len(stmt) > 0:
            line.label, line.opcode, line.operand = lexer(stmt)
            vm.program.append(line)
    while vm.pc <len(vm.program):
        """
        print(f"pc:{vm.pc}")
        print(f"{vm.program[vm.pc]}")
        print(vm.symbols)
        print(f"counter:{vm.counter}")
        """
        parse(vm)
        vm.pc += 1
        if vm.pc >= len(vm.program):
            break
    file.close()

if __name__ == '__main__':
    main()
