import sys
import os
import Analyzer

def remove_comment(lines):
    without_comment = []
    slash_star = False
    i = 0
    for line in lines:
        i += 1
        # line = line.replace(" ", "")
        # print(line)
        line = line.strip()
        if line == '':
            continue
        new_line = ''
        for index, char in enumerate(line):
            if index + 1 < len(line) and char == '/' and line[index + 1] == '*':
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
        output_folder = argument + '/my_xml_code'
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        # output_file_name = os.path.basename(argument) + ".xml"
        # output_path = os.path.join(argument, output_file_name)

        file_name_lst = [name for name in os.listdir(argument) if name[-4:] == 'jack']
        file_path_lst = [os.path.join(argument, filename) for filename in file_name_lst]
        output_path_lst_Txml = [os.path.join(output_folder, filename[:-5] + 'T.xml') for filename in file_name_lst]
        output_path_lst_xml = [os.path.join(output_folder, filename[:-5] + '.xml') for filename in file_name_lst]


    else:
        print("Input should be a path \n")
        return None
    return file_path_lst, file_name_lst, output_path_lst_Txml, output_path_lst_xml


if __name__ == '__main__':
    # todo
    file_path_lst, file_name_lst, output_path_lst_Txml, output_path_lst_xml = file_pipeline(sys.argv[1])
    for i in range(len(file_path_lst)):
        output_Txml = open(output_path_lst_Txml[i], "w")
        output_xml = open(output_path_lst_xml[i], "w")
        with open(file_path_lst[i]) as f:
            jack_code = remove_comment(f.readlines())
            # tokenize
            tokenize_xml_str, tokenize_xml_lst = Analyzer.tokens(jack_code)
            output_Txml.write(tokenize_xml_str)

            # parser
            analyzer = Analyzer.Parser(tokenize_xml_lst)
            analyzer.compile_class()
            output_xml.write(analyzer.output)
        f.close()
        output_Txml.close()
        output_xml.close()
    print("xml files generate in:\n "+sys.argv[1] + '/my_xml_code')
