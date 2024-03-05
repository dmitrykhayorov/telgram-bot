#
# text_cortex & stable_diffusin + tg_bot
#
import os
import telebot
import psycopg2
from telebot import types
from dotenv import load_dotenv
from cortex import transale_cortex
from prompt_gen import PromptGenerator
from diffusion import generateDiffusion

# получаем API ключи
load_dotenv()
bot_token = os.getenv("TG_TOKEN")
text_cortex_token = os.getenv("TXTC_TOKEN")
stable_diffusion_token = os.getenv("DFSS_TOKEN")

# подключение бота
bot = telebot.TeleBot(bot_token)


# база данных пользователей





# Меню
commands = []
commands.append(types.BotCommand(command='start', description='Start the Bot'))
commands.append(types.BotCommand(
    command='lang', description='Change language'))
commands.append(types.BotCommand(command='random',
                description='Get a random image'))
commands.append(types.BotCommand(command='info', description='Info message'))
commands.append(types.BotCommand(command='help', description='Click for Help'))
commands.append(types.BotCommand(command='generate',
                description='Generate an image on prompt'))
bot.set_my_commands(commands)
# bot.set_chat_menu_button(message.chat.id, types.MenuButtonCommands('commands'))

greeting = "Привет, я помогу тебе сгенерировать картинку по текстовому запросу. Набери /help для вывода доступных команд"
en_message = "Английский язык запросов!\nТеперь набери /generate, посмотрим, что получится :)"
ru_message = "Русский язык запросов!\nТеперь набери /generate, посмотрим, что получится :)"
help_msg = """\
/lang - поменять язык запросов (по-умолчанию русский)
/generate - введи запрос и получи картинку
/info - информация по проекту
/random - картинка по случайному запросу
/help - вывести это сообщение
"""
info_msg = """\
Групповой прокт интенсива по питону для цифровой кафедры МГИМО в Школе 21
Команда:
    Perrierh
    Merlenes
    Barsenaf
Бот написан на python
Для перевода запросов на английский язык используется API text-cortex
Для генеарации изображения испольуется API Stable Diffusion
"""

# Кнопки выбора языка
button_ru = types.InlineKeyboardButton('Русский', callback_data='ru')
button_en = types.InlineKeyboardButton('Английский', callback_data='en')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button_ru)
keyboard.add(button_en)

translate = True

# Логика команд


@bot.message_handler(commands=["start"])
def greet_new_member(message):
    bot.send_message(message.chat.id, greeting)


@bot.message_handler(commands=["help"])
def show_help(message):
    bot.send_message(
        message.chat.id, help_msg)


@bot.message_handler(commands=["lang"])
def show_lang_selector(message):
    bot.send_message(
        message.chat.id, text='Выбери язык запросов', reply_markup=keyboard)


@bot.message_handler(commands=["info"])
def greet_new_member(message):
    bot.send_message(message.chat.id, info_msg)


@bot.message_handler(commands=["generate"])
def take_prompt(message):
    bot.register_next_step_handler(bot.send_message(
        message.chat.id, "Введи запрос :)"), process_prompt)


def process_prompt(message):
    text = message.text
    if translate:
        text = transale_cortex(text, 'ru', 'en', text_cortex_token)

    bot.send_message(message.chat.id, "Работаем...")
    image_path = generateDiffusion(text, stable_diffusion_token)
    # print(image_path)
    with open(image_path, 'rb') as ph:
        bot.send_photo(message.chat.id, ph, caption=text)


@bot.message_handler(commands=["random"])
def gen_radnom(message):
    bot.send_message(message.chat.id, "Генерирую случайный запрос...")
    prompt_model = PromptGenerator()
    text = prompt_model.generate_single_prompt()
    image_path = generateDiffusion(text, stable_diffusion_token)
    with open(image_path, 'rb') as ph:
        bot.send_photo(message.chat.id, ph, caption=text)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'en':
        bot.send_message(call.message.chat.id, "Английский язык запросов!")
        translate = False
    elif call.data == 'ru':
        bot.send_message(call.message.chat.id, "Русский язык запросов!")
        translate = True

bot.polling(non_stop=True)
