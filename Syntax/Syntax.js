// Javascript intro and syntax
// JS6 syntax and features
// ! the ';'  is not needed in js but is good practice

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
// * functions can be nested you can return functions and tehy can have default parameters
if (num = 10){
    console.log("num is 10");
}
else if  (num > 10 ||  num < 10 &&  num != 10){
    console.log("num is greater than 10");
    let str = "or"
    let number = 1
    return number || str; // if number DNE then return str
}
else{
    console.log("num is less than 10");
}

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

// * arrow functions 
// format is function name = (arg1, arg2) => {return arg1 + arg2}   // can also specify return type and function type
add = (a, b) => {return a + b}
console.log(add(1, 2));

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

// for of loop
let fruits = ["apple", "banana", "cherry"];
for (let fruit of fruits) {
    console.log(fruit);
}

// for in loop
let personloop = {name: "John", age: 30};
for (let key in personloop) {
    console.log(key + ": " + personloop[key]);
}

// do while loop
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
const constString = `this is x: $ {constString}`;
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
const person = new Person();
console.log(person.greet());