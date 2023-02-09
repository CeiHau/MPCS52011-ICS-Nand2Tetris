// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    @16384  // base addresses of screen
    D = A
    @i  // i refers to the pixel that is going to be writed in black
    M = D // i = 16384, start on base addresses
(INFINITY)
(INPUT)
    @24576  // keyboard
    D = M   // If it's inputing, D != 0
    @CLEAR   
    D; JEQ    //If D == 0, goto CLEAR, start clear the black pixel

    // Write the current pixel in black
    @i
    D = M // D = i
    A = D   // A = i
    M = -1   // write the pixel to black

    // Determine if the screen is filled with black
    @i
    D = M   // D = i
    @24575
    D = A - D // D = 24575 - i
    @INFINITY
    D; JLE  // If (24575 - i) <= 0, stop write in black

    // i point to the next pixel
    @i 
    M = M + 1 //i = i + 1
    @INPUT
    0;JMP
(CLEAR)
    // write the current pixel to white
    @i
    D = M  // D = i
    A = D  // A = i
    M = 0 // write the pixel to white

    // Determine if is still inputing
    @24576  //  keyboard
    D = M   // If it's inputing, D != 0
    @INPUT  
    D; JNE  //If D !=0, start write black pixel

    // Determine if the screen is filled with white
    @i
    D = M   //D = i
    @16384
    D = D - A   //D = i - 16384
    @INFINITY
    D; JEQ //If D == 0, goto INFINITY
    
    @i
    M = M - 1 // i = i - 1
    @CLEAR
    0;JMP
    @INFINITY
    0;JMP