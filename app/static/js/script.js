const signInBtn = document.querySelector('.signin-btn');
const signUpBtn = document.querySelector('.signup-btn');
const formBox = document.querySelector('.form-box');
const mainBlock = document.querySelector('.block');
const body = document.body;

signUpBtn.addEventListener('click', function() { /*обработчик событий на клик*/
    formBox.classList.add('active'); /*При нажатии, добавляем блоку класс active*/
    body.classList.add('active'); /*Меняем фон*/
    mainBlock.classList.add('active');
});

signInBtn.addEventListener('click', function() { /*обработчик событий на клик*/
    formBox.classList.remove('active'); /*При нажатии, убираем у блока класс active*/
    body.classList.remove('active');
    mainBlock.classList.remove('active');
});