/*
// C is a low level language meaning it gives you more control over your code and hardware
// it is staticaly typed meaning you must tell the compiler what type of data you are using ie int x = 5 
// it is a compiled language meaning it must be compiled before it can be run it is compiled directly to machine code making it fast and efficient
// C is also strongly typed meaning after you declare a variable as a data type it cannot be changed or preform an invalid operation with it with first converting it to another type
*/

// ! NOTE: this code dose not run it is just an example of syntax !!!!!!
// ! NOTE: '*' is added to the start of varoables to make it a pointer goto pointers to learn more


// ! Comments & Escape Sequences

// Single-line comment in C using '//'.
// Multi-line comment in C:
/*
   This is a comment
   spanning multiple lines.
*/

// Escape sequences are special characters that start with '\'.
// Common ones include:
printf("Hello, World!\n"); // '\n' is for a new line.
printf("Tab\tSpace\n");    // '\t' is for a tab space.
printf("\"Quoted text\"\n"); // '\"' allows you to print double quotes.

// ! Variables

// Variables in C need to be declared with a data type before use.
int x = 5;       // Declaring an integer variable.
float y = 3.14;  // Declaring a floating-point variable.
char letter = 'A'; // Declaring a character variable (using single quotes for characters).

// ! Data Types

// In C, there are several data types:
// int - Integer type for whole numbers.
// float - Floating-point type for decimal numbers.
// double - Double precision floating-point numbers.
// char - Character type for storing single characters.
int a = 10;      // An integer.
float b = 5.75;  // A float for decimals.
char c = 'Z';    // A character.
double d = 15.123456789; // Double for higher precision decimal values.

// ! Format Specifiers

// Format specifiers in C are used to specify how to print different data types:
printf("Integer: %d\n", a);  // %d for integers.
printf("Float: %f\n", b);    // %f for floats.
printf("Character: %c\n", c); // %c for characters.
printf("Double: %lf\n", d);  // %lf for double.

// ! Constants

// Constants are variables whose value cannot be changed.
const int DAYS_IN_WEEK = 7; // 'const' keyword makes this a constant value.

// ! Arithmetic Operators

// Basic arithmetic operators in C:
int sum = 5 + 3;    // Addition
int diff = 5 - 3;   // Subtraction
int product = 5 * 3; // Multiplication
int quotient = 5 / 3; // Division (integer division)
int remainder = 5 % 3; // Modulo (remainder of division)

// ! Augmented Assignment Operators

// Augmented assignment operators combine arithmetic with assignment:
int x = 10;
x += 5;  // Equivalent to x = x + 5
x -= 3;  // Equivalent to x = x - 3
x *= 2;  // Equivalent to x = x * 2
x /= 2;  // Equivalent to x = x / 2

// ! User Input

// In C, you can take input using `scanf`:
int userInput;
printf("Enter a number: ");
scanf("%d", &userInput);  // Takes an integer input from the user.

// ! Math Functions

// The C Standard Library provides math functions.
#include <math.h>
double result = sqrt(25);  // sqrt() function to find the square root.
double power = pow(2, 3);  // pow() function to find powers (2^3).

// ! If Statements

// If statements in C are similar to Java/Python:
if (userInput > 0) {
    printf("The number is positive.\n");
} else if (userInput < 0) {
    printf("The number is negative.\n");
} else {
    printf("The number is zero.\n");
}

// ! Switch Statements

// Switch statements check for multiple cases, useful when checking multiple conditions:
switch (userInput) {
    case 1:
        printf("You entered one.\n");
        break;
    case 2:
        printf("You entered two.\n");
        break;
    default:
        printf("You entered something else.\n");
}

// ! AND Logical Operator

// AND logical operator checks if both conditions are true.
if (userInput > 0 && userInput < 10) {
    printf("The number is between 1 and 9.\n");
}

// ! OR Logical Operator

// OR logical operator checks if either condition is true.
if (userInput < 0 || userInput > 100) {
    printf("The number is either less than 0 or greater than 100.\n");
}

// ! NOT Logical Operator

// NOT logical operator negates the condition.
if (!(userInput == 0)) {
    printf("The number is not zero.\n");
}

// ! Functions

// Functions in C are similar to other languages, but you need to declare the return type:
int add(int a, int b) {
    return a + b;
}

// Calling the function:
int result = add(5, 3);

// ! Arguments

// Functions can take arguments (inputs):
void printNumber(int num) {
    printf("The number is: %d\n", num);
}

// ! Return Statement

// The return statement is used to return a value from a function.
int multiply(int a, int b) {
    return a * b;
}

// ! Ternary Operator

// Ternary operator is a shorthand for if-else:
int max = (a > b) ? a : b;  // If 'a' is greater than 'b', return 'a', otherwise 'b'.

// ! Function Prototypes

// In C, you often declare function prototypes before defining them:
void greet();  // Prototype declaration.

int main() {
    greet();  // Calling the function.
    return 0;
}

void greet() {
    printf("Hello, World!\n");
}

// ! String Functions

#include <string.h>  // Needed for string functions.

char str1[20] = "Hello";
char str2[20] = "World";
strcat(str1, str2);  // Concatenates str2 to the end of str1.
printf("%s\n", str1);  // Output: HelloWorld

// ! For Loops

for (int i = 0; i < 5; i++) {
    printf("%d\n", i);  // Prints numbers 0 to 4.
}

// ! While Loops

int count = 0;
while (count < 5) {
    printf("%d\n", count);
    count++;
}

// ! Do While Loop

do {
    printf("This will run at least once!\n");
} while (0);  // Condition is false, but it runs once.

// ! Nested Loops

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++) {
        printf("i = %d, j = %d\n", i, j);
    }
}

// ! Break vs Continue

// Break: Exit the loop entirely.
for (int i = 0; i < 5; i++) {
    if (i == 3) {
        break;
    }
    printf("%d\n", i);  // Stops printing after 2.
}

// Continue: Skip the rest of the current iteration.
for (int i = 0; i < 5; i++) {
    if (i == 3) {
        continue;
    }
    printf("%d\n", i);  // Skips printing 3.
}

// ! Arrays

// Arrays are collections of data of the same type.
int numbers[] = {1, 2, 3, 4, 5};
printf("%d\n", numbers[0]);  // Accessing the first element of the array.
// to make a array with a length of 50
int numbers[50];
// just like java at the time of making the array you have to define the length or the elements in the array 

// ! Print an Array with Loop

for (int i = 0; i < 5; i++) {
    printf("%d ", numbers[i]);
}
printf("\n");

// ! 2D Arrays

// 2D arrays are arrays of arrays.
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
printf("%d\n", matrix[0][1]);  // Accesses the second element of the first row.

// ! Array of Strings

char names[3][10] = {"Alice", "Bob", "Charlie"};
printf("%s\n", names[1]);  // Prints "Bob"

// ! Swap Values of Two Variables

// Swapping two values requires a temporary variable.
int temp = a;
a = b;
b = temp;

// ! Sort an Array

#include <stdio.h>
void sortArray(int arr[], int n) {
    int temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// ! Pointers

// A pointer is a variable that stores the memory address of another variable.
int *ptr;
int var = 10;
ptr = &var;  // Storing the address of 'var' in 'ptr'.

// Dereferencing: Accessing the value at the memory address.
printf("%d\n", *ptr);  // Prints the value stored at the address 'ptr' holds (10).

// Function to swap two integers using pointers
void swap(int *a, int *b) {
    int temp = *a; // Store the value pointed by 'a' in 'temp'
    *a = *b;       // Assign the value pointed by 'b' to the location pointed by 'a'
    *b = temp;     // Assign the value in 'temp' to the location pointed by 'b'
}

// ! Memory Addresses

// You can access the memory address of a variable using the '&' operator.
printf("Address of var: %p\n", &var);  // Outputs the memory address of 'var'.

// ! Structs

// Structs are custom data types that group related variables.
struct Student {
    char name[50]; // here name is a char array of size 50
    int age;
    float gpa;
};

struct Student student1 = {"Alice", 20, 3.9};  // Initializing a struct.
printf("%s is %d years old.\n", student1.name, student1.age);  // Accessing struct members.

// ! Structs with Pointers

// Structs can be used with pointers to manage memory dynamically.
struct Student {
    char name[50];
    int age;
};

struct Student *ptrStudent = (struct Student *)malloc(sizeof(struct Student)); // Dynamically allocate memory for a Student struct.

if (ptrStudent != NULL) {
    strcpy(ptrStudent->name, "Alice");  // Using the pointer to set the name.
    ptrStudent->age = 20;                // Using the pointer to set the age.
    printf("%s is %d years old.\n", ptrStudent->name, ptrStudent->age);  // Accessing struct members through pointer.
    free(ptrStudent);  // Freeing the allocated memory.
}

// ! Function Pointers

// Function pointers allow you to store the address of a function and call it.
void sayHello() {
    printf("Hello!\n");
}

void (*funcPtr)() = &sayHello;  // Declaring a function pointer.
funcPtr();  // Calling the function through the pointer.

// ! Callback Functions

// A callback function is a function that is passed to another function as an argument.
void processArray(int *arr, int size, void (*callback)(int)) {
    for (int i = 0; i < size; i++) {
        callback(arr[i]);  // Calling the callback function for each array element.
    }
}

void printNumber(int num) {
    printf("%d\n", num);
}

// Using the callback function:
int numbers[] = {1, 2, 3, 4, 5};
processArray(numbers, 5, printNumber);  // Passing the array and the callback.

// ! Recursion

// Recursion is a function that calls itself.
int factorial(int n) {
    if (n <= 1) {
        return 1;  // Base case
    }
    return n * factorial(n - 1);  // Recursive case
}

// Using recursion:
int fact = factorial(5);  // 5! = 120

// ! Multi-file Programs

// In C, you can separate code into multiple files for better organization.
// Use 'include' to include header files.
#include "myHeader.h"  // Including a custom header file that might contain function declarations.

// ! Header Files

// Header files contain declarations for functions and types, typically ending with '.h'.
#ifndef MYHEADER_H
#define MYHEADER_H

void myFunction();  // Function declaration.

#endif

// In your main file, you would define myFunction and implement its logic.
// Include this header file to use the declared function in your main file.

// ! Inline Functions

// Inline functions are defined using the 'inline' keyword to suggest to the compiler to insert the function code directly where it's called.
inline int square(int x) {
    return x * x;  // Returns the square of x.
}

// Using inline function:
int sq = square(4);  // sq will be 16.

// ! Bit Manipulation

// Bit manipulation is the act of algorithmically manipulating bits or binary digits.
int num = 5;  // In binary: 0101
num |= (1 << 1);  // Set the second bit: num becomes 0111 (7).
num &= ~(1 << 0);  // Clear the first bit: num becomes 0110 (6).
num ^= (1 << 2);  // Toggle the third bit: num becomes 0010 (2).

// ! Unions

// Unions are similar to structs but use the same memory location for all members.
union Data {
    int intValue;
    float floatValue;
    char charValue;
};

union Data data;  // Declaring a union variable.
data.intValue = 10;  // Storing an integer.
printf("%d\n", data.intValue);  // Prints 10.

// Overwriting the memory location:
data.floatValue = 5.5;  // Now the same memory location holds a float.
printf("%f\n", data.floatValue);  // Prints 5.5

// ! Memory Leak

// A memory leak occurs when allocated memory is not properly freed.
int *leakyArray = (int *)malloc(10 * sizeof(int)); // Memory is allocated but not freed.
// To prevent memory leaks, always use free():
free(leakyArray);

// ! Assertions

// Assertions are used for debugging purposes to ensure certain conditions are met.
#include <assert.h>

int divide(int a, int b) {
    assert(b != 0);  // Ensures 'b' is not zero to avoid division by zero.
    return a / b;
}

// Using the function:
int resultDiv = divide(10, 2);  // This is valid.
resultDiv = divide(10, 0);  // This will trigger an assertion failure.

// ! Predefined Macros

// Predefined macros in C give you useful information about the environment.
printf("File: %s\n", __FILE__);  // Current file name.
printf("Line: %d\n", __LINE__);   // Current line number.
printf("Date: %s\n", __DATE__);    // Current date.
printf("Time: %s\n", __TIME__);    // Current time.

// ! Constants in Header Files

// Constants can be declared in header files to be reused across multiple files.
#define MAX_SIZE 100  // Defining a constant.

