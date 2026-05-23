#1) Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data entered by user.
import csv 
data = [
    ['Name','Address','mobile','email'],
    ['Lakshya','Madhav nagar','Jaipur','7357278264','bhandarilakshya14@gmail.com'],
    ['Tanvi', "Noran girl's hostel", 'Jaipur','897645326','tanvimathur@gmail.com']
]

with open('Address_book.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)   
    print("Data written")