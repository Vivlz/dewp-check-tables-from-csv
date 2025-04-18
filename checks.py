import csv
import glob
import os

# Variables for MediaWiki table construction
header = """{| class="wikitable sortable"
|-
! Dialogue Text !! Coversant !! Area !! Difficulty !! Modifiers !! conv_id !! line_id
|- \n"""
end = "|} \n\n"
body = ""

# If anyone else is using this, make sure to change this to your local path
folder_path = '/home/viv/Documents/DEWP Skill Tables/dewp-check-tables-from-csv/csvs'

# Get a list of all .csv files in the folder
csv_files = glob.glob(f"{folder_path}/*.csv")


# Loop through each CSV file and read it
for file in csv_files:
    filename = os.path.basename(file)
    table = ""
    table += filename + "\n"
    table += header   
    with open(file, newline='', encoding='utf-8') as f:
        csv_table = csv.reader(f)

    # Skips first csv table row, since that's just the table head, already implementeted by var header
        iter = 0
        for row in csv_table:

            if iter == 0:
                iter += 1
                continue

            print(row)

            body = ("|" + str(row[4]) + "||"
                    + str(row[3]) + "||"
                    + str(row[2]) + "||"
                    + str(row[6]) + "||"
                    + str(row[7]) + "||"
                    + str(row[0]) + "||"
                    + str(row[1]))
            
            body = body.replace('\n','<p>')

            body += "\n" + "|-" 
                
            table += body
            table += "\n"

            print(table)

        table += end   
        with open("output.txt", "a") as f:
            print(table, file=f)

