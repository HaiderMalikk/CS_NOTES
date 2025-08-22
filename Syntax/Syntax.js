// Javascript intro and syntax
// JS6 syntax and features
// !!! the ';'  is not needed in js but is good practice


console.log("start") // print to console

//  * data types and varibles (any type can be null, bool, Str, symbol(immutable primative), num, obj)
//  * variables (any type can be null, bool, Str, symbol(immutable primative), num, obj) 
// * operators: +, -, *, /, %, **, ++, --, +=, -=, *=, /=, %=, ==, ===, !=, !==, >, <, >=, <=, &&, ||, !, ?:, ??

// PRE increment and decrement operators
// ++var (pre-increment) and --var (pre-decrement) will change the value before it is used
// var++ (post-increment) and var-- (post-decrement) will change the value after it is used
// EX: var = 10, then return --var; // returns 9 and var is now 9, and return var--; // returns 9 but var is now 8 as its decrement after 

// ! 3 ways to declare a variable can be any of the above
var myName = "Haider"; // avalible in whole program no scope ,can be initialized later i.e var myName; myName = "Haider";
let num = 10; // avalible in scope of block only , can be changed later i.e let num; num = 10;
const constant = "Malik"; // cannot change its constant for arrays you cant cahneg array but can change its elements // block only scope 
state = "New York"; // no keyword is used to declare a variable it is automatically declared as a global variable

// you can add strings in js type DN matter
console.log(myName + constant);

// vars in strings in `` use ${var} to place a var in a string
console.log(`My name is ${myName} ${constant}`); // with this everything in `` is a string mening its not the same as "s" + obj  

// * arrays (same as python no type mattercand built ins for various operations)
// !NOTE: arrays are 0 indexed
let arr = [1, 2, 3, 4, 5];
console.log(arr[0]); // 1
console.log(arr.length); // 5
console.log(arr[arr.length - 1]); // 5  
console.log(arr[10]); // undefined  

// adding to arr
arr[5] = 6; // arr = [1, 2, 3, 4, 5, 6]; // adding to the end of the array
arr[7] = 7; // indexs in middel empty like so: arr = [1, 2, 3, 4, 5, 6, <empty item>, 7];
// real use 
arr[arr.length] = 8; // or use push (best) arr = [1, 2, 3, 4, 5, 6, <empty item>, 7, 8];

// deleting
let arr = [1, 2, 3, 4, 5];
delete arr[5];
console.log(arr); // [1, 2, 3, 4, <empty item>]

// to actually delete a element by index:
arr.splice(4, 1); // removes the element at index 4 the 1 means to remove 1 element arr = [1, 2, 3, 4]

let arr = [1, 2, 3, 4, 5];
console.log(arr); // [1, 2, 3, 4, 5]
// adding to array
arr.push(6);
console.log(arr); // [1, 2, 3, 4, 5, 6]
// removing from array
arr.pop();
console.log(arr); // [1, 2, 3, 4, 5]
// removing from beginning of array
arr.shift();
console.log(arr); // [2, 3, 4, 5]
// adding to beginning of array
// sorting array
arr.sort();
console.log(arr); // [1, 2, 3, 4, 5]
// reverse array
arr.reverse();
console.log(arr); // [5, 4, 3, 2, 1]


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

// * functions
// using function keyword
function funcname(arg1){
    console.log("passed "+arg1+" in function");
    // or return;
}
funcname(1); 

// * optional parameters
function funcname2(arg1, arg2 = 2){
    console.log("passed "+arg1+" in function");
    console.log("passed "+arg2+" in function");
    // or return;
}
funcname2(1);

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
// assigning functions to constants
myFunction4 = () => {
  console.log("Hello!");
  // console.log(this);  // `this` refers to the surrounding lexical scope
};
const myFunction4def = myFunction4();
myFunction4def; // Hello!
// we can also assign return values to constants
const myFunction5 = () => {
  return "Hello!";
};
const myFunction5def = myFunction5(); // const holds return value of function
console.log(myFunction5def); // Hello!/
// - returning multiple functions from a function
const myFunction6 = () => {
  return {
    func1: () => {
      console.log("func1");
      // can have a return value here as well
    },
    func2: () => console.log("func2") // in one line
  };
};
const myFunction6def = myFunction6();
myFunction6def.func1(); // func1
myFunction6def.func2(); // func2

// you can also directy return another function from a function like so 
// return function name() { return "Hello" }

// inline arrow funcs
let fn = (a, b, c) => {
    return a + b + c;
};
console.log(fn(1, 2, 3)); // 6

// you can also have functions be var and let with the difference being there not constant and can be changed later 
let myfunc = (name) => {
    return {
        mrname: () => {
            return "Mr" + name
        },
        msname: () => {
            return "Ms" + name
        }
     }
}

name = myfunc("ali")
console.log(name.mrname())

// *  function parametrs 
// optional parameters
const greet = (name, title = "Mr.") => {
    return `Hello ${title} ${name}`;
};

console.log(greet("Ali")); // Hello Mr. Ali
console.log(greet("Ali", "Dr.")); // Hello Dr. Ali

// NOTE: passing more or less then expected:
// If you pass fewer arguments than the function expects The missing ones become undefined.
function f(a, b) { console.log(a, b); }
f(10); // logs: 10 undefined
// If you pass more arguments than the function expects The extra ones are ignored.
function f(a) { console.log(a); }
f(10, 20, 30); // logs: 10
// or use const let or nothing like so 
fn = (x) => x + 1;
console.log(fn(5)); // 6

// how to keep a function variable throuout calls
// in this example we make a function with param n and store it in a variable
// we use this variable to call the same instance of the function where n is only initilized omce 
var createCounter = function(n) {
    
    return function() {
        return n++
    };
};
const counter = createCounter(0); // create a counter starting at 0
console.log(counter()); // 0
console.log(counter()); // 1
console.log(counter()); // 2

// passing a function to a function
// in this example we pass a function to another function and it will run the passed function
// here x is a number and fn is a function that dose a op on x and returns it 
function runOperation(n, fn) {
  return fn(n);
}
fn1 = (x) => x + 1; // fn must take in x and return whatever but it cannot do x[1] or stuff like that because we def x to be a number 
console.log(runOperation(5, fn1)); // 6
// etc

// JS function type hinting
// this feture allows the user to specify the types of parameters and return values for functions this is not enforced at runtime but can be used by IDEs for better autocompletion and error checking
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
function add(a, b) {
    return a + b;
}

// JS type casting
let num1 = "5";
num1 = Number(num1); // cast to number
console.log(num1 + 5); // 10
// cast into arr
let str1 = "1,2,3,4,5";
let arr = str1.split(","); // split string into array
console.log(arr); // ["1", "2", "3", "4", "5"]
// cast into obj
let str2 = '{"name": "John", "age": 30}';
let obj2 = JSON.parse(str2); // parse JSON string into object
console.log(obj2); // {name: "John", age: 30}

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

let iwant = "this is waht i want";
let nowant = "this is what i dont want";
let result_ = iwant != nowant ? "yes" : "NO";
console.log(result_); // yes

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
// add to a nester object, you cannot just add on like person.address.city.district = "x" you must use the correct syntax
person.address.city = {city: person.address.city, district: "Bronx"}
console.log(person.address.city) // { city: 'NYC', district: 'Bronx' }

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
// for in loop loops over the index of an iterable object as a string
for (let fruitindex in fruits) {
    console.log(fruitindex); // * 0, 1, 2 the index is a string not a number 
    console.log(fruits[fruitindex]); // apple, banana, cherry
}

// for in loop, a for 'of' loops cannot be used to iterate over objects as obj[0] DNE we must use the key not the index
let personloop = {name: "John", age: 30};
for (let key in personloop) {
    console.log(key + ": " + personloop[key]); // ex key = name, personloop[key] = personloop["name"] = John
}

// *  to cast a string to a number use parseInt() or parseFloat() to convert a string to a number or float

// do while loop lets the loop run once before checking the condition
let k = 0;
do {
    console.log(k);
    k++;
    } while (k < 10); 

// continue, break, pass, return
// continue - skip the rest of the current iteration and move to the next one
// break - exit the loop entirely
// return - exit the function and optionally return a value
//ex return
function example() {
    return 42;
}
// ex continue
function example() {
    for (let i = 0; i < 10; i++) {
        if (i === 5) {
            continue; // skip the rest of the current iteration
        }
        console.log(i);
    }
} // output: 0, 1, 2, 3, 4, 6, 7, 8, 9
// ex break
function example() {
    for (let i = 0; i < 10; i++) {
        if (i === 5) {
            break; // exit the loop entirely
        }
        console.log(i);
    }
} // output: 0, 1, 2, 3, 4


// * destructuring assignments ie making new variables from existing ones
// old way
const set = {x: 1, y:2, z:3};
const x = set.x;
const y = set.y;
const z = set.z;

// new way
// NOTE: the order of assignment matters 
const newset = {first: x,  second: y, third: z} // frist = x, second = y, third = z // here first is assigned to = x
/// NOTE: first dose not have to exist its not the assignment syntax ie assign empty val to some val its the order of the assignment
const {x: first, x: second, x: third} = newset; // first = x, second = x, third = x // here x is assigned to = first

// string formatting use "  `` "
const xval = 10;
const constString = `this is x: ${xval}`;
console.log(constString);

// * Error Handling
const errfunc = () => {
  try {
      // code that might throw an error
      throw new Error("This is an error"); // at any point in the code we can throw an error to the catch block
  } catch (error) {
      // code to handle the error we got here by 
      // either 1) there was a JS error or a failed promise in the try block or a error was thrown using Error() in the try block
      console.log("error was" +error) // error is the error object that was thrown from the try block using the Error class
  } finally {
      // code to be executed regardless of whether the try block throws an error or not
      console.log("err fin")
  }
}
errfunc()

// EX
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

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

// ex
class ArrayWrapper {
  constructor(nums) {
    this.nums = nums;
  }

  valueOf() {
    let total = 0;
    for (let i = 0; i < this.nums.length; i++) {
      total += this.nums[i];
    }
    return total;
  }

  toString() {
    return `[${this.nums.join(",")}]`;
  }
}

const obj4 = new ArrayWrapper([1, 2]);
const obj5 = new ArrayWrapper([3, 4]);

console.log(obj4 + obj5); // 10
console.log(String(obj4)); // "[1,2]"


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
// accsessing value of key
console.log(location.position?.lat); // if position DNE it will return undefined and wont give error for trying to get lat of something that DNE
// or using bracket notation
console.log(location["position"]?.lat);
// Ex2 using a prop that DNE
console.log(location.positionFormatted?.lat); // positionFormatted DNE so it will return undefined
// error checking with ??
console.log(location.positionFormatted ?? "LocationFormatted DNE"); // if positionFormatted DNE then return "Location DNE"
// geeting keys 
console.log(Object.keys(location)); // gets all keys into a array
// or use a for loop
for (let key in location) {
    console.log(key); // prints all keys of the object
    console.log(location[key]); // prints all values of the object
}
// adding key value pairs to an object, lets add a 'state'
location.state = "NY"; // adding a new key value pair to the object
// if we want a custom key value pair meaning we want to add state or city or etc we do 
const key = 'planet';
const value = 'earth';
location[key] = value; // adding a new key value pair to the object, since key is a var we cannot use it in the object i.e location.key
// removeing key value pairs from an object
delete location.state; // removing a key value pair from the object
// modifying key value pairs from an object
location.city = "LA"; // modifying a key value pair from the object
// increasing key value pairs from an object, lets add 1 to lat
location.position.lat += 1; // NOTE: you cannot have optional parameters when modifying key value pairs from an object

// modifing while checking using '?'
if ("street" in location) {
    location.street = "new street";
} else {
    console.log("DNE");
}
// or 
("street" in location)
    ? location.street = "new street"
    : console.log("DNE");
// or 
location.street === undefined ? console.log("DNE") : location.street = 'new street'; // since location.random would return undifined if random dose not exists 


// * Spread operator
// The spread operator (...) is used to expand an iterable object into individual elements
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combinedArr = [...arr1, ...arr2]; // this will combine the two arrays into one array but ...arr1 will spred all the elements of arr1 into the new array and so on
console.log(combinedArr); // [1, 2, 3, 4, 5, 6] each element is a new item
const combinedArr2 = [...arr1, 7, 8, 9]; // this will add 7, 8, 9 to the end of arr1 = [1, 2, 3, 7, 8, 9]
// this function takes in spred arguments meaning how ever many are given each will be added to the array as a new item
// so here the spred operater was used to unpack the arguments into an array
function mySpredFunction(...args) {
  console.log(args); // prints all arguments as an array
}
mySpredFunction(1, 2, 3); // Output: [1, 2, 3]
// for objects
const obj = { a: 1, b: 2 };
const newObj = { ...obj, c: 3 }; // this will add a new key value pair to the object
console.log(newObj); // Output: { a: 1, b: 2, c: 3 }

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
          // we can also throw an error here using the reject function but we can also use the Error class to throw an error
          if (success === false) {
            throw new Error("unsuccessful"); // this will throw an error to and the catch block or .catch will catch it and print the error = "unsuccessful"
          }
          // Resolve the promise with a success message
          resolve("Data fetched successfully!");
        } else {
          reject("Error fetching data.");
        }
      }, 1000); // Simulate a delay of 1 second
    });
};
  
// Using the Promise use .then to handle resolve and .catch to handle reject from the data
/* 
!! DO NOT ADD ';' AFTER THE FUNCTION CALL OR .THEN() ETC UNTIL THE END AS WE ARE NOT STOPPING THE FUNCTION CALL
 */
fetchData()
    .then((data) => console.log(data)) // Handles resolve
    .catch((error) => console.error(error)); // Handles reject

// Using async/await to handle the Promise
const getData = async () => {
    try {
      const data = await fetchData(); // Waits for the Promise to resolve
      console.log(data); // prints the resolved data = "Data fetched successfully!"
      if (data === "") {
        throw new Error("Data is empty");
      }
    } catch (error) {
      // Handles rejection i.e any Error if data is empty this will print the error which is the parameter passed to the Error class
      // But by default the error is the reject value passed to the reject function = "Error fetching data."
      console.error(error); 
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

// passing promises to a function
// in this example we pass in a single promise fetchdata1 2 3 and 3 sepetly to a function that takes in 1 promise and then logs the value of it 
const logPromiseValue = async (promise) => {
    try {
      const value = await promise;
      console.log(value);
    } catch (error) {
      console.error(error);
    }
  };
  
  logPromiseValue(fetchData1());
  logPromiseValue(fetchData2());
  logPromiseValue(fetchData3());

// passing a parameter to resolve
// in this ex we pass a parameter to resolve so we can do promise.resolve(2) and it prints the square of that number
const squarePromise = (num) => {
    return new Promise((resolve) => {
      resolve(num * num);
    });
  };

squarePromise(2).then((result) => console.log(result)); // 4

// processing many promise results 
// in this example we add the result from 2 promises
const addPromises = async (promise1, promise2) => {
    const result1 = await promise1;
    const result2 = await promise2;
    console.log(result1 + result2);
};

addPromises(squarePromise(2), squarePromise(3)); // Output: 13 (4 + 9) no need to do . then or anything the function handels that 
addPromises(Promise.resolve(2), Promise.resolve(3)); // Output: 5 (2 + 3) // using the Promise class we made 2 promises that resolve right way with a pre def value 

// clearing and setting timeouts
// EX: 
// here if cancel time is > timeout time the function will not run
// we have a timer set for 20ms and the cancel time is 50ms
// so since we return the cancel time right away it waits for 50 seconds before the function is called and the timeout is cleared and the timer is not ran
// but at the same time cancle function is returned the timer starts for time t and after time t it runs the function
// so since 20 ms passes before 50 ms the timer finished and executes + returns the value before cancleFn's 50ms timer is done and hence timer is not cleared 
let cancellable = function(fn, args, t) {
    // schedule fn to run
    const timer = setTimeout(() => {
        fn(...args);
    }, t);

    // return the cancel function
    return function cancelFn() {
        clearTimeout(timer);
    };
};
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => console.log(x * 5), [2], 20);
// cancel after 50ms
setTimeout(cancelFn, cancelTimeMs);

// set and clear interval
// in this example the interval function will run every second until cleared
// dont pass any function into the setInt rather pass a helper func
// here the function is ran for the first time after 1 second,  to run it immediently and then at a interval call the function once before starting the interval
const intervalFn = () => console.log("Interval running");
const intervalId = setInterval(intervalFn, 1000);

// clear the interval after 5 seconds
setTimeout(() => {
    clearInterval(intervalId);
    console.log("Interval cleared");
}, 5000);

// using Array.prototype methods
// ex one using a built in one:
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((n) => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
// making you own
// in this example i make a funciton that when used on any list retunes the last element 
/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
   return (this.length == 0) ? -1 : this[this.length -1]; 
};
const arr = [1, 2, 3];
arr.last(); // 3


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
Array.prototype.length // Returns the number of elements in an array not a function but a property
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