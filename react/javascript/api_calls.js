async function getData(){
    try {
        let raw= await fetch('https://dummyjson.com/user/login');
        let data= await raw.json();
        console.log(data);
        
    } catch (error) {
        console.log(error);
        
    }
}
getData();


function getdata2(){
    fetch('https://dummyjson.com/users')
    .then((raw)=>raw.json())
    .then((data)=>console.log(data))
    .catch((error)=> console.log(error));
    
    
}
getdata2()