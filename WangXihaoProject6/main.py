import sys

comp_table = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    '!D': '0001101',
    '!A': '0110001',
    '-D': '0001111',
    '-A': '0110011',
    'D+1': '0011111',
    '1+D': '0011111',
    'A+1': '0110111',
    '1+A': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'A+D': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'A&D': '0000000',
    'D|A': '0010101',
    'A|D': '0010101',
    'M': '1110000',
    '!M': '1110001',
    '-M': '1110011',
    'M+1': '1110111',
    '1+M': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'M+D': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'M&D': '1000000',
    'D|M': '1010101',
    'M|D': '1010101'
}
dest_table = {
    None: '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111'
}
jump_table = {
    None: '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'
}
symbol_table = {
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
    'SCREEN': 16384,
    'KBD': 24576,
}

symbol_p = 16


def remove_comment_space(lines):
    without_comment = []
    slash_star = False
    i = 0
    for line in lines:
        i += 1
        # line = line.replace(" ", "")
        line = line.strip()
        if line == '':
            continue
        new_line = ''
        for index, char in enumerate(line):
            if char == '/' and line[index + 1] == '*':
                slash_star = True
            elif char == '/' and line[index - 1] == '*':
                slash_star = False
                break
            elif char == '/' and line[index + 1] == '/':
                if index != 0:
                    new_line = new_line + '\n'
                break
            elif slash_star == False:
                new_line = new_line + char

        # print(i, new_line, end='')
        # output.write(new_line)
        if new_line != '':
            new_line = new_line.strip()
            new_line = new_line.replace(" ", "")
            without_comment.append(new_line)
    return without_comment


def find_labels(lines):
    # for index, line in enumerate(lines):
    #     if line[0] == '(':
    #         symbol = line[1:-1]
    #         symbol_table[symbol] = index
    #         lines.pop(index)
    index = 0
    while index < len(lines):
        line = lines[index]
        if line[0] == '(':
            symbol = line[1:-1]
            symbol_table[symbol] = index
            lines.pop(index)
        else:
            index += 1


def parse_a_instructions(instruction):
    global symbol_p
    # if the line is @ xxx,
    addr = instruction[1:]
    if addr.isdigit():  # where xxx is a number, pretty simple
        addr = int(addr)
    else:  # where xxx is a symbol, look it up in the symbol table
        if addr[0] == 'R' and addr[1:].isdigit():
            addr = int(addr[1:])
        elif addr in symbol_table:
            addr = symbol_table[addr]
        else:
            symbol_table[addr] = symbol_p
            addr = symbol_p
            symbol_p += 1
    binary_addr = bin(addr)[2:]
    l = len(binary_addr)
    for i in range(16 - l):
        binary_addr = '0' + binary_addr
    return binary_addr


def parse_c_instructions(instruction):
    equal_sign = instruction.find('=')
    if equal_sign == -1:
        dest = None
    else:
        dest = instruction[:equal_sign]
        dest = dest.strip()
    semicolo_sign = instruction.find(';')
    if semicolo_sign == -1:
        jump = None
        comp = instruction[equal_sign + 1:]
    else:
        jump = instruction[semicolo_sign + 1:]
        jump = jump.strip()
        comp = instruction[equal_sign + 1:semicolo_sign]
    comp = comp.strip()
    C_Ins = '111' + comp_table[comp] + dest_table[dest] + jump_table[jump]
    return C_Ins


def parse_instructions(line):
    if line[0] == '@':
        return parse_a_instructions(line)
    else:
        # if the line is a C-instruction, do some lookups (dest, comp, jump)
        return parse_c_instructions(line)


if __name__ == '__main__':

    input_file = sys.argv[1]
    output_file = input_file[:-4] + ".hack"
    output = open(output_file, "w")
    with open(input_file) as f:
        lines = f.readlines()

    # First pass:
    # 1. Clear out white space
    # 2. Remove comments
    new_lines = remove_comment_space(lines)

    # Second pass:
    # Parse for “(“ label name “)”
    # Put in symbol table with the address of line number (think about this...it’s for jumping the PC)
    # Remove line; this will affect line number of subsequent symbols
    find_labels(new_lines)  #

    # Third pass: go through program again and translate each line:
    # if the line is a C-instruction, do some lookups (dest, comp, jump)
    for line in new_lines:
        binary_code = parse_instructions(line)
        output.write(binary_code + '\n')
    output.close()
    print("Hack file generated in",output_file)

