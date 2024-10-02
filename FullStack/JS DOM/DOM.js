// !!!! DO NOT RUN THIS CODE IN TERMINAL USING NODEJS ITS MENT FOR THE BROWSER!!!!

//! DOM is the Document Object Model its a JS object that contains all the HTML elements in the document so we can accsess and modify them, the html structure is a tree structure but we accsess it with DOM

// intro 

// so to acsess thesw elemets by id
// document.getElementById(""); // the document is a obj with properties and methods
// console .log on this would simply give back the html obj head -> head in html file this obj would include elements like titel body etc
// can aslo use dir but its the html obj is one big obj 
// we can also chnage the element by using the id like doc.titel = x

// Now what if we want users to change these objs
// lets change the username
let username = document.getElementById("username");
username.textContent = "Malik";

// using JS we accsessed and changed the username
// the dom obj is a big obj with properties and methods
// here we used DOM to change the username
// we can alos change style and otehr stuff

// DOM start 




