// Hello World
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");

        // Numeric Data Types
        int integer = 42;
        float floatingPoint = 3.14f;
        double doublePrecision = 3.14159;
        decimal preciseDecimal = 19.99m;
        long largeInteger = 1234567890;

        // Text-Based Data Types
        char singleCharacter = 'A';
        string text = "Hello";

        // Converting String to Numbers
        string numberString = "123";
        int convertedNumber = int.Parse(numberString);
        Console.WriteLine(convertedNumber);

        // Boolean Data Type
        bool isTrue = true;
        bool isFalse = false;

        // Operators
        int a = 10, b = 20;
        Console.WriteLine(a + b); // Addition
        Console.WriteLine(a - b); // Subtraction
        Console.WriteLine(a * b); // Multiplication
        Console.WriteLine(b / a); // Division
        Console.WriteLine(b % a); // Remainder

        // Var Keyword
        var inferredInteger = 42;
        var inferredString = "Hello";

        // Const Keyword
        const double Pi = 3.14159;

        // Exercise - Storing User Data
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Hello, " + name);

        // Exercise - Odd/Even Checker
        Console.Write("Enter a number: ");
        int number = int.Parse(Console.ReadLine());
        Console.WriteLine(number % 2 == 0 ? "Even" : "Odd");

        // Console Input/Output
        Console.WriteLine("WriteLine example");
        Console.Write("Write example without new line");

        // If Statements
        if (number > 0)
            Console.WriteLine("Positive");
        else if (number < 0)
            Console.WriteLine("Negative");
        else
            Console.WriteLine("Zero");

        // Switch Statements
        switch (number)
        {
            case 0:
                Console.WriteLine("Zero");
                break;
            case 1:
                Console.WriteLine("One");
                break;
            default:
                Console.WriteLine("Other number");
                break;
        }

        // For Loops
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("Iteration " + i);
        }

        // While Loops
        int count = 0;
        while (count < 3)
        {
            Console.WriteLine("Count " + count);
            count++;
        }

        // Conditional Operator
        string result = number > 0 ? "Positive" : "Non-positive";
        Console.WriteLine(result);

        // Numeric Formatting
        double currencyValue = 1234.56;
        Console.WriteLine(currencyValue.ToString("C"));

        // TryParse Function
        string input = "456";
        if (int.TryParse(input, out int parsedValue))
        {
            Console.WriteLine("Parsed successfully: " + parsedValue);
        }
        else
        {
            Console.WriteLine("Failed to parse");
        }

        // Exercise - Times Table
        Console.Write("Enter a number for times table: ");
        int timesTable = int.Parse(Console.ReadLine());
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{timesTable} x {i} = {timesTable * i}");
        }

        // Exercise - Fizz Buzz Game
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
                Console.WriteLine("FizzBuzz");
            else if (i % 3 == 0)
                Console.WriteLine("Fizz");
            else if (i % 5 == 0)
                Console.WriteLine("Buzz");
            else
                Console.WriteLine(i);
        }

        // Verbatim String Literal
        string filePath = @"C:\Users\Name\Documents";
        Console.WriteLine(filePath);

        // String Formatting
        string formatted = string.Format("{0} {1}", "Hello", "World");
        Console.WriteLine(formatted);

        // String Interpolation
        Console.WriteLine($"Hello {name}");

        // String Concatenation
        string concatenated = "Hello" + " " + "World";
        Console.WriteLine(concatenated);

        // Empty String
        string empty = string.Empty;
        Console.WriteLine(string.IsNullOrEmpty(empty));

        // String Equals Function
        Console.WriteLine("test".Equals("Test", StringComparison.OrdinalIgnoreCase));

        // String Iteration Looping
        foreach (char c in name)
        {
            Console.WriteLine(c);
        }

        // String IsNullOrEmpty Function
        Console.WriteLine(string.IsNullOrEmpty(name));

        // Exercise - Print String in Reverse
        char[] chars = name.ToCharArray();
        Array.Reverse(chars);
        Console.WriteLine(new string(chars));

        // Exercise - Password Checker
        string password = "abc123";
        Console.Write("Enter password: ");
        string userPassword = Console.ReadLine();
        Console.WriteLine(userPassword == password ? "Access granted" : "Access denied");

        // Arrays
        int[] numbers = { 1, 2, 3, 4, 5 };
        Console.WriteLine(numbers.Length);

        // Array Sorting
        Array.Sort(numbers);

        // Array Reversal
        Array.Reverse(numbers);

        // Array Clearing
        Array.Clear(numbers, 0, numbers.Length);

        // Array IndexOf
        int index = Array.IndexOf(numbers, 3);

        // Lists
        List<int> numberList = new List<int> { 1, 2, 3 };

        // Dictionary
        Dictionary<string, int> dictionary = new Dictionary<string, int>();
        dictionary.Add("key", 42);


        // Exercise - Odd/Even number split
        static (List<int> evens, List<int> odds) SplitOddEven(int[] nums)
        {
            var evens = new List<int>();
            var odds = new List<int>();
            foreach (int num in nums)
            {
                if (num % 2 == 0) evens.Add(num);
                else odds.Add(num);
            }
            return (evens, odds);
        }

        // Exercise - Array of multiples
        static int[] GetMultiples(int baseNum, int count)
        {
            int[] multiples = new int[count];
            for (int i = 0; i < count; i++)
                multiples[i] = baseNum * (i + 1);
            return multiples;
        }

        // Functions
        static void PrintMessage(string message)
        {
            Console.WriteLine(message);
        }

        // Functions arrow 
        static int Add(int x, int y) => x + y;

        // Void functions
        static void SayHello()
        {
            Console.WriteLine("Hello, World!");
        }

        // Return type functions
        static int Multiply(int a, int b)
        {
            return a * b;
        }

        // Function parameters
        static void GreetUser(string userName)
        {
            Console.WriteLine($"Hello, {userName}");
        }

        // Optional parameters
        static void LogMessage(string message, string prefix = "Info")
        {
            Console.WriteLine($"[{prefix}] {message}");
        }

        // Named parameters
        static void PrintDetails(string name, int age)
        {
            Console.WriteLine($"Name: {name}, Age: {age}");
        }

        // Out parameters
        static void CalculateSum(int a, int b, out int sum)
        {
            sum = a + b;
        }

        // Reference parameters
        static void DoubleValue(ref int value)
        {
            value *= 2;
        }

        // Exercise - Area of a Triangle
        static double TriangleArea(double baseLength, double height)
        {
            return 0.5 * baseLength * height;
        }

        // (5:49:55) Exercise - Sum of int Array
        static int SumOfArray(int[] numbers)
        {
            int sum = 0;
            foreach (var num in numbers)
            {
                sum += num;
            }
            return sum;
        }

        // (6:00:51) Exception Handling
        static void HandleException()
        {
            try
            {
                int result = 10 / int.Parse("0");
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine("Cannot divide by zero: " + ex.Message);
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Invalid input: " + ex.Message);
            }
        }

        // (6:03:09) Try…catch
        static void TryCatchExample()
        {
            try
            {
                Console.WriteLine("Enter a number:");
                int number = int.Parse(Console.ReadLine());
                Console.WriteLine("You entered: " + number);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        // (6:12:29) Printing Error Messages
        static void PrintErrorMessages()
        {
            try
            {
                throw new Exception("This is a custom error message.");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }

        // (6:17:13) Exercise - Custom TryParse
        static bool CustomTryParse(string input, out int result)
        {
            try
            {
                result = int.Parse(input);
                return true;
            }
            catch
            {
                result = 0;
                return false;
            }
        }

        // (6:25:41) Debugging
        static void DebuggingExample()
        {
            int a = 5, b = 10;
            int sum = a + b; // Set a breakpoint here to inspect values.
            Console.WriteLine("Sum: " + sum);
        }

        // (6:37:37) Local/Auto Window
        static void LocalAutoWindowExample()
        {
            int x = 10;
            int y = 20;
            int z = x + y; // Inspect variables x, y, z in local/auto windows during debugging.
            Console.WriteLine("Z: " + z);
        }

        // (6:41:17) Watch Window
        static void WatchWindowExample()
        {
            int num1 = 15;
            int num2 = 25;
            int result = num1 * num2; // Add variables to Watch window to track them during debugging.
            Console.WriteLine("Result: " + result);
        }

        // (6:46:21) Exercise - Fix Logic Error
        static int FixLogicError(int a, int b)
        {
            // Original buggy logic: return a - b;
            return a + b;
        }

        // (6:49:55) Structures
        struct Point
        {
            public int X;
            public int Y;

            public Point(int x, int y)
            {
                X = x;
                Y = y;
            }
        }

        // (7:06:38) Classes
        class Person
        {
            public string Name;
            public int Age;

            public Person(string name, int age)
            {
                Name = name;
                Age = age;
            }
        }

        // (7:15:38) Class Functions
        class MathOperations
        {
            public int Add(int a, int b)
            {
                return a + b;
            }
        }

        // (7:21:49) Class Fields
        class Car
        {
            public string Make;
            public string Model;

            public Car(string make, string model)
            {
                Make = make;
                Model = model;
            }
        }

        // (7:37:08) Class Variable/Function Scope
        class ScopeExample
        {
            private int _privateField;
            public int PublicField;

            public void ExampleFunction()
            {
                int localVariable = 10;
                _privateField = localVariable;
            }
        }

        // (7:41:12) Class Properties
        class Rectangle
        {
            public int Width { get; set; }
            public int Height { get; set; }

            public int Area => Width * Height;
        }

        // (8:00:51) Class ToString
        class Book
        {
            public string Title { get; set; }
            public string Author { get; set; }

            public override string ToString()
            {
                return $"Title: {Title}, Author: {Author}";
            }
        }
    }
}
