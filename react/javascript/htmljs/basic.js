console.log(document);
let h1 = document.getElementById('h1tag');

let btn = document.getElementById('btn');
btn.addEventListener('click', () => {
    let body=document.body;
    let p=document.createElement("p");
    p.innerText="this is paragraph";
    body.appendChild(p);
    h1.innerText = "hello";
});

