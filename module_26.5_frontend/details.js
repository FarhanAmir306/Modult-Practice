
const LoadSingleProduct=(id)=>{
    const peram = new URLSearchParams(window.location.search).get("id");
    fetch(`https://fakestoreapi.com/products/${peram}`)
            .then(res=>res.json())
            .then(json=>DisplaySingleProduct(json))

}

const DisplaySingleProduct =(items)=>{
    console.log(items);
    const parent=document.getElementById("single_section")
    const card=document.createElement("div")
    card.classList="single_page_style"
    card.innerHTML=`
    <div class="right">
    <img src="${items.image}" alt="" class="w-25">
    </div>
    <div class="left">
    <h1 class="title">
    ${items.title}
    </h1>
    <p>${items.category}</p>
    <p>${items.description}</p>
    <p>${items.rating.rate}</p>
    <p>${items.rating.count}</p>
    <p>${items.price}</p>
  </div>
    
    `;
    parent.appendChild(card)

 
}
LoadSingleProduct()