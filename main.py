#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sqlite3
import random
from datetime import  datetime
def main():
    while True:
        try:
            global perexod
            perexod = " "
            bot = telebot.TeleBot('6361686380:AAHHukhByQQr-1sHj1rIWX_eodfmkkVJM5M')
            @bot.message_handler(commands=["start", "admin", "answer", "ras", "help", "course", "give", "promo", "delpromo", "addpromo", "db"])
            def start(message, res=False):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("luxu.db")
                c  = db.cursor()
                c.execute("""SELECT idtg FROM users WHERE idtg = ?""", [idtg])
                if c.fetchone() == None:
                    if " " in message.text:
                        if True:
                            print(message.text.split()[1])
                            c.execute("SELECT * FROM users WHERE idtg = ?", [message.text.split()[1]])
                            if c.fetchone() == None:
                                c.execute(f"INSERT INTO users VALUES (?,?,?,?,?,?)",(idtg, 0, "Bronse", 0, 0, None))
                            else:
                                c.execute(f"INSERT INTO users VALUES (?,?,?,?,?,?)",(idtg, 0, "Bronse", 0, 0, message.text.split()[1]))
                            db.commit()
                        else:
                            pass
                    else:
                        c.execute(f"INSERT INTO users VALUES (?,?,?,?,?,?)",(idtg, 0, "Bronse", 0, 0, None))
                        db.commit()
                if "/start" in message.text:
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
                if "/answer" in message.text and idtg == "1359842271":
                    id = int(message.text.split(" ")[1])
                    text = message.text.split(" ")[2]
                    bot.send_message(id, f'''
❗️ Ответ оператора - {text}
                    ''', parse_mode='HTML')
                    bot.send_message(idtg, f'''
❗️ Готово
                    ''', parse_mode='HTML')
                if "/course" in message.text and idtg == "1359842271":
                    c.execute("""SELECT course FROM admin""")
                    course = c.fetchone()[0]
                    new = int(message.text.split(" ")[1])
                    c.execute("UPDATE admin SET course = ?",(new,))
                    db.commit()
                    bot.send_message(idtg, f'''
❗️ Готово
                    ''', parse_mode='HTML')
                if message.text == "/db" and idtg in ["1359842271",  "1058097307"]:
                    c.execute("""SELECT * FROM users""")
                    user = c.fetchall()
                    bot.send_message(idtg, f'''
Количество людей в базе - {len(user)}

DB - {user}
                    ''',  parse_mode='HTML')
                if message.text == "/promo" and idtg in ["1359842271",  "1058097307"]:
                    c.execute("""SELECT * FROM promo""")
                    code = c.fetchall()
                    
                    text = "Ваши промокоды👇"
                    for i in code:
                        text += f"\n\nПромокод - <code>{i[0]}</code>\nСумма - {i[1]}G\nОсталось - {i[2]}шт"
                    bot.send_message(idtg, f'''
{text}

Работа с промокодами:
<code>/delpromo Название</code> - Удаление
<code>/addpromo Название Сумма Количество</code> - Удаление
<code>/promo - Информация</code>
                    ''',  parse_mode='HTML')
                if "/addpromo" in message.text and idtg == "1359842271":
                    try:
                        text = message.text.split(" ")[1]
                        give = int(message.text.split(" ")[2])
                        count = int(message.text.split(" ")[3])
                        c.execute(f"INSERT INTO promo VALUES (?,?,?)",(text, give, count))
                        db.commit()
                        bot.send_message(idtg, f'''
    ❗️ Готово
                        ''',  parse_mode='HTML')
                    except:
                        bot.send_message(idtg, f'''
Произошла ошибка! Проверте правильность заполнения 
                        ''',  parse_mode='HTML')
                if "/delpromo" in message.text and idtg == "1359842271":
                    try:
                        text = message.text.split(" ")[1]
                        c.execute(f"DELETE FROM promo WHERE code = ?",(text,))
                        db.commit()
                        bot.send_message(idtg, f'''
    ❗️ Готово
                        ''',  parse_mode='HTML')
                    except:
                        bot.send_message(idtg, f'''
Произошла ошибка! Проверте правильность заполнения 
                        ''',  parse_mode='HTML')
                if "/ras" in message.text and idtg == "1359842271":
                    text = message.text.split(" ")[1]
                    c.execute("""SELECT idtg FROM users""")
                    id = c.fetchall()
                    for i in id:
                        bot.send_message(i[0], f'''
{text}
                        ''',  parse_mode='HTML')
                    bot.send_message(idtg, f'''
❗️ Готово
                    ''',  parse_mode='HTML')
                if "/give" in message.text and idtg == "1359842271":
                    id = message.text.split(" ")[1]
                    count = int(message.text.split(" ")[2])
                    c.execute("""SELECT balanse FROM users WHERE idtg = ?""", [id])
                    balanse = c.fetchone()[0]
                    c.execute("""SELECT output FROM users WHERE idtg = ?""", [id])
                    output = c.fetchone()[0]
                    c.execute(f"UPDATE users SET balanse = ? WHERE idtg = ?",(balanse + count, id))
                    db.commit()
                    bot.send_message(idtg, f'''
❗️ Готово
                    ''',  parse_mode='HTML')
                    bot.send_message(id, f'''
💡На ваш баланс начислилось {count} G
                    ''', parse_mode='HTML')
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
💵 Баланс: {data[1]}G

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
                    if data[1] < 100:
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Пополнить баланс", callback_data=f"replenish")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
❗️ Вывод работает от 100 голды. ({course} руб)
                        ''',  reply_markup=markup, parse_mode='HTML')
                    else:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Главное меню")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
⭐️ Введите сумму золота которую хотите вывести.
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, vivod1)

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
                        if int(message.text) < course:
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
            def vivod1(message):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
                c.execute("""SELECT * FROM users WHERE idtg= ?""", [idtg])
                data = c.fetchone()
                c.execute("""SELECT course FROM admin""")
                course = c.fetchone()[0]
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
                elif int(message.text) < 100:
                    bot.send_message(idtg, f'''
❗️ Вывод работает от 100 голды. ({course} руб)
⭐️ Введите сумму золота которую хотите вывести.
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(message, vivod1)
                else:
                    c.execute("""SELECT course FROM admin""")
                    course = c.fetchone()[0]
                    prise = round(course / 100 * int(message.text))
                    if prise > data[1]:
                        bot.send_message(idtg, f'''
❗️ Не хватает ₽, пополните баланс!
⭐️ Введите сумму золота которую хотите вывести.
                    ''',  parse_mode='HTML')
                        bot.register_next_step_handler(message, vivod1)
                    else:
                        i = random.randint(10, 99)
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Главное меню")
                        markup.add(btn1)
                        summa = int(message.text) 
                        file = open("vivod.jpg", "rb")
                        bot.send_photo(idtg, file, f'''
Для быстрого и удобного вывода вывтавите пожалуйста:
                                    
TEC-9 "Tie Dye" за <code>{round(summa * 0.25 + summa)}.{i}</code>, нажмите на вкладку "Только мои запросы" и пришлите нам скриншот✅
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, vivod2, summa, prise)
            def vivod2(message, summa, prise):
                idtg = str(message.chat.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
                try:
                    if message.text != "Главное меню":
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Готово", callback_data=f"vivod {idtg} {summa} {prise}")
                        btn2 = types.InlineKeyboardButton(text="Отклонить", callback_data=f"del {idtg}")
                        markup.add(btn1,btn2)
                        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
                        downloaded_file = bot.download_file(file_info.file_path)
                        bot.send_photo(1359842271, downloaded_file, f'''
Новая заявка на вывод!
Количество - {summa}
Сумма - {prise}
id - {idtg}
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.send_message(idtg, f'''
Ожидайте....
                        ''', parse_mode='HTML')
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
                except:
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    markup.add(btn5, btn6, btn7)
                    bot.send_message(idtg, f'''
❌Произошла ошибка!
Нажмите - /start
                    ''',  reply_markup=markup, parse_mode='HTML')
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
            def connect(message):
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
                    bot.send_message(idtg, f'''
Ожидайте, вам ответят в ближайшее время!
                    ''', parse_mode='HTML')
                    bot.send_message(1359842271, f'''
Вопрос от {idtg} 

{message.text}

Что-бы ответить напишите 
<code>/answer {idtg} ответ</code>
                    ''', parse_mode='HTML')
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                global perexod
                perexod = " "
                idtg = str(call.message.chat.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
                if call.data == "1":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
                Чеки проверяются в ручную, а не автоматически. До 24 часов занимает проверка чека.
                    ''', show_alert=True) 
                elif call.data == "2":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
                Вывод золота занимает до 24 часов. Но мы стараемся как можно быстрее вывести вам золото. 
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
                elif call.data == "top3":
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
            Топ месяца:
                    ''', show_alert=True) 
                elif call.data == "course":
                    c.execute("""SELECT course FROM admin""")
                    course = c.fetchone()[0]
                    bot.answer_callback_query(callback_query_id=call.id, text=f'''
            Курс: 100G = {course} Р
                    ''', show_alert=True) 
                elif "+" in call.data:
                    bot.delete_message(idtg, call.message.message_id)
                    id = int(call.data.split(" ")[1])
                    summa = int(call.data.split(" ")[2])
                    c.execute("""SELECT course FROM admin""")
                    course = c.fetchone()[0] / 100
                    summa1 = round(summa / course)
                    print(summa1)
                    c.execute("""SELECT balanse FROM users WHERE idtg = ?""", [id])
                    balanse = c.fetchone()[0]
                    c.execute("""SELECT ref FROM users WHERE idtg = ?""", [id])
                    ref = c.fetchone()[0]
                    if ref != None:
                        c.execute("""SELECT balanse FROM users WHERE idtg = ?""", [ref])
                        balanseref = c.fetchone()[0]
                        c.execute(f"UPDATE users SET balanse = ? WHERE idtg = ?",(balanseref+summa1*0.05, ref))
                        bot.send_message(ref, f'''
💡На ваш баланс начислилось {summa1*0.05}G за реферала!
                        ''', parse_mode='HTML')
                    c.execute("""SELECT given FROM users WHERE idtg = ?""", [id])
                    given = c.fetchone()[0]
                    c.execute(f"UPDATE users SET balanse = ? WHERE idtg = ?",(summa1+balanse, id))
                    c.execute(f"UPDATE users SET given = ? WHERE idtg = ?",(summa+given, id))
                    db.commit()
                    bot.send_message(id, f'''
💡На ваш баланс начислилось {summa1} G
                    ''', parse_mode='HTML')
                elif "-" in call.data:
                    bot.delete_message(idtg, call.message.message_id)
                    id = int(call.data.split(" ")[1])
                    bot.send_message(id, f'''
❌ Ваша заявка на пополнение была отклонена!
                    ''', parse_mode='HTML')
                elif "fake" in call.data:
                    bot.delete_message(idtg, call.message.message_id)
                    id = int(call.data.split(" ")[1])
                    bot.send_message(id, f'''
❌ Ваша заявка на пополнение была отклонена!

💡 Причина: Фейк.
                    ''', parse_mode='HTML')
                elif call.data == "ref":
                    bot.delete_message(idtg, call.message.message_id)
                    bot.send_message(idtg, f'''
Это ваша реферальная ссылка🫳 
<code>https://t.me/LuxuGold_bot?start={idtg}</code>
                                     
За каждого приглашенного гостя который сделает покупку вы получаете 5% от суммы его пополнений!
                    ''', parse_mode='HTML')
                elif "vivod" in call.data:
                    id = int(call.data.split(" ")[1])
                    summa = int(call.data.split(" ")[2])
                    prise = int(call.data.split(" ")[3])
                    bot.delete_message(idtg, call.message.message_id)
                    bot.send_message(id, f'''
Ваш вывод золота был выполнен ✅
Спасибо за покупку
                    ''', parse_mode='HTML')
                    
                    c.execute("""SELECT balanse FROM users WHERE idtg = ?""", [id])
                    balanse = c.fetchone()[0]
                    c.execute("""SELECT output FROM users WHERE idtg = ?""", [id])
                    output = c.fetchone()[0]
                    c.execute(f"UPDATE users SET balanse = ? WHERE idtg = ?",(balanse - summa, id))
                    c.execute(f"UPDATE users SET output = ? WHERE idtg = ?",(summa+output, id))
                    db.commit()
                elif "del" in call.data:
                    bot.delete_message(idtg, call.message.message_id)
                    id = int(call.data.split(" ")[1])
                    bot.send_message(id, f'''
❌ Ваша заявка на вывод была отклонена!
                    ''', parse_mode='HTML')
                elif call.data == "promo":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
💡 Введите промокод:
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(call.message, promo)
            def promo(message):
                idtg = str(message.chat.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
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
                    c.execute("""SELECT count FROM promo WHERE code = ?""", [message.text])
                    if c.fetchone() == None:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton(text="Главное меню")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
❌ Промокод не найден
💡 Введите промокод:
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, promo)
                    else:
                        c.execute("""SELECT idtg FROM promo_users WHERE code = ? and idtg = ?""", [message.text, idtg])
                        if c.fetchone() != None:
                            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                            btn1 = types.KeyboardButton(text="Главное меню")
                            markup.add(btn1)
                            bot.send_message(idtg, f'''
❌ Вы активировали этот промокод
💡 Введите промокод:
                            ''',  reply_markup=markup, parse_mode='HTML')
                            bot.register_next_step_handler(message, promo)
                        else:
                            c.execute("""SELECT count FROM promo WHERE code = ?""", [message.text])
                            count = c.fetchone()[0]
                            if count <= 0:
                                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                                btn1 = types.KeyboardButton(text="Главное меню")
                                markup.add(btn1)
                                bot.send_message(idtg, f'''
❌ Промокод завершил своё существование...
💡 Введите промокод:
                                ''',  reply_markup=markup, parse_mode='HTML')
                                bot.register_next_step_handler(message, promo)
                            else:
                                c.execute("""SELECT give FROM promo WHERE code = ?""", [message.text])
                                give = c.fetchone()[0]
                                c.execute("""SELECT count FROM promo WHERE code = ?""", [message.text])
                                count = c.fetchone()[0]
                                c.execute("""SELECT balanse FROM users WHERE idtg = ?""", [idtg])
                                balanse = c.fetchone()[0]
                                c.execute(f"UPDATE users SET balanse = ? WHERE idtg = ?",(balanse + give, idtg))
                                c.execute(f"UPDATE promo SET count = ? WHERE code = ?",(count - 1, message.text))
                                c.execute(f"INSERT INTO promo_users VALUES (?,?)",(idtg, message.text))
                                db.commit()
                                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                                btn1 = types.KeyboardButton(text="Главное меню")
                                markup.add(btn1)
                                bot.send_message(idtg, f'''
 На ваш счёт начислено {give}G ✅
                                ''',  reply_markup=markup, parse_mode='HTML')
                                bot.register_next_step_handler(message, promo)
            def Pic(message, summa):
                idtg = str(message.chat.id)
                db = sqlite3.connect("luxu.db")
                c = db.cursor()
                try:
                    if message.text != "Главное меню":
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Принять", callback_data=f"+ {idtg} {summa}")
                        btn2 = types.InlineKeyboardButton(text="Отклонить", callback_data=f"- {idtg}")
                        btn3 = types.InlineKeyboardButton(text="Фейк", callback_data=f"fake {idtg}")
                        markup.add(btn1,btn2,btn3)
                        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
                        downloaded_file = bot.download_file(file_info.file_path)
                        bot.send_photo(1359842271, downloaded_file, f'''
Новая заявка на пополнение!
Сумма - {summa}
id - {idtg}
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.send_message(idtg, f'''
Ожидайте....
                        ''', parse_mode='HTML')
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
                except:
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton(text="Главное меню")
                    markup.add(btn1)
                    markup.add(btn5, btn6, btn7)
                    bot.send_message(idtg, f'''
❌Произошла ошибка!
Нажмите - /start
                    ''',  reply_markup=markup, parse_mode='HTML')
            bot.polling(none_stop=False)
        except:
            pass
main()


#Создавала бота White Studio💓