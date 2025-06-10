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
float b = 5.7599;  // A float for decimals. optional to use f or F at the end of the number
char c = 'Z';    // A character.
double d = 15.123456789; // Double for higher precision decimal values.
long e = 1000000; // Long for larger integers.
const int DAYS_IN_WEEK = 7; // Constant value. // * NOTE: constants are only declared once and cannot be changed even if you attempt to redefine them they will retain the original value before the attempt at redefining them
// * as for changing the vlaue of a const that will cause a compile error

// multiple variable declaration
int a, b, c; // Declaring multiple variables of the same type.
int a = 5, b = 10, c = 15; // Declaring and initializing multiple variables of the same type.

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

// ! Static variables
// Static variables retain their value between function calls.
// Static Variables are initialized only once and retain their value between function calls.
// even if we try to redefine a static varible in a function but its already defined before it will not change the value of the variable
// EX:
void func() {
    static int count = 10; // Static variable using 'static' keyword.
    count += 5;
    printf("%d ", count); }
int main() {
    for (int i = 0; i < 4; i++) {
        func(); 
    }
    return 0; 
}
// output 15, 20, 25, 30. even though we try to redefine count its retains it value from the first call and only adds to it each time hence we dont see 15, 15 ...

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

// * C dose not have bound checking for arrays, meaning you can access any index of the array even if it is out of bounds, this can lead to undefined behavior
// * Arrays are zero-indexed, meaning the first element is at index 0.

// Arrays are collections of data of the same type. you must either initialize the array with a size or with values
int numbers[] = {1, 2, 3, 4, 5}; // values defined no more adding values
printf("%d\n", numbers[0]);  // Accessing the first element of the array.
// to make a array with a length of 50, reinitialize the array
int numbers[50]; // numbers = [0,0,0 .... 0] 50 times
int numbers[0] = 5; // numbers = [5,0,0 .... 0] 50 times
// you have 50 elements you can add or access to the array

// arr types
int arr[5]; // this is a array of 5 integers
arr[0] = 1.1; // this is valid but the value will be truncated to 1 as arr is an array of integers

// post and pre increment
int i = 0;
int x = arr[i]++ // x = arr[i] then arr[i] = arr[i] + 1
int x = ++arr[i]; // arr[i] = arr[i] + 1 then x = arr[i]
int x = arr[i++]; // x = arr[i] then arr[i] = arr[i] + 1 
int x = arr[++i] // arr[i] = arr[i] + 1 then x = arr[i]

// Print an Array with Loop

for (int i = 0; i < 5; i++) {
    printf("%d ", numbers[i]);
}
printf("\n");

// * 2D Arrays
// 2D arrays are arrays of arrays.
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
printf("%d\n", matrix[0][1]);  // Accesses the second element of the first row.

// * passing an array to a function
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int numbers[] = {1, 2, 3, 4, 5};
printArray(numbers, 5);  // Passing the array to the function. always pass the size of the array as well or use sizeof 

// passing 2d arrays; we must specify the size of the sub arrays i.e the number of columns or the number of elements in each row
void print(int arr[][3], int rows) {
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < 3; j++)
            printf("%d ", arr[i][j]);
}

int arr[2][3] = {{1, 2, 3}, {4, 5, 6}}; // must specify the size of the inner subarrays its not automatically calculated unlike the size of the arrays
print(arr, 2); // once again pass the size of array of use sizeof

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
printf("%d\n", *ptr);  // Prints the value stored at the address 'ptr' holds (10). the ptr holds the address of var so *ptr is the value of var if we printed p it would print the address of var

// ! Passing Pointers to Functions
void swap(int *a, int *b) {
    int temp = *a; // Store the value pointed by 'a' in 'temp'
    *a = *b;       // Assign the value pointed by 'b' to the location pointed by 'a'
    *b = temp;     // Assign the value in 'temp' to the location pointed by 'b'
}

swap(&a, &b); // passing in a and b by reference to the function, Note we pass the address and the function parameter, a pointer stores a address so we pass the address of the variable

int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;  // Storing the address of the first element of the array in 'ptr'.
int *ptr2 = &arr[0];  // Storing the address of the first element of the array in 'ptr2' since arr[0] is a int we need to use & to get the address

// ! Strings in C
// *  declaring strings using a array of characters (this means the length must be known at compile time or the string must be initialized)
char word[] = "hello";
printf("%c", word); // prints the first character of the string since arrays are pointers to the first element of the array
// to print the whole string use a loop
print("%s\n", word);

// * strings using pointers (can initilize it and change it later)
// since arrays are pointers to the first element we can declare a pointer to a string by declaring a pointer to a char which would be the first character of the string
char *word2 = "World"; // word2 is a pointer pointing to the first character of the string
printf("%s", word2); // prints the whole string
printf("%c", *word2); // prints the first character of the string since dereferencing the pointer gives the value at the address which is the first character of the string

// * Array of Strings using a 2D array
char names[3][10] = {"Alice", "Bob", "Charlie"};
printf("%s\n", names[1]);  // Prints "Bob"

// ! Arrays of Pointers 
// all arrays are references types meaning they store addresses not values, the values are the elements of the arrays
// but we can also store a list of pointers in a array
// Array of pointers to strings. here each elements is a pointer to a string not the string itself
// while we declate the strings the element at index 1 i.e names[1] is a pointer to the string "Bob" meaning its just a address to the first character of the string
// * arrays of strings 
// char *str stores the address of the first character of the string, and char str[] is a array of chars but since its a array str points to the first character of the string
// now here we say char *names this means that names points to a str and *names[] means that names points to a array of pointers in this case the pointers are char pointers i.e strings where the pointer just points to teh first character of the strings in the array
char *names[] = {"Alice", "Bob", "Charlie"}; 
printf("%p\n", names); // prints the array address
printf("%s\n", names[1]);  // Prints "Bob" beacuse we used the %s format specifier to print a string
// using pointer arithmetic, we know the address points to the first element and we also know we can add * to a pointer to get its value so:
printf ("%s\n", *names);  // Prints "Alice" as names gives the first element in the array and doing *names gives the first elements value which is the string "Alice"
printf ("%s\n", *(names+1));  // Prints "Bob" as *(names+1) is the value at the address of the second element of the array
// OR
printf("%s\n", (names+1)[0]);  // Prints "Bob" since (names+1) is the address of the second element of the array and [0] is the first character of the string we must specify this first element as we dont dereference the address pointed by (names+1) the first element at index 0 is enough to get the whole string "Bob" automatically
printf("%c\n", names[1][0]);  // Prints "B" as names[1] is the address of the "Bob" string and [0] is the first character of the string remember that each element of the array names is a string which itself is a array of characters
// or 
printf("%c\n", *(*(names+1))); // Prints "B" as *(names+1) is the address of the "Bob" string and *(*(names+1)) is the value of the first character of the string do *(*(names+1))+n to get the nth character of the string Bob
int arr[4] = {5, 10, 15, 20}; // Array of 4 integers
int (*ptr)[4] = &arr; // Pointer to an array of 4 integers the size of the pointer must match the size of the array now ptr is a pointer to arr's first emelemnt making it the smae is ptr[0] 
// NOTE: this is a array of pointers the elements of ptr are not values but addresses to the values for ex ptr[0] is the address of the first element of the array arr to gets its value we need to dereference it in short *ptr = arr and so we can index it like: *ptr[0] or do ptr[0][0] both are the same as arr[0] and etc
printf("%d %d", (*ptr)[1], ptr[0][3]); // 10 20. the firs one derefrences the arr its its values, as derefrenceing *ptr points to the first element it arr the we can accsess the second element of the array by [1], NOTE that *ptr = arr and *ptr[0] = arr[0] etc so we can use *ptr as a array and index its values 

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

// ! passing in arrays to functions using pointers

// * 1D
void print(int *arr, int size) { // alternitive to size: int size = sizeof(arr) / sizeof(arr[0]); only if the array is statically allocated i.e the size is known at compile time
    for (int i = 0; i < size; i++)
        printf("%d ", *(arr + i)); // alternative to arr[i]
}

int arr[] = {1, 2, 3, 4, 5};
print(arr, 5);

// * 2d
void print(int *arr, int m, int n) {
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            printf("%d ", *((arr + i * n) + j));
}

int arr[][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}; // unlike in 1d arrasy the size of the inner subarrays is not automatically calculated you must specify it but like usual the size of the array is calculated by the compiler
print((int *)arr, 3, 3);  // Pass address of first element * the cast makes the array lose its 2d structure meaning its now a 1d array
// alternative way if we use arr[i][j] instead of *(arr + i * n) + j BUT if we do that we must use the 2d structure of the array meaning we cannot cast the array to a 1d array

//!  pointers to arrays
// if we assign just a pointer to a array its pointing to the first element of the array
// but if we assign a pointer to a whole array its pointing to the address of the array
// this is useful when we want to pass an array to a function as a pointer since we pass the address of the array and the function can access the elements of the array
int arr[4] = {5, 10, 15, 20};  // Array of 4 integers
int (*ptr)[4] = &arr;          // Pointer to an array of 4 integers the size of the pointer must match the size of the array. now ptr = [address of arr] and *(address of array) = arr = [5, 10, 15, 20], this measn derefrencing the first element of ptr, ptr[0] or *(ptr) will give us the arr array which is [5, 10, 15, 20] then we can index this arr to get any element like ptr[0][1] for second element, note that ptr holds one element but its size is def as 4 because it's element holds a array of 4 integers.
printf("%d %d", (*ptr)[1], ptr[0][3]);  // Accessing elements of the array, (*ptr)[1] is the second element of the array as *ptr gets the arr and [1] gets the second element of the arr, ptr[0][3] is the fourth element of the array as ptr[0] gets the arr and [3] gets the fourth element of the arr  

// ! pointers to pointers
int x = 10;      // x is initialized to 10
int *p = &x;     // p is a pointer to x, so print(*p) will print 10
int **q = &p;    // q is a pointer to p (a pointer to a pointer) we use &p to get the address of p as doing **q = p will give a type error

**q = 20;        // Dereferencing q twice assigns 20 to x, **q is the address to p, *q is the value of p which is the address of x and **q is the value of x
printf("%d %d %d", x, *p, **q); // Prints the values of x, *p, and **q

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
// EX 2;
int (*ptr)(int, int);
int add(int a, int b) { return a + b; }
ptr = add;
printf("%d", ptr(3, 4)); // so need to dereference as the function pointer is already a address to the function

int (*ptr)(int, int);
int add(int a, int b) { return a + b; }
ptr = &add; // storing a address of a function in a pointer
printf("%d", (*ptr)(3, 4)); // must dereference the pointer to call the function

// ! Void Pointers
// Void pointers are generic pointers that can store the address of any data type.
void *ptr;  // Declaring a void pointer.
int x = 10;
ptr = &x;  // Storing the address of an integer in the void pointer.
float y = 3.14;
ptr = &y;  // Storing the address of a float in the void pointer.
char c = 'A';
ptr = &c;  // Storing the address of a character in the void pointer.

// for void pointers you must cast the pointer to the type you want to access, 
// this is because the void pointer is a generic pointer that can store any type of pointer
// example
int x = 10;
void *ptr = &x;
// printf("%d\n", *ptr);  // Error: Cannot dereference a void pointer.
printf("%d\n", *(int *)ptr);  // Correct: Cast the void pointer to an integer pointer which is the type it points to and dereference it.

// ! constant pointers
// as we saw in the swap example any pointer we pass to a function can have its value changed in the function
// to avoid this we can use constant pointers which can only access the value at the address but not change it
int x = 10;
int y = 20;
const int *ptr = &x;  // Pointer to a constant integer.
// *ptr = 20;  // Error: Cannot change the value of a constant pointer.
int alessthanb(const int *a, const int *b) { // both arguments are constant pointers which means in this function we cannot change the value of the pointers
    return *a < *b;
}
alessthanb(&x, &y); // we pass the address of x and y to the function

// ! Strings Functions
// Strings in C are arrays of characters.
#include <string.h>  // Needed for string functions.

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

// length of a string
int len = strlen(str);  // Returns the length of the string.

// serching chars in a string
char *ptr = strchr(str, 'l');  // Searches for the first occurrence of 'l' in the string and returns a pointer to it.
// if you want the index of the char = (ptr - str) as the pointer is a address number dont worry about the adderrss is just a number. p + 1 takes you to the next elements address in the string ao do *p+1 to get the value 

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
// Dynamic memory allocation allows you to allocate memory at runtime. but it must be the size of the data type
// * Malloc (allocate memory but does not initialize it) it only allocates one block of memory
// p is a int pointer to a memory location that is the size of a int so p can hold one int
int *p = malloc(sizeof(int)); // Allocating memory for an integer using malloc. optionally you can cast it to a int pointer like int *p = (int *)malloc(sizeof(int)); this is a common practice
*p = 42;  // Assigning a value to the allocated memory. use *p to access the value
printf("%d\n", *p);  // Accessing the value through the pointer.
// * Free (deallocate memory) sets it back to default
free(p);  // Freeing the allocated memory. now we can reuse p for anoehr number 
// free(p) // double free causes a error 

// * calloc (allocate memory and initialize it to 0) it can allocate multiple blocks of memory at once
int *p = calloc(5, sizeof(int)); // Allocating memory for 5 integers and initializing them to 0 using calloc. again you can cast it to a int pointer like int *p = (int *)calloc(5, sizeof(int));
// loop 5 times to assign 5 values or read 5 values
for (int i = 0; i < 5; i++) {
    printf("%d ", p[i]);  // Accessing the allocated memory. at index i we can use array indexing to access the values as p is a pointer to a array of integers
}
*p[0] = 42;  // Assigning a value to the first element of the allocated memory.
printf("%d\n", *p[0]);  // Accessing the value through the pointer.
free(p);  // Freeing the allocated memory. this initializes the memory to 0 and then we can use it

// * realloc (reallocate memory) changes the size of the allocated memory from default to a new size 
// * can be used to increase or decrease the size of the memory block, in the case of multiple blocks like for calloc we need to use the index of the block we want to change or a for loop to change all the blocks
int *p = malloc(5 * sizeof(int)); // Allocating memory for 5 integers.
// p first had 5 integers now it has 10 integers note we reassign using the address hence we dont dereference the pointer. you can also use a different pointer to store the new memory location
p = realloc(p, 10 * sizeof(int)); // Reallocating the memory to 10 integers. again you can cast it to a int pointer like int *p = (int *)realloc(p, 10 * sizeof(int));

// mem alocation example using a 2d array 
int make_and_print__and_delete_2d_array() {
    // a 2d arrays is a array of arrays or a array of pointers where the pointers point to a array of integers
    int rows = 3, cols = 4;

    // Allocate memory for a 2D array (array of pointers) here we allocate memory for the rows only 
    // what we do here is basically make a array and for each element of the array assign it the space of a int pointer 
    // this way insted of the elements holding a value like a 1d array the elements hold a address to a int pointer which in out case we want to be another array
    // the ammount of memory we allocate is the number of rows or the number of subarrays = the numbrer of int pointers out 2d arrays holds as its elements 
    int **array = (int **)malloc(rows * sizeof(int *)); // the casts are optional but good practice, The sizeof(int*) is the size of a int pointer != sizeof(int) as the int pointer holds a address to a int and the int holds a value
    // and alternitie way of making this 2d array is int array[rows][cols]; or int *array[rows]; for a array of pointers to integers all 3 ways are valid

    // Allocate memory for each row
    // here we loop through the array and we assign each row (the inner subarrays) to a array of integers 
    // malloc returns a int * but since arrays are pointers to the first element of the array we can assign the address of the first element to the array
    // i.e int *i = array; is the same as int *i = &array[0] as the array is a pointer to the first element of the array both are valid and show why this loop works
    for (int i = 0; i < rows; i++) {
        array[i] = (int *)malloc(cols * sizeof(int)); // the cast is optional
    }

    // Initialize the 2D array with values, assign each element of the array to a value
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            array[i][j] = i + j;  // Assign random values to the array. alternatively you can use *(*(array + i) + j) = i + j;
        }
    }

    // Print the 2D array
    printf("2D Array:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", array[i][j]); // alternatively you can use printf("%d ", *(*(array + i) + j));
        }
        printf("\n");
    }

    // * NOTE (passing in 2d arrays as args when alocating memory)
    // if the matrix is delclared like matrix[2][3] it will be a 2d array of integers and we can pass in the arr as a arg and the func agr is func(int arr[][3])
    // but with malloc its a pointer no a 2d integer array so we must pass in the array as a pointer to a pointer to a integer i.e func(int **arr)
    // EX
    // func(int **arr) { printf("%d %d %d\n", arr[0][0], arr[0][1], arr[0][2]) } // this notation isvalid along with func(int (*arr)[3]) and pointer arithmatic as long as we dont cast the array
    // func(array); // no cast

    // Free the allocated memory
    // when we free the memory if we just free the whole array the memory of the subarrays will not be freed because they are not inside of the arrays memory block 
    // the subarrays exist somwhere and the array just holds the pointers to them so if we dont free the subarrays we will have a memory leak meaning the 
    // subarrays exists somwehere in memory still but we lost the only ref's which were the pointers in the array so now they are lost in memory (NOTE c has no garbage collection)
    for (int i = 0; i < rows; i++) {
        free(array[i]); // Free each row which is a subarray = pointer to an array this is like freeing a 1d array
    }
    free(array); // Free the array of pointers which is a 2d array since the inside arrays are freed we can now free the array of pointers and all the memory is freed

    return 0;
}


// ! Structs
// Structs can be used with pointers to manage memory dynamically.
// * creating and accessing to a struct with values
struct Student {
    char name[50];
    int age;
};
struct Student s = {"Alice", 20}; // Initializing a struct. with a name and age
printf("%s is %d years old", s.name, s.age); // Accessing struct members using dot notation

// * passing fetures to sturucts 
// * (note structs require a pointer to the struct to be passed in so use the address of the struct) also you must cast the pointer to the struct to the struct type
// in these 2 exs we replace the age with 30 from its original value if it has no prev value then it will be set to 30
void modify(struct student s) { s.age = 30; } // by value 
void modify(struct student *s) { s->age = 30; } // by reference
// usage
struct Student s = {"Alice", 20};
modify(s);
modify(&s);

// * Structs with Pointers and Memory Allocation
struct Student *ptrStudent = (struct Student *)malloc(sizeof(struct Student)); // Dynamically allocate memory for a Student struct. the cast is optional but good practice

if (ptrStudent != NULL) {
    strcpy(ptrStudent->name, "Alice");  // Using the pointer to set the name.
    ptrStudent->age = 20;                // Using the pointer to set the age.
    printf("%s is %d years old.\n", ptrStudent->name, ptrStudent->age);  // Accessing struct members through pointer.
    free(ptrStudent);  // Freeing the allocated memory.
}
// * use after free is when you try to access a pointer after you have freed the memory it points to, this will give you a segmentation fault error

// * Structs with instance variables
struct Student {
    char name[50];
    int age;
} s; // Declaring a struct variable 's' of type Student. this means we create a struct with a name and age called 's' without having to initialize it
s.age = 20;        // Setting the age using the instance variable.

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

// ! bitwise operators
/* 
!NOTE: C has the ability to do any bit operation and do the assignment in one line so for ex &= or >>= or ^= so you dont have to do it separately. this is called compound assignment using compound operators
*/
// Least significant bit (LSB) is the rightmost bit in a binary number, and the most significant bit (MSB) is the leftmost bit.

// Bitwise operators are used to perform operations on individual bits of a number.
// 1. AND (&): Sets each bit to 1 if both bits are 1. ex 0110 & 0101 = 0100 or in decimal 6 & 5 = 4
int x = 6 & 5; // x will be 4
// 2. OR (|): Sets each bit to 1 if either bit is 1. ex 0110 | 0101 = 0111 or in decimal 6 | 5 = 7
int y = 6 | 5; // y will be 7
// 3. XOR (^): Sets each bit to 1 if only one of the bits is 1 or in other words if the bits are different. ex 0110 ^ 0101 = 0011 or in decimal 6 ^ 5 = 3
int z = 6 ^ 5; // z will be 3
// 4. NOT (~): Inverts each bit. ex ~0110 = 1001 or in decimal ~6 = -7
int w = ~6; // w will be -7

// ! bit shifting
// shift right means divide by 2^n and shift left means multiply by 2^n wher n is the value of the shift (i.e 1) in our case below
// 0100 = 4 and 0100 << 1 = 1000 = 8 and 0100 >> 1 = 0010 = 2
// you can shift right with both signed and unsigned integers but you can only shift left with unsigned integers if you shoft left with signed integers it gives undefined behavior.

// Bit shifting is the act of moving bits to the left or right.
int num = 5;  // In binary: 0101
num <<= 1;  // Shifts the bits to the left by 1: num becomes 1010 (10). or int shifted = num << 1; // shifted = 10
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

// * preprocessor to define the length of the array, even before compiling where ARRAY_LENGTH appears it will be replaced with 50
#define ARRAY_LENGTH 50 // this makes compilation faster insted of using a variable, always at the top of the file and all caps
int num[ARRAY_LENGTH];

// ! header files 
// In C, you can separate code into multiple files for better organization.
// Use 'include' to include header files.
#include "myHeader.h"  // Including a custom header file that might contain function declarations.

// Header files contain declarations for functions and types, typically ending with '.h'.
#ifndef MYHEADER_H
#define MYHEADER_H

void myFunction();  // Function declaration.

#endif

// In your main file, you would define myFunction and implement its logic.
// Include this header file to use the declared function in your main file.
// main file def from myHeader.h
// this makes a function declaration which is a prototype of the function in the header file
void myFunction() {
    printf("Hello from myFunction!\n");
}

// ! Inline Functions
// Inline functions are defined using the 'inline' keyword to suggest to the compiler to insert the function code directly where it's called.
// better than macros as they are type safe and can be debugged
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
    // You can also have a union inside a struct
    struct {
        int x;
        int y;
    } point; // this struct var point is inside the union to access the point struct we use data1.point.x and data1.point.y
} data1; // Declaring a union variable data of type Data

union Data data;  // Declaring a union variable of type Data.
data.intValue = 10;  // Storing an integer. or data1.intValue since we declared it as a union variable
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

/* 
// ! TYPES OF C / C++ FILES
### C and C++ File Extensions and Their Purposes

#### **C Language File Extensions**
- `.c`  - C source file
- `.h`  - C header file
- `.i`  - Preprocessed C source file
- `.ii` - Preprocessed C++ source file (used in some cases for C as well)
- `.m`  - Objective-C source file (used in combination with C)
- `.mi` - Preprocessed Objective-C source file
- `.hxx` - Alternate C/C++ header file extension
- `.hh` - Alternate C/C++ header file extension
- `.h++` - Alternate C++ header file extension
- `.hpp` - Alternate C++ header file extension (common in C++ projects, but may be used for C headers as well)

#### **C++ Language File Extensions**
- `.cpp`  - C++ source file
- `.cxx`  - C++ source file (alternative to `.cpp`)
- `.cc`   - C++ source file (used by some Unix-based compilers)
- `.C`    - C++ source file (case-sensitive systems treat it differently from `.c`)
- `.cp`   - C++ source file (rarely used)
- `.c++`  - C++ source file (uncommon, but still recognized by some compilers)
- `.h`    - Header file (used in both C and C++)
- `.hpp`  - C++ header file
- `.hxx`  - C++ header file
- `.hh`   - C++ header file
- `.h++`  - C++ header file

#### **Objective-C and Objective-C++ File Extensions (Uses C/C++ Code)**
- `.m`   - Objective-C source file (can contain C code)
- `.mm`  - Objective-C++ source file (can contain both C++ and C code)
- `.mi`  - Preprocessed Objective-C source file
- `.mii` - Preprocessed Objective-C++ source file

#### **C and C++ Precompiled and Intermediate Files**
- `.pch`  - Precompiled header file
- `.gch`  - Precompiled GNU C/C++ header file
- `.s`    - Assembly file (generated from C or C++)
- `.S`    - Assembly file with C preprocessor support
- `.o`    - Object file (compiled output of C/C++ source files, Unix/Linux systems)
- `.obj`  - Object file (compiled output of C/C++ source files, Windows systems)

#### **C and C++ Debugging and Compiled Files**
- `.a`   - Static library archive (Unix/Linux)
- `.lib` - Static library file (Windows)
- `.so`  - Shared object library file (Unix/Linux, dynamically linked)
- `.dll` - Dynamic-link library file (Windows, dynamically linked)
- `.exe` - Executable file (Windows)
- `.out` - Executable file (Unix default output, e.g., `a.out`)

#### **C and C++ Makefiles and Configuration Files**
- `Makefile` - Script for GNU Make utility to compile C/C++ projects
- `CMakeLists.txt` - Configuration file for CMake build system
- `.mk` - Makefile fragment (used in some projects for modular makefiles)
- `.ninja` - Build file for the Ninja build system (used with C/C++)

#### **Miscellaneous C and C++ Related Files**
- `.def`  - Module-definition file for Windows DLLs
- `.rc`   - Resource script file (Windows, used in C/C++ applications for icons, menus, etc.)
- `.idl`  - Interface Definition Language file (used in COM, CORBA, and other systems)
- `.exp`  - Export file (contains exported symbols from Windows DLLs)
- `.map`  - Memory map file (generated by linkers, used for debugging memory layout)
- `.lst`  - Listing file (generated by some assemblers and compilers for debugging purposes)

This file covers all known C and C++ file extensions and their uses.
*/