import sys

reserve = {"this": "THIS", "that": "THAT", "argument": "ARG", "local": "LCL"}


def vm(command, index):
    command = command.lower().split()
    tag = str(index)
    # Arithmetic / Boolean commands
    if command[0] == 'add':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "M = D + M\n"
    elif command[0] == 'sub':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "M = M - D\n"
    elif command[0] == 'neg':
        return "@SP\n" \
               "A = M - 1\n" \
               "M = -M\n"
    elif command[0] == 'eq':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "D = M - D\n" \
               "M = -1\n" \
               "@continue" + tag + "\n" \
                                   "D; JEQ\n" \
                                   "@SP\n" \
                                   "A = M - 1\n" \
                                   "M = 0\n" \
                                   "(continue" + tag + ")\n"
    elif command[0] == 'gt':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "D = M - D\n" \
               "M = -1\n" \
               "@continue" + tag + "\n" \
                                   "D; JGT\n" \
                                   "@SP\n" \
                                   "A = M - 1\n" \
                                   "M = 0\n" \
                                   "(continue" + tag + ")\n"
    elif command[0] == 'lt':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "D = M - D\n" \
               "M = -1\n" \
               "@continue" + tag + "\n" \
                                   "D; JLT\n" \
                                   "@SP\n" \
                                   "A = M - 1\n" \
                                   "M = 0\n" \
                                   "(continue" + tag + ")\n"
    elif command[0] == 'and':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "M = D & M\n"
    elif command[0] == 'or':
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "A = A - 1\n" \
               "M = D | M\n"
    elif command[0] == 'not':
        return "@SP\n" \
               "A = M - 1\n" \
               "M = !M\n"
    # Memory access commands
    elif command[0] == 'pop':
        if command[1] in reserve:
            return "@" + reserve[command[1]] + "\n" \
                                           "D = M\n" \
                                           "@" + command[2] + "\n" \
                                                          "D = D + A\n" \
                                                          "@13\n" \
                                                          "M = D\n" \
                                                          "@SP\n" \
                                                          "AM = M - 1\n" \
                                                          "D = M\n" \
                                                          "@13\n" \
                                                          "A = M\n" \
                                                          "M = D\n"
        elif command[1] == 'temp':
            return "@" + "5" + "\n" \
                               "D = A\n" \
                               "@" + command[2] + "\n" \
                                              "D = D + A\n" \
                                              "@13\n" \
                                              "M = D\n" \
                                              "@SP\n" \
                                              "AM = M - 1\n" \
                                              "D = M\n" \
                                              "@13\n" \
                                              "A = M\n" \
                                              "M = D\n"
        elif command[1] == 'static':
            return "@" + command[1] + "\n" \
                                  "D = A\n" \
                                  "@" + command[2] + "\n" \
                                                 "D = D + A\n" \
                                                 "@13\n" \
                                                 "M = D\n" \
                                                 "@SP\n" \
                                                 "AM = M - 1\n" \
                                                 "D = M\n" \
                                                 "@13\n" \
                                                 "A = M\n" \
                                                 "M = D\n"
        elif command[1] == 'pointer':
            if command[2] == '0':
                return "@SP\n" \
                       "AM = M - 1\n" \
                       "D = M\n" \
                       "@THIS\n" \
                       "M = D\n"
            elif command[2] == '1':
                return "@SP\n" \
                       "AM = M - 1\n" \
                       "D = M\n" \
                       "@THAT\n" \
                       "M = D\n"
    elif command[0] == 'push':
        if command[1] == 'constant':
            return "@" + command[2] + "\n" \
                                  "D = A\n" \
                                  "@SP\n" \
                                  "A = M\n" \
                                  "M = D\n" \
                                  "@SP\n" \
                                  "M = M + 1\n"
        elif command[1] in reserve:
            return "@" + reserve[command[1]] + "  \n" \
                                           "D = M\n" \
                                           "@" + command[2] + "\n" \
                                                          "A = A + D\n" \
                                                          "D = M\n" \
                                                          "@SP\n" \
                                                          "A = M\n" \
                                                          "M = D\n" \
                                                          "@SP\n" \
                                                          "M = M + 1\n"

        elif command[1] == 'temp':

            return "@" + "5" + "\n" \
                               "D = A\n" \
                               "@" + command[2] + "\n" \
                                              "A = A + D\n" \
                                              "D = M\n" \
                                              "@SP\n" \
                                              "A = M\n" \
                                              "M = D\n" \
                                              "@SP\n" \
                                              "M = M + 1\n"
        elif command[1] == 'static':
            return "@" + "static" + "\n" \
                                    "D = A\n" \
                                    "@" + command[2] + "\n" \
                                                   "A = A + D\n" \
                                                   "D = M\n" \
                                                   "@SP\n" \
                                                   "A = M\n" \
                                                   "M = D\n" \
                                                   "@SP\n" \
                                                   "M = M + 1\n"
        elif command[1] == 'pointer':
            if command[2] == '0':
                return "@" + "THIS" + "\n" \
                                      "D = M\n" \
                                      "@SP\n" \
                                      "A = M\n" \
                                      "M = D\n" \
                                      "@SP\n" \
                                      "M = M + 1\n"
            elif command[2] == '1':
                return "@" + "THAT" + "\n" \
                                      "D = M\n" \
                                      "@SP\n" \
                                      "A = M\n" \
                                      "M = D\n" \
                                      "@SP\n" \
                                      "M = M + 1\n"


def virtual_machine(commands):
    result = []
    for index, command in enumerate(commands):
        str = vm(command, index)
        # if str != None:
        #     print(str)
        # else:
        #     print("None!!!!!!!!! " + command)
        result.append("//" + command + "\n")
        result.append(str)
        result.append("\n")

    return result


def remove_comment(lines):
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
            # new_line = new_line.replace(" ", "")
            without_comment.append(new_line)
    return without_comment


if __name__ == '__main__':
    # s = 'push local 4'
    #
    # print(s.split())
    # print(vm(s, 0))

    # todo
    # Input file
    input_file = sys.argv[1]
    output_file = input_file[:-3] + ".asm"
    output = open(output_file, "w")
    with open(input_file) as f:
        lines = f.readlines()
    # print(lines)

    # Remove comments
    new_lines = remove_comment(lines)

    # Run virtual machine
    result = virtual_machine(new_lines)
    for i in result:
        output.write(i)
    output.close()
    print("Asm file generated in",output_file)
