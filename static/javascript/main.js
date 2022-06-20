var subject_input = document.getElementById('subject_input')
var menu = document.querySelectorAll('#menu-icon')
var exit = document.querySelectorAll('#exit-icon')
var sidebar = document.querySelector('.sidebar')
var closebtnTut = document.querySelectorAll('.close-btn')
var closebtnStud = document.querySelectorAll('.close-btn')
var tut_det = document.querySelector('.tutor-content')
var stud_det = document.querySelector('.student-content')
var main_content = document.querySelector('.main-content')
var add_field = document.getElementById('add_field')
var remove_field = document.getElementById('remove_field')
var counter = 0

for (let index = 0; index < closebtnTut.length; index++) {
    closebtnTut[index].addEventListener('click',() =>{
        tut_det.parentElement.remove()
    }); 
}

for (let index = 0; index < closebtnStud.length; index++) {
    closebtnStud[index].addEventListener('click',() =>{
        stud_det.parentElement.remove()   
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

add_field.addEventListener('click',()=>{
    counter+=1
    if(counter == 1){
        var new_field = document.createElement('input');
        new_field.setAttribute('name','new_subject');
        new_field.setAttribute('placeholder','Add Your Subject');
        
        subject_input.appendChild(new_field)
    }else{
        alert("Only one field can be added")
    }
    console.log(counter)
})

remove_field.addEventListener('click',()=>{
    var input_tags = subject_input.getElementsByTagName('input')
    if(input_tags.length > 0 ){
        subject_input.removeChild(input_tags[(input_tags.length)-1])
        counter = 0
        console.log("remove")
    }
    
})









