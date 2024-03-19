

# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": STOCK_API_KEY,
#     # "datatype": "json"
# }
# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# data = response.json()["Time Series (Daily)"]
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)


# # # TODO 2. - Get the day before yesterday's closing stock price
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# # # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference = float(yesterday_closing_price) - \
#     float(day_before_yesterday_closing_price)
# up_down = None
# if difference > 0:
#     up_down = "🔺"
# else:
#     up_down = "🔻"

# # # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)


# # # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# # if diff_percent > 0.1:
# #     print("Get News")

# # STEP 2: https://newsapi.org/
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


# # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# if abs(diff_percent) > 0.1:
#     news_params = {
#         "apiKey": NEWS_API_KEY,
#         "qInTitle": COMPANY_NAME
#     }
#     news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#     articles = news_response.json()["articles"]
# # print(articles)
# # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
# three_articles = articles[:3]
# print(three_articles)

# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# # to send a separate message with each article's title and description to your phone number.

# # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
# formatted_articles = [
#     f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
# # TODO 9. - Send each article as a separate message via Twilio.
# for article in formatted_articles:
#     message = client.messages.create(
#         body=article,
#         from_="+17042070815",
#         to="+255626361250"
#     )


# # Optional TODO: Format the message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "WWMERIJDDKTD13HK"
NEWS_API_KEY = "6f94e621a2524fcc80bb75f850beb5f6"
TWILIO_ACCOUNT_SID = "ACf0e4e2e9d8f7f7f7f7f7f7f7f7f7f7f7"
TWILIO_AUTH_TOKEN = "f0e4e2e9d8f7f7f7f7f7f7f7f7f7f7f7"
TWILIO_PHONE_NUMBER = "PUT TWILIO NUMBER HERE"


# STEP 1: Get yesterday's closing stock price and the day before yesterday's closing stock price.

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Calculate the percentage difference
difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


# STEP 2: Get news articles related to the COMPANY_NAME if the percentage difference is significant.

if abs(diff_percent) > 0.1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # Print the first 3 articles
    three_articles = articles[:3]
    print(three_articles)

# STEP 3: Send news articles via Twilio.
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if abs(diff_percent) > 0.1:
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles
    ]

    # Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to="PUT RECIPIENT NUMBER HERE"  # your phone number here
        )
