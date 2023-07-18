#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sqlite3
import random
from datetime import  datetime
def main():
    while True:
        if True:
            global perexod
            perexod = " "
            bot = telebot.TeleBot('6361686380:AAHHukhByQQr-1sHj1rIWX_eodfmkkVJM5M')
            @bot.message_handler(commands=["start", "admin"])
            def start(message, res=False):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("luxu.db")
                c  = db.cursor()
                if message.text == "/start":
                    c.execute("""SELECT * FROM users WHERE idtg= ?""", [idtg])
                    if c.fetchone() == None:
                        c.execute(f"INSERT INTO users VALUES (?,?,?,?,?)",(idtg, 0, "Bronse", 0, 0))
                        db.commit()
                    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="🙎🏼‍♂ Профиль")
                    btn2 = types.KeyboardButton(text="💲 Пополнить баланс")
                    btn3 = types.KeyboardButton(text="📤 Вывести")
                    markup.add(btn1, btn2, btn3)
                    btn4 = types.KeyboardButton(text="📦 Другие товары")
                    markup.add(btn4)
                    btn5 = types.KeyboardButton(text="ℹ️ Информация")
                    btn6 = types.KeyboardButton(text="🛠 Поддержка")
                    btn7 = types.KeyboardButton(text="🔢 Калькулятор")
                    markup.add(btn5, btn6, btn7)
                    bot.send_message(idtg, f'''
🔆 Для продолжения выбери нужную команду на клавиатуре
❓ Если есть дополнительные вопросы по поводу бота, нажмите на кнопку «🛠 Поддержка»
                    ''',  reply_markup=markup, parse_mode='HTML')
            @bot.message_handler(content_types=['text'])
            
            def menu(message):
                db = sqlite3.connect("luxu.db")
                c  = db.cursor()
                idtg = str(message.from_user.id)
                if message.text == "🙎🏼‍♂ Профиль":
                    c.execute("""SELECT * FROM users WHERE idtg= ?""", [idtg])
                    data = c.fetchone()
                    
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Реферальная система", callback_data=f"ref")
                    btn2 = types.InlineKeyboardButton(text="🎁Активировать промокод", callback_data=f"promo")
                    markup.add(btn1, btn2)
                    bot.send_message(idtg, f'''
🆔: {idtg}
💵 Баланс: {data[1]}

💵 Всего пополнено: на {data[4]} ₽
🍯 Всего выведено: {data[3]}G
⭐️ Ваш ранг: {data[2]}
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "💲 Пополнить баланс":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
⭐️ Введите сумму в рублях на которую вы хотите пополнить баланс.
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, deposit)
                elif message.text == "📤 Вывести":
                    c.execute("""SELECT * FROM users WHERE idtg= ?""", [idtg])
                    data = c.fetchone()
                    c.execute("""SELECT course FROM admin""")
                    course = c.fetchone()[0]
                    if data[1] <= course:
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Пополнить баланс", callback_data=f"replenish")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
❗️ Вывод работает от 100 голды. ({course} руб)
                    ''',  reply_markup=markup, parse_mode='HTML')
                    else:
                        pass
                elif message.text == "📦 Другие товары":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
На данный момент товары отсутствуют!
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "ℹ️ Информация":
                    markup = types.InlineKeyboardMarkup(row_width = 3)
                    btn1 = types.InlineKeyboardButton(text="📰Отзывы", url="https://t.me/LuxuGoldi")
                    btn2 = types.InlineKeyboardButton(text="Чат", url="https://t.me/+d_4mkGAlBK81M2Ji")
                    markup.add(btn1, btn2)
                    btn3 = types.InlineKeyboardButton(text="Курс📊", callback_data=f"course")
                    markup.add(btn3)
                    btn4 = types.InlineKeyboardButton(text="Топ дня", callback_data=f"top1")
                    btn5 = types.InlineKeyboardButton(text="Топ недели", callback_data=f"top2")
                    btn6 = types.InlineKeyboardButton(text="Топ месяца", callback_data=f"top3")
                    markup.add(btn4, btn5, btn6)
                    bot.send_message(idtg, f'''
📋 Выберите нужный пункт.
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "🛠 Поддержка":
                    markup = types.InlineKeyboardMarkup(row_width = 3)
                    btn1 = types.InlineKeyboardButton(text="1", callback_data=f"1")
                    btn2 = types.InlineKeyboardButton(text="2", callback_data=f"2")
                    btn3 = types.InlineKeyboardButton(text="3", callback_data=f"3")
                    btn4 = types.InlineKeyboardButton(text="4", callback_data=f"4")
                    btn5 = types.InlineKeyboardButton(text="Связаться", callback_data=f"connect")
                    markup.add(btn1,btn2,btn3,btn4, btn5)
                    bot.send_message(idtg, f'''
1. Почему так долго проверяют чек?
2. Почему так долго выводят золото?
3. Сколько по времени выводят золото?
4. Безопасно ли у вас покупать?

Если вы не смогли найти ответ, нажмите кнопку связаться
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "🔢 Калькулятор":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
Введите количество золота
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, calculator)
                else:
                    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="🙎🏼‍♂ Профиль")
                    btn2 = types.KeyboardButton(text="💲 Пополнить баланс")
                    btn3 = types.KeyboardButton(text="📤 Вывести")
                    markup.add(btn1, btn2, btn3)
                    btn4 = types.KeyboardButton(text="📦 Другие товары")
                    markup.add(btn4)
                    btn5 = types.KeyboardButton(text="ℹ️ Информация")
                    btn6 = types.KeyboardButton(text="🛠 Поддержка")
                    btn7 = types.KeyboardButton(text="🔢 Калькулятор")
                    markup.add(btn5, btn6, btn7)
                    bot.send_message(idtg, f'''
🔆 Для продолжения выбери нужную команду на клавиатуре
❓ Если есть дополнительные вопросы по поводу бота, нажмите на кнопку «🛠 Поддержка»
                    ''',  reply_markup=markup, parse_mode='HTML')
            def deposit(message):
                idtg = str(message.from_user.id)
                if message.text == "Главное меню":
                    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="🙎🏼‍♂ Профиль")
                    btn2 = types.KeyboardButton(text="💲 Пополнить баланс")
                    btn3 = types.KeyboardButton(text="📤 Вывести")
                    markup.add(btn1, btn2, btn3)
                    btn4 = types.KeyboardButton(text="📦 Другие товары")
                    markup.add(btn4)
                    btn5 = types.KeyboardButton(text="ℹ️ Информация")
                    btn6 = types.KeyboardButton(text="🛠 Поддержка")
                    btn7 = types.KeyboardButton(text="🔢 Калькулятор")
                    markup.add(btn5, btn6, btn7)
                    bot.send_message(idtg, f'''
🔆 Для продолжения выбери нужную команду на клавиатуре
❓ Если есть дополнительные вопросы по поводу бота, нажмите на кнопку «🛠 Поддержка»
                    ''',  reply_markup=markup, parse_mode='HTML')
                else:
                    try:
                        db = sqlite3.connect("luxu.db")
                        c  = db.cursor()
                        c.execute("""SELECT course FROM admin""")
                        course = c.fetchone()[0]
                        if int(message.text) <= course:
                            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                            btn1 = types.KeyboardButton(text="Главное меню")
                            markup.add(btn1)
                            bot.send_message(idtg, f'''
⚠️Минимальная сумма для пополения {course} рублей
                            ''',  reply_markup=markup, parse_mode='HTML')
                            bot.register_next_step_handler(message, deposit)
                        elif int(message.text) >= course:
                            summa = int(message.text)
                            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                            btn1 = types.KeyboardButton(text="Главное меню")
                            markup.add(btn1)
                            bot.send_message(idtg, f'''
📩 Отправьте деньги на Сбербанк по реквизитам:
2202206210404690 (карта)

Никита Евгеньевич Ч.
💲 Сумма: {message.text} ₽

📷 Отправьте нам скриншот чека.
                            ''',  reply_markup=markup, parse_mode='HTML')
                            bot.register_next_step_handler(message, Pic, summa)
                    except:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Главное меню")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
❗️ Введите целое число.
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, deposit)
            def calculator(message):
                idtg = str(message.from_user.id)
                if message.text == "Главное меню":
                    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="🙎🏼‍♂ Профиль")
                    btn2 = types.KeyboardButton(text="💲 Пополнить баланс")
                    btn3 = types.KeyboardButton(text="📤 Вывести")
                    markup.add(btn1, btn2, btn3)
                    btn4 = types.KeyboardButton(text="📦 Другие товары")
                    markup.add(btn4)
                    btn5 = types.KeyboardButton(text="ℹ️ Информация")
                    btn6 = types.KeyboardButton(text="🛠 Поддержка")
                    btn7 = types.KeyboardButton(text="🔢 Калькулятор")
                    markup.add(btn5, btn6, btn7)
                    bot.send_message(idtg, f'''
🔆 Для продолжения выбери нужную команду на клавиатуре
❓ Если есть дополнительные вопросы по поводу бота, нажмите на кнопку «🛠 Поддержка»
                    ''',  reply_markup=markup, parse_mode='HTML')
                else:
                    try:
                        db = sqlite3.connect("luxu.db")
                        c  = db.cursor()
                        c.execute("""SELECT course FROM admin""")
                        course = c.fetchone()[0]
                        if int(message.text) >= 0:
                            c.execute("""SELECT course FROM admin""")
                            course = c.fetchone()[0]
                            prise = round(course / 100 * int(message.text))
                            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                            btn1 = types.KeyboardButton(text="Главное меню")
                            markup.add(btn1)
                            bot.send_message(idtg, f'''
                    {message.text}G будет стоить {prise} руб.
                            ''',  reply_markup=markup, parse_mode='HTML')
                            bot.register_next_step_handler(message, calculator)
                    except:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Главное меню")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
❗️ Введите целое число.
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, calculator)


            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                global perexod
                perexod = " "
                idtg = str(call.message.chat.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
                if call.data == "1":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
                Чеки проверяются в ручную, а не автоматически. Сотрудники не смогут проверить чек, если вы пополнили в позднее время или раннее вечером. До 24 часов занимает проверка чека.
                    ''', show_alert=True) 
                elif call.data == "2":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
                Вывод золота занимает до 24 часов. Но мы стараемся как можно быстрее вывести вам золото. Возможно сотрудник взял перерыв или ваш скин трудно найти
                    ''', show_alert=True) 
                elif call.data == "3":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
                Вывод золота происходит до 24 часов от запроса на вывод. Но в большинстве вывод происходит от нескольких минут до часа.
                    ''', show_alert=True) 
                elif call.data == "4":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
                Весь товар, который продаётся в боте, получен честным путём. Если вы сомневаетесь в безопасности, то лучше покупать в игре.
                    ''', show_alert=True) 
                elif call.data == "connect":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
📩 Напишите свой вопрос в поддержку
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(call.message, connect)
                elif call.data == "replenish":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
⭐️ Введите сумму в рублях на которую вы хотите пополнить баланс.
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(call.message, deposit)
                elif call.data == "top1":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
            Топ дня:
                    ''', show_alert=True) 
                elif call.data == "top2":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
            Топ недели:
                    ''', show_alert=True) 
                elif call.data == "top2":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
            Топ месяца:
                    ''', show_alert=True) 
                elif call.data == "course":
                    c.execute("""SELECT course FROM admin""")
                    course = c.fetchone()[0]
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
            Курс: 100G = {course}
                    ''', show_alert=True) 
            @bot.message_handler(content_types=['photo'])
            def Pic(message, summa):
                
                idtg = str(message.chat.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
                if message.text != "Главное меню":

                    try:
                        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
                        downloaded_file = bot.download_file(file_info.file_path)
                        bot.send_photo(1058097307, downloaded_file, f'''
Новая заявка на пополнение!
Сумма - {summa}
id - {idtg}
                        ''')

                    except Exception as e:
                        pass

                    
            bot.polling(none_stop=False)
        else:
            pass
main()


#Создавала бота White Studio💓