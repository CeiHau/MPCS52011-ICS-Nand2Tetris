import re

pattern = "(\{|\}|\(|\)|\[|\]|\.|\,|\;|\+|\-|\*|\/|\&|\||\<|\>|\=|\~| )"
jack_keyword = {
    'class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
    'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'

}
jack_symbol = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'}
xml_symbol = {'<': '&lt;', '>': '&gt;', '&': '&amp;'}

op = {"+", "-", "*", "/", "|", "&lt;", "&gt;", '&amp;', "="}
unary_op = {"-", "~"}


def tokenizer(code_line):
    output = ""
    xml_output = []
    code_words = re.split(re.compile(pattern), code_line)
    string_tag = False
    for word in code_words:
        if len(word) != 0:
            if string_tag == True:
                if word[-1] == '"':
                    string_tag = False
                    if len(word) != 1:
                        string_constant += word[:-1]
                    output += "<stringConstant> " + string_constant + " </stringConstant>\n"
                    xml_output.append("<stringConstant> " + string_constant + " </stringConstant>\n")
                else:
                    string_constant += word
            elif word[0] == '"':
                if word[-1] == '"':
                    string_constant = word[1:-1]
                else:
                    string_tag = True
                    string_constant = word[1:]

            elif word != ' ':
                if word in jack_keyword:
                    output += "<keyword> " + word + " </keyword>\n"
                    xml_output.append("<keyword> " + word + " </keyword>\n")
                elif word in jack_symbol:
                    if word in xml_symbol:
                        output += "<symbol> " + xml_symbol[word] + " </symbol>\n"
                        xml_output.append("<symbol> " + xml_symbol[word] + " </symbol>\n")
                    else:
                        output += "<symbol> " + word + " </symbol>\n"
                        xml_output.append("<symbol> " + word + " </symbol>\n")
                elif word.isdigit():
                    output += "<integerConstant> " + word + " </integerConstant>\n"
                    xml_output.append("<integerConstant> " + word + " </integerConstant>\n")
                else:
                    output += "<identifier> " + word + " </identifier>\n"
                    xml_output.append("<identifier> " + word + " </identifier>\n")

    return output, xml_output


def tokens(codes):
    code = "<tokens>\n"
    xml_code = ["<tokens>\n"]

    for line in codes:
        output, xml_output = tokenizer(line)
        code += output
        xml_code += xml_output

    code += "</tokens>"
    xml_code += ["</tokens>"]
    return code, xml_code


class Parser:

    def __init__(self, code_lines):
        self.output = ""
        self.code_lines = code_lines
        self.indent_level = 0
        self.index = 1  # ignore <tokens>

    def compile_class(self):
        self.tag_start("<class>")
        self.compile_next()  # <keyword> class </keyword>
        self.compile_next()  # <identifier> 'className' </identifier>
        self.compile_next()  # <symbol> { </symbol>
        while (('static' in self.code_lines[self.index]) or ('field' in self.code_lines[self.index])):
            self.compile_class_var_dec()
        while 'constructor' in self.code_lines[self.index] or 'function' in self.code_lines[self.index] or 'method' in \
                self.code_lines[self.index]:
            self.compile_subroutine_dec()
        self.compile_next()  # <symbol> } </symbol>
        self.tag_end("</class>")

    def compile_class_var_dec(self):
        self.tag_start("<classVarDec>")
        self.dec()
        self.tag_end("</classVarDec>")

    def compile_subroutine_dec(self):
        self.tag_start("<subroutineDec>")
        self.compile_next()  # <keyword> consturctor/function/method </keyword>
        self.compile_next()  # <keyword >void|type </keyword>
        self.compile_next()  # <identifier> subroutineName </identifier>
        self.compile_next()  # <symbol> ( </symbol>
        self.compile_parameter_list()
        self.compile_next()  # <symbol> ) </symbol>

        self.compile_subroutine_body()
        self.tag_end("</subroutineDec>")

    def compile_parameter_list(self):
        self.tag_start("<parameterList>")
        if ')' not in self.code_lines[self.index]:
            self.compile_next()  # <keyword|identifier> type/className </keyword|/identifier>
            self.compile_next()  # <identifier> varName </identifier>
        while ')' not in self.code_lines[self.index]:
            self.compile_next()  # <symbol> , </symbol>
            self.compile_next()  # <keyword|identifier> type/className </keyword|/identifier>
            self.compile_next()  # <identifier> varName </identifier>
        self.tag_end("</parameterList>")

    def compile_subroutine_body(self):
        self.tag_start("<subroutineBody>")
        self.compile_next()  # <symbol> { </symbol>
        while "var" in self.code_lines[self.index]:
            self.compile_var_dec()
        self.compile_statements()
        self.compile_next()  # <symbol> } </symbol>
        self.tag_end("</subroutineBody>")

    def compile_var_dec(self):
        self.tag_start("<varDec>")
        self.dec()
        self.tag_end("</varDec>")

    def dec(self):
        self.compile_next()  # <keyword> var </keyword>
        self.compile_next()  # <keyword|identifier> type/className </keyword|/identifier>
        self.compile_next()  # <identifier> varName </identifier>
        while ',' in self.code_lines[self.index]:
            self.compile_next()  # <symbol> , </symbol>
            self.compile_next()  # <identifier> varName </identifier>
        self.compile_next()  # <symbol> ; </symbol>

    def compile_statements(self):
        self.tag_start("<statements>")
        while 1:
            if 'let' in self.code_lines[self.index]:
                self.compile_let_statement()
            elif 'if' in self.code_lines[self.index]:
                self.compile_if_statement()
            elif 'while' in self.code_lines[self.index]:
                self.compile_while_statement()
            elif 'do' in self.code_lines[self.index]:
                self.compile_do_statement()
            elif 'return' in self.code_lines[self.index]:
                self.compile_return_statement()
            else:
                break
        self.tag_end("</statements>")

    def compile_let_statement(self):
        self.tag_start("<letStatement>")
        self.compile_next()  # <keyword> let </keyword>
        self.compile_next()  # <identifier> id </identifier>
        if '[' in self.code_lines[self.index]:
            self.compile_next()  # <symbol> [ </symbol>
            self.compile_expression()
            self.compile_next()  # <symbol> ] </symbol>
        self.compile_next()  # <symbol> = </symbol>
        self.compile_expression()
        self.compile_next()  # <symbol> ; </symbol>
        self.tag_end("</letStatement>")

    def compile_if_statement(self):
        self.tag_start("<ifStatement>")
        self.compile_next()  # <keyword> if </keyword>
        self.compile_next()  # <symbol> ( </symbol>
        self.compile_expression()
        self.compile_next()  # <symbol> ) </symbol>

        self.compile_next()  # <symbol> { </symbol>
        self.compile_statements()
        self.compile_next()  # <symbol> } </symbol>

        if "else" in self.code_lines[self.index]:
            self.compile_next()  # <keyword> else </keyword>
            self.compile_next()  # <symbol> { </symbol>
            self.compile_statements()
            self.compile_next()  # <symbol> } </symbol>

        self.tag_end("</ifStatement>")

    def compile_while_statement(self):
        # while_code = "<whileStatement>"
        self.tag_start("<whileStatement>")
        self.compile_next()  # <keyword> while </keyword>
        self.compile_next()  # <symbol> ( </symbol>
        self.compile_expression()
        self.compile_next()  # <symbol> ) </symbol>
        self.compile_next()  # <symbol> { </symbol>
        self.compile_statements()
        self.compile_next()  # <symbol> } </symbol>

        self.tag_end("</whileStatement>")

    def compile_do_statement(self):
        self.tag_start("<doStatement>")
        self.compile_next()  # <keyword> do </keyword>

        # subroutine call can create a sparate method
        self.compile_next()  # <identifier> subroutineName </identifier>
        if '.' in self.code_lines[self.index]:
            self.compile_next()  # <symbol> . </symbol>
            self.compile_next()  # <symbol> subroutineName </symbol>
        self.compile_next()  # <symbol> ( </symbol>
        self.compile_expression_lst()
        self.compile_next()  # <symbol> ) </symbol>
        self.compile_next()  # <symbol> ; </symbol>

        self.tag_end("</doStatement>")

    def compile_return_statement(self):
        self.tag_start("<returnStatement>")
        self.compile_next()  # <keyword> return </keyword>
        if ';' not in self.code_lines[self.index]:
            self.compile_expression()
        self.compile_next()  # <symbol> ; </symbol>
        self.tag_end("</returnStatement>")

    def compile_expression(self):
        self.tag_start("<expression>")
        self.compile_term()
        while self.is_op():
            self.compile_next()  # <symbol> Op </symbol>
            self.compile_term()
        self.tag_end("</expression>")

    def compile_term(self):
        self.tag_start("<term>")
        if self.is_unary_op():
            self.compile_next()  # <symbol> unaryOp </symbol>
            self.compile_term()
        elif '(' in self.code_lines[self.index]:
            self.compile_next()  # <symbol> ( </symbol>
            self.compile_expression()
            self.compile_next()  # <symbol> ) </symbol>
        else:
            self.compile_next()  # <identifier> id </identifier>
            if '[' in self.code_lines[self.index]:
                self.compile_next()  # <symbol> [ </symbol>
                self.compile_expression()
                self.compile_next()  # <symbol> ] </symbol>
            elif '.' in self.code_lines[self.index]:
                self.compile_next()  # <symbol> . </symbol>
                self.compile_next()  # <identifier> id </identifier>
                self.compile_next()  # <symbol> ( </symbol>
                self.compile_expression_lst()
                self.compile_next()  # <symbol> ) </symbol>
            elif '(' in self.code_lines[self.index]:
                self.compile_next()  # <symbol> . </symbol>
                self.compile_expression_lst()
                self.compile_next()  # <symbol> ) </symbol>
        self.tag_end("</term>")

    def compile_expression_lst(self):
        self.tag_start("<expressionList>")
        # self.compile_next()  # <symbol> ( </symbol>
        # self.compile_expression()
        if ')' not in self.code_lines[self.index]:
            self.compile_expression()
        while ')' not in self.code_lines[self.index]:
            self.compile_next()  # <symbol> , </symbol>
            self.compile_expression()
        self.tag_end("</expressionList>")

    def tag_start(self, tag):
        self.output += '    ' * self.indent_level + tag + '\n'
        self.indent_level += 1

    def tag_end(self, tag):
        self.indent_level -= 1
        self.output += '    ' * self.indent_level + tag + '\n'

    def compile_next(self):
        self.output += '    ' * self.indent_level + self.code_lines[self.index]
        self.index += 1

    def is_op(self):
        tag, attribute = self.extract(self.code_lines[self.index])
        return attribute in op

    def is_unary_op(self):
        tag, attribute = self.extract(self.code_lines[self.index])
        return attribute in unary_op

    def extract(self, xml_code: str):
        for index, c in enumerate(xml_code):
            if c == ">":
                tag = xml_code[1:index]
                attribute_index = index + 2
            elif c == "<" and index > 0:
                attribute = xml_code[attribute_index:index - 1]
                return tag, attribute
