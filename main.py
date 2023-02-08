import random

import pandas
bday_df = pandas.read_csv("birthdays.csv")
bday_dict = bday_df.to_dict("records")
DOBS = []

for item in bday_dict:
    name = item["name"]
    year = item["year"]
    month = item["month"]
    day = item["day"]
    DOBS.append((year,month,day))

import datetime as dt

bday_index = 0

def find_bday():
    global bday_index
    now = dt.datetime.now()
    current_day = (now.year,now.month,now.day)
    for index,date in enumerate(DOBS):
        if date == current_day:
            bday_index = index

find_bday()

import smtplib
def send_email(letter,email):
    USER = "busjackson37@gmail.com"
    PASS = "yqhpkksgkiwllbob"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER,password=PASS)
        connection.sendmail(from_addr=USER,to_addrs=email,msg=f"Subject: Happy Birthday!! \n\n{letter}")

if bday_index != 0:
    name = bday_dict[bday_index]["name"]
    email = bday_dict[bday_index]["email"]
    rand = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{rand}.txt") as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace("[NAME]",name)
        send_email(new_letter,email)