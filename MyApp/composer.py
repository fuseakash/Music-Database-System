#!C:\Users\Akash phuse\PycharmProjects\pythonProject\venv\Scripts\python.exe
import cgi, cgitb 
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage() 
 

userid = form.getvalue('name')
print("Content-type:text/html\r\n\r\n")
print("<html>")







print('''
<html>
<body>

<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
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
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}







header{
      margin: 10px 10px 10px 10px;
      padding: 5px 5px 215px;
}
header {
  background-color: green;

     width:100%;
     background-image:url("img/headphone.jpg");
}

h1{
  position: relative;
  left: 9px;
  top: 175px;
  text-transform: uppercase;
   color:#DEB887
}
body{
      background-color: #ffffff;
      padding: 5px;
      margin: 5px;
}

body {
  background-image: url('img/background.jpg');
	background-repeat: no-repeat;
	background-attachment: fixed;
 background-size: 100% 100%;
}
nav{
      text-align: center;
}
nav>a{
      display: inline-block;
      font-size: 125%;
      color: #000000;
      background-color: #ffffff;
      width: 200px;
      text-align: center;
      padding: 5px;
      text-decoration: none;
      border-radius: 5px;
      margin: 10px;
      margin-top: 10px;
      opacity: 0.65;
}

nav>a:hover{
      color: #000FFF;
      opacity: 1;
}
nav>a:focus{
      color: #FFFFFF;
}

.active{
    background-color: #FFFFFF;
    color:  #001FFF ;
    opacity: 1;
}
table{
      display: inline-table;
      font-size: 140%;
      font-family: Arial, georgia, times;
      color: #000000;
      width: 85%;
      line-height: 80px;
      text-align: center;
      margin: 260px;
      margin-top: 100px;
      border: 2px;
      border-bottom: 25px;
      border-spacing: 4px;
      opacity: 0.8;
}
table th{
      color: #FFFAF0;
       text-align: center;
      width: 130px;
      height: 20px;
      background-color: #800080;
      border: 3px #00FF7F;

      border-bottom: solid #000000;
      border-radius: 5px 5px 0 0;
}
table tr>td{
    opacity: 0.8;
    text-align: center;
    padding: 0.5%;
    font-weight: bold;
    font-size: 100%;
    color: #8B0000;
    background-color: #EE82EE;
    border-radius: 5px;
    text-shadow: 0 0 3px #FFA000;
}
table tr >:first-child{
    text-align: center;
}
table tr:hover td{
    opacity: 1;
}
img{
      display: block;
      margin-bottom: 15px;
      height: 150px;
      width: 200px;
      border: solid 2px #000000;
}
.left{
	background: #767613;
	margin: 0px 5px 5px 5px;
	padding: 7px;
	float: left;
}

.right {
	display: inline-block;
	width: 80%	;
	float: left;
}
.searchbar .sb-search { margin: 5px 5px; }
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
</head>
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
<header>
<h1> Composer</h1>
	</header>

<p>
</p>
<div class="search-container">
    <form action="searchcomposer.py">
      <input type="text" placeholder="Enter the Composer name." name="sname">
      <button type="submit">Search</button>
      <input type="hidden" name="name" value='''+str(userid)+'''></form>
  </div>
</div>


	<main>
		<div class="searchbar" style="position: absolute;">

		<div id="sb-search" class="sb-search">
		
		<section class = "right">
	<table>
		<tr>
			<th>Sr No</th>
			
			<th>Composer Name</th>
		</tr>
		<tr>
			<td>1</td>
			
			<td>Ajay-Atul</td>
		</tr>
		<tr>
			<td>2</td>
			
			<td>Mithoon</td>
		</tr>
		<tr>
			<td>3</td>
			
			<td>Mithoon</td>
		</tr>
		<tr>
			<td>4</td>
			
			<td>Avinash</td>
		</tr>
		<tr>
			<td>5</td>
			
			<td>Pritam</td>
		</tr>
		<tr>
			<td>6</td>
			
			<td>Ismail Darbar</td>
		</tr>
		
			</table>



		</section>
	</main>

</body>
</html>
''')