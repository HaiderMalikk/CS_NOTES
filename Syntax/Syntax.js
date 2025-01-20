// Javascript intro and syntax
// JS6 syntax and features
// !!! the ';'  is not needed in js but is good practice


console.log("start") // print to console

//  * data types and varibles (any type can be null, bool, Str, symbol(immutable primative), num, obj)
// same operators as python/ java

// ! 3 ways to declare a variable can be any of the above
var myName = "Haider"; // avalible in whole program no scope ,can be initialized later i.e var myName; myName = "Haider";
let num = 10; // avalible in scope of block only , can be changed later i.e let num; num = 10;
const constant = "Malik"; // cannot change its constant for arrays you cant cahneg array but can change its elements // block only scope 

// you can add strings in js type DN matter
console.log(myName + constant);

// * arrays (same as python no type mattercand built ins for various operations)
// some stuff is arr = [...arr] to make a copy of array etc use 0-> len-1

// * functions
// using function keyword
function funcname(arg1){
    console.log("passed "+arg1+" in function");
    // or return;
}
funcname(1); 

// * conditionals if will run always no matter if a privious if was true else if will run if previous if was false and else runs if all fails
// * and and or is same as java
// here we use a arrow function to return a value
// const function
const processNumber = (num) => {
    if (num === 10) {
      console.log("num is 10");
    } else if (num > 10 || (num < 10 && num !== 10)) {
      console.log("num is greater than 10");
      let str = "or";
      let number = 1;
      return number || str; // Returns `number` if it exists; otherwise, `str`
    } else {
      console.log("num is less than 10");
    }
};
  
// Example 
const result = processNumber(11);
console.log("Returned value:", result);
  

// * arrow functions, used to create functions in a more concise way than normal functions
// format is function name = (arg1, arg2) => {return 'code'}   // can also specify return type and function type
add = (a, b) => {return a + b}
console.log(add(1, 2));
// ex with calling function from a function using arrow function 
// here we pass in no parameters and call the add function in the function code meaning it will add 2 and 2 always
funcname2 = () => {
  return add(2, 2)
}
console.log(funcname2());

// * Function keyword vs const,let,var function vs arrow function
// with function keyword you can call the function from another function before it is defined
// this function cannot be changed later in the same scope, but if we have the same function defined in another scope like inside another function it can be changed
myFunction();  // Works even before the function is defined
function myFunction() {
  console.log("Hello!");
  //console.log(this); // `this` depends on how it's called 
}
// const function same as function keyword but its a const so it cannot be changed or called before its defined
// myFunction2(); //cannot call the function from another function before it is defined myFunction2();
const myFunction2 = function() {
  console.log("This is a regular function assigned to a constant!");
};
myFunction2(); 
// with const ARROW function you cannot call the function from another function before it is defined
// myFunction3();  // Error: myFunction is not defined
const myFunction3 = () => {
  console.log("Hello!");
  // console.log(this);  // `this` refers to the surrounding lexical scope
};
// Using Functions in Objects
// Ex using Funtions in objects to show effect of this keyword
const obj1 = {
  name: "Test Object",
  // cannot be const
  arrowFunc: () => {
    console.log(this.name); // Inherited `this` (e.g., global `this`)
  },
  // cannot be const
  regularFunc: function () {
    console.log(this.name); // `this` refers to `obj`
  }
};
obj1.arrowFunc();  // Undefined or global value
obj1.regularFunc(); // "Test Object"
// let vs var vs const for functions
/* 
const function is constant and cannot be changed later
let function is not constant and can be changed later
var function is not constant and can be changed later but can cause issues with scope so use let instead
*/


// * switch case (always cehcks equality and type ie ===)
switch (num) {
    case 10: // if num is 10 do this
        console.log("num is 10");
        break;
    // if var = 20, 30, 40 so for alll cases print num is 20 or 30 or 40
    case 20:
    case 30:
    case 40:
        console.log("num is 20, 30, or  40");
        break;
    default:
        console.log("num is not 10 or 20");
        break;
}

// * one line condtionals
iwant = "this is waht i want"
nowant = "this is what i dont want"
// format is (condition) ? (if true) : (if false)
iwant != nowant ? console.log("iwant is not nowant") : console.log("iwant is nowant");
// alternate format using ??
var1 = null;
var2 = 88;
console.log(var1 ?? var2); // if x DNE then return y

// * equality operators
// '=' just assigns '==' checks equality only '===' checks equality and type
// NOTE all these can be used with '!' for 'not' operation
console.log(1 == 1); // true
console.log(1 === 1); // true
console.log(1 == "1"); // true
console.log(1 === "1"); // false

// * objects with key: value pars (there are many built in functions to modify and accsess  objects)
let person = {
    name: "John",
    age: 30,
    address: {
        street: "123 main st",
        city: "NYC"
    }
};

// to acccsess
console.log(person.name); // John
console.log(person["name"]); // John but '' for dynamic key meaning key is not known at compile time if name DNE it will return undefined
console.log(person.address.street); // 123 main st
person.work = "google";  // add new key value pair

// can also store in arrays (can be nested)
let Objarray  = [
    {name: "John", age: 30},
    {name: "Jane", age: 25, loves: {Work: "No", Sleep:"yes"}},
];

// * loops*
// for loop
for (let i = 0; i < 10; i++) {
    console.log(i);
    }

// while loop
let j = 0;
while (j < 10) {
    console.log(j);
    j++;
}

// for of loop the 'of' is used to iterate over the values of an iterable object
let fruits = ["apple", "banana", "cherry"];
for (let fruit of fruits) {
    console.log(fruit);
}
// for in loop loops over the index of an iterable object
for (let fruitindex in fruits) {
    console.log(fruitindex); // 0, 1, 2
    console.log(fruits[fruitindex]); // apple, banana, cherry
}

// for in loop, a for 'of' loops cannot be used to iterate over objects as obj[0] DNE we must use the key not the index
let personloop = {name: "John", age: 30};
for (let key in personloop) {
    console.log(key + ": " + personloop[key]); // ex key = name, personloop[key] = personloop["name"] = John
}

// do while loop lets the loop run once before checking the condition
let k = 0;
do {
    console.log(k);
    k++;
    } while (k < 10);

// * try catch (is teh same as in python try{try this} catch{if try fails do this}) 

// * destructuring assignments ie making new variables from existing ones
// old way
const set = {x: 1, y:2, z:3};
const x = set.x;
const y = set.y;
const z = set.z;

// new way
// !NOTE: the order of assignment matters 
const newset = {first: x,  second: y, third: z} // frist = x, second = y, third = z // here first is assigned to = x
/// NOTE: first dose not have to exist its not the assignment syntax ie assign empty val to some val its the order of the assignment
const {x: first, x: second, x: third} = newset; // first = x, second = x, third = x // here x is assigned to = first

// string formatting use "  `` "
const xval = 10;
const constString = `this is x: ${xval}`;
console.log(constString);

// * objects in JS 
class Person{
    // here the constructer is not a function but an object in JS so we cannot create it using class name
    constructor() {
        this.name = "John";
        this.age = 30;
    }
    // NO IDENTIFIER NAME like const or function
    greet() {
        return "Hello, my name is " + this.name + " and I am " + this.age + " years old.";
    }

}

// creating objs here const is not needed but is good practice
const personex = new Person();
console.log(personex.greet());

// * ptional parameters use '?' after the parameter name
// if we are accessing a property of an object that DNE it will return undefined so if we say obj1.name and obj 1 DNE it will return undefined
// this is better beacuse if obj1.name DNE it will throw an error when we try to accsess its property name
// ex of optional parameters
let location = {
    street: "123 main st",
    city: "NYC",
    country: "USA",
    position: {
        lat: 40.7128,
        lng: -74.0060
    }
}

// Ex1
console.log(location.position?.lat); // if position DNE it will return undefined and wont give error for trying to get lat of something that DNE
// Ex2 using a prop that DNE
console.log(location.positionFormatted?.lat); // positionFormatted DNE so it will return undefined
// error checking with ??
console.log(location.positionFormatted ?? "LocationFormatted DNE"); // if positionFormatted DNE then return "Location DNE"


// * Async, Await, Promises
// a async function is a function that returns a promise
// a promise is an object that represents the eventual completion or failure of an asynchronous operation
// await is used to wait for a promise i.e a async function to resolve 

// asyncrnous means that the code will not wait for the function to finish before moving on to the next line of code 
// it will run in the background parallel to the rest of the code

// Create a Promise, here resolve and reject are functions that are passed to the Promise and are responsible for resolving or rejecting the promise
// no arguments are passed to the resolve or reject functions
// its a arrow function not a normal function because it returns a promise
const fetchData = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const success = true;
        if (success) {
          resolve("Data fetched successfully!");
        } else {
          reject("Error fetching data.");
        }
      }, 1000); // Simulate a delay of 1 second
    });
};
  
// Using the Promise use .then to handle resolve and .catch to handle reject from the data
fetchData()
    .then((data) => console.log(data)) // Handles resolve
    .catch((error) => console.error(error)); // Handles reject

// Using async/await to handle the Promise
const getData = async () => {
    try {
      const data = await fetchData(); // Waits for the Promise to resolve
      console.log(data);
    } catch (error) {
      console.error(error); // Handles rejection
    }
};
  
getData();

// handling multiple promises, we dont have a reject here beacuse our promises will always resolve in this example, but the catch block will still run if any promise fails
const fetchData1 = () => {
    return new Promise((resolve) => setTimeout(() => resolve("Data 1"), 1000));
  };
  
  const fetchData2 = () => {
    return new Promise((resolve) => setTimeout(() => resolve("Data 2"), 2000));
  };
  
  const fetchData3 = () => {
    return new Promise((resolve) => setTimeout(() => resolve("Data 3"), 1500));
  };
  
  // Using Promise.all
const fetchAllData = async () => {
    try {
      const results = await Promise.all([fetchData1(), fetchData2(), fetchData3()]);
      console.log("All data fetched:", results);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
};
  
fetchAllData();

// common js functions
/* 
console.log() // Outputs data to the console
alert() // Displays an alert dialog box
prompt() // Displays a prompt dialog box for user input
confirm() // Displays a confirmation dialog box
parseInt() // Parses a string and returns an integer
parseFloat() // Parses a string and returns a floating-point number
isNaN() // Checks if a value is NaN (Not-a-Number)
setTimeout() // Executes a function after a specified delay (in milliseconds)
setInterval() // Repeatedly executes a function at specified intervals (in milliseconds)
clearTimeout() // Clears a previously set timeout
clearInterval() // Clears a previously set interval
Math.random() // Generates a random number between 0 (inclusive) and 1 (exclusive)
Math.round() // Rounds a number to the nearest integer
Math.floor() // Rounds a number down to the nearest integer
Math.ceil() // Rounds a number up to the nearest integer
Math.max() // Returns the largest of the given numbers
Math.min() // Returns the smallest of the given numbers
Math.pow() // Raises a number to the power of another
String.prototype.charAt() // Returns the character at a specified index in a string
String.prototype.includes() // Checks if a string contains a specified substring
String.prototype.split() // Splits a string into an array of substrings
Array.prototype.push() // Adds one or more elements to the end of an array
Array.prototype.pop() // Removes the last element from an array
Array.prototype.shift() // Removes the first element from an array
Array.prototype.unshift() // Adds one or more elements to the beginning of an array
Array.prototype.map() // Creates a new array by applying a function to each element of the array
Array.prototype.filter() // Creates a new array with elements that pass a test
Array.prototype.reduce() // Applies a function to reduce all array elements to a single value
Array.prototype.forEach() // Executes a function on each element of the array
Array.prototype.sort() // Sorts the elements of an array
Array.prototype.find() // Finds the first element in the array that satisfies a condition
Object.keys() // Returns an array of a given object's own enumerable property names
Object.values() // Returns an array of a given object's own enumerable property values
Object.entries() // Returns an array of a given object's enumerable string-keyed property [key, value] pairs
JSON.parse() // Parses a JSON string and returns the corresponding JavaScript object
JSON.stringify() // Converts a JavaScript object into a JSON string
encodeURIComponent() // Encodes a URI component by escaping special characters
decodeURIComponent() // Decodes a URI component
set() // Creates a new Set (collection of unique values)
get() // Retrieves a value from a Map or Set
Promise() // Creates a new promise object for asynchronous operations
fetch() // Fetches resources asynchronously (e.g., making HTTP requests)
addEventListener() // Attaches an event listener to an element
removeEventListener() // Removes an event listener from an element
localStorage.setItem() // Stores data in localStorage
localStorage.getItem() // Retrieves data from localStorage
sessionStorage.setItem() // Stores data in sessionStorage
sessionStorage.getItem() // Retrieves data from sessionStorage
document.querySelector() // Selects the first element matching a CSS selector
document.querySelectorAll() // Selects all elements matching a CSS selector
*/