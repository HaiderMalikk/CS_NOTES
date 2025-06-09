// ! .tsx stands for TypeScript JSX and is used for React components written in TypeScript instead of plain JavaScript.
// ! TypeScript is a superset of JavaScript meaning its all of javascript plus more, note at runtime it is still JavaScript

// ! NOTE: React is a library and not a framework you must have react installed to use typescript in react
// ! IN THIS FILE A ERROR IS GIVEN BEACUSE OF THAT BUT THIS INS JUST FOR SYNTAX EXAMPLES NOT TO COMPILE

import React from 'react';

// * TSX

// * type anotation
// In .tsx files, you can (and should) define types for your component props, state, and other variables.
// a interface is a type that describes the structure of an object
interface GreetingProps {
    name: string;
    age?: number; // Optional prop
  }
  
  function Greeting(props: GreetingProps) {
    return <h1>Hello, {props.name}!</h1>;
}

// * typescript types for props and state
import React, { useState } from 'react'; // example of import 

function Counter() {
  // here we use hooks in react NOTE THAT YOU CAN ONLY PASS ONE PARAMETER FOR THE FUNCTION USING useState
  // here the count is the var the setcount is the function 
  // This uses array destructuring to assign names to the two elements returned by useState. so the part 'const [count, setCount]'
  // The <number> after useState is a TypeScript type annotation that tells TypeScript that the state variable count is type number and innitially is 0.
  // and it says that setcount is a function that takes a number
  // so when we use count it will be a nmber variable and for set count we can pass any number in its argument 
  const [count, setCount] = useState<number>(0); 

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}

// class ex
import React from 'react';

// Define the state interface
interface CounterState {
    count: number; // The state will hold a single property 'count' of type number
}

class Counter2 extends React.Component<{}, CounterState> {
    // The Counter2 class extends React.Component, which allows it to use lifecycle methods and manage state.
    // The first generic type '{}' indicates that this component does not expect any props.
    // The second generic type 'CounterState' specifies the shape of the component's state.
    
    constructor(props: {}) {
        super(props); // Call the constructor of the parent class (React.Component)
        this.state = { count: 0 }; // Initialize the state with 'count' set to 0
    }

    render() {
        return (
            <div>
                <p>You clicked {this.state.count} times</p> {/* Display the current count value */}
                <button onClick={() => this.setState({ count: this.state.count + 1 })}>
                    Click me {/* Button to increment the count */}
                </button>
            </div>
        );
    }
}

export default Counter2; // Export the Counter2 component for use in other files

// * optinal props
interface UserProps {
    name: string;
    age?: number; // Optional prop
  }
  
  function User({ name, age }: UserProps) {
    return (
      <div>
        <p>{name}</p>
        {age && <p>Age: {age}</p>}
      </div>
    );
}
  
// * default props 
interface ButtonProps {
    label: string;
    size?: 'small' | 'medium' | 'large'; // Optional with specific allowed values
}
  
  const Button = ({ label, size = 'medium' }: ButtonProps) => (
    <button className={`btn-${size}`}>{label}</button>
);
  
// * elemets with ts
import React from 'react';

const MyComponent = () => {
    // Define the click handler
    function handleClick(event: React.MouseEvent<HTMLButtonElement>) {
        console.log(event.currentTarget); // Logs the button element
    }

    // Return the JSX that should be rendered
    return (
        <button onClick={handleClick}>Click me</button>
    );
};

export default MyComponent; // Export the component for use in other files

// Strict typing
//TypeScript ensures that your JSX follows the correct structure and that props are passed with the correct types
interface InputProps {
    value: string;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  }
  
  function TextInput({ value, onChange }: InputProps) {
    return <input type="text" value={value} onChange={onChange} />;
}

