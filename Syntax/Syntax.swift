import SwiftUI

// * Struct Definition and @State Variable
// struct is a data structure and can contain properties and methods 
// the view is defined in the body of the struct adn allows us to display the screen
struct ContentView: View {
    // @State variable to hold a simple value
    // can be public private and be null at first
    @State var count: Int = 0
    
    // Body of the view
    var body: some View {
        VStack { // Vertical Stack
            Text("Count: \(count)")
                .padding()
            
            // Button to increment count
            Button(action: {
                count += 1 // Increment count
            }) {
                Text("Increment")
            }
            .foregroundColor(.white) // Button text color
            .background(Color.blue) // Button background color
            .cornerRadius(10) // Rounded corners
            
            // * Stacks and Layout
            // Here we explore various stack layouts
            
            ZStack { // Overlapping elements
                Color.green // Background color
                    .edgesIgnoringSafeArea(.all) // Extend to edges
                
                VStack { // Vertical Stack inside ZStack
                    HStack { // Horizontal Stack inside VStack
                        Text("Hello")
                        Spacer() // Spacer to push content apart
                        Text("World")
                    }
                    .padding() // Padding around the HStack
                    
                    // Additional content in VStack
                    Text("This is a VStack inside a ZStack")
                        .padding()
                }
            }
            .frame(maxWidth: .infinity, maxHeight: 300) // Limit the height of the ZStack
            
            // Additional content outside the ZStack
            Text("Below the ZStack")
        }
    }
}

// * View Type
// Some View protocol defines the body property of a SwiftUI View
extension ContentView {
    var body: some View {
        // Main Content
    }
}

// * Preview Content View
// This allows you to preview the UI in SwiftUI
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

// * Working with Images
// Example of adding an image to the view
Image("exampleImage") // Replace with your image name
    .resizable()
    .scaledToFit()
    .frame(width: 200, height: 200)

// * Working with Text
Text("Hello, World!")

// ! NOTE THE OPERATION SET IS SAME AS JAVA ie &&, ||, !, +, - etc

// * Conditionals
let number = 10
if number > 5 {
    print("Number is greater than 5")
} else {
    print("Number is 5 or less")
}

// * Switch Statements
switch number {
case 1:
    print("One")
case 2:
    print("Two")
default:
    print("Greater than Two")
}

// * Loops
// For Loop
for i in 1...5 {
    print(i)
}

// While Loop
var index = 0
while index < 5 {
    print(index)
    index += 1
}

// Do-While Loop
repeat {
    print(index)
    index -= 1
} while index > 0

// * Functions
// Function definition the return type is optional 
func greet(name: String) -> String {
    return "Hello, \(name)"
}

// * Classes and Object-Oriented Programming
class Animal {
    var name: String
    
    // Initializer
    init(name: String) {
        self.name = name
    }
    
    func speak() {
        print("\(name) says hello!")
    }
}

// Class Inheritance
class Dog: Animal {
    override func speak() {
        print("\(name) barks!")
    }
}

// Creating objects
let dog = Dog(name: "Buddy")
dog.speak() // Output: Buddy barks!

// * Data Types
var myInt: Int = 10 // Integer
let myDouble: Double = 20.5 // Double
let myString: String = "Hello" // String
static let pi: Double = 3.14 // Static constant

// * Arrays
var numbers: [Int] = [1, 2, 3, 4, 5]
numbers.append(6) // Adding an element

// * Dictionaries
var person: [String: String] = ["name": "John", "age": "30"]
let name = person["name"] // Accessing a value

// ! var vs let in Swift 
// a var is mutable and a let is immutable meaning it can't be changed

// * Enums
// Enums allow you to define a group of related values
enum Direction {
    case north
    case south
    case east
    case west
}

var currentDirection = Direction.north
switch currentDirection {
case .north:
    print("Heading North")
case .south:
    print("Heading South")
default:
    print("Heading East or West")
}

// * Sets
// Sets are unordered collections of unique values
var fruits: Set<String> = ["Apple", "Banana", "Orange"]
fruits.insert("Mango") // Adding an item
fruits.remove("Banana") // Removing an item
print(fruits.contains("Apple")) // Checking for membership

// * if let (Optional Binding)
// Used to safely unwrap optionals
var name: String? = "John"
if let unwrappedName = name {
    print("Hello, \(unwrappedName)")
} else {
    print("No name provided")
}

// * Nil Coalescing Operator
// Provides a default value if the optional is nil
let defaultName = name ?? "Guest" // If name is nil, use "Guest"

// * Guard Statement
// Used to exit early if a condition is not met
func greet(person: String?) {
    guard let unwrappedPerson = person else {
        print("No person provided")
        return
    }
    print("Hello, \(unwrappedPerson)")
}

// * Force Unwrapping
// Using an exclamation mark (!) to force unwrap an optional
let forcedName: String = name!

// * Extensions
// Extensions allow you to add functionality to existing types
extension Int {
    func squared() -> Int {
        return self * self
    }
}

let number = 4
print(number.squared()) // Prints 16
