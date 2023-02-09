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

//-----------------------------------Class1.vm-----------------------------------
//function Class1.set 0
(class1.set)

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

//pop static 0
@Class1.static0
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

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

//pop static 1
@Class1.static1
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//push constant 0
@0
D = A
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

//function Class1.get 0
(class1.get)

//push static 0
@Class1.static0
D = M
@SP
A = M
M = D
@SP
M = M + 1

//push static 1
@Class1.static1
D = M
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

//push constant 6
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1

//push constant 8
@8
D = A
@SP
A = M
M = D
@SP
M = M + 1

//call Class1.set 2

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
@2
D = D - A
@ARG
M = D

// LCL = SP
@SP
D = M
@LCL
M = D

// goto f
@class1.set
0;JMP

// set return address
(RETURN_ADRESS_1)

//pop temp 0
@5
D = A
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

//push constant 23
@23
D = A
@SP
A = M
M = D
@SP
M = M + 1

//push constant 15
@15
D = A
@SP
A = M
M = D
@SP
M = M + 1

//call Class2.set 2

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
@2
D = D - A
@ARG
M = D

// LCL = SP
@SP
D = M
@LCL
M = D

// goto f
@class2.set
0;JMP

// set return address
(RETURN_ADRESS_2)

//pop temp 0
@5
D = A
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

//call Class1.get 0

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
@class1.get
0;JMP

// set return address
(RETURN_ADRESS_3)

//call Class2.get 0

// push return-address
@RETURN_ADRESS_4
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
@class2.get
0;JMP

// set return address
(RETURN_ADRESS_4)

//label WHILE
(while)

//goto WHILE
@while
0;JMP


//-----------------------------------Class2.vm-----------------------------------
//function Class2.set 0
(class2.set)

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

//pop static 0
@Class2.static0
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

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

//pop static 1
@Class2.static1
D = A
@13
M = D
@SP
AM = M - 1
D = M
@13
A = M
M = D

//push constant 0
@0
D = A
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

//function Class2.get 0
(class2.get)

//push static 0
@Class2.static0
D = M
@SP
A = M
M = D
@SP
M = M + 1

//push static 1
@Class2.static1
D = M
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

