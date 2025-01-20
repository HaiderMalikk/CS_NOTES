// Javascript intro and syntax
// JS6 syntax and features
// !!! the ';'  is not needed in js but is good practice


console.log("start") // print to console

//  * data types and varibles (any type can be null, bool, Str, symbol(immutable primative), num, obj)
// same operators as python/ java

// ! 3 ways to declare a variable can be any of the above
var myName = "Haider"; // avalible in whole program no scope
let num = 10; // avalible in scope of block only 
const constant = "Malik"; // cannot change its constant for arrays you cant cahneg array but can change its elements // block only scope 

// you can add strings in js type DN matter
console.log(myName + constant);

// * arrays (same as python no type mattercand built ins for various operations)
// some stuff is arr = [...arr] to make a copy of array etc use 0-> len-1

// * functions
function funcname(arg1){
    console.log("passed "+arg1+" in function");
    // or return;
}
funcname(1); 

// * conditionals if will run always no matter if a privious if was true else if will run if previous if was false and else runs if all fails
// * and and or is same as java
// here we use a arrow function to return a value
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

// loops*
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

// * objects in JS (same as java for most part exept syntax most OOP is same like getters setters etc)
class Person{
    // here the constructer is not a function but an object in JS so we cannot create it using class name
    constructor() {
        this.name = "John";
        this.age = 30;
    }
    greet() {
        return "Hello, my name is " + this.name + " and I am " + this.age + " years old.";
    }

}

// creating objs here const is not needed but is good practice
const personex = new Person();
console.log(personex.greet());

// optional parameters use '?' after the parameter name
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


// Async, Await, Promises
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

