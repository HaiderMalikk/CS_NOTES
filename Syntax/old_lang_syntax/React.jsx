// ! React JS is a JavaScript library used for building user interfaces, particularly single-page applications.
// ! JSX is a syntax extension that allows you to write HTML-like code inside JavaScript. It looks like HTML but has the full power of JavaScript. !

// ! THIS IS ONLY EXAMPLES OF SYNTAX THE REAL PROSIBLITIES OF CREATING THINGS ARE ENDLESS

// * JSX
const element = <h1>Hello, world!</h1>; // this is JSX syntax here this code makes a h1 tag with text Hello, world!

// * Props and Componenets 
// components are functions or classes that return JSX menaing they return HTML they are also reuseable
// props are data passed to a component from the parent
// here the parent conmonent creates the child component and specifies the message and name
// the prop passef in child compoent is message and name respectively using '.' we can accsess the props name and message
function ChildComponent(props) {
    return (
        <div>
            <h1>{props.message}</h1>
            <p>{props.name}</p>
        </div>
    );
}

function ParentComponent() {
    return <ChildComponent message="Hello, World!" name="John Doe" />;
}

// class component
class Welcome extends React.Component {
    render() {
      return <h1>Hello, {this.props.name}</h1>;
    }
}

// * states
import React, { useState } from 'react'; // ex of a import in react
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

// * Events
function handleClick() {
    alert('Button clicked!');
  }
  
return <button onClick={handleClick}>Click me</button>;

// * conditional rendering (rendering componets only if the condition is true)
function Greeting(props) {
    if (props.isLoggedIn) {
      return <h1>Welcome back!</h1>;
    } else {
      return <h1>Please sign in.</h1>;
    }
}

// * lists and keys 
// When rendering lists of elements, React requires a special key prop to efficiently update and render elements.
// here we use a map function to create a new list of elements with a unique key for each item.
// the code will loop through the items array and create a new list item for each item in the array and assign a unique key to each item.
// now we can use the key prop in the <li> element to identify each item in the list.
const items = ['Apple', 'Banana', 'Orange'];
const listItems = items.map((item, index) =>
  <li key={index}>{item}</li>
);



