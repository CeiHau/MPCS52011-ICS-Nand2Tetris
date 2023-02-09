import sys
import os

reserve = {"this": "THIS", "that": "THAT", "argument": "ARG", "local": "LCL"}

return_index = 0


def vm(command, index, curr_class):
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
            return "@" + curr_class + command[1] + command[2] + "\n" + \
                   "D = A\n" \
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
            return "@" + curr_class + "static" + command[2] + "\n" + \
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
    # Program flow commands
    elif command[0] == 'label':
        return "(" + command[1] + ")\n"
    elif command[0] == 'goto':
        return "@" + command[1] + "\n" \
                                  "0;JMP\n"
    elif command[0] == "if-goto":
        return "@SP\n" \
               "AM = M - 1\n" \
               "D = M\n" \
               "@" + command[1] + "\n" \
                                  "D;JNE\n"

    # Function calling commands
    elif command[0] == 'function':
        if command[2] != '0':
            return initial_func(command[1], command[2])
        else:
            return "(" + command[1] + ")\n"
    elif command[0] == 'return':
        return return_func()
    elif command[0] == 'call':
        return call_func(command[1], command[2])


def initial_func(func_name, n_vars):
    # Initialize n local variables
    label = "init_" + func_name + n_vars
    initial_command = "(" + func_name + ")\n" + \
                      "\n//Initialize function\n" + \
                      "@" + n_vars + "\n" + \
                      "D = A\n" + \
                      "(" + label + ")\n" + \
                      "@SP\n" + \
                      "A = M\n" + \
                      "M = 0\n" + \
                      "@SP\n" + \
                      "M = M + 1\n" + \
                      "D = D - 1\n" + \
                      "@" + label + "\n" + \
                      "D;JNE\n"
    return initial_command


def return_func():
    # return command
    # FRAME = LCL
    return_command = "// FRAME = LCL\n" \
                     "@LCL\n" + \
                     "D = M\n" + \
                     "@FRAME\n" + \
                     "M = D\n"
    # RET = *(FRAME - 5)
    return_command += "\n// RET = *(FRAME - 5)\n" \
                      "@FRAME\n" + \
                      "D = M\n" + \
                      "@5\n" + \
                      "A = D - A\n" + \
                      "D = M\n" + \
                      "@RET\n" + \
                      "M = D\n"
    # *ARG = pop()
    return_command += "\n // *ARG = pop()\n" \
                      "@SP\n" + \
                      "AM = M - 1\n" + \
                      "D = M\n" + \
                      "@ARG\n" + \
                      "A = M\n" + \
                      "M = D\n"

    # SP = ARG + 1
    return_command += "\n // SP = ARG + 1\n" \
                      "@ARG\n" + \
                      "D = M + 1\n" + \
                      "@SP\n" + \
                      "M = D\n"

    # THAT = *(FRAME - 1)
    return_command += "\n// THAT = *(FRAME - 1)\n" \
                      "@FRAME\n" + \
                      "A = M - 1\n" \
                      "D = M\n" \
                      "@THAT\n" \
                      "M = D\n"

    # THIS = *(FRAME - 2)
    return_command += "\n // THIS = *(FRAME - 2)\n" \
                      "@2\n" \
                      "D = A\n" \
                      "@FRAME\n" \
                      "A = M - D\n" \
                      "D = M\n" \
                      "@THIS\n" \
                      "M = D\n"
    # ARG = *(FRAME - 3)
    return_command += "\n // ARG = *(FRAME - 3)\n" \
                      "@3\n" \
                      "D = A\n" \
                      "@FRAME\n" \
                      "A = M - D\n" \
                      "D = M\n" \
                      "@ARG\n" \
                      "M = D\n"
    # LCL = *(FRAME - 4)
    return_command += "\n// LCL = *(FRAME - 4)\n" \
                      "@4\n" \
                      "D = A\n" \
                      "@FRAME\n" \
                      "A = M - D\n" \
                      "D = M\n" \
                      "@LCL\n" \
                      "M = D\n"
    # goto RET
    return_command += "\n// goto RET\n" \
                      "@RET\n" \
                      "A = M\n" \
                      "0;JMP\n"
    return return_command


def call_func(func_name, nargs):
    global return_index
    return_addr = "RETURN_ADRESS_" + str(return_index)
    return_index += 1
    # push return-address
    call_command = "\n// push return-address\n" + \
                   "@" + return_addr + "\n" + \
                   "D = A\n" + \
                   "@SP\n" + \
                   "A = M\n" + \
                   "M = D\n" + \
                   "@SP\n" + \
                   "M = M + 1\n"
    # push LCL, ARG, THIS, THAT
    mem_lst = ["LCL", "ARG", "THIS", "THAT"]
    for mem in mem_lst:
        call_command += "\n// push " + mem + "\n" + \
                        "@" + mem + "\n" + \
                        "D = M\n" \
                        "@SP\n" \
                        "AM = M + 1\n" \
                        "A = A -1\n" \
                        "M = D\n"
    # ARG = SP - n - 5
    call_command += "\n// ARG = SP - n - 5\n" + \
                    "@SP\n" \
                    "D = M\n" \
                    "@5\n" \
                    "D = D -A\n" \
                    "@" + nargs + "\n" + \
                    "D = D - A\n" \
                    "@ARG\n" \
                    "M = D\n"
    # LCL = SP
    call_command += "\n// LCL = SP\n" \
                    "@SP\n" \
                    "D = M\n" \
                    "@LCL\n" \
                    "M = D\n"

    # goto f
    call_command += "\n// goto f\n" \
                    "@" + func_name + "\n" + \
                    "0;JMP\n"

    # set return address
    call_command += "\n// set return address\n" \
                    "(" + return_addr + ")\n"
    return call_command


def bootstrap():
    # set set SP to 256
    bootstrap_code = "//-----------------------------------bootstrap-----------------------------------\n"
    bootstrap_code += "// set set SP to 256\n" \
                      "@256\n" \
                      "D = A\n" \
                      "@SP\n" \
                      "M = D\n"
    # call Sys.init 0
    bootstrap_code += call_func("sys.init", "0")
    return bootstrap_code


def virtual_machine(commands, curr_class):
    result = []
    for index, command in enumerate(commands):
        code = vm(command, index, curr_class)
        # if code != None:
        #     print(code)
        # else:
        #     print("None!!!!!!!!! " + command)
        result.append("//" + command + "\n")
        result.append(code)
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
            elif not slash_star:
                new_line = new_line + char

        # print(i, new_line, end='')
        # output.write(new_line)
        if new_line != '':
            new_line = new_line.strip()
            # new_line = new_line.replace(" ", "")
            without_comment.append(new_line)
    return without_comment


def file_pipeline(argument):
    if os.path.isdir(argument):
        output_file_name = os.path.basename(argument) + ".asm"
        output_path = os.path.join(argument, output_file_name)

        file_name_lst = [name for name in os.listdir(argument) if name[-2:] == 'vm']
        file_path_lst = [os.path.join(argument, filename) for filename in file_name_lst]

        output = open(output_path, "w")
        output.write(bootstrap())
    elif os.path.isfile(argument):
        output_path = argument[:-3] + ".asm"
        file_path_lst = [argument]
        file_name_lst = [os.path.basename(argument)]
        output = open(output_path, "w")

    else:
        print("Input should be a path or filename\n")
        return None
    return file_path_lst, file_name_lst, output, output_path


if __name__ == '__main__':

    file_path_lst, file_name_lst, output, output_path = file_pipeline(sys.argv[1])

    # generate asm file
    for i in range(len(file_path_lst)):
        output.write(
            "\n//-----------------------------------" + file_name_lst[i] + "-----------------------------------\n")

        with(open(file_path_lst[i])) as f:
            print("Translate the "+file_name_lst[i])
            curr_class = file_name_lst[i][:-2]
            vm_code = f.readlines() #get the vm code
            new_vm_code = remove_comment(vm_code)   # remove comment
            asm_code = virtual_machine(new_vm_code, curr_class) # generate asm code
            for line in asm_code:
                output.write(line)

    output.close()
    print("\nGenerate the " + os.path.basename(output_path)+", on the following path\n"+output_path)
    # # todo
    # # Input file
    # input_file = sys.argv[1]
    # output_file = input_file[:-3] + ".asm"
    # output = open(output_file, "w")
    #
    # with open(input_file) as f:
    #     lines = f.readlines()
    # # print(lines)
    #
    # # Remove comments
    # new_lines = remove_comment(lines)
    #
    # # Run virtual machine
    # result = virtual_machine(new_lines)
    # for i in result:
    #     output.write(i)
    # output.close()
    # print("Asm file generated in", output_file)
