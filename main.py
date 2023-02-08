##################### Extra Hard Starting Project ######################
import random

import pandas
# 1. Update the birthdays.csv
bday_df = pandas.read_csv("birthdays.csv")
bday_dict = bday_df.to_dict("records")
DOBS = []

for item in bday_dict:
    name = item["name"]
    year = item["year"]
    month = item["month"]
    day = item["day"]
    DOBS.append((year,month,day))

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt

bday_index = 0

def find_bday():
    global bday_index
    now = dt.datetime.now()
    current_day = (now.year,now.month,now.day)
    for index,date in enumerate(DOBS):
        if date == current_day:
            bday_index = index +1

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if bday_index != 0:
    rand = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{rand}.csv") as letter_file:
        letter = letter_file.read()



# 4. Send the letter generated in step 3 to that person's email address.




