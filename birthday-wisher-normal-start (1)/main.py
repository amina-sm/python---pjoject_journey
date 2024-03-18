from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "emmystivin24@gmail.com"
MY_PASSWORD = "bovoekajrocfabze"

try:
    # 2. Check if today matches a birthday in the birthdays.csv
    today = datetime.now()
    today_tuple = (today.month, today.day)

    # HINT 2: Use pandas to read the birthdays.csv
    data = pandas.read_csv("birthdays.csv")

    # HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (
        index, data_row) in data.iterrows()}

    # HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            print(file_path)
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                MY_EMAIL, birthday_person["email"], f"Subject: Happy Birthday! \n\n {contents}")
            print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
