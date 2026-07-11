
"""Aseembly-Like Basic"""

class GlobalVals:

    varlist = {}
    print_buffer = ""
    input_buffer = ""

class Line:
    def __init__(self):
        self.line_number = 0
        self.label = ""
        self.opcode = ""
        self.operand = ""

def lexer(stmt):
    ptr = 0
    """string into label pointer opcode operand"""
    line_number = stmt[ptr]
    ptr += 1 
    label = ""
    if stmt[ptr][0] == "*":
        label = stmt[ptr][1:]
        ptr += 1
    opcode = stmt[ptr]
    ptr += 1
    operand = stmt[ptr]
    return line_number, label, opcode, operand

def parse(line):
    global GlobalVals
    GlobalVals.varlist[line.line_number] = line.label
    op = line.opcode
    if op == "print":
        GlobalVals.print_buffer += line.operand.replace("_"," ")
    elif op == "input":
        GlobalVals.input_buffer = input(GlobalVals.print_buffer)
        GlobalVals.print_buffer = ""
    elif op == "println":
        stg = GlobalVals.print_buffer + line.operand.replace("_"," ")
        print(stg)
        stg = ""
        GlobalVals.print_buffer = ""
        
    elif op == "data":
        pass
    elif op == "add":
        pass
    elif op == "sub":
        pass
    elif op == "subs":
        pass


def main():
    file = open('hello.albas')
    program = file.readlines()
    for current_line in program:
        stmt = current_line.replace("'"," ").replace(","," ").replace("..",",").split()
        line = Line()
        line.line_number, line.label, line.opcode, line.operand = lexer(stmt)
        parse(line)
    file.close()

if __name__ == '__main__':
    main()
