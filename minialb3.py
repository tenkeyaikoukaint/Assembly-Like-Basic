
"""Assembly-Like Basic standard implementation"""

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
    if stmt[ptr].startswith("&"):
        label = stmt[ptr].replace("&","")
        if len(stmt)>=2:
            ptr += 1
    if len(stmt)>=1:
        opcode = stmt[ptr]
        if len(stmt)>=1:
            opcode = stmt[ptr]
        if len(stmt) >= 2:
            ptr += 1
            operand = stmt[ptr]
    return label, opcode, operand

def parse(line):
    global Vals
    op = line.opcode
    argin = Vals.counter
    argout = line.operand
    if op == "print" or op == "print*":
        # Vals.print_buffer += line.operand.replace("_"," ")
        print(f"{Vals.acc}")
    elif op == "prints" or op == "prints*+":
        Vals.print_buffer = ""
        for i in range(0,Vals.acc):
            Vals.print_buffer += chr(Vals.memory[Vals.counter])
            Vals.counter += 1
        print(Vals.print_buffer)
    elif op == "input" or op == "input*":
        Vals.input_buffer = input(Vals.print_buffer)
        Vals.print_buffer = ""
    elif op == "inputs" or op == "inputs*+":
        pass
    elif op == "store" or op == "store+":
        Vals.memory[Vals.counter] = ord(line.operand[i])
    elif op == "stores" or op == "stores*+":
        for i in range(0,Vals.acc):
            Vals.memory[Vals.counter] = ord(line.operand[i])
            Vals.counter +=1
    elif op == "load" or op == "load*":
         Vals.acc = int(argout)
    elif op == "set" or op == "set+":
         Vals.counter = int(argout)
    elif op == "add" or op == "add*":
        Vals.acc += int(argout)
    elif op == "sub" or op == "sub*":
        Vals.acc -= int(argout)
    elif op == "inc" or op == "inc+":
        Vals.counter += 1
    elif op == "dec" or op == "dec+":
        Vals.counter -= 1
    elif op == "cinc" or op == "cinc*+":
        if Vals.acc == arg:
            Vals.counter += 1
    elif op == "cdec" or op == "cdec*+":
        if Vals.acc == arg:
            Vals.counter -= 1
    elif op == "jpnz" or op == "jpnz+":
        if Vals.counter != 0:
            Vals.pc = labeltolinenum(line.operand)

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
