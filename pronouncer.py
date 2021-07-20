from playsound import playsound
import cgi, cgitb

#declares the input name as a variable
form = cgi.fieldstorage()
name = str(form.getvalue("name"))

#uses input name to  navigate to corresponding filepath
namefile = name + "-1.mp3"
#CHECK: print(namefile)
audiopath = "D:/NamePronouncer/recordings/"+namefile
#CHECK: print(audiopath)

#plays audio file corresponding to input name
playsound(audiopath)
