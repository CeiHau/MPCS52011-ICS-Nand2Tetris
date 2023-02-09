// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.



// Put your code here.
    @result
    M = 0 //result = 0
    @0
    D = M   // D = R0
    @i
    M = D // i = R0
(LOOP)
    @i 
    D = M   // D = i = R0 
    @END
    D; JLE  // If i<=0 goto END
    @1
    D = M   // D = R1
    @result
    M = M + D // result = R1 + result
    @i
    M = M - 1 // i = i - 1 
    @LOOP
    0;JMP
(END)
    @result
    D = M // D = result
    @2
    M = D // R2 = result
    @END
    0;JMP