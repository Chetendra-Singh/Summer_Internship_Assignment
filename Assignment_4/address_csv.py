# create csv file for address book have columns for
# name,address,mobile,email and insert  some data in it.

import csv


# data insert
data=[["Name","Address","Email","Mob_no"],
      ["Chetan","Jaipur","cs27102004@gmail.com","8118824525"],
      ["Arjun Mehta", "Kota", "arjun.mehta@email.com", "9012345678"],
      ["Neji", "Delhi", "neji@gmail.com", "9876543210"],
      ["Ananya Verma", "Ahmedabad", "ananya.verma@email.com", "9090909090"]]

# write mode, insert all data in Data.csv file
with open("Data.csv","w",newline="",encoding="utf8") as file:
    writer=csv.writer(file)
    for row in data:
        writer.writerow(row)

# read mode, fetch all data in read mode
with open("Data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)