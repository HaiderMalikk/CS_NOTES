// ! typescript is a superset of javascript meaning it adds to the features of javascript so it has all of js + more
// ! typescript must by compiled with tsc (typescript compiler) in order to work the file will come out as .js
// ! with node to complile download 'npm install -g typescript' 
// ! then use tsc filename.ts if you get no error a js file with the same name will be created
// ! to debbug in ts we must make a json and config files this depends workspace to workspace
// ! we can use tsc filename.ts -w to watch for changes in the file ie see errors
// ! note that you cant rediclare variables from a js file to a ts file meanign if 'name' vaible is in js file in the same folder as the ts file it will give an error
// ! NOTE after making your js file ts file will give errors as now you have a js file with the same var names as your ts file 
// * SO THIS CODE IN A EXTENSION OF JS SYNTAX FILE

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
// arrow function
const add2 = (a: number, b: number): number => {
    return a + b;
};
  
// * objects (no class)
// Defining an object with specific properties
let person: { name: string; age: number } = {
    name: "Alice",
    age: 25
};

// how to iterate over an object
// in js you can use for in loop but in ts you cant becauseof type checking
// EX:
let car2: {[key: string]: string | number | null } = {
  make: "Toyota",
  model: "Corolla",
  year: 2021
};
for (let key in car2) {
  console.log(`${key}: ${car2[key]}`);
}
// or
for (const key of Object.keys(car2)) {
  console.log(key, car2[key as keyof typeof car]); // the key as keyof typeof car is used to tell ts that the key is a key of the car object
}

// * ADVANCED TYPES
// Create a type alias for a complex object type
type User = {
    name: string; // use ? after name to make it optional
    age: number; 
};
  
let myuser: User = { name: "Bob", age: 30 };

// Union types allow multiple types for a variable
let id: number | string;
id = 10;
id = "ABC";


// * interfaces 
// Interfaces define the structure of an object
interface Car {
  make: string;
  model?: string; // Optional property
  year: number;
}

// an object that follows the interface in this object we must have a make and year property but model is optional
let car: Car = {
  make: "Toyota",
  model: "Corolla",
  year: 2021
};

// * types vs interfaces
// Types and interfaces are very similar but have some differences
// Types can be used with union types, intersection types, and more
// Interfaces can be merged, while types can't
// interfaces can be used to extend other interfaces and can be changed later on to add more properties to the interface
// types are final and can't be changed but you can use union types and intersection types with them to merge them
// Creation

// - Using type
type Cartype = {
  make: string;
  model: string;
  year: number;
};
// Using interface
interface Carinterface {
  make: string;
  model: string;
  year: number;
}
//  - declaration merging
interface Carx {
  make: string;
}

// Adding more properties
interface Carx {
  model: string;
  year: number;
}
//using the interface
const myCar: Carx = {
  make: "Toyota",
  model: "Corolla",
  year: 2021
};

type CarY = {
  make: string;
};
// Error: Duplicate identifier
// type Car = {
  //   model: string;
  // };

// - more shapes 
type Status = "success" | "error" | "loading"; // Union means it can be any of the 3 choices
type Point = { x: number; y: number } & { z: number }; // Intersection means it must have all 3 properties
type StringOrNumber = string | number; // Union of primitives means it can be either a string or a number
type Callback = (value: number) => void; // Function type means it's a function that takes a number and returns void
type Tuple = [string, number]; // Tuple type means it's an array with 2 elements, a string and a number
// interfaces dont have these features

// - inheritance
interface Vehicle {
  make: string;
}

interface CarZ extends Vehicle {
  model: string;
  year: number;
}

type Vehiclez = {
  make: string;
};

type CarZ2 = Vehicle & {
  model: string;
  year: number;
};

// * Optional parameter with `?`
function greet(name?: string): void {
  console.log(`Hello, ${name || "Guest"}`);
}

// * optional chaining
// Optional chaining helps avoid runtime errors when accessing deep properties
// the ? is used to indicate that the property is optional
let userObject: { name?: { first?: string } } = {};
console.log(userObject?.name?.first); // undefined

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
  

  