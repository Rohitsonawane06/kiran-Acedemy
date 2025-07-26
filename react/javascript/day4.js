// Synchronous
console.log("started");
for(let i=1;i<5;i++){
    console.log(i);
    
}
console.log("Ended");



//Asynchronous
console.log("started");
setTimeout(()=>{
    console.log("Mid");
    
})
console.log("Ended");

console.log("-----------------setInterval---------------------");
let count=0;
let id =setInterval(()=>{
    count++;
    console.log(count);

    if (count==5){
    clearInterval(id);
    }

    
},1000)


