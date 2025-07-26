1]how to define  varibale in javascript

    syntax:
        there are three types of to define varibale
        1] var age=20;
            # var varibale can be redeclared ,reassigned
            # using the function scope 

        2] let firstname="Ram";
            # letr varible can be reassigned but not  redeclared
            # scope : block
            example:
                function f1(){
                    var a=10 # function level scope
                    if(true){
                        let a=20 # block level scope
                    }
                }

        3] const pi=3.14
            # one time declared the value are not changeable


2] Data Types

    typeof "Hello"     // "string"
    typeof 123         // "number"
    typeof true        // "boolean"
    typeof undefined   // "undefined"
    typeof null        // "object"  // (This is a known JavaScript bug)
    typeof {a:1}       // "object"
    typeof [1,2,3]     // "object"  // Arrays are also objects
    typeof function(){} // "function"



3] Oprator


4] function
    1]filter:
        filterout some data from exissting as per condition
        example:
            suppose student given test and now there rsult stored in somewhere the user  want to findout such
            students whose marks is 80 or more  
    2] Map:
        to transfored or modify existing data that we used map function
        example:
            user want to display every student firstname in uppercase


        can we user both map& Filter at a time >>yes

        example:
            if user want to increasee salary of person whose belong pertcular department

    3] reduce:
        The reduce() method in JavaScript is used to reduce an array to a single value (like sum, product, object, etc.) by applying a function to each element.

    4]find:
        The find() method returns the first element in the array that satisfies a condition (callback function).
        If no element is found, it returns undefined.


    5] slice :
        The slice() method returns a shallow copy of a portion of an array (or string) into a new array, without modifying the original one.

            start – index to start slicing (inclusive)

            end – index to stop slicing (exclusive)

    6]push:
        The push() method is used to add one or more elements to the end of an array.
        It modifies the original array and returns the new length of the array.

    7]forEach:
        The forEach() method is used to loop through each element in an array and perform a specific action.
        It does not return anything and does not change the original array (unless modified manually).

    8]pop:
        remove the last Element by default set the alredy to using the pop function 

    9]shift:
        remove the firct element by default and return this elemennt 

    10]unshift:
          The unshift method is used to add one or more elements to the start of an array.
    
    11]every:
        check all employee salry to equal or not the salary is not eual to retur the false
    
    12]some:
        check the whose the employee salary are same the retrn the true.

    13]string literlas:
        to contact the string 

    14] Default function paramter:
            Default function parameters allow you to assign a default value to a function parameter if no value is passed 
            (or if undefined is passed) when the function is called.
    
-------------------------------------------------------------------------------------------------------------------------------------
Destructuring
Destructuring is a feature in JavaScript that allows you to unpack values from arrays or extract properties from objects into separate variables in a clean and simple way.

--------------------------------------------------------------------------------------------------------------
Spread
The spread operator (...) is used to "spread out" the elements of an array or properties of an object into individual items.
-----------------------------------------------------------------------------------------------------------------------------
# Synchronous
    
Synchronous means one task is executed at a time, and next task starts only when the previous one is finished.

# Asynchronous
  Asynchronous means JavaScript does not wait for a task to finish — it starts the task and moves to the next line immediately.

# setInterval
setInterval() is a JavaScript function that runs a piece of code again and again after a fixed time gap (interval).
-----------------------------------------------------------------------------------------------------------------------------

# DOM-(Document Object Model Manipulation)

