import csv
import os

# Variables for MediaWiki table construction
header = """{| class="wikitable sortable"
|-
! Task !! Gained from !! Description !! Essential to plot progression 
|- \n"""
end = "|} \n\n"
body = ""


# Get a list of all .csv files in the folder
csv_file = open('/home/viv/Documents/DEWP Skill Tables/dewp-check-tables-from-csv/Tasks.csv')

table = ""
csv_file = csv.reader(csv_file)
table += header   

    # Skips first csv table row, since that's just the table head, already implementeted by var header
iter = 0
for row in csv_file:

    if iter == 0:
        iter += 1
        continue

    body = ("|" + "[[" + str(row[0]) + "]]" + "||"
            + str(row[1]) + "||"
            + str(row[2]) + "||"
            + str(row[3]))
    
    body = body.replace('\n','<p>')

    body += "\n" + "|-" 
        
    table += body
    table += "\n"

    print(table)

table += end   
with open("output.txt", "w") as f:
    print(table, file=f)