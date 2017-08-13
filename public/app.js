'use strict';

//Hide modal when index page loads
function hideModal(){
  $('#login-signup').hide();
};

//Display modal when join is clicked
function displayModal(){
  $('.join-box').on('click', function(){
    $('#login-signup').show();
    $('#login-signup').addClass('wrapper');
    $('body').addClass('wrapper-body');
    $('#footer, #header .content-container, .top-section').addClass('wrapper-body');
  });
};

//This needs to go somewhere else in a function for when it shows.
function defautState(){
  $('.signup-form__container').hide();
}

function signUpState(){
  $('#modal__right').on('click', function() {
    $('#modal__left').removeClass('tab--active');
    $('.login-form__container').hide();
    $('.signup-form__container').show();
    $('#modal__right').toggleClass('tab--active');
  });
};

function loginState(){
  $('#modal__left').on('click', function() {
    $('#modal__right').removeClass('tab--active');
    $('.signup-form__container').hide();
    $('.login-form__container').show();
    $('#modal__left').toggleClass('tab--active');
  });
};

hideModal();
displayModal();
defautState();
signUpState();
loginState();
