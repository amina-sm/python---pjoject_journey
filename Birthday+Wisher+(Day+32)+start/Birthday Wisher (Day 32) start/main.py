import smtplib
import datetime as dt
import random


MY_EMAIL = "PUT YOUR EMAIL HERE"

PASSWORD = "PUT YOUR PASSWORD HERE"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("Birthday Wisher (Day 32) start\quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}")
