//! Hash Map
// Hash Map is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
// It is a non-sequential data structure, meaning that the order of elements is not guaranteed.
// Hash Map is a collection of key-value pairs, where each key is unique. It is also known as a dictionary, map, or associative array.
// Hash Map is a part of the Java Collections Framework and is present in java.util package. unlike python it is not a built-in data structure in Java.
// ex of hash table {'apple': 1, 'banana': 2, 'orange': 3} here the keys are the apple, banana and orange and the values are 1, 2 and 3 respectively
// * NOTE: keys must be unique and values can be duplicate

// ! Hash map vs hash table
/* 
 * Comparison Between HashMap and Hashtable in Java:
 * 
 * 1. Thread Safety:
 *    - HashMap: Not synchronized (not thread-safe).
 *    - Hashtable: Synchronized (thread-safe).
 * 
 * 2. Null Keys/Values:
 *    - HashMap: Allows one null key and multiple null values.
 *    - Hashtable: Does not allow null keys or null values.
 * 
 * 3. Performance:
 *    - HashMap: Faster due to lack of synchronization.
 *    - Hashtable: Slower because of synchronization overhead.
 * 
 * 4. Legacy Status:
 *    - HashMap: Part of the Java Collections Framework (introduced in Java 1.2).
 *    - Hashtable: Legacy class (introduced in Java 1.0).
 * 
 * 5. Usage in Modern Code:
 *    - HashMap: Preferred for non-threaded applications.
 *    - Hashtable: Rarely used; ConcurrentHashMap is preferred for thread-safe usage. 
*/

// Hash Map:
package Java.Data_Structures;
import java.util.HashMap;
import java.util.ArrayList;

public class Hash_Map {
    public static void main(String[] args) {
        // * Create a HashMap syntax: HashMap<KeyType, ValueType> mapname = new HashMap<>();
        HashMap<Integer, String> map = new HashMap<>();

        // Insert key-value pairs using the put() method
        map.put(1, "Apple");
        map.put(2, "Banana");
        map.put(3, "Cherry");

        // print the map
        System.out.println(map); // Output: {1=Apple, 2=Banana, 3=Cherry}

        // Retrieve a value by key using the get() method using the key
        System.out.println("Value for key 2: " + map.get(2)); // Output: Banana

        // Check if a key exists using the containsKey() method using the key
        System.out.println("Contains key 1: " + map.containsKey(1)); // Output: true

        // Remove a key-value pair using the remove() using the key
        map.remove(3);

        // Iterate over the HashMap using a for-each loop where we iterate over the keys in the HashMap using the keySet() method which returns a Set of keys
        for (Integer key : map.keySet()) {
            System.out.println("Key: " + key + ", Value: " + map.get(key)); // use get method to get the value of the key
        }

        // * assigning an list to a hash maps keys as a value using the ArrayList
        // Creating a HashMap with String keys and ArrayList values
        HashMap<String, ArrayList<Integer>> maplist = new HashMap<>(); 
        
        // * array list
        // Adding an ArrayList for key "A"
        // array list is a better data structure than arrays as it is dynamic and can grow or shrink in size
        // its also has many methods built in for manipulating the list
        // array list syntax: ArrayList<DataType> listname = new ArrayList<>();
        ArrayList<Integer> listA = new ArrayList<>();
        listA.add(1);
        listA.add(2);
        listA.add(3);
        maplist.put("A", listA); //listA = [1, 2, 3]
        
        // Adding an ArrayList for key "B"
        ArrayList<Integer> listB = new ArrayList<>();
        listB.add(4);
        listB.add(5);
        maplist.put("B", listB);

        // Adding more values to the list of key "A"
        maplist.get("A").add(4);
        
        // Output the map
        System.out.println(maplist);  // Output: {A=[1, 2, 3, 4], B=[4, 5]}
        
        // Access values in the list for key "A"
        ArrayList<Integer> retrievedList = maplist.get("A");
        System.out.println("Values for key 'A': " + retrievedList); // Output: Values for key 'A': [1, 2, 3, 4]

    }
}
