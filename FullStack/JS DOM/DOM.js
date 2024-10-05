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
// WE CAN ALSO DO THIS WITH CLASS NAME GIVEN INSIDE A NODE using '.classname'
// ! const queryselect = document.querySelector('.button'); // here button is a class name


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

// DOM NODES AND TREE (in the picture in file all elements like h1 titel etc are nodes in the DOM tree)
// Document is root node element everything else i are children or siblings
// * HOW to traverse DOM tree

// Parent node traversal (upwards)
// NODE vs ELEMENT
// a node is nothing but an object that contains properties and methods
// a element is type of node that contains properties and methods
// NOTE hmtl tag has no parent element but it has a parent node
// ! A node is the object itself the element is the property of the node ie h1 is a node h1's text is a element

let ul1 = document.querySelector('ul');
console.log(ul1.parentNode); // will print our parent of ul which is div contaner 
console.log(ul1.parentElement); // with node gives us the nob
// to go back twice 
console.log(ul1.parentNode.parentNode); // prints body as 2 levels up from ul is body, so ul->div->body
// to get the highest parent
console.log(document.documentElement); // prints html the start of the tree

// child node traversal (downwards)
let ul2 = document.querySelector('ul');
console.log(ul2.childNodes); // prints all the child nodes of ul ie all li
//  return just test '' as its a text node and not an element
console.log(ul2.firstChild); // fist node of ul
console.log(ul2.lastChild); // last node of ul

// to overcome modifying the child node
ul2.firstElementChild.style.color = 'red';
// to do this by index
ul2.childNodes[1].style.color = 'red';

// to get all the child elements
console.log(ul2.children); // prints all the child elements of ul ie all li we can now modify this too

// Sibling node traversal (same level) h4 and ul are siblings 
let ul3 = document.querySelector('ul');
console.log(ul3.previousSibling); // prints text node as h1 is a text node
console.log(ul3.nextSibling); // prints text node but is null as no next sibling

// to print the values ie get elements
console.log(ul3.previousElementSibling); // prints h1
console.log(ul3.nextElementSibling); // prints null as no next sibling


// * EVENT LISTENERS
// alows us to listen for events ie when an element is clicked like when a button is clicked
// we can add multiple event listeners

// add event listener (first methdo in directly in the htlm file like onclick at div1)

// ADD event using js
// form: element.addEventlistner(typeofevent, function to do, true or false) // defult is false event can be like click element can be like div
const button = document.querySelector('.button');
function handleClick(){
    alert('I was clicked with JS');
}
button.addEventListener('click', handleClick);

// Mouse Events
const button2 = document.querySelector('.button2');
function handleMouseOver(){
    button2.style.backgroundColor = 'red';
}
button2.addEventListener('mouseover', handleMouseOver);
// lets now make it so the colour will change back
function handleMouseOut(){
    button2.style.backgroundColor = 'green';
}
button2.addEventListener('mouseout', handleMouseOut);


// * Reveling hidden elements
// NOTE FRO THIS WE STILL HAVE TO HIDE TEXT IN HTML see end of style in HTML 
// here we will click a button to reveal text
const revealBTN = document.querySelector('.reveal-btn');
const HiddenContnet = document.querySelector('.hidden-content');

// call back function which will be called when button is clicked
// will cheack if hidden content has class of reveal button

// EXPLINATION: when we call click listen it will check if class list has class revealbtn
// if it dose it will remove it if not it will add it to the class list
// the class list has all the classes and by adding to it we add to the HTML
// NOTE: the funtion only runs when we click 
function handleReveal(){
    if(HiddenContnet.classList.contains('reveal-btn')){
        HiddenContnet.classList.remove('reveal-btn');
    }else{
        HiddenContnet.classList.add('reveal-btn');
    }
}
revealBTN.addEventListener('click', handleReveal);



// * EVENT Propigation
// An event that goes throug all the nodes in the dom until it reaches the target node or the root node or its stopped 
// NOTE: event bubbling and event propagation are the same thing
// three phases (note that the event will progitage from root to target the root is the highest node ie document)
// 1) event capturing (starts from root to the target and tells all nodes under as its travaling that some button is being clicked for EX, here that button is the target)
// 2) targeting (reaches the target, here target phase it triggerd and stuff happens)
// 3) event bubbling (starts from target to the root notifying all nodes that its done and stuff happened)

// add event listners for elements note we make a function to call back
//! the thrid parameter is true it allows to chose event capture or bubbling as its true this mean event capturing
//! if we set the boolean to false it will allow event bubbling and we will travel from click back to root
//! here we will manually stop propigation at div 4
//! we can also skip document the second time using once: true so its true once on second time we will skip it
window.addEventListener('click', function(){
    console.log('window');
}, true); 

document.addEventListener('click', function(){
    console.log('document');
}, {once: true});

document.querySelector(".div4").addEventListener("click", function(e){
    e.stopPropagation()
    console.log('div4');
}, true);

document.querySelector(".div3").addEventListener("click", function(){
    console.log('div3');
}, true);

// e is the event obj it holds all teh info about the event
document.querySelector(".EventButton").addEventListener("click", function(e){
    console.log(e.target.innerText = "Clicked"); // the target is the element that triggered the event here we change the text upon click
}, true);
// on click we will get info anout event and where it was triggered etc


// * EVENT Delegation
// !we can add event listners to parent element and then it will add that event listner to all current and future child elements
// lets do this with the ul element so we can add event listner to all of its childer ie li (list iteam)
// we can add the listner to each child element ie list iteam or we can add it to the parent element ul 

// lets look at cahnging the bg color of one li football
// document.querySelector ('#football').addEventListener('click', function(e){
//     console.log('football clicked');
//     const target = e.target;
//     if(target.matches('li')){
//         target.style.backgroundColor = 'lightgrey';
//     }
// },);
// now we can chose to copy thos fro every li or use event delegation 
// so we will apply it to the parent element so that everytime li is clicked it will bubble up to ul and change the bg color this way we can do it for every li 

// here when our target the list iteams inside sport which all have a attribute id, when its clicked we will display that id so ex football and from that we can also change the bg color
document.querySelector('#sports').addEventListener('click', function(e){
    console.log(e.target.getAttribute('id') + ' is clicked');
    const target = e.target;
    if(target.matches('li')){
        target.style.backgroundColor = 'lightgrey';
    }

})

// note that this will aplly to future child elements lets make one this will have the same effect as for the elements above
const sports = document.querySelector('#sports');
const newSport = document.createElement('li');
newSport.innerText = 'Hockey';
newSport.setAttribute('id', 'hockey');
sports.appendChild(newSport);
