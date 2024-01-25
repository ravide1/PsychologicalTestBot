import json
import os

from telebot.types import ReplyKeyboardRemove
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message
from info import question_list, recomendation_list, get_recomendation_list

import telebot
from telebot import types

TOKEN = "6908626260:AAHQzwDUk_HQCAP9qUoRCx0Nv1RBg2WjiA8"
bot = telebot.TeleBot(TOKEN)

current_question_number = 0
points = 0
users_dictionary = {

}

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('Начать анкетирование'))

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Привет, меня зовут {bot.get_my_name().name}."
                                      f"\nСегодня мы с вами узнаем вероятность того, что вы совершите преступление."
                                      f"\nЕсли хотите узнать дополнительную информацию о боте, нажмите \"/help\""
                                        "\nЧтобы начать тестирование, нажмите \"Начать\"", reply_markup=markup)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Тест состоит из 12 вопросов, на категории они не разделяются, но бы каждый вопрос дается определенное количесво баллов в зависимости от его харрактера.")


@bot.message_handler(content_types=['text'])
def handle_question(message: Message):
    global points
    global current_question_number

    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    yes_button = types.KeyboardButton("Да")
    no_button = types.KeyboardButton("Нет")
    markup.add(yes_button, no_button)

    if message.text.upper() == "НАЧАТЬ АНКЕТИРОВАНИЕ":
        users_dictionary[chat_id] = {"points": 0, "current_question_number": 0}
        #points = 0
        #current_question_number = 0
        bot.send_message(chat_id, question_list[0]["question"], reply_markup=markup)

    elif message.text.upper() == "ДА" or message.text.upper() == "НЕТ":

        if message.text.upper() == question_list[current_question_number]["answer_add_points"]:
            users_dictionary[chat_id]["points"] += question_list[users_dictionary[chat_id]["current_question_number"]]["points"]
            points += question_list[current_question_number]["points"]
        current_question_number += 1

        if current_question_number >= len(question_list):
            bot.send_message(chat_id, "Тест пройден!", reply_markup=ReplyKeyboardRemove())
            bot.send_message(chat_id, f"Шанс, что вы совершите преступление {points}%")
            bot.send_message(chat_id, get_recomendation_list(points))

        else:
            bot.send_message(chat_id, question_list[current_question_number]["question"], reply_markup=markup)
    else:
        bot.send_message(chat_id, "Неверный ввод, нажмите кнопку да или нет.", reply_markup=markup)


bot.polling()