
const LoadAllProduct = () => {
    fetch('https://fakestoreapi.com/products')
            .then(res=>res.json())
            .then(json=>DisplayProduct(json))
        .catch(error => console.error('Error fetching data:', error));
};

const DisplayProduct = (items) => {
    const parent = document.getElementById("card_container");
        parent.innerHTML=""
        console.log(items);
        items.forEach(item => {
        
        const card_section = document.createElement("div");
        card_section.classList="full_card"
        card_section.innerHTML=`
        
        <div class="card" style="width: 18rem;">
        <img src="${item.image}" class="card-img-top " alt="">
            <div class="card-body">
                <h5 class="card-title">${item.title}</h5>
                <h5 class="card-text">${item.category}</h5>
                <p class="card-text">${item.description.slice(0, 140)}</p>
                <p class="card-text">Price :$${item.price}</p>
                <p class="card-text">Rating :${item.rating.rate} </p>
                <p class="card-text ">Count : ${item.rating.count} </p>
                <a href="#" class="btn btn-primary">BuyNow</a>
                <a href="singlepage.html?id=${item.id}" class="btn btn-primary">Details</a>
            </div>
      </div>
        `;
        parent.appendChild(card_section)
        });
       
};

const LoadAllCategory=()=>{
    fetch('https://fakestoreapi.com/products/categories')
            .then(res=>res.json())
            .then(json=>DisplayAllCategory(json))
            .catch(error => console.error('Error fetching data:', error));

}



const DisplayAllCategory = (category) => {
    const parent = document.getElementById("button_section");
    category.forEach(cat=>{
        const button_section = document.createElement("div");
        button_section.classList = "button_container";
        button_section.innerHTML = `
        <button onclick='LoadCategoryWise("${cat}")' type="button" class="btn btn-danger">${cat}</button>
        `;
        parent.appendChild(button_section);

    })
    // const button_section = document.createElement("div");
    // button_section.classList = "button_container";
    // button_section.innerHTML = `
        
    // // `;

    // for (let i = 0; i < category.length; i++) {
    //     console.log(category);
    //     const button_section = document.createElement("div");
    //     button_section.classList = "button_container";
    //     button_section.innerHTML = `
    //         <button onclick="LoadCategoryWise('${category[i]}')" type="button" class="btn   btn-danger">${category[i]}</button>
    //     `;
    //     parent.appendChild(button_section);
    // };
}

const LoadCategoryWise = (cat) => {

    fetch(`https://fakestoreapi.com/products/category/${cat}`)
        .then(res => res.json())
        .then(json =>{
            
            DisplayProduct(json)})
        .catch(error => console.error('Error fetching category:', error));
}

const DisplayCategoryWise=(item)=>{
    console.log(item);
}




LoadAllProduct();
LoadAllCategory();
// LoadCategoryWise()
