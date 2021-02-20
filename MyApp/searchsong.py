#!C:\Users\Akash phuse\PycharmProjects\pythonProject\venv\Scripts\python.exe
import cgi, cgitb 
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage() 


if form.getvalue('search'):
   song = form.getvalue('search')
else:
   song = "Please Select song"

song="'"+song+"'"
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print('''<head>

   
<style>
p{
font-size:30px;}
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
}

body{
    font-family: 'Raleway', sans-serif;
    background: #000;
}

.background{
    background: url(img/gu.jpg) no-repeat center center fixed;
    background-size: cover;
    height:100vh;


    
  
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
</head>
<body>


<main>
<div class="background">
<center>


<center><img src="img/music.jpg" style="width:300px;height:300px;"></center>
<form  action="playsong.py" method='POST'>


<p style="font-size:add_size"> <b>Song Name :''' +song+'''</b>  </p>

<input type="hidden" name="name" value='''+song+'''>




<button class="button" type="submit"><strong>Play</strong></button>


<br>
<br>

</form>
<a href = "songs.py"><center><button class="button1"><strong>Back</strong></button></center></a>

</p>

</center>
</div>
</main>

    

</body>

''')
print("</body>")
print("</html>")