/*jslint devel: true */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
/*eslint-env es6*/
/*exported showAlert()*/
/* eslint-disable no-console */


function uppercase() {
            document.getElementById("myP").style.textTransform = "capitalize";} 
            
function attyChange() {
            document.getElementById("myP").className = "orange";}
            
function insertFunc3() {
    var elementToBeAddedTo = document.getElementById("AddToThisElement");
    elementToBeAddedTo.insertAdjacentHTML('afterend', '<div>To learn more about World Hunger, visit the sites on the bottom of this page! </div>');}

let visitingWebsite = true;
    let notVistingWebsite = false;

    if (visitingWebsite){
        alert("Welcome to WHI's Contact page!");
    } else {
        alert('Visit my Contact page!');
}

function removioli() {
var elementToRemove = document.getElementById("RemoveThisParagraph");
elementToRemove.remove();}  
                
function attChange() {
    document.getElementById("myPa").className = "orange";}
                
function insertFunc1() {
var elementToBeAddedTo = document.getElementById("AddToThisElement");
    elementToBeAddedTo.insertAdjacentHTML('afterend', '<p>My email is already above 😂 However, in case you removed it, it is ymorsi8@gmail.com</p>');}

function removiolisection() {
var elementToRemove = document.getElementById("RemoveThisSection");
   elementToRemove.remove();}      
    
// (JS Rubric Item 7) Below is one of the 5 required JS variables (2)
// (JS Rubric Item 3) Below is a use of the innerHTML element with JavaScript(1)              
var var2 = ["Here, you will have access to:"];
    document.getElementById("var2").innerHTML = var2;
  
// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction1();}
//(JS Rubric Item 10) Below is one of the function uses in JavaScript(3)    
function myFunction1() {
// (JS Rubric Item 7) Below is one of the 5 required JS variables (5)    
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";}  

function insertFunc2() {
            var elementToBeAddedTo = document.getElementById("AddToThisElement");
    elementToBeAddedTo.insertAdjacentHTML('afterend', '<section><b>Below you will be able to find important links to organizations that you can donate to to help resolve this large, international issue! There is also a calculator that you can use to calculate how much you can donate to the cause!</b></section>')}

// (JS Rubric Item 7) Below is one of the 5 required JS variables (3)
var rangeslider = document.getElementById("sliderRange"); 
// (JS Rubric Item 7) Below is one of the 5 required JS variables (4)    
var output = document.getElementById("demo"); 
output.innerHTML = rangeslider.value; 
  
rangeslider.oninput = function() { 
  output.innerHTML = this.value; }        
     
//(JS Rubric Item 10) Below is one of the function uses in JavaScript(2)-->      
       
function donate() { 
    num1 = output.innerHTML/'100';
    num2 = document.getElementById("secondNumber").value;
        document.getElementById("result").innerHTML = (num1 * num2);}

// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction3()};

function myFunction3() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}    
    

function noice() {
  var txt;
  var r = alert("You're Going To A New Window!");
  if (r == false) {
    txt = "Thanks for Staying!";
  } else {
    txt = "Bye!";  }
  document.getElementById("sampletext").innerHTML = txt;}

// (JS Rubric Item 7) Below is one of the 5 required JS variables (1)
            var vplaces = ["Burundi", " Eritrea", " Timor-Leste", " Comoros", " Chad", " Ethiopia", " Yemen", " Zambia", " Haiti", " Instanbul", " Madagascar"];
            document.getElementById("places").innerHTML = vplaces;

function removiolidiv(){
    var elementToRemove = document.getElementById("RemoveThisDiv");
    elementToRemove.remove();}
 
/*
function changeText(){
	   document.getElementById("sampletext").innerHTML = "A Reminder of the Cause";}

function changeText2(){
	document.getElementById("sampletext1").innerHTML = "@Unicef";}

function attChange() {
    document.getElementById("myPa").className = "orange";} */







