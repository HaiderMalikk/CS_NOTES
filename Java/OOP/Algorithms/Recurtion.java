package Java.OOP.Algorithms;

public class Recurtion {
    // function static so it can be called in static method main

    // * factorial non tail (given int n n factorial is n * (n-1) * (n-2) * ... * 1)
    // this is non tail recution as no result is being accumulated and we calculate the fib once the base case is reached
    // then we return from each function call and calculate the fib and pass the result the the previous call until we reach the first call
    static int fact(int n){
        // base case
        if (n == 0 || n == 1){
            return n;
        }
        // recursive case
        return n * fact(n-1);
    }
    /* here the fact reach base case then goes 1*2 retunes the rusult and then 3*2 returns the result and so on until n * n-1 happens and we return this result */
    // * tail recurtion 
    // her ewe calculate the factorial before we pass it into the function now the function has the result of the last factorial
    // after the final calulation and base case we already have the reult of thr factorial on n now we simply return this result to the previous call
    // and so on until we reach the first call but the value returned at each call is the final result
    // for n=5 we go 5 * fact(5-1) until n=1 then we go 2*1 as for we return 1 to the function call with n=2 this 2*1 is returned to the function call with n=3
    // her we do 3*2 and then 4*6 and then 5*24 = 120 and thats returnd
    static int factTail(int n, int acc){ // acc is the accumulator it accumulates the result so far.
        // base case
        if (n == 0 || n == 1){
            return acc;
        }
        // recursive case
        return factTail(n-1, n * acc); // here we calculate the factorial before we pass it into the function
    }
    /// here we start by multipling n*1 as acc is one initially then we pass that result to the function call as acc
    /// in the next call we multiply n-1 by this acc value, so for n=5 we go 5*1 = 5 then in the next call ts 4*5 and we pass that as the acc value
    // then we go 3*20 and so on until we reach the base case of n=1 or 0 here acc is 120 as in the last case we would have done 1*120
    // then we return the acc value which is the factorial of n we return 120 to the last function call and so on until we reach the first call
    // NOTE: YOU MUST PASS ACC AS 1 when calling the function as at first we are multiplying n*1

    // * Fibonacci (given int n n fibonacci is F(n) = F(n-1) + F(n-2) where F(0) = 0 and F(1) = 1) n is the nth number in the sequence
    static int fib(int n){
        // base case
        if (n == 0 || n == 1){
            return n;
        }
        // recursive case
        return fib(n-1) + fib(n-2); // finish the left side (fib(n-1) before we can do the right side (fib(n-2)) as the function fib(n-1) is called before fib(n-2) in every recursive call
    }

    static boolean isPalindrome(String s){
        // base case
        if (s.length() == 0 || s.length() == 1){
            return true;
        }
        // recursive case
        return s.charAt(0) == s.charAt(s.length()-1) && isPalindrome(s.substring(1, s.length()-1)); // check is first and lats letters of the curretn string are equal and then do the same for the string minus the first and last letters we just checked
    }
    // all positve
    /* 
    to check if all elements in an array are positive we can use recurtion
    but insted of passing in a smaller and smaller copy array we inted use pointers to point at the start and finish of the array
    using this we can make the pointers shorter and shorter to pass in a smaller and smaller version of the array
    we make the array smaller by changing the range we are evaluating

    in this function the idea is make the array shorter by changing the range we are evaluating until the range start and end is the same
    at that point we can evaluate the current element for being positive and compare it with the start pointer for the array from the last call
    this start pointer from the last call is one less the current start pointer so we would be checking is the element before the one that was positive
    is also positive we keep doing this for the element before untill we reach the start pointer of the array passed in at the first call
    */
    static boolean allPositive(int[] a) {
        return allPositiveHelper (a, 0, a.length - 1); // start at the beginning and end of the array
    }
    static boolean allPositiveHelper (int[] a, int from, int to) {
        if (from > to) { /* base case 1: empty range */
            return true; // since no elements its true as is equivalent to all positive
        }
        else if(from == to) { /* base case 2: range of one element */ 
            return a[from] > 0; // since there is only one element we can check if it is positive (one element as start and end are the same)
        }
        else { /* recursive case */
            // check if the current starting element is positive and if the rest of the array is positive
            // once we reach the base case of only comparing one element the recurtion call will return true
            // and we compare with a[from] but since this would be the caller of the function that caused base case 
            // 'from' would give the element before the one that was positive (from = end - 1)
            // short circuiting ensurees if the first element is not positive we do not need to check the rest of the array
            return a[from] > 0 && allPositiveHelper (a, from + 1, to); 
        }
    }

    static boolean isSorted(int[] a) { // for non-decreasing array
        return isSortedHelper (a, 0, a.length - 1);
    }
    static boolean isSortedHelper (int[] a, int from, int to) { 
        if (from > to) { /* base case 1: empty range */ // as to is len-1 if arr is emty to is -1 while from is 0 so the array is empty 
            return true; 
        }
        else if(from == to) { /* base case 2: range of one element = reached the last element */ 
            return true;
        }
        else {  
            // check if current element is less than the next element and if the rest of the array is sorted
            // at base case we reaach one element return true them comapre to the previous element and so on for the rest of the array
            return a[from] <= a[from + 1] && isSortedHelper (a, from + 1, to);
        }
    }
    /* 
     without using two points to mark the start and end of the array we would need to make a copy of the array and pass in the copy
     if (arr.length == 1){ // new base case as we are making a copy of the array at some point it will reach a length of 1 as we keep making it smaller
            return true;
    }
     // make a copy of the array where we skip the first element of the original array
     int[] newarr = new int[arr.length-1];
        for(int i = 0; i<arr.length-1; i++){
            newarr[i] = arr[i+1];
        }
        // check if the first element of the original array is less than the first elementof the original array
        // then pass teh new array to check if its sorted 
        return arr[0] < arr[1] && issorted(newarr);

        // this is mucb slower than using two pointers
     */


    public static void main(String[] args) {
        System.out.println(fact(5)); // 120
        System.out.println(factTail(5, 1)); // 120
        System.out.println(fib(10)); // 55 (fib sequence = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55) 55 is the 10th number in the sequence
        System.out.println(isPalindrome("racecar")); // true
        System.out.println(allPositive(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10})); // true
        System.out.println(isSorted(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10})); // true
    }

}