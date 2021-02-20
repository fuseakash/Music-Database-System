#!C:\Users\Akash phuse\PycharmProjects\pythonProject\venv\Scripts\python.exe
import cgi, cgitb ,time
cgitb.enable()
form = cgi.FieldStorage() 
songname = form.getvalue('name')
import playsound

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print('''
<h1>'''+
    playsound.playsound("C:/xampp/htdocs/MyApp/audio/"+str(songname)+".mp3", True)
      +'''</h1>
   
''')

print("</body>")
print("</html>")

