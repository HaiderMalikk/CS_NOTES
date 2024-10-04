// !!!! DO NOT RUN THIS CODE IN TERMINAL USING NODEJS ITS MENT FOR THE BROWSER!!!!

//! DOM is the Document Object Model its a JS object that contains all the HTML elements in the document so we can accsess and modify them, the html structure is a tree structure but we accsess it with DOM
// ! we can change 'DOM' ie objects of a website like change the theme or press a button and do something ETC
// ! in teh first example we accsessed the username ie changed the h1 object
// ! Document node is parent node of all the other nodes

// intro 

// so to acsess thesw elemets by id
// document.getElementById(""); // the document is a obj with properties and methods
// console .log on this would simply give back the html obj head -> head in html file this obj would include elements like titel body etc
// can aslo use dir but its the html obj is one big obj 
// we can also chnage the element by using the id like doc.titel = x

// Now what if we want users to change these objs
// lets change the username
// let username = document.getElementById("username");
// username.textContent = "Malik";

// using JS we accsessed and changed the username
// the dom obj is a big obj with properties and methods
// here we used DOM to change the username
// we can alos change style and otehr stuff

// DOM start 

// * methods of selecting dom elements

// Get elements by id (returns single element)
const option1 = document.getElementById('football');
console.log(option1);

// get elements by class (returns a array of elements)
const option2 = document.getElementsByClassName('basketball');
console.log(option2);

// get elements by tag (returns a array of elements with same tag)
const classli = document.getElementsByTagName('li');
console.log(classli);

// query selector (can get div tag class etc) get sfirst element that matches selector here div h4
const queryselect = document.querySelector('div');
console.log(queryselect);

// query selector all (selects all the elements that match the selector here all the divs)
const  querySelectAll = document.querySelectorAll('div');
console.log(querySelectAll);

// * changing styling of html

option1.style.color = 'red'; // chaning the color of the element (inline selecting dose not work with list iteams we must loop through them)

for (i=0 ; i < classli.length; i++){
    classli[i].style.color = 'red';
}

// creating elements
const ul = document.querySelector('ul'); // get the ul tag
const li = document.createElement('li'); // create a new li tag NOT IN HTML

// apending element li to ul
ul.append(li);
//adding text to li
li.textContent = "Swimming";  // adding text there are other methods
// print li to console
console.log(li);

// modifing html attributes and classes
li.id = 'swimming';
li.setAttribute('id', 'swimming');
li.setAttribute('class', 'newIteam')
li.removeAttribute('class') // removing property class
li.classList.add('container'); // setting class so now li has class container so its inside class contanor so if we modify the class it will change

// getting all new li's so we can change new colour
const liList = document.getElementsByTagName('li');
console.log(liList);
// cahne all colors in conataer to blue
for (i=0 ; i < liList.length; i++){
    liList[i].style.color = 'blue';
}

// removing elemets
li.remove(); // removes last element here it was swimming



