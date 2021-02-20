#!C:\Users\Akash phuse\PycharmProjects\pythonProject\venv\Scripts\python.exe
import cgi, cgitb 
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage() 
 
#get the values
email = form.getvalue('username')
username  = form.getvalue('username')
password  = form.getvalue('psw')
password1  = form.getvalue('psw-repeat')

print("Content-type:text/html\r\n\r\n")
print("<html>")

#check the repeat password is same or not
if (password!=password1):
    print("<body>")
    print("<h1>Password NOT match</h1>")
    print("<a href='http://localhost//myapp/signup.html'>Try Again !</a>")
    print("</body>")
    print("</html>")
else:
   
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="music database")
    mycursor = mydb.cursor()
    mycursor.execute("select * from user where user_name='"+username+"'")
    result=mycursor.fetchall()
    
    #check username is already present or not
    if len(result)!=0:
        print("<body>")
        print("<h1>Account Exist with Username</h1>")
        print("<a href='http://localhost//myapp/signup.html'>Try Again !</a>")
        print("</body>")
        print("</html>")
    
    else:
        mycursor.execute("SELECT MAX(user_id) FROM user")
        result=mycursor.fetchall()
        #mycursor.execute("INSERT INTO info('"+username+"','"+password+"','"+email+"')")
        mycursor.execute("INSERT INTO user (user_id,user_name, password, user_email) VALUES ("+str(result[0][0]+1)+",'"+username + "', '" + password + "', '" + email + "')")
        mydb.commit()
        userid=result[0][0]+1
        print('''
        <head>
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>DBE PROJECT</title>
<link rel="stylesheet" href="homepage.css">
	 <script >
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 4000); // Change image every 2 seconds
}

</script>

 </head>

	 <style>
	 .mySlides {display:none;}
	 h1{
	 	color: #8B0000;
	 	font-size: 80px;
		font-style: bold;
	 	text-transform: uppercase;
	 	text-align: center;
		 background-color: #FFFAF0;
		 border: 5px solid #87C;
	 }
	 body {
	   margin: 0;
	   font-family: Arial, Helvetica, sans-serif;
	 }

	 .topnav {
	   overflow: hidden;
	   background-color: #800080;
	 }

	 .topnav a {
	   float: left;
	   color: #f2f2f2;
	   text-align: center;
	   padding: 14px 16px;
	   text-decoration: none;
	   font-size: 17px;
	 }

	 .topnav a:hover {
	   background-color: #ddd;
	   color: blue;
	 }

	 .topnav a.active {
	   background-color: #4CAF50;
	   color: white;
	 }
	body {
  		background-image: url('img/BGWEL.png');
		background-repeat: no-repeat;
		background-attachment: fixed;
 		background-size: 100% 100%;
	}
	img{
		opacity: 0.9;
		border: 5px solid #FAF;
	}

	marquee{
		margin-top: 20px;
	}
	h3{
		font-size: 50px;
		 text-decoration: underline;
		text-shadow: 2px 2px 5px red;
		margin: 70px 455px;
		width: 70%;
	}

	p{
		font-size: 40px;
		font-style: bold;
		color:#4B0082;
		font-family: "Sans-serif";
		text-align: center;
		text-shadow: 2px 2px 5px red;
		margin: 20px 190px;
		width: 70%;
 	}
    .button {
  background-color:  #4CAF50;
  border: none;
  color: white;
  padding: 16px 76px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  transition-duration: 0.4s;
  cursor: pointer;
}


.Lbut:hover { 
 background-color: #ddd;
  color: black;
}
div#frm *{display:inline} 

	 </style>
	 <body>
		 <div id="frm">
  <form action="home.py"><button type="submit"  class = "button Lbut"><strong>Home</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>
 
  <form action="songs.py"><button type="submit" class = "button Lbut " ><strong>Songs</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>
  
  <form action="albums.py"><button type="submit" class = "button Lbut"><strong>Albums</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>
  
  <form action="myplaylist.py"><button type="submit" class = "button Lbut"><strong>Myplaylist</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>

  <form action="singer.py"><button type="submit"class = "button Lbut"><strong>Singer</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>
  
  <form action="composer.py"><button type="submit" class = "button Lbut"><strong>Composer</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>

  <form action="startpage.html"><button type="submit" class = "button Lbut"><strong>Log_Out</strong></button></form>
</div>

	 <div class="w3-container">
		 <marquee width="140%" direction="left" height="120px" scrollamount="18">
	   <h1>Welcome to OUR MUSIC WEB application</h1>
		 </marquee>

	 <div class="w3-content w3-section" style="max-width:550px">
	   <img class="mySlides w3-animate-left" src="img/alb.jpg" style="width:100%">
	   <img class="mySlides w3-animate-left" src="img/tar.jpg" style="width:100%">
	   <img class="mySlides w3-animate-left" src="img/musc.jpg" style="width:100%">
	   <img class="mySlides w3-animate-left" src="img/music_2-wide.jpg" style="width:100%">
		 <img class="mySlides w3-animate-left" src="img/121725.jpg" style="width:100%">
		 <img class="mySlides w3-animate-left" src="img/121717.jpg" style="width:100%">
		 <img class="mySlides w3-animate-left" src="img/unplash.jpg" style="width:100%">
		 <img class="mySlides w3-animate-left" src="img/album.jpg" style="width:100%">
	 </div>


	 <h3>     Group Members:<br></h3>
	 <p>
	 Akash Fuse<br><br>
	 Gurunatharudh Bhandarkavathe<br><br>
	 Sanjana Doshi<br><br>
	 Pravin Konasirasgi<br><br>
	 Tukaram Pawar<br><br>
 </p>
	 <script>
	 var myIndex = 0;
	 carousel();

	 function carousel() {
	   var i;
	   var x = document.getElementsByClassName("mySlides");
	   for (i = 0; i < x.length; i++) {
	     x[i].style.display = "none";
	   }
	   myIndex++;
	   if (myIndex > x.length) {myIndex = 1}
	   x[myIndex-1].style.display = "block";
	   setTimeout(carousel, 2000);
	 }
	 </script>

</body>
</html>
        ''')
        
