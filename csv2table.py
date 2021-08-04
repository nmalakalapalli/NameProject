# Python program to convert
# CSV to HTML Table


import pandas as pd

# to read csv file
nTable = pd.read_csv("namer.csv")

# to save as html file
# named as "Table"
nTable.to_html("nameTable.htm", escape=False, index=False, table_id="NameTable")

# assign it to a
# variable (string)
#html_file = a.to_html()