'use strict';

$(document).ready(function(){
  $('.signup-form__container').hide();
});

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

signUpState();
loginState();
