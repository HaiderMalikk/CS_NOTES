package Java.Data_Structures;
import java.util.ArrayList;

public class Array_Lists {
    public static void main(String[] args) {
        // * array list
        // array list is a better data structure than arrays as it is dynamic and can grow or shrink in size
        // its also has many methods built in for manipulating the list
        // array list is a part of the java collections framework and is present in java.util package
        ArrayList<Integer> list = new ArrayList<>(); // creating an array list of integers
        list.add(1); // adding an element to the array list
        list.add(2);
        list.add(3);
        System.out.println(list); // Output: [1, 2, 3]
        System.out.println(list.get(0)); // Output: 1
        System.out.println(list.get(1)); // Output: 2
        System.out.println(list.get(2)); // Output: 3
        System.out.println(list.size()); // Output: 3
        list.remove(1); // removing an element from the array list
        System.out.println(list); // Output: [1, 3]
        list.set(1, 4); // updating an element in the array list
        System.out.println(list); // Output: [1, 4]
        list.clear(); // removing all elements from the array list
        System.out.println(list); // Output: []
        
        // * nested array list 2d array list
        ArrayList<ArrayList<Integer>> nestedList = new ArrayList<>();
        ArrayList<Integer> innerList1 = new ArrayList<>();
        innerList1.add(1);
        innerList1.add(2);
        ArrayList<Integer> innerList2 = new ArrayList<>();
        innerList2.add(3);
        innerList2.add(4);
        nestedList.add(innerList1);
        nestedList.add(innerList2);
        System.out.println(nestedList); // Output: [[1, 2], [3, 4]]
        System.out.println(nestedList.get(0)); // Output: [1, 2]
        System.out.println(nestedList.get(1)); // Output: [3, 4]
        System.out.println(nestedList.get(0).get(0)); // Output: 1
        System.out.println(nestedList.get(1).get(1)); // Output: 4
        nestedList.get(0).set(1, 3); // updating an element in the nested array list
        System.out.println(nestedList); // Output: [[1, 3], [3, 4]]
        nestedList.clear(); // removing all elements from the nested array list
        System.out.println(nestedList); // Output: []
    }
}