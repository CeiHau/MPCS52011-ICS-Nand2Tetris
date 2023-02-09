
//-----------------------------------BasicLoop.vm-----------------------------------
//push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1

//pop local 0
@LCL
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

//label LOOP_START
(loop_start)

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

//push local 0
@LCL  
D = M
@0
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

//pop local 0
@LCL
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

//if-goto LOOP_START
@SP
AM = M - 1
D = M
@loop_start
D;JNE

//push local 0
@LCL  
D = M
@0
A = A + D
D = M
@SP
A = M
M = D
@SP
M = M + 1

