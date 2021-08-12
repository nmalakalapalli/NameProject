# Python program to convert
# CSV to HTML Table
namelist = open('random_500_names.txt').read().split()
namelist = [x.capitalize() + ",<i class=\"bi bi-play-circle\" style=\"font-size:2rem\" onclick=\"playAudio('./Voices/1/" + x + ".mp3')\"></i>" \
                                                                                  ",<i class=\"bi bi-play-circle\" style=\"font-size:2rem\"  onclick= \"playAudio('./Voices/2/" + x + ".mp3')\"></i>" \
                                                                                  ",<i class=\"bi bi-play-circle\" style=\"font-size:2rem\"  onclick= \"playAudio('./Voices/3/" + x + ".mp3')\"></i>" \
                                                                                 ",<i class=\"bi bi-play-circle\" style=\"font-size:2rem\"  onclick= \"playAudio('./Voices/4/" + x + ".mp3')\"></i>" \
                                                                                 ",<i class=\"bi bi-play-circle\" style=\"font-size:2rem\"  onclick= \"playAudio('./Voices/5/" + x + ".mp3')\"></i>" for x in namelist]

with open('namefile.csv', 'w') as f:
    f.write("Name, Speaker 1, Speaker 2, Speaker 3, Speaker 4,Speaker 5 \n")
    for item in namelist:
        f.write("%s\n" % item)


import pandas as pd

# to read csv file
nTable = pd.read_csv("namefile.csv")

# to save as html file
# named as "Table"
nTable.to_html("nameTable.htm", escape=False, index=False, table_id="NameTable")

# assign it to a
# variable (string)
html_file = nTable.to_html(escape=False, index=False, table_id="NameTable")
print(html_file)

homepage = open('index.html', 'rt')
data = homepage.read()
data = data.replace('<!--***-->', html_file)
print(data)
homepage.close()
homepage = open('index.html', 'wt')
homepage.write(data)
homepage.close()