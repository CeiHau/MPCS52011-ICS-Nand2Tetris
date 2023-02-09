//-----------------------------------bootstrap-----------------------------------
// set set SP to 256
@256
D = A
@SP
M = D

// push return-address
@RETURN_ADRESS_0
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push LCL
@LCL
D = M
@SP
AM = M + 1
A = A -1
M = D

// push ARG
@ARG
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THIS
@THIS
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THAT
@THAT
D = M
@SP
AM = M + 1
A = A -1
M = D

// ARG = SP - n - 5
@SP
D = M
@5
D = D -A
@0
D = D - A
@ARG
M = D

// LCL = SP
@SP
D = M
@LCL
M = D

// goto f
@sys.init
0;JMP

// set return address
(RETURN_ADRESS_0)

//-----------------------------------Main.vm-----------------------------------
//function Main.fibonacci 0
(main.fibonacci)

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

//lt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@continue3
D; JLT
@SP
A = M - 1
M = 0
(continue3)

//if-goto IF_TRUE
@SP
AM = M - 1
D = M
@if_true
D;JNE

//goto IF_FALSE
@if_false
0;JMP

//label IF_TRUE
(if_true)

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

//return
// FRAME = LCL
@LCL
D = M
@FRAME
M = D

// RET = *(FRAME - 5)
@FRAME
D = M
@5
A = D - A
D = M
@RET
M = D

 // *ARG = pop()
@SP
AM = M - 1
D = M
@ARG
A = M
M = D

 // SP = ARG + 1
@ARG
D = M + 1
@SP
M = D

// THAT = *(FRAME - 1)
@FRAME
A = M - 1
D = M
@THAT
M = D

 // THIS = *(FRAME - 2)
@2
D = A
@FRAME
A = M - D
D = M
@THIS
M = D

 // ARG = *(FRAME - 3)
@3
D = A
@FRAME
A = M - D
D = M
@ARG
M = D

// LCL = *(FRAME - 4)
@4
D = A
@FRAME
A = M - D
D = M
@LCL
M = D

// goto RET
@RET
A = M
0;JMP

//label IF_FALSE
(if_false)

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

//call Main.fibonacci 1

// push return-address
@RETURN_ADRESS_1
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push LCL
@LCL
D = M
@SP
AM = M + 1
A = A -1
M = D

// push ARG
@ARG
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THIS
@THIS
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THAT
@THAT
D = M
@SP
AM = M + 1
A = A -1
M = D

// ARG = SP - n - 5
@SP
D = M
@5
D = D -A
@1
D = D - A
@ARG
M = D

// LCL = SP
@SP
D = M
@LCL
M = D

// goto f
@main.fibonacci
0;JMP

// set return address
(RETURN_ADRESS_1)

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

//call Main.fibonacci 1

// push return-address
@RETURN_ADRESS_2
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push LCL
@LCL
D = M
@SP
AM = M + 1
A = A -1
M = D

// push ARG
@ARG
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THIS
@THIS
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THAT
@THAT
D = M
@SP
AM = M + 1
A = A -1
M = D

// ARG = SP - n - 5
@SP
D = M
@5
D = D -A
@1
D = D - A
@ARG
M = D

// LCL = SP
@SP
D = M
@LCL
M = D

// goto f
@main.fibonacci
0;JMP

// set return address
(RETURN_ADRESS_2)

//add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M

//return
// FRAME = LCL
@LCL
D = M
@FRAME
M = D

// RET = *(FRAME - 5)
@FRAME
D = M
@5
A = D - A
D = M
@RET
M = D

 // *ARG = pop()
@SP
AM = M - 1
D = M
@ARG
A = M
M = D

 // SP = ARG + 1
@ARG
D = M + 1
@SP
M = D

// THAT = *(FRAME - 1)
@FRAME
A = M - 1
D = M
@THAT
M = D

 // THIS = *(FRAME - 2)
@2
D = A
@FRAME
A = M - D
D = M
@THIS
M = D

 // ARG = *(FRAME - 3)
@3
D = A
@FRAME
A = M - D
D = M
@ARG
M = D

// LCL = *(FRAME - 4)
@4
D = A
@FRAME
A = M - D
D = M
@LCL
M = D

// goto RET
@RET
A = M
0;JMP


//-----------------------------------Sys.vm-----------------------------------
//function Sys.init 0
(sys.init)

//push constant 4
@4
D = A
@SP
A = M
M = D
@SP
M = M + 1

//call Main.fibonacci 1

// push return-address
@RETURN_ADRESS_3
D = A
@SP
A = M
M = D
@SP
M = M + 1

// push LCL
@LCL
D = M
@SP
AM = M + 1
A = A -1
M = D

// push ARG
@ARG
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THIS
@THIS
D = M
@SP
AM = M + 1
A = A -1
M = D

// push THAT
@THAT
D = M
@SP
AM = M + 1
A = A -1
M = D

// ARG = SP - n - 5
@SP
D = M
@5
D = D -A
@1
D = D - A
@ARG
M = D

// LCL = SP
@SP
D = M
@LCL
M = D

// goto f
@main.fibonacci
0;JMP

// set return address
(RETURN_ADRESS_3)

//label WHILE
(while)

//goto WHILE
@while
0;JMP

