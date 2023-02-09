
//-----------------------------------FibonacciSeries.vm-----------------------------------
//push argument 1
@ARG  
D = M
@1
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

//pop pointer 1
@SP
AM = M - 1
D = M
@THAT
M = D

//push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1

//pop that 0
@THAT
D = M
@0
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1

//pop that 1
@THAT
D = M
@1
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//push argument 0
@ARG  
D = M
@0
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

//push constant 2
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1

//sub
@SP
AM = M - 1
D = M
A = A - 1
M = M - D

//pop argument 0
@ARG
D = M
@0
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//label MAIN_LOOP_START
(main_loop_start)

//push argument 0
@ARG  
D = M
@0
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

//if-goto COMPUTE_ELEMENT
@SP
AM = M - 1
D = M
@compute_element
D;JNE

//goto END_PROGRAM
@end_program
0;JMP

//label COMPUTE_ELEMENT
(compute_element)

//push that 0
@THAT  
D = M
@0
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

//push that 1
@THAT  
D = M
@1
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

//add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M

//pop that 2
@THAT
D = M
@2
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//push pointer 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1

//push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1

//add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M

//pop pointer 1
@SP
AM = M - 1
D = M
@THAT
M = D

//push argument 0
@ARG  
D = M
@0
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

//push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1

//sub
@SP
AM = M - 1
D = M
A = A - 1
M = M - D

//pop argument 0
@ARG
D = M
@0
D = D + A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//goto MAIN_LOOP_START
@main_loop_start
0;JMP

//label END_PROGRAM
(end_program)

