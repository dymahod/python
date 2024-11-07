import telebot
import schedule
import time
from datetime import datetime, timedelta, date

bot = telebot.TeleBot("6452366881:AAGF6vZJft0ec3MSpnYw2IzjajpGoEbzhgE")

# функция для отправки картинки


def send_image():
    chat_id = "-1001948926802"
    list = [
        "monday.jpg",
        "tuesday.jpg",
        "wednesday.jpg",
        "thursday.jpg",
        "friday.jpg",
        "saturday.jpg",
        "sunday.jpg",
    ]
    if int(datetime.weekday(date.today())) == 0:
        img = open("monday.jpg", "rb")
    if int(datetime.weekday(date.today())) == 1:
        img = open("tuesday.jpg", "rb")
    if int(datetime.weekday(date.today())) == 2:
        img = open("wednesday.jpg", "rb")
    if int(datetime.weekday(date.today())) == 3:
        img = open("thursday.jpg", "rb")
    if int(datetime.weekday(date.today())) == 4:
        img = open("friday.jpg", "rb")
    if int(datetime.weekday(date.today())) == 5:
        img = open("saturday.jpg", "rb")
    if int(datetime.weekday(date.today())) == 6:
        img = open("sunday.jpg", "rb")
    bot.send_photo(chat_id, img)


# задаем расписание отправки картинки
schedule.every().day.at("10:00").do(send_image)

# запускаем бесконечный цикл для проверки расписания
while True:
    schedule.run_pending()
    time.sleep(1)
