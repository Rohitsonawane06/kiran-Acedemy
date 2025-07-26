// Destructuring
// Types of Destructuring:
// Array Destructuring
    number=[33,22,36,4]
   let [a,b,c]=[33,22,36,43];
    console.log(a);
    console.log(b);
    console.log(c);
// Object Destructuring
student={id:101,name:'rohit',age:25}
let {id,name}=student
console.log(id)
console.log(name)

//Spread
console.log(number);
console.log(...number,87);
console.log(number);


ne=[...number,18];
console.log(ne);



arryone=[1,2,3,4];
arrtwo=[5,6,7,8]
merge=[...arryone,...arrtwo];
console.log(...merge);


//Date and Time

