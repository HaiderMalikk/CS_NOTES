package Java.OOP;

import java.util.Scanner;

// !old notes -------------------------------------------------------------------------------------
public class OOP_Basics{} // to fix errors the rest of the file is not made of public classes so when you press run you can choose what class to run

// a object in a tangeble thing that like a pen, ball
// but even a bank account is a object even though you cant touch it 
// but bank has properties money, owner. it also has actions that it can preform 
// you can have methods to preform actions ect widraw and deposit money
// object has identity properties behaviour states but all are uniqe 
// OOP or object oriented programing is based on the concenpt of objects
// many programs are written to do things taht concern the real world
// software objects are like real life objects
// to code a bank acounts records() a object ) someone had to use OPP
// OPP makes programing easier it prevents long codes and allows to split up code in diffrent files
// objects identite(name) state(vars) and behaviour(methods) is stored in memory  
// you need a main method !!!
// it was fine at first to only use the main method 
//For an application, the first method to run is the method named main(). 
//There should be only one method named main() in an application. 
//In a small application, main() might do by itself all the computation that needs to be done. 
//In a larger application, main() will create objects and use their methods.
// you need framework imagine a car fetures come later firt comes body
// you need framework to define the identity behavour state
// frameworks are known as class in java
// classes create a object then we give the object values
// classes are used to make objects mostly 
// static is a type of method
// if a class has methods not shared by the object it creates its a static method
// use static for basic things like 
// a instance is a type of methods a constructer 
// object is instance of class the only time you can use instance method is when you use a object

 

    // create variables of the class
    // none are static, so each Car object we create will have their own copy of these variables

    // empty var
    /* class vars can be used anywhere in var */
class Car{
    String carMake;
    String carModel;
    String carColor;
    int carYear;
    // these 2 vars are not empty and have a pre determined value so they will not be innitilized
    boolean fillUp = false; // all car objects will have a full tank of gas
    int kmTravelled = 0; // all car objects will have travelled 0 km to start


    // Car constructors
    /*
    a comstructor initilizes attributes so we can make onjects using it 
    This special method is used when we create (also known as instantiate) a car object
    Take the variables we just defined, and get their
    values based on the parameters given to the constructor when the object
    is created.
    */
    // constructer gives empty var a value
    /* the args are all method vars and can be used in this method only */
    public Car(String make, String model, String color, int year){
        /* this is a local var can be used in method only */
        carMake = make; // this keyword is optional but in cases where both local and class var have the same name it is used to avoid confusion
        carModel = model;
        carColor = color;   
        carYear = year; 
    }
    
    // a simple method that will indicate the gas tank needs filling
    public void fillGasTank() {
       if (fillUp == true) {
        fillUp = false;
        System.out.println("Gas tank is now full!");
       }

    }

    public void travel() {
        kmTravelled += 2;
        System.out.println(carMake+" "+carModel+" has travelled 2km!");
        System.out.println("Your total distance travelled is now "+kmTravelled+"km");

        if(kmTravelled % 5 == 0) {
            fillUp = true;
            System.out.println("You have run out of gas! Time to fill up.");
        }
    }

    public String toString() {
        return "Car Make: "+carMake+"\nCar Model: "+carModel;
    }

    public static void main(String[] args) {
        // create an object // beetle points to memory //new creates new object //
        // NOTE: beetle is ref type var is points to memory you can change ut to another ref type like beetle = beetle 2 if beetle 2 also a ref type made using a constructor
        Car beetle = new Car("Volkswagen", "Beetle","orange",2004);
        Car rondo = new Car("Kia","Rondo","grey",2011);

        System.out.println(beetle);

        rondo.travel();

        for(int i=0; i < 5; i++) { // travel 10 km
            beetle.travel();
        }

       beetle.fillGasTank(); // reset the gas tank

       beetle.travel(); // continue travelling

       rondo.travel(); // rondo travels
    }
}

// EX 2 PERSON
// CONSTRUCTER looks like this classname(vars) it creates the object
// then we can use the "this" function to assign stuff it help java know what object 
//ex int age; in constructer this.age = age then defien age as a paramiter when calling constructer 
// to change this.age = this.age + 1 but in constructer you can do this.age = age+1

class Person {

    String name;
    int age;
    String occupation;

    //constructer name must = class name
    Person(String name, int age, String occupation) {
        this.name = name;
        this.age = age;
        this.occupation = occupation;
    }

    // to string prints value of string insted of memory location
    public String toString() {
        return "This person's name is "+this.name;
    }
    
    public void sleep() {
        System.out.println(this.name+" falls asleep for 8 hours!");
    }

    public void eat() {
        System.out.println(this.name+" has paused for a snack.");
    }

    
    public static void main(String[] args) {
        Person p1 = new Person("Haider",28,"student");
        Person p2 = new Person("Talal",25,"data scientist");

        System.out.println(p1);
        System.out.println(p2);

        p1.sleep();
        p2.sleep();

        p2.eat();
    }
}

class Dog {
    
    // creating our vars for dog
    String name;
    String breed;
    int age;
    String gender;
    String bark = "Woof"; // this var has a default value ie the value is alredy given to it its not chnaged so its not initilized in constructor
    String size;

    // constructer 
    // in this constructer we create a new vars that match with the vars for dogs 
    // we dont use bark as that is a phrase its alredy defined 
    // we use the "this" method to give the empty strings a value. this.parameter = var for dog
    public Dog(String name, String breed, int age, String gender, String size) {
        this.name = name;
        this.breed = breed;
        this.age = age;
        this.gender = gender;
        this.size = size;
    }

    // method you can look at this as a function it dose something 
    // this method takes name + bark 
    // to print this you would have to call method
    public String greeting() {
        return name+" says "+bark;
    }

    // this method takes name + bread but calling the method toString converts it to string
    public String toString() {
        return "The dog's name is "+name+". The dog's breed is "+breed+".";
    }
    // main method
    public static void main(String[] args){
        // this is the actual object the format is classname varname = new Objectnamefromconstructer (parameters)
        // the new keyword creates a new object
        // parameters correspond to the constructer
        Dog chris = new Dog("Chris","Chihuahua",50,"female","small");

        // dose not acctually print the object the object it self just has arguments 
        // you need methods to do stuff with those arguments now that the vars are defined to arguments 
        // chris prints the toString that is default 
        // to print other thngs you have to name your method Ex chris.greeting the program auto converts to string
        System.out.println(chris);
        System.out.println(chris.greeting());
    }
}

class Bank{

    String fristname;
    String lastname; 
    int age;
    double limit = 1000;
    double balance;
    boolean activation;

    public Bank(String firstname, String lastname, int age, double balance){
        this.fristname = firstname;
        this.lastname = lastname;
        this.age = age;
        this.balance = balance;
    }

    public String greeting(){
        return "Hello " + fristname +" "+ lastname + " welcome to the bank";
    }

    public String currentbalance(String balancetype) {
        return "Your " +balancetype+ " is: "+ balance; 
    }

    public double addfunds(double ammountadd){
        double deposit = ammountadd;
        System.out.println("you deposited: "+deposit+"$");
        return balance += deposit;
    }

    public String accountactivation() {
        String message = "Acount Active: ";
        String messagebad = ", Reason: OVER LIMIT WITHDRAW MONEY";
        if (balance > limit) {
            return message + "false" + messagebad; 
        } else {
            return message + "true";
        }
    }

    public Double Withdraw(Double ammoutwithdraw){
        double withdraw = ammoutwithdraw;
        System.out.println("you withdrawed: "+withdraw+"$");
        return balance -= withdraw;
    }

    public static void main(String[] args){

    Bank banker = new Bank("Haider", "Malik", 18, 950.0);

    System.out.println(banker.greeting());
    System.out.println(banker.currentbalance("current balance"));
    System.out.println(banker.accountactivation());
    System.out.println(""); // space new line

    // add funds this adds funds to balance but the new balance has to printed to show the added funds
    banker.addfunds(50.0);
    // new updated balance 
    System.out.println(banker.currentbalance("new balance"));
    System.out.println(banker.accountactivation());
    System.out.println(""); // space new line

    banker.addfunds(50.0);
    // new updated balance 
    System.out.println(banker.currentbalance("new balance"));
    System.out.println(banker.accountactivation());
    System.out.println(""); // space new line

    banker.Withdraw(500.00);
    System.out.println(banker.currentbalance("new balance"));
    System.out.println(banker.accountactivation());

    }

}



/* //!---------------------------------------------------------------------------------------------------------------- */
// !NEW NOTES


/* 
*  NOTE: "this" keyword is used when the name of new initilized variable is the same this see var shawdow for what 'this' dose
// a example is carMake = make the new globaly used var is make and it has a different name than carmake the initial variable 
// the "this" keyword is used for something like this.carmake = carmake
// the constructor just intilizes the values on class vars so we can pass them by calling the method and they update the class vars so everyone has the same values
* constructors always public 
 // note that constructors dont alwasys just initilize variables they can do other things like increment a counter create a array etc
*/

/* 
 * == vs .equals
 for ref type == checks the address in memory is same .equals checks the actual value ie the string or int inside
 for primitive
 == checks the value .equals is not used for primitive
*/

/* 
* Accsessor (getters) is a method that returns a value but dosent change any attributes ex int w = j.getbmi // here getbmi will return value, these methods cannot be used as values, has anything but void return
* Mutator (setters) is a method that changes a value but returns nothing ex jim.setweight(80) // here setweight will change weight not return it, these methods cannot not be used as values, has only void return

*/

/* 
* Null pointer exeption NPE
you are trying to call a method on a null object or a objects methods 
ie if you do jim.getheight and gethight dne this will give NPE
if you do obj1.x and obj one DNE or is not def then its a NPE
if you have obj1.m3.m2.m1 if obj1 is null as it DNE you get NPE for trying to get obj1.m3
if obj1 exits but m3 null you get NPE for trying to get m2.m1
if obj1.m3 exits but m2 null NPE for m1 
but if everything but m1 null then you will only get NPE if you try to accsess something from m1

*/

/*         
* refrence alising = copying refrence values
i could also do Product p3 = p2 all this dose is copy the address of p2 to p3 now both p2, p3 point to same address but now any change made to p2 will be reflected in p3 and vise versa as they share the same object in memeory 

// you can also store objects into array indexs to index 0 of a array can point to a object in memory so you can accsess that object as obj1.etc or arraywithobj[0].etc

/*
 * variable shawowing means that method or class etc has a shadow over the variable ie it can only be used in that class method etc
 to use it outside its shawdow we use the this keyword for methods allwing method variables to be accsessed in class
 */


// * in class example making objs in methods
class Point{
    int y;
    int x;
    public Point(int x, int y){
        this.x = x; // this refers to current obj, so for any object this.x gets the class var x and assigns it the value of x passed through the constructor upon creation of the obj
        this.y = y;
    }

    public void moveUp(int y){
        // when a obj calles this method the class level var is updated to y, here the class lvl var is accesible as we are in the class
        // BUT we use this keyword to specify that we want to update the class var and to avoid shadowing 
        this.y = y; // ! mutator only sets value
    }

    public Point moveUpBy(int i){
        Point newPoint = new Point(this.x, this.y); // creates a new obj of point with x and y from class vars hence this keyword was used Note that x and y were set in the main method and were passed throug the Point constructor witch then set the variables in the class using the this keyword
        newPoint.moveUp(i); // the newPoint had same values for its parameters as the lastest point objs values but there not the same obj new keyword makes a new obj so they dont have the same address
        return newPoint; // ! accesor must return 

    }

    public int getycor() {
        return this.y;
    }

    public static void main(String[] args) {
        Point p1 = new Point(1, 2);
        p1.moveUp(2);
        Point p2 = p1.moveUpBy(2);
        System.out.println(p1 == p2); // false
        System.out.println(p1.getycor() == p2.getycor()); // true

    }
}

/* 
* HELPER METHODS

In Java, helper methods are small utility methods that help perform common tasks or calculations within a class. 
These methods are typically private, though they can be public if meant to be accessed from outside the class\
basicaly helper methods help other methods preform a task, calculation, validation etc

in the following example add and multiply methods are helper methods
they help the addandMultiply method preform its task
the main methods can use a helper method to preform a task or just return its value 
*/

class Calculator {

// Public method that uses helper methods
public int addAndMultiply(int a, int b, int multiplier) {
    int sum = add(a, b); // calling helper method
    return multiply(sum, multiplier); // calling helper method
}

// Private helper method for addition
// this helper method is a accesor
private int add(int x, int y) {
    return x + y;
}

// Private helper method for multiplication
private int multiply(int x, int y) {
    return x * y;
}

public static void main(String[] args) {
    Calculator calc = new Calculator();
    System.out.println(calc.addAndMultiply(2, 3, 4)); // Output: 20
}
}


/*  
* anonomous objects */
/* In Java, anonymous objects are objects that are created and used without being explicitly assigned to a variable. 
They're typically used when you only need the object for a short period of time, such as passing
 it to a method or performing an action without needing to reference the object later. */
class MyPersonAnonymous {
    public String name;

    public MyPersonAnonymous(String name) {
        this.name = name;
    }

    public void greet() {
        System.out.println("Hello, my name is " + name);
    }

    public static void main(String[] args) {
        // Anonymous object: no reference to the object is created (can only call once here)
        new MyPersonAnonymous("John").greet(); // This creates the object, calls greet(), and discards the object - here we used the constructor as a method without specifiying class and var name ie no ref to obj

        // Non-anonymous object: the object is assigned to a variable ie i use the class 
        MyPersonAnonymous jane = new MyPersonAnonymous("Jane");
        jane.greet(); // Can call greet multiple times because we have a reference to the object
    }
}


// * refrence to this keyword 
// ! Note when using areguemnts passed through objs here its 'other', you can use the 'this' keywork to refer to the current obj
// ! meanign when you make the object the 'this' will refer to the object the methid in called on while the argument here 'other' will refer to the other obj which was passed as arg in this case 
// ! meaning java knows the context object here the context of other is jim so for elsa and amy they both refer to jim meanig 'this' for them is jim here
class MyPerson{
    public String name;
    public MyPerson spouse; // making a peson obj called spouse
    public MyPerson(String name){
        this.name = name;
    }

    public void marry(MyPerson other){
        // to check if marrage legal check if ethier maried logic. not p or not p = not(p and q)
        if (this.spouse != null || other.spouse != null ) {
            System.out.println("You are already married cannot marry: "+ other);
        }
        else{
            // note that this refers to current obj and spouse is a class lvl var so this.spouse refers to the class var spouce 
            this.spouse = other; // ! this refers to current obj so at first this is jim.spouse, java knows the context obj here the context of other is jim
            other.spouse = this;
        }

    }

    // the to string converts the obj address to string, here in the sout in if block in marry prints the address
    // but with this to string it will print the name of the person obj
    public String toString() {
        return name.toString();
    }
    public static void main(String[] args) {
        MyPerson jim = new MyPerson("jim");
        MyPerson elsa = new MyPerson("elsa");
        MyPerson amy = new MyPerson("amy");
        jim.marry(elsa); // elsa is other
        jim.marry(amy);
        // note spouce and name are bot hpublic so we can accsess them like this jim.spouse.name
        System.out.println(jim.spouse.name); // elsa is output, note that elsa the obj was assigned to the obj spouce using the marry method, now if we use the .spouce it will accsess jim objs wife obj, by using .name i accsess the obj spouces name that was set when we made the elsa obj, jim.spuce points to jims wife attribute that attribute goes to wife obj
    }
}

// * global vars i.e static variables
/* 
global variables are variables that are shared by all obj of the class. meaning when you create them they will be part of all the objects created with that class
this means all objs can do: obj.globalvar and it will return the same value for all objs of the class
we can change the global var but it will then be updated for all new objects made after the change
to create a global var use static variable
 */

// * Static Variables and methods
/* 
/ static method belongs to class not the object the class creates 
 every obj has diffrent variables thast passed in its paramater , but static variables are shared by all obj of the class as the same variable 
 but you can modify so that objs have diffrent versions of the static variable
 EX:in the constructor: x = staticvar, static counter ++, now each time a new obj is made 
 the static counter will be incremented and each obj will have its own version of the static counter, but if ++ was not done they would all have x = static var
 make sure x is not a static var too as that will make it shared by all obj and we want x to be different for all objs ie they all have obj.x = a different value
 Why not use a regular variable 1) you cant accsess and modify it as part of the obj, 2) you dont need to set it its set by defualt
 the static counter would be shared by all obj so it would be the same for all objs
 note that the static var is global meaning it must be initilized right away, and it is shared by all obj of the class
 for local varable you can declare and initilize in any order and anywhere in constructor 
 you can change the static variable anytime just like local varable but the change will be reflected in all obj of the class
 in local variable the change of the var will only be reflected in the obj that the var belongs to 
 with mutating method you can modify static var like a local varable
 but! you would not use 'this' you simply use the var name
 to call it outisde your class you would do classname.staticvarname = ....
 ! NOTE: you cannot use non-static var in a static method but you can use any type in a non static method, also static methods can be any type.
 ! Static means it belongs to the class and not the obj, static vars can be cahnged and updated in the class
 ! Ex of making a static var, 'public static int myStaticVar = 10;' with method, 'public static int getMyStaticVar()'

 !!!! YOU CANNOT USE NON STATIC METHODS IN A STATIC METHOD AND NOT VICE VERSA, YOU CANNOT USE NON STATIC VAR IN A STATIC METHOD BUT YOU CAN USE ANY TYPE IN A NON STATIC METHOD
 
 the this keyword calls the class if you use this.var in a static method it will throw an error
 to fix this use a non static method

 // * a static class is a class that is shared by all obj of the class so if inside the main class i have a static class 
 // * that static class will be shared by all obj of the main class,
 // *  NOTE: The static method of any class including a static calss is called automatically when a obj of the main class is created
 */

// ! Static vars and method
/* 
 A static variable in Java (or in other object-oriented programming languages) is shared by all instances of the class, 
 meaning that it is common to all objects created from that class. a static varible belongs to the class not the obj
 meaning if i have class A and i create 2 objects using that class and change the varible using one of the objects it will be changed for the other object too
 also you can call the static var without creating a object from that class first, i.e A.myStaticVar will give you the value of myStaticVar in class A no object was created of class A
 * you can use static vars in static and non-static methods
 * you cannot use non-static vars in static methods
 * you can accsess a static var by using a obj of that class or its subclass, use obj.staticvarname to get its value
 
 A Static method is a method that also belongs to the class not the obj, meaning that it can be called without creating an instance of the class ie a object of the class
 meaning if i have a class A with static method. A.myStaticMethod() will retun the static method even if no object of class A was created
 BUT it can still be called using an object of the class, ie obj.myStaticMethod() where obj is of class A
 * you can only use static vars in static methods, and you can only use static methods in static methods
 * *** NOTE!!!: you cannot override static methods
 * Static methods can only be called from the class containing them not from an object of that class or a extension of that class

  *                                           **** SUMMARY *****
 * in short both static variable and static methods can be accsessed by the class or a object of that class
 * BUT unlike non static var and methods you can accsess them without creating an object of that class, but you can still make a object of that class and use it to call the static var and methods
 * a static variable is shared meaning a change in it will be reflected in all objects of the class
 * This also means we can accsess satic variables and methods of one class from another class by using classname.staticvarname or methodsname
 * BUT we can accses static variables and methods inside classes that are extensions of the other classes by using the classname.staticvarname or methodsname or just the staticvarname or methodsname in the child classes, 
 * you can also use super to specify the parent class to get the static var and methods 
 NOTE: where i say you can accses a static var i assume its public otherwise you need a getter method
 */
class MyPersonStatic{
    public String name;
    static int mystatic = 0;
    public MyPersonStatic(String name){
        this.name = name;
    }
    // i can use static var in static methods but not non static vars in static methods
    public void setstatic(){ 
        name = "jimmy"; // ok as non static method
        mystatic ++; // static var can be in non static method
    }
    public static int returnstatic(){
        // name = "jimmy"; // error as non static var in static method
        return mystatic; // static var can be in static method
    }
}
class staticEX {
    public static void main(String[] args) {
        // * the static vaiable should be accessed in static way means using the class name and not the object name but here i show for both
        MyPersonStatic jim = new MyPersonStatic("jim");
        MyPersonStatic elsa = new MyPersonStatic("elsa");
        jim.setstatic();
        // * non recomended way to access static var, but it works
        System.out.println(jim.mystatic); // output 1
        System.out.println(elsa.mystatic); // output: 1
        System.out.println(elsa.returnstatic());
        // BOTH obj output one as the static variables change is reflected in all obj dosent matter if i use tha class or a obj of that class to change the static var
        System.out.println(MyPersonStatic.returnstatic()); // output 1
        // * recomended way to access static var is using the class name
        System.out.println(MyPersonStatic.mystatic); // output 1 ok as mystatic is a static variable so i can use it without obj from that class
        //MyPersonStatic.setstatic(); // NOT allowd set static not static
        // MyPersonStatic.name; // not allowed as no obj was created so no name yet
        System.out.println(jim.name); // ok as jim has attribute name prints jimmy as jim called setstatic
        jim.setstatic(); // allowed ad jim is obj of mypersonstatic
        System.out.println(elsa.mystatic); //output = 2 change reflected in all obj
        // NOTICE how the static method is not ran after a obj was created this could be changes if you want
        // simply call the staic method in the constructor to change it when the obj is created
        // now the static var is incremented when each obj is created and is the same for all obj
    }
}

 /* 
   ! caller vs calle
   caller is the obj that is calling the method or the obj that initializes the method the cllaer passes any arguments to the method
   calle is the method that is being called by the caller
   EX:  myobj.mymethod() the caller is myobj and the calle is mymethod
  */

/*  
! call chain using stack 
EX: myobj.mymethod1().mymethod2().mymethod3()
1) myobj.mymethod1() is called
2) myobj.mymethod1() calls myobj.mymethod2()
3) myobj.mymethod2() calls myobj.mymethod3()
after the last method is called the code will return to the previous method and 
then the previous method and so on until it returns to the caller
putting a method on the stack is called push and removing something is called pop
so first in last out so frist method called = last method to return to
*/

/* 
 ! java exeptions example 
 in java exeptions are used to handle errors at runtime 
 when they occur the flow of executuion is disrupted 
 the sytax for throwing an exeption is throw new Exceptionname();
 the sytax for catching an exeption is try{ code that might throw an exeption } 
 catch (Exceptionname e){ code to handle the exeption }
 you can have multiple catch blocks to handle different types of exeptions
 when we call the throw new exeption line first  the code in the try block is 
 executed and then the exeption is thrown 
 and the code in the catch block is executed if the exeption is not caught 
 it will be passed up the call chain until it is caught or the  program terminates
 
exeptions in call stack
lets say we call m1 and we go from m1 to m2 to m3 and m3 threw an exeption
1) m3 throws an exeption
2) m3 is popped off the stack and m2 is called
3) m2 can either handel the exeption or send it further down the stack if it cant handel the error (ie go to m1)
4) if m2 does not handle the exeption it is passed to m1
5) in m1 the exeptioan is caught using for ex : catch (Exception e)
6) if m1 handel the exeption the program continues to run and go to the next line of code in m1
- if m1 last method does not handle the exeption the it will go to the main method ie the caller of m1
- if the caller of m1 does handle the exeption the program will continue to run
- if the caller of m1 does not handle the exeption the program will terminate

NOTE: the call stack can be as long as you want meaning if the expection thrown by class can keep going lower
ie passed onto the next method then next method "where it would run the try catch" until its handeled and then it stops. 
if its never caught and delt with its given to the console ie the user gets it 
NOTE: the class can also handel the exeption itself by using a try catch block
NOTE: there is a deafult expection is java simple in catch put "Exeption" and all exeptions will be caught but this is not good
NOTE: you can have multiple catches for different types of exeptions so if we try x and x can throw multiple different errors we can have multiple catches for each exeption
NOTE: method opting for specify means it propigates the exeption to another method meanign it specifies where the exeption should be handled ie caught.
* NOTE: say we specify n times and say we are in a different class we still have accsess to all the variables of the original caller  
*/

// ! EXCEPTIONS
class A{
    // any caller of this method should know that it may throw a exeption so we say throws NEG....
    // here we did not do public but we could have
    // This method 'specifies'  exeption
    void ma(int i) throws NegValueException {
        if (i<0){
            // if condition met code runs and exeption is thrown it goes to negvalueexeption class 
            // *NOTE: here we could have just used a console output but that is not good this as if it dose not terminate the code it will continoue to run and produce the wrong output
            throw new NegValueException("Neg value"+ i); 
        }
        else {
            // if not neg do whatever here nothing so just return to caller
            // here a diffrent conditional can throw a different exeption
        }
    }
}

// this method is called with A obj so it runs class a
// this method 'catchs' exeption 
// catch vs specify; Catch means the exeption is caught by this method, specify means the exeption is passed to another method, the method that throws the exeption dose not count as specifier or catcher
class B {
    void mb(int i){
        A oa = new A();

        /*
        *
         insted of trying to handle the exeption here we are passing it up the call stack ie to A where it will be handled
         at A we do handle the exeption by calling throw new NegValueException("Neg value"); 
         if the negvalue exection happens after we try passing i through A then i was neg and the error given by A back to B after A's execution will be caught using catch(expectionName)
         and we can print wjat we want in B if the catch did not run that means the try worked no exeption was thrown and the program will continue to run. Note at B call stack is cut ie if B passed error to another class it would not go there the error stops at B
         */

        try {
            oa.ma(i);
            System.out.println("NVE did not happen i not neg"); 
            // can do whatever here if not neg one thing is setting a bool to true to escape a while loop 
        }
        catch (NegValueException e){
            System.out.println("NegValueException caught i was neg"); // i is neg
            // if negvalue exeption is caught here we can do whatever we want if try runs no exeption was thrown catch dose not run
            System.out.println(e); // print the exeption message 'Neg value' this was passed from A when we throw the exeption we mass a String message this 'e' is that message
        }
        // if the class A can throw multiple exeptions we can have a catch for each exeption
    }
}

// short ver
// her ewe try the code and catch the exeption if its thrown from the conditional i<0
// note we do not need to say tryset throws NegValueException because we catch the exeption here so we dont specify that the method throws the exeption
// before with A/B, A's method thorws the expeption but dose not handle it hence it specifies it throws a NegValueException
// that throw from A is caugth by B after trying from thr try block
// here the error is thrown and caught in the same method hence we do not need to specify that the method throws the exeption
class C{
    void tryset(int i){
        try{
            if(i<0){
                throw new NegValueException("i is neg");
            }
            System.out.println("i is not neg");
        }
        catch(NegValueException e){
            System.out.println(e);
        }
    }
}

// NEGVALUEEXEPTION DNE here we make the exeption
// extends is used to create a new class that is a sub class of the class that is being extended
// class NegValueException extends Exception which is a real java class
class NegValueException extends Exception {
    public NegValueException(String message) {
        super(message); // super is used to call the constructor of the parent class
        }
}

// test our exeptions
// exeptions should be in another class!
class Exep{
    public static void main(String[] args) throws NegValueException {
        // one pass one fail see B for details
        B ob =  new B();
        ob.mb(23);
        ob.mb(-1);
        // ! if we called the value directly with A then we get a error as A only throws it dose not catch it so we will see NVE neg value i but it will be as a error and execution terminates "A specifies " "B catches" dont call A!

        C ob2 = new C();
        ob2.tryset(23); // out: i is not neg
        ob2.tryset(-1); // out: NegvalueException: i is neg
    }
}

// call stakc of exeptons
/* 
// posiblities Cos "catch or specify"
1) origin
2) method subject to CoS req
3) method free from  CoS req
4) case 1 here exeption handeld earliest
5) case 2 here exeption never handeled earliest

note that when a input is given either the output is normal or an exeption is thrown
 */

// EXEPTIONS CONT
// here lets make a while loop tthat takes in input and handels errors using truy catch use the Integer class and parse int
// here the integer class throws an exeption if not a number so we need to catch it only.

class UserInputExceptions {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = 0;
        boolean valid = false;

        while (!valid) {
            System.out.print("Enter a number: ");
            try {
                num = Integer.parseInt(scanner.next());
                valid = true;
            } catch (NumberFormatException e) {
                System.out.println("Invalid number. Please try again.");
            }
        }
        System.out.println("You entered: " + num);
        scanner.close();
    }
}

// nested try catch
// here we have a try catch block inside another try catch block
// the inner try catch block will be executed first and if it throws an exeption then the outer try catch block will be executed
// if the inner try catch block does not throw an exeption then the outer try catch block will be executed
// if the inner try throws a error the inner catch will run but if the outer try throws an exeption then the outer catch will catch it
// the outer dose not throw a error if the inner try throws a error 
// * the finaly block is executed no matter what
// EX
class NestedTryCatchExample {
    public static void nestedtrycatchEX(String[] args) {
        try {
            // Outer try block
            System.out.println("Outer try block started.");

            try {
                // Inner try block
                System.out.println("Inner try block started.");
                
                // This will throw an ArithmeticException
                int result = 10 / 0;
                System.out.println("Result: " + result);
                
            } catch (ArithmeticException e) {
                // Handle the exception in the inner try block
                System.out.println("Caught ArithmeticException in inner catch: " + e.getMessage());
            }

            // Additional code in the outer try block
            int[] arr = new int[3];
            
            // This will throw an ArrayIndexOutOfBoundsException
            arr[5] = 10;

        } catch (ArrayIndexOutOfBoundsException e) {
            // Handle the exception in the outer try block
            // this only runs if the outer try block throws an exeption not if the inner try block throws an exeption the inner catch is responsible for that   
            System.out.println("Caught ArrayIndexOutOfBoundsException in outer catch: " + e.getMessage());
        } finally {
            System.out.println("Outer finally block executed.");
        }

        System.out.println("Program continues after nested try-catch.");
    }
}


// ! Test Driven Dev or Regertion Testing
// inceremntal dev = rerun test after each change this can be after each new logical unit in incremented
// regestion testing = keep adding test cases after each change and builing on top of existing ones
// normal vs disruptive testing (meanign sometime a failed test is what we expect so in that case it should pass)

// Lets say we have a exeption thrown by a method and we want to test it using Junit text 
// lets say we have a method that throws an exeption called getValue() that returns value
// lets say value is bounded 0->3 and the setters are decrement and increment and they cant go past 0 or 3
// each method trows value to small and to big expetions respectively 
// and we want to test it using Junit text we. Note that we want some tests to pass and some to fail depending of if exeption is thrown or not
/// we can use assert equals to test that the exeption is thrown 
// * we can have try cathe exeptions in junit

// code conter class nd from notes
/* 
in this test no exeption should be thrown as min value = 0 and that means try blovk runs and increments
@ Test 
public void testGetValue() {
    counter c = new counter(); new counter obj ASSUME INITIAL VALUE 0
    assertEquals (minValue, c.getValue()); // min val = 0 innitally 
    try{
        c.increment();
        assertEquals (1, c.getValue());
    }
    catch (ValueTooLargeEXeption e){
        // fail alwasy fails a test. 
        // here we want to throw fail as this should not run we can incerment and get value its ok here so the ctach should not run
        fail ("ValueTooLargeExeption should not have been thrown"); 
    }
}

here we expect an exeption as min value = 0 and new counter will be 0 so its get value is zero and so decrement will throw exeption
@Test
    public void testDecFromMinValue() {
        Counter c = new Counter();
        assertEquals(Counter.MIN_VALUE, c.getValue()); // passes as min value = 0 and new counter will be 0 so its get value is zero
        try {
            c.decrement();
            // we put a fail here and this should not run, we cannot deceremt from min value
            // NOTE: after the line in  a try block fails we go to the catch block so in this case the fail should not run and decerement should not run
            fail ("ValueTooSmallException is expected.");
        }
        catch(ValueTooSmallException e) {
         // Exception is expected to be thrown.
         // can do like e.print(" ..... ")
        }
    }

* note in the 2 examples after we fail a test we go to the catch block but what was wrong? did we increment after max value 
* did we decrement after min value? how will the catch block know the error type. 
* onr way to solve is using a loop that keeps on running as long as we dont get the exeption when we do we know what the exetion is and what the numbers were

*/

// ! Obejct equality 
// object equality (overide or no overide)
/* 
 d = 7 e = 7
 then d == e true
 is obj p1 and obj p2 exist 
 p1 == p2 false as they are comparing the address not the values
 p1.equals(p2) true -> as we compare the values of the objects 
 * the equals method is only avalible for reference types. the .equals used on primitive types is the same as using the '==' operator
 the equals method is built into the object class in java
 by deafult when we use .equals it overrides equals in the object class but we can change it using override
 p1.equals(p2) is turned into p1 == p2 wher we override (meaning change the equals method
 this is called inheriting the equals method from the object class. 
 in the class is would look like this: 
 // Object is a java build in class
 class Object{
    public boolean equals(Object obj){
        return this == obj; // note that 'this' refers to teh context object here that would be the object p1 so we would do p1 == obj where the object here is p2
    }
 }
 */
// ex:
class personbad {
    String name;
    int age;
    public personbad(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
class Personeq {
    String name;
    int age;
    public Personeq(String name, int age) {
        this.name = name;
        this.age = age;
    }
    // use source actions to generatre equals and hashcode on varables 
    @Override
    public boolean equals(Object obj) {
        // this is to avoid NPE as the next conditional would throw an exception if obj is null thats why this must come first 
        // NOTE 'this' refers to the object that is calling the equals method
        // if obj empty then return false or if the two objects are from different class then they are not the same object
        // we dont check if the context object is null as for it to call the method it must exist, and if it dosent the compiler will throw an exception before the method
        if (obj == null || this.getClass() != obj.getClass()) {
            return false;
        }
        // if the two objects we are comparing are equlas then they are the same object as the == compares address and if two objects have the same address they are the same object
        if (obj == this) {
            return true;
        }
        // * Why cast obj to personeq?
        // we are given obj as type Object meaning it can be any object of any class, but this Object class is built into java and dose not have access the methods and attributes of the personeq class which we must compare for the equals method
        // to gain access to the methods and attributes of the personeq class we must cast obj to type personeq, since obj is of type Object casting it to personeq is downcasting as every class is a child of the Object class which is built into java
        // * why do we pass obj as type obj? 
        // we do this beacuse we need to override the equals method in the Object class of java and to overide that method we must pass in a obj of type Object, as the Object classes equals method takes in an obj of type Object, and when overriding any method we must pass in the same type and number of parameters as the original method
        Personeq p = (Personeq) obj; // ! here we add cast obj to personeq 
        return this.name == p.name && this.age == p.age; // returns true if name and age of obj p1 and obj passed into equals are equal. // 'this' is still the context obj and 'p' is the casted version of 'obj'
        // * NOTE in the line above we can use '==' as we are no longer dealing with reference types name and age are primitive (string and int). Also for name we could have used .equals() but here it dose not matter
    }
    // * since our class has a equals method when we do .equal we have a method to use if we did not it would use the default equals method in the object class
    public static void main(String[] args) {
        // two objects with the same name and age
        Personeq p1 = new Personeq("John", 30);
        Personeq p2 = new Personeq("John", 30);
        Personeq p3 = new Personeq("John", 31);
        // * if the equals method is not overriden then both will return false as both will be comparing the address
        System.out.println(p1.equals(p2)); // true
        System.out.println(p1 == p2); // false as this compares the address
        System.out.println(p1.equals(p3)); // false

        personbad p4 = new personbad("John", 30);
        System.out.println(p2.equals(p4)); // false as p4 is of type personbad and p2 is of type Personeq
    }
}

// * satic type, dynamic type, and type cast 
// static type: a ref variables decrated type
// dynamic type: type of address curruntly stored in a ref variable (changes at runtime)
// type casting: is a way to convert one type to another type in the personeqclass in the equals oeriden method we cast obj as Personeq so we convert the object type to Personeq type
// Ex
/* 
 class C1(){
    public m1{}
 }
 class C2(){
    public m2{}
 }

 main:
 C1 o1 = new c1();
 C2 o2 = new c2();
 o1.m1(); static type as o1 has m1
 o3 = o1
 o3.m1 // dynamic type as o3 must goto o1 and get m1
 // type casting 
 o3 = (C1) o1; // here we cast o1 whcih is of type C2 to C1 type now we can use C1's methods and do o3.m1
 */

// !Assert equals for dynamic vs static and Overriding equals
/* 
Lets say obj p1 is a object with a overriden equals method
 then let p2 be an object with a default equals method
 if we say p2 = p1
 then we do p2.equals(p2) 
 p2 points to p1 meaning p2's equals method is called on p1 so we are using p2's equal method
 also in the equals method we return true as p1 ==  p2, also p1 == p1 returns true as well as p2 == p2 returns true
 
 ! NOTE: if two objects are from different classes then there not not equal in terms of address and value so class1obj.equals(class2obj) is false always

 // SAY WE HAVE THIS CODE
public class PointV2 {
    private int x; private int y;
    public boolean equals (Object obj) {
        if(this == obj) { return true; }
        if(obj == null) { return false; }
        // must compare classes are objs from 2 different classes cannot be equals interms of ref or value
        if(this.getClass() != obj.getClass()) { return false; } PointV2 other = (PointV2) obj;
        return this.x == other.x && this.y == other.y;
    } 
}

// then
1 String s = "(2, 3)";
2 PointV2 p1 = new PointV2(2, 3);
3 PointV2 p2 = new PointV2(2, 3);
4 PointV2 p3 = new PointV2(4, 6);
5 System.out.println(p1 == p2);  false as its comparing the address
6 System.out.println(p2 == p3); false
7 System.out.println(p1.equals(p1));  true 
8 System.out.println(p1.equals(null));  false 
9 System.out.println(p1.equals(s)); /false 
10 System.out.println(p1.equals(p2)); true 
11 System.out.println(p2.equals(p3)); false 

if we say p2 = p3
then we do p2.equals(p3) 
p2 points to p3 meaning p2's equals method is called on p3 but since p2 points to p3 p3's equals method is called on p3 which returns true

 */

// !IMPLICATION
/* 
 if obj1 == obj2 then obj1.equals(obj2) == true as if the two objs have the same address they must have the same values 
 the opposite is NOT true as if two objects have the same values that dose not mean that they must have the same values 
 in notation this is "obj1 == obj2 => obj1.equals(obj2)"
 
  
 */

// !assertsame vs assertequals
/* 
 in junit we have assertsame and assertequals
 assert equal is for objects equality for its values is both exp1 and ep2 (assertEquals(exp1, exp2)) are primitive its just '==' if its references type then its exp1.equals(exp2) the order of the assert method arguments (exp1/2) matters
 assert same is for objects equality for its refernce and only passes if the two objects are the same object: assertsame(obj1, obj2) is true if both obj1 and obj2 are the same object meaning they have the same address
 assert same is the same as Asserttrue(obj1 == obj2) or Asserttrue(obj1.equals(obj2)) or assert false with the '!' t oflip value // NOTE this is for the case assertsame is true 
 ! NOTE: For assert equals there are 3 options for the equals method: 1,Obj class default (if no overriden) 2, the exp1's equals method (if overriden) 3, the exp1's equals method and exp2's equals method (if overriden) 
 */

// ! OBJ CLASS DIFFERENCES NOTE:
 /* 
    if we have p1, p2 and they are from different classes then p1 == p2 will not run its a error as we cannot compare objects from different classes if they were the same class this would compare the address
    if we now do p1.equals(p2) this will return false as in teh overriden equals method we have a conditional to check the classes of the two objects and if they are the same object then it will return true
    if we have not overridded the equals method "here for p1 ans we call p1's equal method on p2" than the default equals method in the object class will be called and we will return false as it dose p1 == p2 which just compares there address
    also the default equals method dose not check the dynamic type i.e it dose not see if the two obj's p1 and p2 are the same class or not all the defult equals method dose is p1 == p2
 */
// ! Comparing types in the equals method +  equality for array
/* 
 lets say we have a person class with name and age
 we have two objects p1 and p2 in our equals method we do this.name == other.name where other is p2 it will use the string equals method to evaluate 
 BUT lets say we were iteraing through a list of objects type person and we checked if this.person[i] == other.person[i] we now use the person class equals method specificly this.persons equals method
 this will go into the person equals method where we can define what attributes of person to compare ie name age etc. if no eq meth exits the address is compared and false is returned
 */

// ! short circuit effect
/* 
 MATH Logic vs LOGIC in java ie short circuit
 NOTE p and q and p or q are not the same as p&&q and p||q. 
 because p and q == q and p and same for or They are commutitive but && and || are not commutitive meaning p&&q and q&&p are not the same
 at runtime the evaluation of these logics are left to right the right sides evaluation depends of the left side passing or failing 
 EX: if p = false and q = true and we do p&&qthen after checking p if false it wont run q and returns false as q is not evaluated as we know the result is false
 how ever its not the same as q&&p as q is true it will run q then as its true we proceed to evaluate p then see that p is false so we return false
 EX: the same is true for p||q if p is true we skip over q and return true as its true no matter value of q 
 if p was false we would need to check q and return true as its true. from this we can say p||q is not q||p as in the first one p determines if we can short circuit and in the second one q determines if we can skip over p (short circuit)
 THIS is known as short circuiting

 Actual use case for short circuiting:
 if we want to divide a number by 0 then we can check the value of the devisor and if its 0 then we should not evaluate the division and return 0 right away note how the order we check matters and is not commutitive 
 checking if a value is null before trying to accses it for something 
 */

 // !Call by value (primative vs reference)
/* 
 call by value is when we pass a value to a method as a parameter and the method makes a copy of the value and works on the copy then returns the copy
    lets say we have: int radius and void setradius(int r){this.radius = r} and we have a circle object C, when we do C.setraduis(4) we are passing 4 to the method setradius, the method makes a copy of 4 by doing r = 4 and works on the copy here its 'r' then returns the copy to int radius var
    EX2: Lets say we have a method void number (i) {i = i+1 return i} and we say number(2) it will return 3 but the value of 2 is not changed only i is changed and i is a copy of 2
 
 call by reference is when we pass a reference to a method and the method works on the reference here no copy is made and we return the reference
    lets say we have int radius method setradius(Circle c){this.radius = c.radius} and in a class we have a circle object C and another circle object C2 both with a radius defined, then we do C.setradius(c2) we are passing C2 to the method setradius, the method works on the reference of C2 in the method its 'c' then returns the reference to int radius var now the value of c's radius is changed 
    NOTE: we could make a copy of the object and pass that to our method to preserve the original object.
    EX2: NOTE we want to not use copies and most likely we want out object to chnage after we call some methods on it hence why we dont make a copy for references when we call by reference
    if we did make a copy then we would make a new local objec tfor setradius method and that would not be the same object as C2 so the change would be lost (meaning they would be reflected in the copy of obj).

 call by value and equals methods: in a equals method we pass a object as a parameter and later we cast it and say p1 = (Personeq) obj. p1 is now a copy of obj but still have the same address as obj 
 
 */

// ! container:
/* 
 a container is an object that holds other objects ie a list of objects (a container can have one or more objects)
 a containee in the objects that are in the container (these objects can have their own attributes and methods)
 NOTE: let BigOBJ = [obj1, obj2] obj1 and obj2 = {name, age}. Here container  is BigOBJ and containee is obj1 and obj2 we can accsess name and age from obj1 and obj2 or BIGOBJ by first using BIGOBJ to get to obj1/2 then using obj1/2 to get to name/age.
 NOTE: if there is a BIGOBJ2 with obj1 then there is sharing(alasing) between BIGOBJ and BIGOBJ2 over obj1 this means chanign obj1 will change obj1 in BIGOBJ and BIGOBJ2. 
 // ! Aggrigation = sharing, composition = not sharing
 in diagram: CLASS then a arrow (line); start of arrow if (aggrigation = dimond ) end of arrow has number of contanees (1 = single, * =  multiple) 
 Dot NOATTION: BIGOBJ.obj1.name will get name. NOTE if we cannot acsess name in another class if name was a private attribute. but we can have a getter method in that class that is also in BIGOBJ and we can call that method to get name. 
 NOTE: this is because if both BIGOBJS share the same method and they will both get the same result. so if we get private var name from BIGOBJ one using getname, then add getname to BIGOBJ (the method with private var) then BIGOBJ2 (the place we want to accsess var) they botg will get the same name.
 NOTE: to actually get the name we need to call the method getname on BIGOBJ2 (as we want this bigobj to get 'name') using BIGOBJ2.getname(). this will go to the getname method and get name from BIGOBJ
 //! note that the getname method since its in both classes has accsess to the variables in both BIGOBJ classes so when it dose get name it will get it from BIGOBJ.
 NOTE: if we made a method to use the getname method in a method: BIGOBJ2{ methodgetter{this.getname()} } the 'this' context obj specifies that when we call this method 'methodgetters' using say class BIGOBJ2.methodgetter() the 'this' will be the object of BIGOBJ2.
 */

 // ! AGGREGATION
 // * aggregation objects have a relationship with other objects, in aggrigation a big object has smaller objects within it, the objects are shared, meaning the smaller objects can be used by multiple big objects 
 // * but these smaller objects are not part of the big object, the smaller objects can exist independently of the big object hence they will have there own methods and attributes usally
 // * best way to identify: in teh big obj the smaller obj is created and then passed in as a argument
 // * in short a library can have books, ebooks etc where those books can be independent objects and a library can have books a home can have books and the type of books can be in either library or home at once etc. (sharing)
 class Book {
    private String title;
    private String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    // Getters for title and author
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }
}

class Library {
    // List of books in the library (aggregation relationship)
    // for library to hold objects of type Book we need a array of Book objects
    private Book[] books;
    private int numBooks;

    public Library() {
        this.books = new Book[10]; // assuming a maximum of 10 books
    }

    // Method to add a book to the library
    public void addBook(Book book) {
        this.books[this.numBooks++] = book; // from this book object the library class can access all its attributes and methods
    }

    // Method to display all books in the library
    public void displayBooks() {
        for (int i = 0; i < this.numBooks; i++) {
            System.out.println("Book: " + books[i].getTitle() + " by " + books[i].getAuthor());
        }
    }
}

class aggregationEx {
    public static void main(String[] args) {
        // Create book objects independently
        Book book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald");
        Book book2 = new Book("1984", "George Orwell");
        Book book3 = new Book("To Kill a Mockingbird", "Harper Lee");

        // Create a library and add books to it
        Library library = new Library();
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);

        // Display books in the library
        library.displayBooks();
    }
}



 // ! COMPOSITION
/* composition is when we do not share objects within other objects(containers) opposite of aggrigation 
 EX: say we have 2 contaers BIGOBJ and BIGOBJ2. BIGOBJ has a obj1 and BIGOBJ2 has a obj2. no methods are shared meaning we do not share the attribuites of obj2 not in BIGOBJ, it cannot accsess obj2 and vise versa for BIGOBJ2.

 NOTE: composition can be used to create a new object that is a combination of other objects. EX: making a car using engine ex where the car object takes in a engine objec to be built as a car
 */
// Component class engine for MyCar
// * in composition objects have relationships with other objects. in composition a big object has smaller objects within it, the objects are not shared meaning smaller objects cannot be used by multiple big objects
// * but these smaller objects belong to the big object as they are a part of the big object the smaller object belongs to the big object
// * this means the smaller object cannot exist without the big object, usally indicated by the smaller obj having no constructor
// * best way to identify: the smaller object is created in the big objs constructor 
// * in short the car owns the engine a car can have engine transmission etc but the engine cannot be used by another car at once, it belongs to the car (not shared)
class Engine {
    private int mileage;

    // Constructor to set initial mileage
    public Engine() {
        this.mileage = 0;
    }

    public String start() {
        return "Engine started. Mileage: " + mileage;
    }

    public String stop() {
        return "Engine stopped. Mileage: " + mileage;
    }

    public void addMileage(int miles) {
        this.mileage += miles;
    }
}

// Composite class MyCar is the main class that uses Engine component
class MyCar {
    private Engine engine; // here we make an object of type Engine

    // Constructor to initialize MyCar with an Engine
    // by creating a car objec twe make a new Engine object by calling the Engine constructor inside the MyCar constructor
    // here we only need 1 engine object for the car object and we do that manually to avoid confusion insted of making a arrya of a varible to
    // hold a engine made by the user we create and pass the engine object to the car object
    public MyCar() {
        this.engine = new Engine();
    }

    public String start() {
        return "MyCar started. " + engine.start();
    }

    public String stop() {
        return "MyCar stopped. " + engine.stop();
    }

    // Method to drive the car and increase mileage no sharing we are using the engine class to increase the mileage
    public void drive(int miles) {
        engine.addMileage(miles);
        System.out.println("Driving " + miles + " miles. Total mileage: " + (engine.start()));
    }
}

// Main class to test the functionality
class CompositionEX {
    public static void main(String[] args) {
        MyCar myCar = new MyCar();

        // Using methods of the composite class
        System.out.println(myCar.start()); // Output: MyCar started. Engine started. Mileage: 0
        myCar.drive(50);                   // Driving 50 miles, adding to mileage
        System.out.println(myCar.stop());  // Output: MyCar stopped. Engine stopped. Mileage: 50
    }
}


 // ! COPY  CONSTRUCTOR
 /* 
  copy constructor is when we make a copy of an object using object address as a parameter we do not make any new objects
  Class  A{ A(A other){numberA = other.numberA }} // here we pass in a object into this contructor that has numberA  and we make a copy of that numberA and assign it to this numberA in the A class
  */

// ! INHERITANCE
/* 
 inheritance is when we have a class that is a child of another class (parent) and has access to its attributes and methods, NOTE: we can still override the methods in the child class this will change the default method from the parent.
 we would use this is we want a set of methods to be in the child class but we dont want to add every method we can define it once in parent and all childern can inherit it and accsess those methods (or override them)
 also insted of initilizing all the variables (self.this = this .... many times) we can pass all initilizing variables into parent class we can use the parent class to do it for us so this saves us from repating the commonly initlized variables
 we give a class its parent using the keyword extends (class name extends parent class name), we call the parent classes constructor using super(var to initilize)
 NOTE: unlike in some languages like python in JAVA we can only inherit from 1 parent class but we can have multiple child classes
 
 * basically a child class inherits all the attributes and methods from the parent class and each subclass can add its own attributes and methods ontop. but there wont be in the parent class. also any private methods or attributes will not be inherited
 * in the child class we use the default method from the parent class but we can override it to make our own version of the method we however cannot redeclare variables in the child class. for constructor method we use super() to call the parent class constructor
 * the parent class dose not have access to the child class but the child class has access to the parent class
 */

// Parent Class (Superclass)
class Animal {
    protected String name;  // Protected so subclasses can access it, by using the protected keyword this string name is accessible to all subclasses
    protected Boolean isAnimal = true; // all child classes can access this variable
    protected static String doggysaid; // static so all objects of this class can access it including child classes
    // * NOTE inheritence is one way while all children of animal class can asses is animal the parent class cannot accsess teh childs attributes like breed for ex
    // Constructor of the parent class
    public Animal(String name) {
        this.name = name;
    }

    // Method (this is the defualt method all subclasses can access)
    // prtected method means all subclasses can access it outide the package, all classe in this package can setill access it
    protected void speak() {
        System.out.println("Animal speaks his name is "+ name);
    }

    public void washanimal() {
        System.out.println("Animal clean");
    }

    // to accsess atttributes/ methods in siblinging classes we goto the parent class 
    // here we will set what doggy said in the doggy class then accsess it in the child class gaurd dog
    public void whatdoggysaid(String input) {
        // static variable must be accessed using the class name
        Animal.doggysaid = input; // we are setting the doggysaid in the parent class
    }
    public String getwhatdoggysaid() {
        return Animal.doggysaid; // we are getting the doggysaid from the parent class
    }

    // * NOTE!
    /* NOTE: we used static vaible because if we said doggy setwhatdoggysaid this sets it only for the animal class instance that doggysaid is being set for and not for any other instance
      when we create gaurd dog we create another instance of the animal class and hence if we want to have what doggy said in the gaurd dog class we must set what doggy saif to a static variable
      before static if we make a doggy obj we need to set doggysaid for that obj and call getwhatdoggysaid from that obj as any other child class would have created a diffrent instance of the animal class
      one which would require a set and get doggy said of its own. with static onve any child of the animal class sets what doggy said it and all other children (instances of animal class) 
      now have access to what doggy said.
    */
    public void info() {
        System.out.println("Animal info");
    }
}

// Child Class (Subclass)
class Doggy extends Animal {  // Subclass doggy extends Animal means animal is the  parent class of doggy, the extends keyword makes this a child class or whatever it extends
    private String breed;   // Private so only the class itself can access it
    // isAnimal = false; can change the static var or any var in the parent class
    // Constructor of the child class
    public Doggy(String name, String breed) { 
        // Call the parent class constructor and passing in the name this will pass the var name into the parent class's constructor which takes name as a parameter 
        // * we must call the parent constructor because the type doggy extends animal in creating a new doggy object we are creating a new animal object at the same time and the animal obj takes a name as a parameter so we must give it that
        super(name); // PARENT CONSTRUCTOR call must be the first line in the child class constructor
        this.breed = breed; // breed is a local var so we cannot access it in the parent class hence some vars are initilized in the constructor on child class (not evert animal has a breed but dose have name)
    }

    // Overriding the speak method if we did not do this it would print "Animal speaks" as doogy.speak() would call the parent class speak method
    @Override // this  is a annotation that tells the compiler that we are overriding a method its not required
    public void speak() {
        System.out.println("Woof! Woof!"); // making our own  speak method for doggy
    }

    // Getter for breed (Java often uses getters to access private fields)
    public String getBreed() {
        return breed;
    }
    public Boolean getIsAnimal() {
        return isAnimal; // static variabel available to the child class, BUT not a object of the child class hence must be used in a getter method
        // OR return super.isAnimal;
    }

    // to call any method from the parent class we use super.method()
    // here we call what dog said from the parent class and set a value here
    public void setwhatdoggysaid(String input) {
        super.whatdoggysaid(input); // calling the parent class method (whatdoggysaid)
        // we can also directly change the static variable in the parent class but we are calling the method to make it clear what we are doing
        // Animal.doggysaid = input; // we are setting the doggysaid in the parent class
    }
    public void info() {
        System.out.println("Doggy info");
    }

    // using super to select which version of the method to call
    public void getinfo() {
        info(); // calling the info method from this class
        super.info(); // calling the info method from the parent class
    }
}

// another child class
class GuardDog extends Animal {
    private String state;  // State specific to GuardDog

    // Constructor to initialize the name and state
    public GuardDog(String name, String state) {
        super(name);  // Call the Animal constructor to initialize the name 
        this.state = state;  // Set the GuardDog's state
    }

    // Method for guarding behavior
    public void guard() {
        System.out.println("Guarding the house");
    }
    
    // no overriding speak method now the speak method from the parent class (animal) will be called

    // we can use super to not only call the constructor but any  method in the parent class
    public void clean() {
        super.washanimal(); // calling the parent class method (washanimal)
    }

    // Method to display the state
    public String getState() {
        return state;  // Return the GuardDog's state
    }

    // here we will get waht doggy said but we will include the parent method and add our own stuff
    public String getwhatdoggysaid() { // name cannot be the same as the parent class method
        System.out.println("doggy said: "); // adding our own stuff
        return super.getwhatdoggysaid(); // calling the parent class method (whatdoggysaid) and returning its value
        // OR return Animal.doggysaid; using the class name to access the static variable
        
    }
}
// Usage
class inheritanceEX {
    public static void main(String[] args) {
        Doggy doggy = new Doggy("Buddy", "Golden Retriever");  // Updated instance creation
        System.out.println(doggy.name);        // Output: Buddy
        System.out.println(doggy.getBreed());   // Output: Golden Retriever
        doggy.speak();                          // Output: Woof! Woof!
        System.out.println(doggy.getIsAnimal()); // Output: true
        doggy.getinfo();                           // Output: Doggy info and Animal info
        

        // **** Static vars in inheritance ****
        // Child classes do not inherit static variables from the parent class
        // doggy.doggysaid; not allowed add class Doggy though it extends Animal dose not have accsess to Animal classes static variables like doggysaid
        // correct way
        Animal.doggysaid = "doggy says hi"; // all child classes and parent class will reflect this change from now on
        // not recomened but works way: 
        Animal myAnimal = new Animal("Generic"); // you can create a new instance of the parent class you will have accsess to all the Animal classes variable and attributes
        myAnimal.doggysaid = "doggy says hi"; // not recomened but works way

        // Create a GuardDog instance with a name and state
        // * NOTE: we used super in gaurd dog class so the name is initialized in the parent class so even the default method of speak has access to the name of the guard dog's name when we do guardDog.speak()
        // * the name attribute now belongs to the Animal class where a class level var called name holds the name value either passed when making a Animal or gaurd Dog object. since its a protected var
        // * this means not only does the parent class 'Animal' have a name attribute but also the child class 'GuardDog' has a name attribute becuse it extends the parent class "Animal" hence has all its atributes including name 
        GuardDog guardDog = new GuardDog("Rex", "alert");
        System.out.println(guardDog.name);    // Output: Rex (Print the guard dog's name)
        System.out.println(guardDog.getState());   // Output: alert (Print the guard dog's state)
        guardDog.speak();        // Output: Animal speaks his name is Rex 
        guardDog.guard();       // Output: Guarding the house (Invoke the guard method specific to GuardDog)
        guardDog.clean();  // Call the clean method from the GuardDog class (calls a method from the parent class)

        // calling what doggy said from the parent class here we will set what doggy said in doggy class
        // the doggy calss sets this in the whatdoggysaid method in the parent class
        // then the gaurd dog class calls the whatdoggysaid method from the parent class and accesses the value that doggy set
        // Set what doggy said in the Doggy class
        doggy.setwhatdoggysaid("doggy says hi"); // this will set the value of whatdoggysaid in the parent class and will be reflected in all child classes and parent classe
        
        // Now get what doggy said in the GuardDog class
        System.out.println(guardDog.getwhatdoggysaid()); // Should print: "doggy said: doggy says hi"

        // !  type casting

        // * upcasting (alwasy safe all subclasses gaurd dog, doggy etc are a type of animal)
        // upcasting the gaurd dog to a animal (alwasy imlicit i.e can directly assign obj from child class to parent class)
        // is safe because gaurd dog is a type of animal, is the format parent class = child class its always safe (upcasting)
        Animal animal = new GuardDog("Rex", "alert"); // Upcasting (GuardDog to Animal)
        animal.speak(); // this will call the speak method from the parent class deafult method still prints REX as we use super to initilize name in the parent class from gaurd dogs constructor
        // animal is still just of type Animal but we used a gaurd dog object to create a Animal obj 'animal' hence animal.speak has a name from the gaurd dog object
        
        // * downcasting (not alwasy safe as we are adding more expectation for the object)
        // downcasting the animal to a gaurd dog (always explicit i.e uses bracktes to indicate cast (class to cast to) obj from parent class)
        // not alwasy safe as animal might not always be of type gaurd dog here it is (see upcasting) animal is gaurd dog
        GuardDog downcastedGuardDog = (GuardDog) animal; // Downcasting (Animal to GuardDog)
        downcastedGuardDog.guard(); // Access the GuardDog-specific method ok as downcastedGuardDog is of type GuardDog
        System.out.println(downcastedGuardDog.getState()); // Access GuardDog's state attribute ok as downcastedGuardDog is of type GuardDog
        // here animal before was assigned to a gaurd dog object but now we are downcasting it to a gaurd dog object so animal is now of type gaurd dog
        // this changes the typr that animal is before animal was assigned to gaurd dog but still type Animal so it only had animal methods and not gaurd dog methods
        // but by downcasting we changed animal to be of type gaurd dog so now animal assigned to downcastedGuardDog is of type gaurd dog and has gaurd dog methods
        // remember this is safe as animal pointed to a gaurd dog object so downcasting it to a gaurd dog object type is safe

        // * error ex
        // here this is not allowed as will cause a error
        // Animal animal3 = new Animal("Some Animal"); // animal is of type Animal and points to an Animal object
        // GuardDog downcastedGuardDog2 = (GuardDog) animal3; // Downcasting (Animal to GuardDog)
        // downcastedGuardDog2.guard(); // Access the GuardDog-specific method will cause an error
        // this causes a error because animal3 is of type Animal and points to a animal object
        // so downcasting it to a gaurd dog object is not ok as that would be increasing the expectation for the object i.e animal would need gaurd dog methods which is not the case

        // * for sibling classes you cant cast between the or directly as thats neither upcasting nor downcasting.
        /* 
        GaurdDog mygaurddog = new Dog() and then 
        Dog doggy = (Dog) mygaurddog
        THIS IS NOT ALLOWED
        */ 

        // see dynamic binding notes and instance of notes for more
    
    }


}
/*
 ! IMPORTANT NOTES for inheritance:

 - you cannot redeclare inherented attribute in a child class meaning you cannot have a variable with the same name in the child class, you can still make a copy of the attribute in the child class
 - we can override (make our own version of) methods in the child class from methods in the parent class, if we dont override we can only use the methods in the parent class's defualt method, when overriding use @Override before the method
 - a staric variable is shared by all instances of a class, meaning all the child classes can access it, but static variables cant be overridden so note 1 about redeleration dose not apply to static variables
 - while you can accsess parent class methods and variables from the child class, you cant access child class methods and variables from the parent class

// ! polymorphism
/*
Polymorphism is a feature in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. 
This means that the same method can be called on objects of different classes, and the behavior of the method will vary depending on the actual class of the object being called on.
the method that can be called by different objects is called a polymorphic method  
*/

// * EX using the code from inheritanceEX
// New class to call the speak method of a given animal
class Pets {
    public void makeAnimalSpeak(Animal animal) { 
        animal.speak(); // Calls the speak method, demonstrating polymorphism
    }
    // *NOTE method return void becuse it doesnt return anything rather calls a method that returns something
    // *If in the gaurd dog animal etc classes insted of printing the result in speak() we returned it that would mean
    // *the speak method returns a string to the polymorphic method so we would need to return animal.speak()
    // * this would mena that makeAnimalSpeak(Animal animal) would return a string
}

// Main class to test the functionality
class polymorphismEX {
    public static void main(String[] args) {
        Pets pets = new Pets();

        Animal genericAnimal = new Animal("Generic");
        Doggy doggy = new Doggy("Buddy", "Golden Retriever");
        GuardDog guardDog = new GuardDog("Rex", "Alert");

        // polymorphic method takes in obj of type animal but since all child classes of animal 
        // are also of type animal, we can pass in obj of type animal or any of its child classes as a obj of type animal
        pets.makeAnimalSpeak(genericAnimal); // Output: Animal speaks his name is Generic
        pets.makeAnimalSpeak(doggy);        // Output: Woof! Woof!
        pets.makeAnimalSpeak(guardDog);     // Output: Animal speaks his name is Rex
    }
}

// rule for polymorphism,  you cannot pass in a object to the polymorphic method that is not type animal as the object needs to be a dencended of animal class

/*
// ! Scope of identifiers in java (Protected, Public, Private)
# we have the concept of multiple packages in java, a package is a collection of classes, interfaces, and subpackages, we can use the package keyword to define a package and then we can use the import keyword to import classes from other packages
 - this public, private, and protected keywords is known as the modifier of the attribute method or class and it determines there accessibility
 * NOTE for us subclasses are child classes, class inside a class is called a inner class or nested class
 Clases:
    - public class is avalible anywhere in the package
    - private class is only avalible in the parent class (the class its defined in)
    - if no modifier is used the class is default and is avalible in the package and any class
    - NOTE: for classes we can only have one public class in a file, but we can have multiple classes in a file. inner classes are classes that are defined inside another class and they can be public or private.

 Methods:
    - public method is avalible anywhere in the package, class or its subclasses
    - private method is only avalible in the parent class (the class its defined in)
    - protected method is avalible in the parent class and its subclasses in the same package outiside the pakage its only for the subclasses
    - if no modifier is used the method is default and is avalible in the package and any class
    - NOTE: for methods we can have multiple public and private methods in a class.

 Attributes:
    - public attribute is avalible anywhere in the package, class or its subclasses
    - private attribute is only avalible in the parent class
    - protected attribute is avalible in the parent class and its subclasses
    - if no modifier is used the attribute is default and is avalible in the package and any class

 - To use classes and method from a different file or a file in a different package we use the import keyword to import the file by using class name of that file.
 - a package is a collection of classes, interfaces etc, basically a collection of files or a folder. this folder sits in the src folder.
*/

// * NOTE: we cannot assign a object made from the subclass to the object made using the parent class (this is called downcasting). this can be done the otehr way aroud(upcasting)

// * dynamic binding and static binding
// dynamic binding
// static binding
// in static binding the method is called by the class that is calling it
// in dynamic binding the method is called by the object that is calling it
 
// !  Rules of substitution for objects and classes for inheritance (dynamic binding):
// lets make 3 objects with classes: SmartPhone, IOS extends SmartPhone, and iphone extends IOS
// the obejcts = {SmartPhone_1, IOS_1, iphone_1}
// EX1: we can say IOS_1 = smartPhone_1 as IOS_1 is a subclass of SmartPhone_1 but we cannot say IOS_1 = SmartPhone_1 or iphone_1 = smartPhone_1
// Because: 1) IOS_1 is the child class and SmartPhone_1 is the parent class so while assigning the parent to the class is ok we cannot assign the child to the parent
// 2) because IOS_1 extends SmartPhone 1 it cannot replace SmartPhone_1,
// EX2: we can say iphone_1 = IOS_1 as iphone_1 is a subclass of IOS_1 but we cannot say IOS_1 = iphone_1 as IOS is not a decendant of iphone_1 rather iphone is a decendant of IOS, (decenndent means the class is the child class of the parent class)
// * RS = parent class LS = child class (for it to work) here the LS must directly inherit from the RS by being a decendant of the RS meaning its parent class is the RS or its parents parent ... is the RS
// let: some other type of phone like andriod that extends SmartPhone and a class Samsung extends Andriod we could say Andriod_1 = SmartPhone_1 and Samsung_1 = Andriod_1
// but i cannot say iphone_1 = Andriod_1 or Andriod_1 = iphone_1 as because iphones parent is not Andriod and Andriod parent is not iphone they are both unrelated
// so we can say Smartphoe IOS_phone = new IOS_1() but we cannot do this the other way around (LS has parent and RS has child)
// so we can also then say smartphone_1 new_smartphone_1 = new iphone_1() but we cannot do this the other way around as iphone is a decendant of smartphone but not the other way around
// * siblings classes will also not work with substitution rule or with the ex before 
// LAST dynamic type just means the type of the object at runtime so if we make a smartphone object and assign it to an iphone object then the reassign the smartphone object to the andriod object 
// Then the last dynamic type is type andriod and first dynamic type is type iphone. 

// substitution with type casting
/* 
 
EX: 
smartphone_1 my_phone = new IOS_1();
IOS_1 my_ios_phone = my_phone;
* this is invalid as we are assigning a type ios to a type smartphone but myphone is type smartphone and smartphone is not a decendant of IOS (we can do this the other way around)

* to type cast the my_ios_phone to type IOS before we can assign it to my_phone which is now a type IOS
IOS_1 my_ios_phone = (IOS_1) my_phone;

EX: 
smartphone_1 aphone = new IOS;
IOS for_iphone = (iphone_1) aphone; 
this cast is valid as aphone is of type IOS and IOS is a decendant of iphone

ex of anonymous assigning
((iphone_1) aphone).faceTime(); // if facetime is a method in class iphone_1 we must put the cast in parentesis as we must cast before we can call the method

* upward vs downward casting
upward casting is when we cast from a child class to a parent class (reduces the expected methods and attributes avalible)
downward casting is when we cast from a parent class to a child class (increses the expected methods and attributes avalible)
if you try to cast to the same class it is not a cast and will not throw an exception

* problem if we cast we nned to makde sure the object we are casting too can fulfill the methods and attributes of the class we are assigning to
for IOS for_iphone = (iphone_1) aphone; iphone one has all the methods so its fine
so if we have a new class that extends ios called iphone_mini as we cast a type iphone to type iphone mini we cannot use the iphones methods with IOS type anymore

* for siblings classes we cannot cast from one to the other directly 
but you can first update to the siblings parent class and then downcast to the sibling class.
you can also keep going up untill you reach the paremnt of both classes then you go downward to the sibling classe
here in a ex :
given treeo of hierarchy
     A
    / \
   B   D
  /
 C
from b to D is not possible
 */


// ! instanceof keyword
// instanceof keyword is used to check if an object is an instance of a specific class, instance means an object of a class
// it returns a boolean value that indicates whether the object is of the specified class or a subclass of it
// syntax : object instanceof ClassName returns true if object is an instance of ClassName or a subclass of it and false otherwise
// EX:
// Parent class
class Vehicle {
    public void start() {
        System.out.println("Vehicle is starting...");
    }
}

// Child class: CarEX 
class CarEX extends Vehicle {
    public void drive() {
        System.out.println("CarEX is driving...");
    }
}

// Child class: Bike
class Bike extends Vehicle {
    public void pedal() {
        System.out.println("Bike is pedaling...");
    }
}

// Test class
class InstanceOfExample {
    public static void main(String[] args) {
        // Example 1: Upcasting (Implicit)
        // A CarEX object is created and implicitly upcasted to a Vehicle reference
        Vehicle myCarVehicle = new CarEX(); // Implicit upcasting
        myCarVehicle.start(); // Only Vehicle methods are accessible now
    
        // Example 2: Downcasting (Explicit)
        // Downcasting the Vehicle reference back to CarEX
        if (myCarVehicle instanceof CarEX) { // Check to ensure it's safe to cast
            CarEX myCarEX = (CarEX) myCarVehicle; // Explicit downcasting
            myCarEX.drive(); // Now CarEX-specific method is accessible
        } else {
            System.out.println("myCarVehicle is not an instance of CarEX."); // This won't run
        }
    
        // Example 3: Upcasting (Implicit) for a Bike
        // A Bike object is created and implicitly upcasted to a Vehicle reference
        Vehicle myBikeVehicle = new Bike(); // Implicit upcasting
        myBikeVehicle.start(); // Only Vehicle methods are accessible
    
        // Example 4: Downcasting (Explicit) with an error handled using if-else
        // Attempting to cast a Bike reference to CarEX, which will fail
        if (myBikeVehicle instanceof CarEX) {
            CarEX myInvalidCar = (CarEX) myBikeVehicle; // This won't execute as the cast is invalid
            myInvalidCar.drive();
        } else {
            // This will execute since myBikeVehicle is not an instance of CarEX
            System.out.println("Error: myBikeVehicle cannot be cast to CarEX."); 
            System.out.println("Attempting to cast a Bike object to CarEX will cause a ClassCastException.");
        }
    
        // Example 5: Valid Downcasting for Bike
        // Checking and safely downcasting the Vehicle reference back to Bike
        if (myBikeVehicle instanceof Bike) { 
            Bike myBike = (Bike) myBikeVehicle; // Explicit downcasting
            myBike.pedal(); // Accessing Bike-specific method
        } else {
            System.out.println("myBikeVehicle is not an instance of Bike."); // This won't run
        }
    
        // Example 6: Direct Error Demonstration (Uncomment to see runtime error)
        /*
        CarEX invalidCar = (CarEX) myBikeVehicle; // This will throw a ClassCastException
        invalidCar.drive(); // This line will not execute
        */
    
        // Example 7: Using unrelated class with instanceof
        String str = "Hello, world!";
        if (str instanceof String) {
            System.out.println("str is an instance of String."); // Always true
        }
    }
    
}

/* 
 EX:
 given treeo of hierarchy
     A
    / \
   B   D
  /
 C
 
 A a = new C()
 a instanceof B -> true // true B is a instance of B
 a instanceof D -> false // false B is not a instance of D 
 */


// ! Interfaces
// * there are 2 way to implement interface 1) using interface and implements keyword 2) using abstract class
// *method 1
/* 
// using interface 
 - Declared with the interface Keyword

- Interfaces are defined using the interface keyword.
    interface Animal {
    void makeSound(); // Abstract method
    }

- Cannot Contain Constructors
    Interfaces cannot have constructors because they cannot be instantiated, meaning you cant make a object out of it, you must use the child class to make an object from the interface

    - Methods Are Public and Abstract by Default
    No need to specify public or abstract explicitly for methods.
    Starting with Java 8, interfaces can have default and static methods with implementations.

    - Fields Are Public, Static, and Final by Default
    Any variable declared in an interface is automatically a constant.

    - Supports Multiple Inheritance
    A class can implement multiple interfaces.

    - Implements Keyword
    A class implements an interface using the implements keyword.

    - Classes that implement an interface: you just need to use the interface name to get the method, super only exist for multiple interfaces where its used to specify which interfaces methods to use 
                                         : have accsess to all the vaiables of the interface
// * NOTE: abstact methods are incomplete methods that must be overridden in the class that implements the interface
 */

// *method 2
/**
 * // Using Abstract Classes:
 * 
 * - Declared with the abstract Keyword:
 *   Abstract classes are defined using the abstract keyword.
 * 
 * - Can Contain Constructors:
 *   Abstract classes can have constructors to initialize common properties. but you still cant make an object out of it
 * 
 * - Can Contain Abstract and Concrete Methods:
 *   Abstract methods must be overridden in subclasses, while concrete methods can be inherited or overridden.
 * 
 * - Can Have Instance Variables:
 *   Unlike interfaces, abstract classes can have instance variables (not just constants).
 * 
 * - Cannot Be Instantiated Directly:
 *   Only subclasses of an abstract class can be instantiated. the abstract class itself cannot make a object as it is incomplete
 * 
 * - Supports Single Inheritance:
 *   A class can extend only one abstract class.
 * 
 * - Extends Keyword:
 *   A class extends an abstract class using the extends keyword.
 * 
 * - Classes that extend an abstract class: have accsess to all its variables and methods, can use super as abstact classes have constructors and as its a class and is extended 
 */

 // * interface vs abstract class
 /* 
  -Interface: Use when you want to define a contract for behavior that multiple unrelated classes can implement.
  -Abstract Class: Use when you want to provide a base class with shared code and a common structure for related classes.
  */
  // * both interface and abstact classes cannot create an object of themself, they are used to create objects of their child classes

// * NOTE on static variables 
/* 
 just like in inheritance a child class that extends of implements a parent class dose not have access to the parent class static variables
 // in the case of interfaces we cannot create a object from the interface hence we must use the interface Classname to access the static variables
 // in the case of abstact classes we cannot create a object from the abstact class hence we must use the abstact class Classname to access the static variables
 this is different from inheritance and other stuff that involves normal classes this is beacuse Abstact classes, interfaces or abstact classes are imcomplete
 hence you cant make a object out of them so the only way to access their static variables is to use the class name to access them
 */

// ! interface classes (method 1)
// ex for interfaces using interface classees -> interface keyword and implements keyword
// in a interface class i.e a class made with interface keyword every method is abstact unless its static or default
// static is static (see static methods notes) 
// the default method is a method that has a body and is not static or abstract so just like a normal method but in an interface
// in interfaces we cannot have public, private or protected access modifiers. we can set those for abstract methods once we override them in a class
interface Animal2 {
    boolean IsAnimal = true; // this var is static final and public by default, cannot be changed, so this var is a constant, belongs to the interface not the that implements it
    // Abstract method (must be implemented by a class that implements the interface)
    void makeSound();

    // Default method (has a body) dose not require an implementation i.e override, but can still be overridden
    default void sleep() {
        System.out.println("Sleeping...");
    }

    // Static method (has a body) since its static it can be called without an instance of the interface, it cannot be overridden, the class that impliments it dosent get access to it
    static void info() {
        System.out.println("This is an interface for animals.");
    }
}

// Implementing the interface
// this class implements the Animal2 interface meaning it has all its methods the abstact ones it must implement and the default ones it can use
class Dog2 implements Animal2 {
    // since this is a class here we can have a constructor, public, private or protected methods etc
    @Override
    public void makeSound() { //must match the method name and return type of the interface but can add a identifier
        System.out.println("Bark!");
    }
    // using the parent interface's is animal variable 
    // we can define a method in this class that uses the parent interface's variable
    public void isAnimal() {
        System.out.println(IsAnimal); 
        Animal2.info(); // calling a method from the child class of a parent interface
    }

    // to use a method just use its name no need to reference the parent interface
    // EX: sleep() is a method in the parent interface so we can use it here by doing
    // public void callSleep() {
    //     sleep(); // calls the sleep method in the parent interface   
    // }
}

class Cat2 implements Animal2 {
    @Override
    public void makeSound() { 
        System.out.println("Meow!");
    }
}

class Bird2 implements Animal2 {
    @Override
    public void makeSound() {
        System.out.println("Chirp!");
    }

    @Override
    public void sleep() { // override the default sleep method
        System.out.println("Bird is sleeping differently...");
    }
}

class InterfaceExample {
    public static void main(String[] args) {
        // Access static method from the interface
        Animal2.info();

        // Create objects of classes that implement the interface
        Animal2 dog = new Dog2(); // syntax: interface name = new class that implements the interface
        Animal2 cat = new Cat2();
        Animal2 bird = new Bird2();

        // Call methods
        dog.makeSound(); // Bark!
        dog.sleep();     // Sleeping...

        cat.makeSound(); // Meow!
        cat.sleep();     // Sleeping...

        bird.makeSound(); // Chirp!
        bird.sleep();     // Bird is sleeping differently...

        // call the isAnimal method in the Dog2 class using a object of the Dog2 class
        Dog2 d = new Dog2(); // ok as Dog2 is a class and can have a object (has a constructor)
        // we must first make a dog 2 object, this is ok as dog 2 is a class and has a constructor
        // then we can call the isAnimal method
        d.isAnimal(); // true && prints info 
        // or 
        // ((Dog2) dog).isAnimal(); // since dog points to a Dog2 object we can casr dog which is of type animal 2 to type Dog2

        // static vars
        // dog.IsAnimal; // why cant do this as the static variable belongs to the class and not the object of that interface
        // we must use the class name as we cannot make a object from teh interface to accses the static variable
        /// you need to use this expression as part of a complete statement, such as printing it or assigning it to a variable, cant have Animal2.IsAnimal alone 
        boolean isAnimal = Animal2.IsAnimal; // true

    }
}

// ! multiple interface implementation
// unlike extends which you can only have 1 parent class with implements you can have multiple interfaces
interface Animal4 {
    boolean IsAnimal = true;
    default void speak() {
        System.out.println("Animal speaks");
    }
    default void greet() {
        System.out.println("Hello");
    }
}

interface Dog4 {
    boolean IsAnimal = true;
    default void speak() {
        System.out.println("Woof");
    }
    default void sleep() {
        System.out.println("Sleeping...");
    }
}

// here beagle4 is a class that implements both Animal4 and Dog4
// this means it has accses to all the methods in both interfaces see below how to deal with multiple interface methods
class Beagle4 implements Animal4, Dog4 { 
    @Override
    public void speak() {
        // Resolving the conflict by specifying which interface's default method to use
        Dog4.super.speak(); // Uses Dog4's default speak method
        // Or you could call Animal4.super.speak() if you want to use Animal4's default method
        // using the is animal variable

    }
    public void isAnimal() {
        // for vaiables of the same name we dont use super instead we use the class name as variables are static by default
        System.out.println(Animal4.IsAnimal);
        System.out.println(Dog4.IsAnimal);
    }
}

class MultipleIntefaceEX {
    public static void main(String[] args) {
        Beagle4 b = new Beagle4();
        b.speak(); // Output: Woof
        b.sleep(); // Output: Sleeping...
        b.isAnimal(); // true, true
    }
}

//! abstract classes (method 2)
// Ex for interfaces using abstract class
// Abstract class: Animal3
abstract class Animal3 { // using keyword abstract to indicate that this class is abstract (may contain abstract methods hence we must use the abstract keyword)
    protected String name; // Shared attribute for all animal3 subclasses
    protected static boolean isAnimal = true;

    // Constructor: Initializes the name of the animal
    public Animal3(String name) {
        this.name = name;
    }

    // Abstract method: Must be implemented by all subclasses
    // her ethe abstact keyword is used to indicate that this method is abstract (may not have a body i.e incomplete)
    // every class that extends it must override this method and provide its own implementation
    public abstract void speak();

    // Concrete method: Shared behavior for all subclasses but can still be overridden if needed
    public void eat() {
        System.out.println(name + " is eating.");
    }
}

// Subclass: Doggy3
class Doggy3 extends Animal3 {

    // Constructor: Passes the dog's name to the superclass
    public Doggy3(String name) {
        super(name);
    }

    // Implements the abstract speak method, muts keep the same method identifier, return and name but remove abstract keyword
    @Override
    public void speak() {
        System.out.println(name + " says Woof! Woof!"); // uses the name from the parent abstract class, set by this classes constructor using super
    }
}

// Subclass: Cat3
class Cat3 extends Animal3 {

    // Constructor: Passes the cat's name to the superclass
    public Cat3(String name) {
        super(name);
        isAnimal = true; // redefine the isAnimal variable to true again, just to show that we can accsess static variables from the parent class
    }

    // Implements the abstract speak method
    @Override
    public void speak() {
        System.out.println(name + " says Meow!");
    }

    // calling the eat method from the parent class
    public void eat() {
        super.eat(); // calls the eat method from the parent class
    } 
}

// Main class to test the abstract class and its subclasses
class AbstractClassExample {
    public static void main(String[] args) {
        // Abstract class Animal3 cannot be instantiated directly
        // Animal3 animal = new Animal3("Some Animal"); // Uncommenting this will cause an error

        // Create instances of Doggy3 and Cat3
        Animal3 dog = new Doggy3("Buddy"); // Using a reference of type Animal3
        Animal3 cat = new Cat3("Whiskers");

        // Call the speak method (abstract method implemented by subclasses)
        dog.speak();  // Output: Buddy says Woof! Woof!
        cat.speak();  // Output: Whiskers says Meow!

        // Call the eat method (shared concrete method from the Animal3 class)
        dog.eat();    // Output: Buddy is eating.
        cat.eat();    // Output: Whiskers is eating. this method exist in the cat class but in the method it actually calls the eat method from the parent class

        // since the child classes are still classes we can do
        // Cat3 newcat = new Cat3("Whiskers"); // valid because Cat3 is a class

        // static vars
        // Animal3 newanimal = new Animal3("generic animal"); // invalid canot made object of abstract class
        // correct:
        boolean isAnimal = Animal3.isAnimal; // true, accseing the static var using class name
    }
}

// ! NOTE:
// in general if a class extends or interfaces a class it dose not need to use classname.methodname or classname.varname 
// to access the methods and variables it is inherited from the parent class or interface so simply use the method name or varname like you were in the parent class or interface
// but in the main method for ex you need to use the class name to access the methods and variables in the parent class or interface


// ! Final classes and methods
/* 
 you can use a final keyword to make:
  a) a variable final (cannot be changed) 
  b) a class final (cannot be inherited) 
  c) a method final (cannot be overridden)
 */

class FinalClassExample { // This class is final so it cannot be inherited
    final int a = 10; // a is a final variable (cannot be changed)
    final void print() { // print is a final method (cannot be overridden)
        System.out.println("Hello");
    }
}


// ! De refencing
/* 
 Dereferencing in Java refers to accessing or manipulating the value of an object via a reference to it. It involves using a reference variable to "point to" the actual object and access its fields or methods. Dereferencing allows you to work with the object that the reference variable refers to.

Key Points About Dereferencing
Reference Variables: In Java, variables that store the memory address of an object (instead of the object itself) are called reference variables.
Dereferencing: When you use the reference variable to access the fields or methods of the object, it's called dereferencing.

obj is a reference variable that points to an Example object.
When we use obj.display() or obj.value, we dereference obj to access the object's methods or fields.

Dereferencing a null Reference
If a reference variable is null, dereferencing it (i.e., attempting to access fields or methods through it) will result in a NullPointerException.
Example obj = null; // obj does not point to any object
obj.display();      // This will throw NullPointerException
 */
// EX
class Example {
    int value;

    Example(int value) {
        this.value = value;
    }

    void display() {
        System.out.println("Value: " + value);
    }
}

class Main {
    public static void main(String[] args) {
        Example obj = new Example(10); // obj is a reference to an Example object
        obj.display();                // Dereferencing obj to call the display method
        System.out.println(obj.value); // Dereferencing obj to access the value field, output: Value: 10
    }
}