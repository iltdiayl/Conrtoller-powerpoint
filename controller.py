import telebot
from telebot import types
import pyautogui 

bot = telebot.TeleBot("token") # your telegram bot token
@bot.message_handler(commands=['start'])
def send_welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Back")
    btn2 = types.KeyboardButton("Next")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Можно начинать", reply_markup=markup)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Back")
    btn2 = types.KeyboardButton("Next")
    markup.add(btn1, btn2)

    if message.text == "Back":
        pyautogui.press("Backspace")
    if message.text == "Next":
        pyautogui.press("Enter")
bot.infinity_polling()
