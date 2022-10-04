index_markup = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TalkItOut</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.12/typed.min.js"></script>

    <style>
        /* Google font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Ubuntu:wght@400;500;700&display=swap');
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    scroll-behavior: smooth;
}
:root{
    --primary-color:#581B98;
    --black-color:#1d1d1d;
    --white-color:#e7e3e3;
}
body *{
    transition: 0.3s;
}
body{
    font-family: 'Poppins', sans-serif;
    background-color: var(--white-color);
}
/* Custom Scroll Bar css */
::-webkit-scrollbar{
    width: 10px;
}
::-webkit-scrollbar-track{
    background-color: #f1f1f1;
}
::-webkit-scrollbar-thumb{
    background-color:var(--primary-color);
    border-radius: 12px;
    transition: all 0.3s ease;
}
::-webkit-scrollbar-thumb:hover{
    background-color:var(--primary-color);
}
/*navbar styling */
nav{
    position: fixed;
    width: 100%;
    padding: 20px 0;
    z-index: 999;
    transition: all 0.3s ease;
}
nav.sticky{
    background-color: var(--primary-color);
    padding: 13px 0;
}
nav .navbar{
    width: 90%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: auto;
} 
nav .navbar .logo a{
    font-weight: 500;
    font-size: 35px;
    color: var(--primary-color);
}   
nav.sticky .navbar .logo a{
    color:var(--white-color);
}
nav .navbar .menu{
    display: flex;
    position:relative;
}
nav .navbar .menu li{
    list-style: none;
    margin: 0 8px;
}
nav .navbar .menu a{
    font-size: 18px;
    font-weight: 500;
    color: var(--black-color);
    padding: 6px 0;
    transition: all 0.4s ease;
}
.navbar .menu a:hover{
    color: var(--primary-color);
}
nav.sticky .menu a{
    color: var(--white-color);
}
nav.sticky .menu a:hover{
    color: var(--black-color);
}
.navbar .media-icons a{
    color: var(--primary-color);
    font-size: 30px;
    margin: 0 6px;
}
nav.sticky .media-icons a{
    color: var(--white-color);
}

/* Side navigation Menu button CSS */
nav .menu-btn,
.navbar .menu .cancel-btn{
    position: absolute;
    color: var(--white-color);
    right: 30px;
    top:20px;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: none;
}
nav .menu-btn{
    color: var(--primary-color);
}
nav.sticky .menu-btn{
    color:var(--white-color);
}
.navbar .menu .menu-btn{
    color: var(--white-color);
}

/* home section styling */
.home{
    height:100vh;
    width: 100%;
    background-color: var(--white-color);
    background-size: cover;
    background-position: center center;
    background-attachment: fixed;
}
.home .home-content{
    width: 90%;
    height: 100%;
    margin: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.home .text-one{
    font-size: 25px;
    color: var(--black-color);
}
.home .text-two{
    font-size: 75px;
    font-weight: 600;
    margin-left: -3px;
    color: var(--black-color);
}
.home .text-three{
    font-size: 40px;
    margin: 5px 0;
    color: var(--black-color);
}
.home .text-three span{
    font-size: 40px;
    margin: 5px 0;
    font-weight: 500;
    color: var(--primary-color);
}

.home .text-four{
    font-size: 23px;
    margin: 5px 0;
    color: var(--black-color);
}
.home .button2{
    margin: 14px 0;
}
.home .button2 button{
    outline: none;
    padding: 8px;
    border-radius: 6px;
    font-size: 25px;
    font-weight: 400;
    background-color: var(--primary-color);
    color: var(--white-color);
    cursor: pointer;
    border: 2px solid transparent;
    transition: all 0.4s ease;
}
.home .button2 button:hover{
    border-color: var(--primary-color);
    background-color: var(--white-color);
    color: var(--primary-color);
}
/* Footer CSS */
footer{
    background: var(--primary-color);
    padding: 15px 0;
    text-align: center;
    font-family: 'Poppins', sans-serif;
}
footer .text span{
    font-size: 17px;
    font-weight: 400;
    color: var(--white-color);
}
footer .text span a{
    font-weight: 500;
    color:var(--white-color);
}
footer .text span a:hover{
    text-decoration:underline;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Nunito', sans-serif;
    font-weight: 400;
    font-size: 100%;
    background: #F1F1F1;
}

*, html {
    --primaryGradient: linear-gradient(93.12deg, #581B98 0.52%, #9C1DE7 100%);
    --secondaryGradient: linear-gradient(268.91deg, #581B98 -2.14%, #9C1DE7 99.69%);
    --primaryBoxShadow: 0px 10px 15px rgba(0, 0, 0, 0.1);
    --secondaryBoxShadow: 0px -10px 15px rgba(0, 0, 0, 0.1);
    --primary: #581B98;
}

/* About Section Styling */
section{
    padding-top: 40px;
}
section .content{
    width: 80%;
    margin: 40px auto;
    font-family: 'Poppins' sans-serif;
}
section .title{
    display: flex;
    justify-content: center;
    margin-bottom: 40px;
}
section .title span{
    color: var(--black-color);
    font-size: 30px;
    font-weight: 600;
    position: relative;
    padding-bottom: 8px;
}
section .title span::before,
section .title span::after{
    content: '';
    position: absolute;
    height: 3px;
    width: 100%;
    background: var(--primary-color);
    left:0;
    bottom: 0;
}

section .title span::after{
    bottom:-7px;
    width: 70%;
    left:50%;
    transform:translateX(-50%);
}
.about .about-details{
    display:flex;
    justify-content: space-between;
    align-items: center;
}
.about .about-details .left{
    width: 45%;
}
.about .left img{
    height: 400px;
    width: 400px;
    object-fit:contain;
    border-radius: 12px;
}
.about .about-details .right{
    width: 55%;
}
section .topic{
    color: var(--black-color);
    font-size: 25px;
    font-weight: 500;
    margin-bottom: 10px;
    font-family: 'Poppins', sans-serif;
}
.about-details .right p{
    text-align: justify;
    color: var(--black-color);
    font-family: 'Poppins', sans-serif;
}
section .button{
    margin:16px 0;
    
}
section .button button{
    outline: none;
     background: var(--white-color);
    padding: 8px 16px;
    border-radius: 4px;
    font-size: 25px;
    font-weight: 400;
    color: var(--white-color);
    border: 2px solid transparent;
    cursor: pointer;
    transition: all 0.4s ease;
}
section .button button:hover{
    border-color: var(--primary-color);
    background: var(--white-color);
    color: var(--primary-color);
}

.contact .button{
    margin: 14px 0;
}
.contact .button button{
    outline: none;
    padding: 8px;
    border-radius: 6px;
    font-size: 20px;
    font-weight: 400;
    background-color: var(--white-color);
    color: var(--white-color);
    cursor: pointer;
    border: 2px solid transparent;
    transition: all 0.4s ease;
}
.contact .button button:hover{
    border-color: var(--primary-color);
    background-color: var(--white-color);
    color: var(--primary-color);
}

.contact .content{
    font-size: 18px;
    font-family: 'Nunito', sans-serif;
}

/* My Skills CSS */
.skills{
    background: #f0f8ff;
}
.skills .content{
    padding: 40px 0;
}
.skills .skills-details{
    display:flex;
    justify-content: space-between;
    align-items: center;
}
.skills-details .text{
    width:50%;
}
.skills-details p{
    color: var(--black-color);
    text-align: justify;
}
.skills .skills-details .experience{
    display: flex;
    align-items: center;
    margin: 0 10px;
}
.skills-details .experience .num{
    color: var(--black-color);
    font-size: 80px;
}
.skills-details .experience .exp{
    color:var(--black-color);
    margin-left: 20px;
    font-size: 18px;
    font-weight: 500;
    margin:0 6px;
}
.skills-details .boxes{
    width:45%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.skills-details .box{
    width: calc(100% / 2 - 20px);
    margin: 20px 0;
}
.skills-details .boxes .topic{
    font-size: 20px;
    color:var(--primary-color);
}
.skills-details .boxes .per{
    font-size: 60px;
    color: var(--primary-color);
}

/* My Services CSS */
.services .boxes{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.services .boxes .box{
    margin:20px 0;
    width:calc(100% / 3 - 20px);
    text-align: center;
    border-radius: 12px;
    padding: 30px 10px;
    box-shadow: 0 5px 10px rgba(0,0,0,0.12);
    cursor: default;
    transition: all 0.4s ease;
}
.services .boxes .box:hover{
    background: var(--primary-color);
    color: var(--white-color);
}
.services .boxes .box .icon{
    height: 50px;
    width: 50px;
    background: var(--primary-color);
    border-radius: 50%;
    text-align: center;
    line-height: 50px;
    font-size: 18px;
    color: var(--white-color);
    margin: 0 auto 10px auto;
    transition: all 0.4s ease;
}
.boxes .box:hover .icon{
    background: var(--white-color);
    color: var(--primary-color);
}
.services .boxes .box:hover .topic,
.services .boxes .box:hover p{
    color: var(--white-color);
    transition: all 0.4s ease;
}

/* CHATBOX
=============== */
.chatbox {
    position: absolute;
    bottom: 30px;
    right: 30px;
}

/* CONTENT IS CLOSE */
.chatbox__support {
    z-index: 100;
    display: flex;
    flex-direction: column;
    background: #eee;
    width: 300px;
    height: 350px;
    opacity: 0;
    transition: all .5s ease-in-out;
}


/* CONTENT ISOPEN */
.chatbox--active {
    transform: translateY(-40px);
    z-index: 123456;
    opacity: 1;

}

/* BUTTON */
.chatbox__button {
    text-align: right;
}

.send__button {
    padding: 6px;
    background: transparent;
    border: none;
    outline: none;
    cursor: pointer;
}


/* HEADER */
.chatbox__header {
    position: sticky;
    top: 0;
    right:2;
    background: orange;
}

/* MESSAGES */
.chatbox__messages {
    margin-top: auto;
    display: flex;
    overflow-y: scroll;
    flex-direction: column-reverse;
}

.messages__item {
    background: orange;
    max-width: 60.6%;
    width: fit-content;
}

.messages__item--operator {
    margin-left: auto;
}

.messages__item--visitor {
    margin-right: auto;
}

/* Contact Me CSS */
.contact{
    background: #f0f8ff;
}
.contact .content{
    margin: 0 auto;
    padding: 30px 0;
}
.contact .text{
    width: 80%;
    text-align: center;
    margin:auto;
}

/* FOOTER */
.chatbox__footer {
    position: sticky;
    bottom: 0;
}

.chatbox__support {
    z-index: 1-000
    background: #f9f9f9;
    height: 450px;
    width: 350px;
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

/* HEADER */
.chatbox__header {
    background: var(--primaryGradient);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 15px 20px;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    box-shadow: var(--primaryBoxShadow);
}

.chatbox__image--header {
    margin-right: 10px;
}

.chatbox__heading--header {
    font-size: 1.2rem;
    color: white;
}

.chatbox__description--header {
    font-size: .9rem;
    color: white;
}

/* Messages */
.chatbox__messages {
    padding: 0 20px;
}

.messages__item {
    margin-top: 10px;
    background: #E0E0E0;
    padding: 8px 12px;
    max-width: 70%;
}

.messages__item--visitor,
.messages__item--typing {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
}

.messages__item--operator {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    border-bottom-left-radius: 20px;
    background: var(--primary);
    color: white;
}

/* FOOTER */
.chatbox__footer {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 20px 20px;
    background: var(--secondaryGradient);
    box-shadow: var(--secondaryBoxShadow);
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
    margin-top: 20px;
}

.chatbox__footer input {
    width: 80%;
    border: none;
    padding: 10px 10px;
    border-radius: 30px;
    text-align: left;
}

.chatbox__send--footer {
    color: white;
}

.chatbox__button button,
.chatbox__button button:focus,
.chatbox__button button:visited {
    padding: 10px;
    border: none;
    outline: none;
    border-top-left-radius: 50px;
    border-top-right-radius: 50px;
    border-bottom-left-radius: 50px;
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
}

/* Responsive Media Queries */
@media (max-width:1190px){
    section .content{
        width: 85%;
    }
}
@media (max-width:1000px){
    .about .about-details{
        justify-content: center;
        flex-direction: column;
    }
    .about .about-details .left{
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .about .about-details .rights{
        width:90%;
        margin:40px 0;
    }
    .services .boxes .box{
        margin:20px 0;
        width: calc(100% / 2 - 20px);
    }
    
}
@media (max-width:900px){
    .about .left img{
        height:350px;
        width: 350px;;
    }
    section .button button{
        font-size: 20px;
    }
}
@media (max-width:750px){
    nav .navbar{
        width: 90%;
    }
    nav .navbar .menu{
        position: fixed;
        left: -100%;
        top: 0;
        background: var(--primary-color);
        height: 100vh;
        max-width: 400px;
        width: 100%;
        padding-top: 60px;
        flex-direction: column;
        align-items:center;
        transition: all 0.5s ease;
    }
    .navbar.active .menu{
        left: 0;
    }
    nav .navbar .menu a{
        font-size: 23px;
        display:block;
        color: var(--white-color);
        margin: 10px 0;
    }
    nav.sticky .menu a:hover{
        color:var(--primary-color);
    }
    nav .navbar .media-icons{
        display: none;
    } 
    nav .menu-btn,
    .navbar .menu .cancel-btn{
        display: block;
    }
    .home .text-two{
        font-size: 65px;
    }
    .home .text-three{
        font-size: 35px;
    }
    .skills .skills-details{
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .skills-details .text{
        width: 100%;
        margin-bottom: 50px;
    }
    .skills-details .boxes{
        justify-content:center;
        align-items: center;
        width: 100%;
    }
    .services .boxes .box{
        margin: 20px 0;
        width: 100%;
    }
    .contact .text{
        width: 100%;
    }
    section .button button{
        font-size: 15px;
    }
}
@media(max-width:500px){
    .home .text-two{
        font-size: 55px;
    }
    .home .text-three{
        font-size: 33px;
    }
    .skills-details .boxes .per{
        font-size: 50px;
        color: var(--primary-color);
    }
}
body{
    background: #f0f8ff;
}
.home{
background-color:#f0f8ff;
}
.about{
background-color: #f0f8ff;
}
.skills{
background: #f0f8ff;
}
.services{
background: #f0f8ff;
}
.contact{
background: #f0f8ff;
}
.remove-btn {
opacity: 0;
}
    </style>

   
</head>
<body>
 
<!--Navbar-->
    <nav>
        <div class="navbar">
        <div class="logo"><a href="#">Talk-it-Out.</a></div>
        <ul class="menu">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About Me</a></li>
            <li><a href="#services">About the team</a></li>
            <li><a href="#contact">Join us</a></li>
            <div class="cancel-btn">
                <i class="fas fa-times"></i>
            </div>
        </ul>
        <div class="media-icons">
            <a href="https://discord.gg/Xs6jXbcb"><i class="fab fa-discord"></i></a>
            <a href="https://chat.whatsapp.com/JLJVULcL5f3Iv8U3WdS5Wv"><i class="fab fa-whatsapp"></i></a>
        </div>
        </div>
        <div class="menu-btn">
            <i class="fas fa-bars"></i>
        </div>
    </nav> 

<!--Home Section Start-->
    <section class="home" id="home">
  <div class="home-content">
      <div class="text">
          <div class="text-one">Hello, My Name Is</div>
          <div class="text-two">NIMBUS2000</div>
          <div class="text-three">I can be your <span class="typing"></span></div>
          <div class="text-four">but a little less than Jarvis</div>
  </div>
  <div class="button2">
      <button>Use me</button>
      </div>
  </div>
    </section>
<!--Chat-bot-->
<div class="container">
    <div class="chatbox">
        <div class="chatbox__support">
            <div class="chatbox__header">
                <div class="chatbox__image--header">
                    <img src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png" alt="image">
                </div>
                <div class="chatbox__content--header">
                    <h4 class="chatbox__heading--header">Nimbus2000</h4>
                    <p class="chatbox__description--header">Hii, How can I help you?</p>
                </div>
            </div>
            <div class="chatbox__messages">
                <div></div>
            </div>
            <div class="chatbox__footer">
                <input type="text" placeholder="Write a message...">
                <button class="chatbox__send--footer send__button">Send</button>
            </div>
        </div>
        <div class="chatbox__button">
            <button id="some-btn">Nimbus2000</button>
        </div>
    </div>
</div>
<!--About Me-->
<section class="about" id="about">
    <div class="content">
        <div class="title"><span>About Me</span></div>
        <div class="about-details">
            <div class="left">
                <img src="Nimbus2000.png" alt="Bot-logo">
            </div>
            <div class="right">
                <div class="topic">Need a friend? I am right here!!!</div>
                <p>Just the way harry potter got his support from his nimbus2000, I am right here to provide you
                    guys the support we all deserve. You ever wanna talk about feelings you'll find me right here.
                    I can be your personal diary who will keep encouraging you at every point of life. And just how bestfriend works
                    I can ever recommend you amazing movies ,series ,songs or even games. For your every problem I can be your solution.
                </p>
            </div>
        </div>
    </div>
    </section>

<!--About Us-->
    <section class="services" id="services">
        <div class="content">
            <div class="title"><span>About the Team</span></div>
            <div class="boxes">
                <div class="box">
                    <div class="icon">
                        <i class="fas fa-paint-brush"></i>
                    </div>
                    <div class="topic">Ritvik Rana</div>
                    <p>Hey!! I am Btech cse Student from Amity University. My hobbies are singing , coding and reading books</p>
                </div>
                <div class="box">
                    <div class="icon">
                        <i class="fas fa-desktop"></i>
                    </div>
                    <div class="topic">Ayush Verma</div>
                    <p>Hey!! I am Btech cse Student from Amity University. My hobbies are gaming , reading books and trading into stocks and crypto</p>
                </div>
                <div class="box">
                    <div class="icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="topic">Shreya Singh</div>
                    <p>Hey!! I am Btech ece Student from Jaypee University. My hobbies are Bhangra , Singing and Coding</p>
                </div>
            </div>
        </div>
        </section>

<!--Contact Me Section Start-->
    <section class="contact" id="contact">
    <div class="content">
        <div class="title"><span>Get In Touch</span></div>
        <div class="text">
            <div class="topic">Wanna join the crew?</div>
            <p>We can always appreciate a little contribution from you guys too.
                Together we all can fight back these mental problems.
                Here's a link to join our Discord channel. Where you can talk to other members of our team. 
            </p>
                <div class="button">
                    <button><a href="https://discord.gg/Xs6jXbcb">Join Us now</a></button>
                </div>
        </div>
    </div>
    </section>

<!--Footer Section Start-->
    <footer>
    <div class="text">
        <span>Created By <a href="#">Team Gryffindor</a> | &#169; 2022 All Rights Reserved.</span>
    </div>
    </footer>


<script>
//Typing animation script
var typed = new Typed(".typing",{
    strings: ["Friend","Teacher","Helper","Go-to bot"],
    typeSpeed: 100,
    backSpeed: 60,
    loop:true,
});
let nav = document.querySelector("nav");
let scrollBtn = document.querySelector(".scroll-button a");

let val;

window.onscroll = function(){
    if(document.documentElement.scrollTop > 20){
        nav.classList.add("sticky");
        scrollBtn.style.display = "block";
    }else{
        nav.classList.remove("sticky");
        scrollBtn.style.display = "none";
    }
}

// Side Navigation Menu Js
let body = document.querySelector("body");
let navBar = document.querySelector(".navbar");
let menuBtn = document.querySelector(".menu-btn");
let cancelBtn = document.querySelector(".cancel-btn");

menuBtn.onclick = function(){
    navBar.classList.add("active");
    menuBtn.style.opacity ="0";
    menuBtn.style.pointerEvents = "none";
    body.style.overflowX = "hidden";
    scrollBtn.style.pointerEvents = "none";
}
cancelBtn.onclick = function(){
    navBar.classList.remove("active");
    menuBtn.style.opacity ="1";
    menuBtn.style.pointerEvents = "auto";
    body.style.overflowX = "auto";
    scrollBtn.style.pointerEvents = "auto";
}
// Side Navifation Bar close while we click on navigation links

let navLinks = document.querySelectorAll(".menu li a");
for(var i = 0; i< navLinks.length; i++){
    navLinks[i].addEventListener("click", function(){
        navBar.classList.remove("active");
        menuBtn.style.opacity = "1";
        menuBtn.style.pointerEvents ="auto";
    });
}

//ChatBox

class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            openButton: document.querySelector('.button2'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
            document.querySelector(".chatbox__button #some-btn").classList.add('remove-btn')
        } else {
            chatbox.classList.remove('chatbox--active')
            document.querySelector(".chatbox__button #some-btn").classList.remove('remove-btn')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();
</script>

</body>
</html>
"""
