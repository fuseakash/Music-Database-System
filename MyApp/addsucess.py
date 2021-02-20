#!C:\Users\Akash phuse\PycharmProjects\pythonProject\venv\Scripts\python.exe
import cgi, cgitb 
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage() 


if form.getvalue('name'):
   userid = form.getvalue('name')
else:
   userid = "User not found!"

if form.getvalue('sname'):
   name = form.getvalue('sname')
else:
   name = "User not found!"
   
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="music database")
mycursor = mydb.cursor()
mycursor.execute("select song_name from playlist where user_id=" + str(userid))
result1 = mycursor.fetchall()
result1 = result1[0][0][1:-1].split(",")

mycursor.execute("select number from song where song_title='" + name + "'")
result2 = mycursor.fetchall()
result2 = result2[0][0]
if str(result2) in result1:
    pass
else:
    flag = True
    result1.append(str(result2))
    result1 = ",".join(result1)
    result1='"'+result1+'"'
    mycursor.execute("UPDATE playlist SET song_name ='" + result1 + "' WHERE user_id=" + str(userid))
    mydb.commit()
print("Content-type:text/html\r\n\r\n")
print("<html>")
print('''
<head>
<style>


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
.pu{
margin-top:300px;
margin-left:350px;
font-size:35px;
}
.but{
margin-left:400px;
width:60px;
height:35px;
font-size:25px;

background:linear-gradient(-45deg,blue,red);
}
.background{
    background: url(img/gu.jpg) no-repeat center center fixed;
    background-size: cover;
    height:100vh;
    display:flex;
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


<div class="background">
<center>
<center><p class="pu"><b> Song is Added to your playlist</b></p></center>
<br>
       <form action="myplaylist.py"><button type="submit"><strong>Back</strong></button>
  <input type="hidden" name="name" value='''+str(userid)+'''></form>
</center>
</div>
</center>
</body>
''')


print("</html>")