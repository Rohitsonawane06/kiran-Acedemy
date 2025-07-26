//Date

date=new Date();
console.log(date);

date2=new Date("2025-07-27")
console.log(date2);


date3=new Date(2025,7,22,15,18,45,111);
console.log(date3);

//Predifined Function
console.log(date.getFullYear());
console.log(date.getMonth());
console.log(date.getDay());
console.log(date.getDate());


mydate=new Date();
mydate.setFullYear(2024);
mydate.setMonth(4);

console.log(mydate);



//Date Formating

console.log(mydate.toDateString());
console.log(mydate.toTimeString());


//custome Date Formating
// console.log(mydate.toLocalDatestring());

function formatDate(d){
    return `${d.getFullYear()}-${d.getMonth()}-${d.getDay()}`
}
console.log(formatDate(mydate));



console.log("USING INTL");
let formater=INTLDateTimeformat('en-US');
console.log(formater.format(mydate));

