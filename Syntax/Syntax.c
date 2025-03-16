/*
// C is a low level language meaning it gives you more control over your code and hardware
// it is staticaly typed meaning you must tell the compiler what type of data you are using ie int x = 5 
// it is a compiled language meaning it must be compiled before it can be run it is compiled directly to machine code making it fast and efficient
// C is also strongly typed meaning after you declare a variable as a data type it cannot be changed or preform an invalid operation with it with first converting it to another type

// C is a procedural language meaning it is based on procedures or routines, it is not object oriented like C++ or Java
// the program is a series of functions that are called in a sequence to preform a task each line is executed one at a time
// C has no classes the main function is the entry point of the program and all other functions are called from the main function
// the main function can have 2 arguments argc and argv argc is the number of arguments passed to the program and argv is a array of strings that are the arguments passed to the program
// so we have int main() or int main(int argc, char *argv[]) NOTE the main function is a int because it returns a integer value 0 for success and any other number for failure
*/

// ! NOTE: this code dose not run it is just an example of syntax !!!!!!

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
float b = 5.7599;  // A float for decimals.
char c = 'Z';    // A character.
double d = 15.123456789; // Double for higher precision decimal values.
const int DAYS_IN_WEEK = 7; // Constant value. // * NOTE: constants are only declared once and cannot be changed even if you attempt to redefine them they will retain the original value before the attempt at redefining them
// * as for changing the vlaue of a const that will cause a compile error

// ! Format Specifiers

// Format specifiers in C are used to specify how to print different data types you cannot do printf(a) you must use a format specifier
printf(a) // * This will print the value of a but is not garunteed to work as the compiler may not know how to print the value of a.
printf("Integer: %d\n", a);  // %d for integers.
printf("Float: %f\n", b);    // %f for floats.
printf("Character: %c\n", c); // %c for characters.
printf("Double: %lf\n", d);  // %lf for double.
// rounding float example 
printf("Float: %.2f\n", b);  // %f for floats with 2 decimal places. b = 5.75 so this will print 5.76 as it rounds up
// this means for printing things liek arrays we need a loop

// ! Constants 

// Constants are variables whose value cannot be changed.
const int DAYS_IN_WEEK = 7; // 'const' keyword makes this a constant value.

// ! Arithmetic Operators

// Basic arithmetic operators in C:
int sum = 5 + 3;    // Addition
int diff = 5 - 3;   // Subtraction
int product = 5 * 3; // Multiplication
int quotient = 5 / 3; // Division (integer division rounds down)
int division = 5.0 / 3.0; // Division (decimal division dose not round down)
int remainder = 5 % 3; // Modulo (remainder of division)

// ! Augmented Assignment Operators

// Augmented assignment operators combine arithmetic with assignment:
int x = 10;
x += 5;  // Equivalent to x = x + 5
x -= 3;  // Equivalent to x = x - 3
x *= 2;  // Equivalent to x = x * 2
x /= 2;  // Equivalent to x = x / 2
// post increment vs pre increment
int x = 5;
int y = x++; // y = 5, x = 6
int z = ++x; // y = 6, x = 7
// x = 7
x = --x * 2; // x = 12 its done right to left so the value of x on right side is --x = 6 then * 2 = 12
// just by it self
int x = 5;
x++; // x = 6
++x; // x = 7
/* 
every operation is done left to right except for the assignment operator and pre increment which are done right to left EX: --x, x=1+1, x += x + 1
in all these examples the left side is done first then the right side is done, in all other cases the right side is done first then the left side EX: x && y is done left to right
*/

// ! User Input
// In C, you can take input using `scanf`, for non ref types like int, float, etc. you must pass the address as thats the only way scanf knows where to put the value
// for ref types like arrays, strings, etc. you do not need to pass the address as the array is already a address
int userInput;
printf("Enter a number: ");
scanf("%d", &userInput);  // Takes an integer input from the user.
// taking a input for a array
int arr[5];
for (int i = 0; i < 5; i++) {
    printf("Enter a number: ");
    scanf("%d", &arr[i]); // use & as we are accsessing a int
}

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

// ! switch case
int userInput = 1;
// switch case is used to check multiple conditions:
switch (userInput) {
    case 1:
        printf("You entered one.\n");
        break; // must break to avoid fall through i.e the cases after this will be executed as well
    case 2:
        printf("You entered two.\n");
        break;
    default:
        printf("You entered something else.\n");
}

// ! Function Prototypes

// In C, you often declare function prototypes before defining them:
void greet();  // Prototype declaration.

// ! main function is the entry point of the program in C
int main() {
    greet();  // Calling the function.
    return 0; // Return 0 to indicate success.
    // exit(1) to indicate failure where we exit the program with a non-zero exit code
}

void greet() {
    printf("Hello, World!\n");
}

// ! For Loops

for (int i = 0; i < 5; i++) {
    printf("%d\n", i);  // Prints numbers 0 to 4.
} // can do for(;;) to make an infinite loop but use break to exit the loop


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

// Arrays are collections of data of the same type. you must either initialize the array with a size or with values
int numbers[] = {1, 2, 3, 4, 5}; // values defined no more adding values
printf("%d\n", numbers[0]);  // Accessing the first element of the array.
// to make a array with a length of 50, reinitialize the array
int numbers[50]; // numbers = [0,0,0 .... 0] 50 times
int numbers[0] = 5; // numbers = [5,0,0 .... 0] 50 times
// you have 50 elements you can add or access to the array

// 2d arrays
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
printf("%d\n", matrix[0][1]);  // Accesses the second element of the first row.

// ! preprocessor to define the length of the array, even before compiling where ARRAY_LENGTH appears it will be replaced with 50
#define ARRAY_LENGTH 50 // this makes compilation faster insted of using a variable, always at the top of the file and all caps
int num[ARRAY_LENGTH];

// arr types
int arr[5]; // this is a array of 5 integers
arr[0] = 1.1; // this is valid but the value will be truncated to 1 as arr is an array of integers

// post and pre increment
int i = 0;
int x = arr[i]++ // x = arr[i] then arr[i] = arr[i] + 1
int x = ++arr[i]; // arr[i] = arr[i] + 1 then x = arr[i]
int x = arr[i++]; // x = arr[i] then arr[i] = arr[i] + 1 
int x = arr[++i] // arr[i] = arr[i] + 1 then x = arr[i]

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

// ! Memory Addresses
// You can access the memory address of a variable using the '&' operator. addresses have the '%p' format specifier
printf("Address of var: %p\n", &var);  // Outputs the memory address of 'var'.
printf("Address stored in ptr: %p\n", ptr);  // Outputs the memory address stored in 'ptr'. no & is needed as ptr is already a address, printing &ptr will give you the same address


// ! Pointers NOTE: '*' is used to denote a pointer. at runtime we can use *pointername to access the value at that address and &pointername to get the address
// A pointer is a variable that stores the memory address of another variable. if its a ref type it is the address of the variable if not we use the address operator to get it
int *ptr; // Declaring a pointer to an integer using the '*' operator. now a var ptr exits that is ready to store the address of an integer
int var = 10; // Declaring an integer variable. var holds the value 10
ptr = &var;  // Storing the address of 'var' in 'ptr' using &var to get the address of var. he address not the value of var. the address looks like 0x7fffbf7b1b4c

// Dereferencing: Accessing the value at the memory address., if you try to get the value from a null pointer it will give you a segmentation fault error
// use *pointername to get the value at that address that the pointer holds
printf("%d\n", *ptr);  // Prints the value stored at the address 'ptr' holds (10). the ptr holds the address of var so *ptr is the value of var, %d as ptr holds a address to a integer

// Function to swap two integers using pointers
void swap(int *a, int *b) {
    int temp = *a; // Store the value pointed by 'a' in 'temp'
    *a = *b;       // Assign the value pointed by 'b' to the location pointed by 'a'
    *b = temp;     // Assign the value in 'temp' to the location pointed by 'b'
}

swap(&a, &b); // passing in a and b by reference to the function, Note we pass the address and the function parameter, a pointer stores a address so we pass the address of the variable

int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;  // Storing the address of the first element of the array in 'ptr'.
int *ptr2 = &arr[0];  // Storing the address of the first element of the array in 'ptr2' since arr[0] is a int we need to use & to get the address

// ! Function Pointers
// Function pointers allow you to store the address of a function and call it.
void sayHello(char *name) {
    printf("Hello, %s!\n", name);
}

void (*funcPtr)(char *);  // Declaring a function pointer. funcPtr is a pointer that points to a function that takes a char pointer as a argument
funcPtr = sayHello;  // Storing the address of the function in the pointer. this mathces the one char * name
// NOTE: we can do this in one line as well by: void (*funcPtr)(char *) = sayHello; // no declaration needed
funcPtr("Alice");  // Calling the function using the pointer.
// and array of function pointers can be used to store multiple functions

// ! Arrays of Pointers 
// all arrays are references types meaning they store addresses not values, the values are the elements of the arrays
// but we can also store a list of pointers in a array
// Array of pointers to strings. here each elements is a pointer to a string not the string itself
// while we declate the strings the element at index 1 i.e names[1] is a pointer to the string "Bob" meaning its just a address to the first character of the string
// * arrays of strings 
// char *str stores the address of the first character of the string, and char str[] is a array of chars but since its a array str points to the first character of the string
// now here we say char *names this means that names points to a str and *names[] means that names points to a array of pointers in this case the pointers are char pointers i.e strings where the pointer just points to teh first character of the strings in the array
char *names[] = {"Alice", "Bob", "Charlie"}; 
print("%p\n", names) // prints the array address
print("%s\n", names[1]);  // Prints "Bob" beacuse we used the %s format specifier to print a string
// using pointer arithmetic, we know the address points to the first element and we also know we can add * to a pointer to get its value so:
printf ("%s\n", *names);  // Prints "Alice" as names gives the first element in the array and doing *names gives the first elements value which is the string "Alice"
printf ("%s\n", *(names+1));  // Prints "Bob" as *(names+1) is the value at the address of the second element of the array
printf("%c\n", names[1][0]);  // Prints "B" as names[1] is the address of the "Bob" string and [0] is the first character of the string remember that each element of the array names is a string which itself is a array of characters
// or 
printf("%c\n", *(*(names+1))); // Prints "B" as *(names+1) is the address of the "Bob" string and *(*(names+1)) is the value of the first character of the string do *(*(names+1))+n to get the nth character of the string Bob

// ! Pointer Arithmetic
// an array is a reference type meaning if we have int arr = [20]; arr hold a address to the first element of the array i.e arr is a address not a value
// so to store the array in a pounter is different from storing a single value in a pointer
int arr[5] = {1, 2, 3, 4, 5};
int *ptrArr = arr;  // Storing the address of the first element of the array in a pointer no need for &arr as we said arr is a address
printf("%d\n", *ptrArr);  // Prints the value at the address stored in 'ptrArr' (1) like we said the address is to the first element of the array
printf("%d\n", *(ptrArr + 1));  // Prints the value at the next address (2). and so on

// 2 d arrays 
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};
// both of these are the same
printf("%d", matrix[1][2]);
printf("%d", *(*(matrix+1)+2)); // the *(matrix+1) selects {5, 6, 7, 8} so let *(matrix+1) = arr = {5, 6, 7, 8} then this is = *(arr+2) = 7 which is like the last example

// But arrays elements are all just a offset from the first element i.e if a element is 8bytes then the first element is at 0x00, the second is at 0x08 and so on each 8 bytes apart
// so we can multiple the base address (the start index) by a multiple to get the address of the element we want in the 8 byte case the 3rd element is at 0x00 + 8*2 = 0x10
// this is C code is just the address of the array + n where n is the index of the element we want to access the offset is done by the compiler
// * more syntax for pointer arithmetic always use parenthesis to avoid errors
char *colors[] = {"red", "green", "blue", "yellow"};
printf("%s\n", colors[2]);  // Prints "blue".
printf("%s\n", *(colors + 2));  // Prints "blue". as *(colors) is the address of the first element of the array + 2 is index 2 = "blue"
print("%s\n", *(colors + 2)[0]); // Prints "b" as *(colors + 2) is the address of the "blue" string and [0] is the first character of the string
// alternative way
print("%s\n", (colors + 2)[0]); // equivalent to *(colors + 2) // the [0] is not for the first element of the index 2
print("%s\n", (colors + 2)[0][0]); // equivalent to *(colors + 2)[0] // the [0] is for the first character of the "blue" string = "b"
/// or 
print("%s\n", *(*(colors + 2))); // equivalent to (colors + 2)[0][0] = "b" the inner pointer gets the lement blue and the outer pointer gets the first character of the string as the base address of blue is the address of the first character of the string

print("%s\n", (colors + 2)[2]); // equivalent to *(colors + 2 + 2) = *(colors + 4) = "yellow"

//!  pointers to arrays
int arr[4] = {5, 10, 15, 20};  // Array of 4 integers
int (*ptr)[4] = &arr;          // Pointer to an array of 4 integers the size of the pointer must match the size of the array
printf("%d %d", (*ptr)[1], ptr[0][3]);  // Accessing elements of the array, (*ptr)[1] is the second element of the array as *ptr gets the values and [1] gets the second element of the array, ptr[0][3] is the fourth element of the array as ptr[0] gets the values and [3] gets the fourth element of the array  

// ! pointers to pointers
int x = 10;      // x is initialized to 10
int *p = &x;     // p is a pointer to x, so print(*p) will print 10
int **q = &p;    // q is a pointer to p (a pointer to a pointer)

**q = 20;        // Dereferencing q twice assigns 20 to x, **q is the address to p, *q is the value of p which is the address of x and **q is the value of x
printf("%d %d %d", x, *p, **q); // Prints the values of x, *p, and **q

// ! String Functions
// Strings in C are arrays of characters.
#include <string.h>  // Needed for string functions.

// declaring strings using a array of characters
char word[] = "hello";
printf("%c", word); // prints the first character of the string since arrays are pointers to the first element of the array
// to print the whole string use a loop
print("%s\n", word);

// strings using pointers 
// since arrays are pointers to the first element we can declare a pointer to a string by declaring a pointer to a char which would be the first character of the string
char *word2 = "World"; // word2 is a pointer pointing to the first character of the string
printf("%s", word2); // prints the whole string
printf("%c", *word2); // prints the first character of the string since dereferencing the pointer gives the value at the address which is the first character of the string

// * see arrays of pointers for how to make arrays of strings

char str1[20] = "Hello"; // strings are just arrays of characters in C each char has a index starting at 0
char str2[20] = "World";
char str3[] = "C is awesome!"; // the string is terminated by a null character '\0'
strcat(str1, str2);  // Concatenates str2 to the end of str1.
printf("%s\n", str1);  // Output: HelloWorld

// comparing strings
char str[] = "Hello";
char str2[] = "Hello";
// if the strings are equal strcmp will return 0, we Cannot say str == str2 as it will compare the memory address of the strings
if (strcmp(str, str2) == 0) {
    printf("The strings are equal.\n");
}
// but for ints we can do == to compare them

// ! Structs
// Structs are custom data types that group related variables.
struct Student {
    char name[50]; // here name is a char array of size 50
    int age;
    float gpa;
};

struct Student student1 = {"Alice", 20, 3.9};  // Initializing a struct.
printf("%s is %d years old.\n", student1.name, student1.age);  // Accessing struct members.

// ! Dynamic Memory Allocation

// ! sizeof operator
// The sizeof operator returns the size of a variable or data type in bytes.
// its important to know the size of a data type to avoid buffer overflows
// sizeof(int) will give you the size of an integer in bytes
// sizeof(struct student) will give you the size of a struct in bytes
// getting length of an array
int arr[] = {1, 2, 3, 4, 5};
// Getting the length of the array. divide the size of the array by the size of the first element of the array to get the length of the array 
// note that the first or any element repersents the size of one element of the array in bytes
// so this length has a total of 5 elements each of which is 4 bytes = 20 bytes. 20/4 = 5 = length of the array
int size = sizeof(arr) / sizeof(arr[0]); 
// NOTE this only works if the array is statically allocated i.e the size of the array is known at compile time 

// ! Memory allocation and deallocation
// in C memory is allocated using malloc and free is used to free the memory
// * Dynamic Memory Allocation
// Dynamic memory allocation allows you to allocate memory at runtime.
int *p = malloc(sizeof(int)); // Allocating memory for an integer using malloc.
*p = 42;  // Assigning a value to the allocated memory.
printf("%d\n", *p);  // Accessing the value through the pointer.
free(p);  // Freeing the allocated memory.

// * Structs with Pointers and Memory Allocation
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
// * use after free is when you try to access a pointer after you have freed the memory it points to, this will give you a segmentation fault error

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

// ! bit shifting
// shift right means divide by 2 and shift left means multiply by 2 so 
// 0100 = 4 and 0100 << 1 = 1000 = 8 and 0100 >> 1 = 0010 = 2
// you can shift right with both signed and unsigned integers but you can only shift left with unsigned integers if you shoft left with signed integers it gives undefined behavior.

// Bit shifting is the act of moving bits to the left or right.
int num = 5;  // In binary: 0101
num <<= 1;  // Shifts the bits to the left by 1: num becomes 1010 (10).
num >>= 1;  // Shifts the bits to the right by 1: num becomes 0101 (5).

// ! bit masking
// Bit masking is the act of extracting specific bits from a number.
int num = 5;  // In binary: 0101
int mask = 3;  // In binary: 0011
int maskedNum = num & mask;  // Applies a bitwise AND operation to extract the bits: maskedNum becomes 0011 (3).

// ! bit clearing
// Bit clearing is the act of clearing specific bits in a number.
int num = 5;  // In binary: 0101
int mask = 3;  // In binary: 0011
int clearedNum = num & ~mask;  // Applies a bitwise AND operation to clear the bits: clearedNum becomes 0100 (4).

// ! bit toggling
// Bit toggling is the act of toggling specific bits in a number.
int num = 5;  // In binary: 0101
int mask = 3;  // In binary: 0011
int toggledNum = num ^ mask;  // Applies a bitwise XOR operation to toggle the bits: toggledNum becomes 0110 (6).

// ! command line arguments
// Command line arguments are arguments passed to a program when it is executed.
// it allows users to pass data to the program from the command line.
// main func version with command line arguments, argc is the number of arguments and argv is the array of arguments
int main(int argc, char *argv[]) {
    printf("Number of arguments: %d\n", argc);
    for (int i = 0; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    return 0;
}

// ! Preprocessor and compilation
/* 
Directives are instructions to the preprocessor that tell it to perform specific actions., they are:
- #include: Includes a header file.
- #define: Defines a macro.
- #ifdef/#ifndef: conditional compilation.
- #if/#elif/#else/#endif: conditional compilation.
- #error: Prints an error message.
- #undef: Undefines a macro.
*/
// EX: 
#include <stdio.h> // include the standard input/output header file
#define SQUARE(x) ((x) * (x)) // define a macro to calculate the square of a number
printf("The square of 5 is: %d", SQUARE(5));
// EX of conditional compilation, to prevent multiple inclusions of the same header file
#if !defined(MYHEADER_H)
#define MYHEADER_H
// header file content
#endif


// ! -------------------------------------------------------------------------------------------------------------------------------------------------->>

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
