#!C:\Users\Akash phuse\PycharmProjects\pythonProject\venv\Scripts\python.exe
import cgi, cgitb 
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage() 


if form.getvalue('sname'):
   name = form.getvalue('sname')
else:
   name = "Please Select song"
   
if form.getvalue('name'):
   userid = form.getvalue('name')
else:
   userid = "Please Select song"

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="music database")
mycursor = mydb.cursor()
mycursor.execute("select singer_id from singer where singer_name='" + name+"'")
result1 = mycursor.fetchall()
result1=result1[0][0]

mycursor.execute("select song_title from song where singer_id=" + str(result1))
result2 = mycursor.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print('''<html>
<body>
  <head>
  	<meta name="viewport" content="width=device-width, initial-scale=1">

  	<title>Singer1</title>

  	<link rel="stylesheet" href="searchalbumsingercomposer.css">

   </head>
<style>
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 110px;
}

body {
  background-image: url('img/gu.jpg');
	background-repeat: no-repeat;
	background-attachment: fixed;
 background-size: 100% 100%;
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
.zoom {
  padding: 50px;
  background-image: url('img/Singer.jpg');
  text-align: center;
  transition: transform .2s;
  width: 333px;
  height: 330px;
  margin: 90px 500px;
}

.zoom:hover {
  transform: scale(1.5);
}
h2{
  font-size: 50px;
  	font-family: "Sans-serif";
  text-shadow: 2px 2px 5px red;
  margin: 70px 240px;
  width: 70%;
  text-align: center;
}
li{
  font-size: 30px;
  color: #191970;
  font-family: "Sans-serif";
  text-shadow: 2px 2px 5px #C71585;
  margin: 70px 590px;
  	text-align: center;
}
button{
  margin: 15px 585px;
  width: 140px;
  padding: 20px;
  font-family: "Sans-serif";
  font-size: 25px;
  color: #000FFF;
  opacity: .5;
  border-radius: 5px;
}
button:hover{
      color: #000FFF;
      opacity: 1;
}

</style>
<p>
</p>

<div class="zoom"></div>
<h2><u>Singer Name</u></h2>

<ul>
  <li>'''+name+'''</li>

</ul>

<h2><u>Song List</u></h2>

<ul>''')
for i in result2:
    print('''<li>'''+i[0]+'''</li>''')
print('''
</ul>



 <form action="singer.py"><button type="submit"><strong>Back</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>
</div>
</body>
''')
print("</html>")