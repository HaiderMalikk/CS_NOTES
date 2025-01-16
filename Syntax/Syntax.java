package Syntax;


import java.util.Arrays;
import java.util.Scanner;

// name must mach file name unless public is removed
public class Syntax { 
  // since i declated var in class i can use  it any where in class NOTE: in class if no value given it will have defualt val here its 0 for ints
  static int myage = 21; // STATIC METHOD ONLY WORKS WITH SATTIC METHOID 
  // make a public method called main main is a special name you must have a main method to run your code (return type is void or any)
  public static void main(String[] args) {
    
    System.out.println("Hello, World!"); // hello world

    // java vars (must declare type then name then value end with;) // THESE ARE LOCAL VARS only used inside method here its the main method
    // int age = 27; one way
    // or 2nd way
    int age; // declare
    age = 27; // assign value
    System.out.println("i am" + age + "years old" ); // print age
    age = 20; // you can change val or var anythime
    System.out.println("i am" + age + "years old" ); // print age new age
    System.out.println("this is the age outside method" + myage); // age here is declared outside method

    // data types 
    // 1. primitive data types (stores a data like int)
    // int types
    byte aSingleByte = 100; 
    short aShort = 10000;
    int aInt = 1000000;
    long aLong = 1000000000;
    // decimal types
    float aFloat = 100.0f; 
    double aDouble = 100.0; // larger than float

    // 1.5 String type is a non primitive data type its a class the string class and has many methods of its own NOTE: you can compare strings 
    String aString = "Hello, World!"; // string is a class in java, String is reference data type

    // 2. reference data types (stores a memory address like array)
    boolean aBoolean = true;
    char aChar = 'A'; // ! ANY CHAR NEEDS SINGLE QUOTES 'A' NOT "A" so when you compare a char with char use single quotes

    // you can convert data types but only smaller to larger ones ex int to float unless you state it using (data type)
    // ex: int to float
    int num1 = 5;
    double num2 = num1; // here we are casting num1 to float
    System.out.println(num2); // output 5.0

    double numb1 = 5.8;
    int numb2 = (int) numb1; // here we are casting num1 to int must use int
    System.out.println(numb2); // output 5

    // final keyword can be used before objects to make them final ie they cannot be chaged
    final int num3 = 5; 

    // NOTE to get a unrounded number from 2 integer divvition cast one of the numbers to a double 
    // EX 
    int num4 = 5;
    int num5 = 2;
    System.out.println(num4 / num5); // output 2
    System.out.println((double) num4 / num5); // output 2.5

    // Big Boolean vs Small Boolean
    // boolean is a primitive data type it can only be true or false
    // Boolean is a class in java and can be true or false or null
    Boolean bigBoolean = null;

    // big int vs Integer 
    // int is a primitive data type it can only be positive or negative numbers
    // Integer is a class in java and can be positive or negative numbers or null
    Integer bigInt = null;
    // this class also has many methods

    // operators NOTE: "=" is assignment "== is comparision", bedmass applys to arithmatic
    // 1. arithmetic operators
    // + - * / % (modulus) ++ -- (increment/decrement) -> add, sub, mult, div, remander of two number division, +=1 or -=1)
    // 2. comparison operators
    // == != > < >= <= -> (equal, not equal, greater than, less than,) 
    // 3. logical operators
    // && (and) || (or) ! (not) // NOTE: not flips true and flase values so if x = true !x is false
    // 4. assignment operators
    // = += -= *= /= %= -> (assign, add, sub, mult, div, div remander) all these do a operation and assign at once
    // ! NOTE a int / int = int but a int / double = double atleaste one must be double for result to be double

    // if you use two diffrent data types result will be the of the lerger data type
    // ex: int + double = double

    // incerment / dec operator
    // ++x or x++ (both do same thing) increment x by 1 //NOTE: if x = 1, --x will make x = 0 for the remeander of code

    // String methods (some common ones also some of these might have parameters) to use this format like this: Stringname.Stringmethod(parameters if any) 
    // 1. length() -> returns the length of the string
    // 2. charAt() -> returns the character at the specified index
    // 3. toUpperCase() -> returns the string in uppercase
    // 4. toLowerCase() -> returns the string in lowercase
    // 5. trim() -> returns the string with leading and trailing spaces removed
    
    // 6. substring() -> returns the substring of the string
    // substring method java 
    // string.substring(start, end) 
    // returns a new string that is a substring of this string from the start index (inclusive meaning it includes the character at the start index) 
    // to the end index (exclusive meaning it does not include the character at the end index)
    // this is beacuse the string is treated as a array of characters

    // 7. replace() -> returns the string with the specified value replaced
    // 8. split() -> returns the array of strings split at the specified value
    // 9. toCharArray() -> returns the character array
    // 10. equals() -> returns true if the string is equal to the specified value
    // 11. compareTo() -> returns the comparison of the string to the specified value
    // 12. concat() -> returns the string concatenated with the specified value
    // 13. startsWith() -> returns true if the string starts with the specified value
    // 14. endsWith() -> returns true if the string ends with the specified value
    // 15. contains() -> returns true if the string contains the specified value
    // 16. indexOf() -> returns the index of the specified value
    // 17. lastIndexOf() -> returns the last index of the specified value
    // 18. replaceAll() -> returns the string with the specified value replaced
    // 19. toLowerCase() -> returns the string in lowercase
    // 20. toUpperCase() -> returns the string in uppercase
    // EX: 
    String str = "Hello";
    System.out.println(str.length()); // output 5
    
    // you can insert letter inside of stings with percent signs to use as vars Ex %s holds a strings at the end of the string use , then the var or value for %s
    // ex: System.out.println("Hello, %s!", name); // name is a var %s is ment for string only 
    // you can also format numbers to a specific decimal place using this if you have a double var
    // ex: System.out.printf("%.2f", 3.14159265359); // here i used a value insted or var output here is 3.14 2f = 2 decimal places can be used with print f
    // list of all % operators based on the data type: (common ones)
    // %b boolean
    // %c char
    // %d int
    // %e double
    // %f double
    // %h short

    // User inputs Must import scanner class to use scanner object
    Scanner scanner = new Scanner(System.in); // this is the sytax new creates a new scanner obj
    // scanner object has a method called next() that returns the next token from the input stream
    // ex: String name = scanner.next(); // this will get the next token from the input
    // scanner also has a method called nextLine() that returns the next line from the input stream
    // ex: String name = scanner.nextLine(); // this will get the next line from the input
    // scanner also has a method called nextInt() that returns the next int from the input stream
    // ETC ETC

    System.out.print("this is the promt for user name:  ");
    String name = scanner.nextLine(); // this will get the next line from the input
    // Note print f is a special print type
    // \n creats a newline after the print stament
    System.out.printf("Hello, %s how are you \n" ,name); // this will print out the user input NOTE: println will put input on next line print will put the input on the same line as this print statement
    // you can also use scanner to get multiple inputs at once (you can enter it on teh same line or press enter of the first input then enter the second one if you have multiple inputs with no print statement in between)
    System.out.println("tell us your name");
    String name2 = scanner.nextLine(); // this will get the next token from the input
    System.out.println("your age");
    int ageinput = scanner.nextInt(); // this will get the next int from the input
    System.out.printf("Hello, %s you are %d years old\n", name2, ageinput); // optinally you can format the inputs so a error dose not show up if you enter a letter for age
    scanner.close(); // close scanner to prevent data leaks


    // conditinals NOTE: else if will run if is not true to run two if staments just dont use else if
    // if statement
    // if (condition) {
    //     // code to be executed if condition is true
    // }
    // else if (condition) {
    //     // code to be executed if condition is true
    // }
    // else {
    //     // code to be executed if condition is false
    // }

    // a elseif vs two ifs
    int x = 7;
    if (x > 5) {
        System.out.println("x is greater than 5");
    }
    if (x < 10) {
        System.out.println("x is less than 10");
    } // this will print both staments as both ifs are ran even if one is false
    else{
      System.out.println("x is not greater than 5 or less than 10");
    }

    int y = 20;
    if (y > 5) {
        System.out.println("y is greater than 5");
    }
    else if (y < 30) {
        System.out.println("y is less than 30");
    } // here even though y is less then 30 this block stops at if stament as its true if the if was false the else if would run
    else{
      System.out.println("y is not greater than 5 or less than 30");
    }

    // Switch case is a better version of if else 
    // switch (var) {
    //     case value1:
    //         // code to be executed if var equals value1
    //         break;
    //     case value2:
    //         // code to be executed if var equals value2
    //         break;
    //     default:
    //         // code to be executed if var does not match any case
    //         break;
    // }
    int z = 10;
    switch (z) {
      case 5:
      System.out.println("z is 5");
      break;
      case 10:
      System.out.println("z is 10");
      break;
      default:
      System.out.println("z is not 5 or 10");
      break;
      }

    // OR //
    int z2 = 5;
    switch (z2) {
      case 5 -> System.out.println("z2 is 5");
      case 10 -> System.out.println("z2 is 10");
      default -> System.out.println("z2 is not 5 or 10");
      }

    // ternary operator
    // condition ? expression1 : expression2; // where expression1 is executed if condition is true and expression2 is executed if condition is false
    int a = 5;
    int b = 10;
    int c = a > b ? a : b;
    System.out.println(c);
    
    

    // arrays IN JAVA YOU NEED TO KNOW THE ELEMENTS OF THE ARRAY OR THE SIZE OF TEH ARRAY if you know elements its type[] name = {val1, vax, valn} if you know the len of array then type[] name = new type[len of array]
    // to make a empty array with size 5 and 1
    int array[] = new int[5]; // simple array format: arraytype[] name = new arraytype[arraylength]
    //OR
    int[] array2 = new int[1];
    // these arrays are empty
    int[] numbers = {1, 2, 3, 4, 5}; // simple array format: arraytype[] name = {elements} here the array has elements in it
    // the first element is index 0 last is index len -1 to print the first element 
    System.out.println(numbers[0]);
    // you can also do many things with a aray like add or delete elements and even replace elements 
    // to add an element to the array you need to know the size of the array 
    int[] numbers2 = new int[5]; // note that you can pass any int in parameter ie someotherarray.length as len of numbers 2 array
    numbers2[0] = 1;
    numbers2[1] = 2;
    numbers2[2] = 3;
    numbers2[3] = 4;
    numbers2[4] = 5;
    // to delete an element you need to know the index of the element you want to delete
    // to replace an element you need to know the index of the element you want to replace
    // to replace the first element of the numbers array with 0
    numbers2[numbers2.length - 1] = 0; // lreplacing ast element of array to 0
    // array num2 is now print using tostring
    System.out.println(Arrays.toString(numbers2));
    // ending index is not inclusive
  

    // usefull array methods for variuos data types using arrays import NOTE array here is called numbers
    // Arrays.sort(numbers); // sorts the array in ascending order
    // Arrays.sort(numbers, Collections.reverseOrder()); // sorts the array in descending order
    // Arrays.fill(numbers, 0); // fills the array with 0
    // Arrays.toString(numbers); // prints the array
    // Arrays.stream(numbers).forEach(System.out::println); // prints the array
    // Arrays.stream(numbers).mapToInt(Integer::intValue).sum(); // sums the array
    // Arrays.stream(numbers).mapToInt(Integer::intValue).max(); // finds the max of the
    // Arrays.stream(numbers).mapToInt(Integer::intValue).min(); // finds the min of the
    // Arrays.stream(numbers).mapToInt(Integer::intValue).average(); // finds the average of

    // creating a array with randome nums 
    int[] randomNumbers = {1, 3, 2, 5, 6};
    // Arrays.sort(randomNumbers); sorts whole array
    Arrays.sort(randomNumbers, 0, 3); // sorts the array from index 0 to 2 dose not include 3
    // print the sorted array using sout
    System.out.println(Arrays.toString(randomNumbers));

    // NOTE copys of array dont create a new array they just make a refrence to the array 
    // so if you change the array you will see the change in the copy
    // i will make a array called firstarray then make a copyarray and assign it to first array 
    int[] firstArray = {1, 2, 3, 4, 5};
    int[] copyArray = firstArray; // copyarray is just a refrence to firstarray but note deleteing one of the arrays will not affect the other as it points to refrence not the obj

    // if i tamper with copy array and print both arrays using to string both arrays will have same stuff done to it
    copyArray[0] = 10;
    System.out.println(Arrays.toString(firstArray));
    System.out.println(Arrays.toString(copyArray));
    // both arrasy are same
    // note you can copy array addresses and effectivly make a copy of the array but anychanges to the array will be reflected in both arrays


    // JAVA loops these loops can all contain conditionals
    // for loop format: for(starting point initial var, condition to run the loop, what to do after each time loop is ran)
    // will only print till 9 as as 10 is not included as i < 10 so upto 9 not including 10 if this was a array with 10 elements it would print whole array as array start at index 0
    for (int i = 0; i < 10; i++) {
      System.out.println(i);
      }
    // while loop, while condition is true loop runs
    int r = 0;
    while (r < 10) {
      System.out.println(r);
      r++;
      }
    // do while loop, do {this} while (this is true)
    int k = 0;
    do {
      System.out.println(k);
      k++;
      } while (k < 10);
    // for each loop, for (var: list) the var will asiign itslef to all th elements of the list one by one after each iteration number++
    int[] numbersloop = {1, 2, 3, 4, 5};
    for (int number : numbersloop) {
      System.out.println(number);
      }

    // nested for loop a loop inside a loop with a a 2d array 
    int[][] nestedArray = {{1, 2, 3}, {4, 5, 6}}; // syntax for double array note: int[0][0] is first subarrays first element so = 1 
    for (int i = 0; i < nestedArray.length; i++) {
      for (int j = 0; j < nestedArray[i].length; j++) {
        System.out.println(nestedArray[i][j]);
        }
    }
    // you can also nest otehr types of loops
    
    // ! sometimes the arrays address is printed to avoid this we will add to a trype string the values of the array using stringbuilder
    String[] strarr = {"one", "two", "three"}; // works for string array int array etc
        
        StringBuilder strarrnew = new StringBuilder();
        // loop over array and add the elements to strarrnew
        for (int i = 0; i < strarr.length; i++){
            strarrnew.append(strarr[i]);
            if (i < strarr.length-1){
                strarrnew.append(", "); // if we still have a element to add add a comma
            }
        }
        
        System.out.println(strarrnew); // prints [one, two, three]

    // break vs continue
    // break will stop the loop and move to the next statement after the loop
    // continue will skip the rest of the code in the loop and move to the next iteration
    for (int i = 0; i < 10; i++) {
      if (i == 5) {
        break; // stop the loop
        }
        System.out.println(i);
        }
        // continue
        for (int i = 0; i < 10; i++) {
          if (i == 5) {
            continue; // skip the rest of the code in the loop
            }
            System.out.println(i); // will print 0-4 and 6-9
            }
            // * you can also use break and continue with if statements
    
  }    // end of main method

} // end of class

// ! SEE OOP_Intro.java for notes on OOP
