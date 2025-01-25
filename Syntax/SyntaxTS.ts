// ! typescript is a superset of javascript meaning it adds to the features of javascript so it has all of js + more
// ! typescript must by compiled with tsc (typescript compiler) in order to work the file will come out as .js
// ! with node to complile download 'npm install -g typescript' 
// ! then use tsc filename.ts if you get no error a js file with the same name will be created
// ! to debbug in ts we must make a json and config files this depends workspace to workspace
// ! we can use tsc filename.ts -w to watch for changes in the file ie see errors
// ! note that you cant rediclare variables from a js file to a ts file meanign if 'name' vaible is in js file in the same folder as the ts file it will give an error
// ! NOTE after making your js file ts file will give errors as now you have a js file with the same var names as your ts file 

console.log('Hello World!'); // SAME AS JS!

// * Declaring variables with type annotations (these cant be cahnged ie a number cant be cahnged to a string later on)
// NOTE: IF THE TYPE IS NOT DECLARED IT WILL BE INFERRED BY THE VALUE SO DONT NEED TO DECLARE IT EX: let age = 30;
let isDone: boolean = false; // Boolean type
let decimal: number = 6; // Number type
let color: string = "blue"; // String type
let notDefined: undefined = undefined; // Undefined type
let notPresent: null = null; // Null type

// * Using basic types: number, string, boolean
let age: number = 30;
let myname: string = "John";
let isAdult: boolean = true;

// * TS variable types
// `any` can hold any type
let randomValue: any = 10;
randomValue = "a string";

// `void` indicates a function that returns nothing
function logMessage(message: string): void {
  console.log(message);
}

// `never` is for functions that never return (e.g., infinite loops or errors)
function throwError(message: string): never {
  throw new Error(message);
}

// `unknown` type forces you to do a type check before using the value
let value: unknown = "Hello";
if (typeof value === "string") {
  console.log(value.toUpperCase());
}

// * arrays
// Declaring an array of numbers
let numbers: number[] = [1, 2, 3, 4];

// Using generic type for arrays
let strings: Array<string> = ["apple", "banana"];

// * tuples
// Tuples allow you to specify the exact type of elements in an array
let user: [number, string] = [1, "John"];

// * enums
// Enums are used to define named constants
enum Direction {
    Up,
    Down,
    Left,
    Right
}
  
let currentDirection: Direction = Direction.Up;

// * functions
// you can use arrow functions in ts
// Function with typed parameters and return type
function add(a: number, b: number): number {
    return a + b;
  }
  
  // Optional parameter with `?`
function greet(name?: string): void {
    console.log(`Hello, ${name || "Guest"}`);
}
  
// * objects (no class)
// Defining an object with specific properties
let person: { name: string; age: number } = {
    name: "Alice",
    age: 25
};

// * ADVANCED TYPES
// Create a type alias for a complex object type
type User = {
    name: string;
    age: number;
  };
  
let myuser: User = { name: "Bob", age: 30 };

// Union types allow multiple types for a variable
let id: number | string;
id = 10;
id = "ABC";

// Intersection types combine multiple types into one
type CanSwim = {
  swim: () => void;
};

type CanFly = {
  fly: () => void;
};

type Superhero = CanSwim & CanFly;

let hero: Superhero = {
  swim() {
    console.log("Swimming");
  },
  fly() {
    console.log("Flying");
  }
};

// Literal types allow you to specify exact values for variables
let direction: "left" | "right" | "up" | "down";
direction = "left";

// Union with null or undefined for nullable types
let nullableName: string | null = null;

// * optional chaining
// Optional chaining helps avoid runtime errors when accessing deep properties
// the ? is used to indicate that the property is optional
let userObject: { name?: { first?: string } } = {};
console.log(userObject?.name?.first); // undefined

// * interfaces 
// Interfaces define the structure of an object
interface Car {
    make: string;
    model: string;
    year: number;
  }
  
let car: Car = {
    make: "Toyota",
    model: "Corolla",
    year: 2021
};

// * type aliases vs interfaces
// Type aliases allow you to define types for various entities
type myDog = { name: string; age: number };

// Interfaces allow for more flexibility, like extending other interfaces
interface Animal {
  species: string;
}

interface Dog extends Animal {
  breed: string;
}

// * Dom using ts (NOTE here document is Undifined)
// Using TypeScript to interact with DOM elements
const button = document.querySelector("button");

button?.addEventListener("click", () => {
  console.log("Button clicked!");
});

// * classes
// Defining a class with properties and methods
class myPerson {
    private name: string;
  
    constructor(name: string) {
      this.name = name;
    }
  
    greet(): void {
      console.log(`Hello, my name is ${this.name}`);
    }
}
  
let john = new myPerson("John");
john.greet();
  
// * generics
// Using generics to create reusable components by passing type parameters meaning they can be used with any type
function identity<T>(arg: T): T {
    return arg;
  }
  
let output1 = identity<string>("Hello");
let output2 = identity<number>(100);
  
// * generic interfaces
// Defining an interface with a generic type
interface Box<T> {
    contents: T;
}
  
let stringBox: Box<string> = { contents: "A book" };
let numberBox: Box<number> = { contents: 100 };
  

  