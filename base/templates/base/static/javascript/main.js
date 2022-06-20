
var menu = document.querySelectorAll('#menu-icon')
var exit = document.querySelectorAll('#exit-icon')
var sidebar = document.querySelector('.sidebar')
var closebtnTut = document.querySelectorAll('.close-btn')
var closebtnStud = document.querySelectorAll('.close-btn')
var tut_det = document.querySelector('.tutor-content')
var stud_det = document.querySelector('.student-content')
var main_content = document.querySelector('.main-content')

console.log(closebtnTut.length)
console.log(closebtnStud.length)

for (let index = 0; index < closebtnTut.length; index++) {
    closebtnTut[index].addEventListener('click',() =>{
        tut_det.parentElement.style.display = "none"
        console.log("yes")
    }); 
}

for (let index = 0; index < closebtnStud.length; index++) {
    closebtnStud[index].addEventListener('click',() =>{
        stud_det.parentElement.style.display = "none"
        console.log("yes")
    });
}

for (let index = 0; index < menu.length; index++) {
    menu[index].addEventListener('click',() =>{
   
        sidebar.style.width = "250px"
        menu[index].classList.remove('bx-x');
    });
}

for (let index = 0; index < exit.length; index++) {
    exit[index].addEventListener('click',() =>{
        sidebar.style.width = "0px"
        main_content.style.marginLeft = "0px"  
        menu[index].classList.add('bx-menu');
    });
    
}









