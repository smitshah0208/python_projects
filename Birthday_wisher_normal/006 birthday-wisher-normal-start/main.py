import smtplib
import datetime as dt
import pandas as pd
import random


# From
my_email = "test.python.rdx@gmail.com"
password = "mjofrwrcynuspsgu"


today = (dt.datetime.today().month, dt.datetime.today().day)
data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']) : data_row for index, data_row in data.iterrows()}

if today in birthdays_dict:
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[today]['email'],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )
else:
    print("No matches for today")




