const targetElement = document.body;
const header = document.createElement("header");
const navbar = document.createElement("nav");
navbar.id = "headBar";
const navList = document.createElement("ul");
navList.classList.add("title-link");

const navItems = [
    { text: 'Home', href: 'index.html' },
    { text: 'About Me', href: 'aboutMe.html' },
    { text: 'Now', href: 'now.html' },
    { text: 'Projects', href: 'projects.html' },
    { text: 'Contact me', href: 'contactme.html' }
];

navItems.forEach(itemData=>{
    const listItem = document.createElement("li");
    const link = document.createElement('a');
    link.href = itemData.href;
    link.textContent = itemData.text;
    link.classList.add("title-link");
    listItem.appendChild(link);
    navList.appendChild(listItem);
})

navbar.appendChild(navList);
header.appendChild(navbar)
targetElement.prepend(header);