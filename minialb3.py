
"""Assembly-Like Basic minimum implementation"""

import sys

class Vals:

    program = []
    memory = [0 for i in range(0,256)]
    acc = 0
    counter = 0
    pc = 0
    print_buffer = ""
    input_buffer = ""
    symbols = []

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

def parse(line):
    global Vals
    op = line.opcode
    arg = line.operand
    if op == "print" or op == "print*":
        # Vals.print_buffer += line.operand.replace("_"," ")
        print(f"{Vals.acc}")
    elif op == "prints" or op == "prints*+":
        Vals.print_buffer = ""
        for i in range(0,Vals.acc):
            Vals.print_buffer += chr(Vals.memory[Vals.counter])
            count(1)
        print(Vals.print_buffer)
    elif op == "input" or op == "input*":
        # Vals.input_buffer = input(Vals.print_buffer)
        num = input()
        Vals.acc = int(num)
    elif op == "inputs" or op == "inputs*+":
        string = input()
        for i in range(0, Vals.acc):
            if Vals.acc <= len(string):
               Vals.memory[Vals.counter] = ord(string[i])
               count(1)
    elif op == "store" or op == "store+":
        Vals.memory[Vals.counter] = int(arg)
    elif op == "stores" or op == "stores*+":
        for i in range(0,Vals.acc):
            if Vals.acc <= len(arg):
                Vals.memory[Vals.counter] = ord(arg[i])
                count(1)
    elif op == "load" or op == "load*":
         Vals.acc = int(arg)
    elif op == "set" or op == "set+":
         Vals.counter = int(arg) % 256
    elif op == "add" or op == "add*+":
        Vals.acc += Vals.memory[Vals.counter]
    elif op == "sub" or op == "sub*+":
        Vals.acc -= Vals.memory[Vals.counter]
    elif op == "inc" or op == "inc+":
        count(1)
    elif op == "dec" or op == "dec+":
        count(-1)
    elif op == "cinc" or op == "cinc*+":
        if Vals.acc == int(arg):
            count(1)
    elif op == "cdec" or op == "cdec*+":
        if Vals.acc == int(arg):
            count(-1)
    elif op == "jpnz" or op == "jpnz+":
        if Vals.counter != 0:
            Vals.pc = labeltolinenum(arg)-1
    elif op == "call" or op == "call+":
         Vals.memory[Vals.counter] = Vals.pc
         count(1)
         Vals.pc = labeltolinenum(arg)-1
    elif op == "ret" or op == "ret+":
         count(-1)
         Vals.pc = Vals.memory[Vals.counter]

def count(arg):
    if arg>= 0:
        if Vals.counter < 255:
            Vals.counter += arg:
    else:
        if Vals.counter > 0:
            Vals.counter += arg

def labeltolinenum(label):
    code = Vals.program
    linenum = 0
    for i in range(0, len(code)):
        if code[i].label == label:
            linenum = i
    return linenum

def main():
    global Vals
    file = open(sys.argv[1])
    source = file.readlines()
    for current_line in source:
        stmt = current_line.replace("'"," ").replace(","," ").replace("..",",").replace(":"," ").split()
        line = Line()
        if len(stmt) > 0:
            line.label, line.opcode, line.operand = lexer(stmt)
            Vals.program.append(line)
    while True:
        """
        print(f"pc:{Vals.pc}")
        print(f"{Vals.program[Vals.pc]}")
        print(Vals.symbols)
        print(f"counter:{Vals.counter}")
        """
        parse(Vals.program[Vals.pc])
        Vals.pc += 1
        if Vals.pc >=len(Vals.program):
            break
    file.close()

if __name__ == '__main__':
    main()
