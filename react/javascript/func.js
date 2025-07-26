// // Array of Functions
// console.log("=======================Array of Functions=======================");
// //filter function
// //The filter() method in JavaScript is an array method that creates a new array containing all elements from the original array that satisfy a specific condition. It does not modify the original array.

// productsname=["laptop","mobile","tablet","smartwatch"];
// data=productsname.filter(product => product== "tablet");
// console.log(data);

// let products=[
//     {id:101,name:"laptop",price:500,qty :100},
//     {id:102,name:"mobile",price:200,qty :200},
//     {id:103,name:"tablet",price:300,qty :150},    
//     {id:104,name:"smartwatch",price:100,qty :300}
// ];
// data=products.filter(product => product.price > 100 && product.qty > 150);
// console.log(data);


// //map function
// //The map() method in JavaScript is a higher-order function available on Array instances. It is used to create a new array by applying a provided callback function to each element of the existing array. The key characteristics of map()

// console.log("=======================Map Function=======================");
// number=[1,2,3,4,5];
// square=number.map(num => num * num);
// console.log(square);

// productsname=["laptop","mobile","tablet","smartwatch"];
// captil=productsname.map(product=>product.toUpperCase());
// console.log(captil);


// let names = ["rohit", "amit", "sneha"];

// let capitalizedNames = names.map(name => name[0].toUpperCase() + name.slice(1));

// console.log(capitalizedNames);

// console.log("=======================Map Function change price =======================");
// discount=products.map(product=>product.price*1.15);
// console.log(discount);
// console.log(products);   

// updateproducts=products.map(product=>{
//     product.price=product.price*1.15;
//     return product;
// });
// console.log(updateproducts)


console.log("reduce function");
//The reduce() method in JavaScript is a higher-order function available on Array instances. It is used to apply a provided callback function to each element of the array, reducing the array to a single value. The reduce() method takes two arguments: a callback function and an optional initial value.
console.log("=======================Reduce Function=======================");
employees=[
    {id:101,name:"rohit",salary:5000},
    {id:102,name:"amit",salary:6000},
    {id:103,name:"sneha",salary:7000},
    {id:104,name:"rohit",salary:8000}
];

// sum=employees.reduce((sum,curtEmp)=>sum+curtEmp.salary,0);
// console.log(sum);

// nm=employees.find(emp=>emp.name==="rohit")
// console.log(nm);


// slice=employees.slice(1,3);
// console.log(slice);

// emp=employees.push({id:105, name:"Vijat",salary:30000})
// employees.push(emp);

// emp=employees.forEach(emp=>console.log(emp));
// console.log(emp);

// nm=employees.pop();
// console.log(nm);
// console.log(employees);

// emp=employees.shift({id:105, name:"Vijat",salary:30000})
// employees.shift(emp);
// console.log(employees)

// emp=employees.unshift({id:101,name:"Rohit",salary:50000})
// employees.unshift(emp);
// console.log(employees);

// emp=employees.every(emp=>emp.salary==6000);
// console.log(emp);



emp=employees.some(emp=>emp.salary==6000);
console.log(emp);

// username='rohit'
// msg=`hello,${username}`;
// console.log(msg);

function hello(name){
    console.log(`hii ${name}`)
}
hello('rohit');

