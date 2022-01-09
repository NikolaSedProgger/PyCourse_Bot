import telebot
from telebot import types
from datetime import datetime
from time import sleep

bot = telebot.TeleBot('5038164782:AAG7koIwUCUgdB92eL1PiqTdIplWhmpdxM0')

stage = 0
complete_stage = types.InlineKeyboardMarkup()
complete_stage_button = types.InlineKeyboardButton(text='Продолжить', callback_data='complete_stage')
complete_stage.add(complete_stage_button)

current_year = datetime.now().year


def course_variables(call):
    bot.send_message(call.message.chat.id, "Первым делом мы познакомимся с перепенными")
    bot.send_message(call.message.chat.id, "Переменные представляют из себя некую коробочку, которая хранит информацию.")
    bot.send_message(call.message.chat.id, "Например ящик = яблоки + апельсины.", reply_markup=complete_stage)


def course_variables_types(call):
    bot.send_message(call.message.chat.id, "Теперь узнаем, каких видов бывают наши переменные")
    bot.send_photo(call.message.chat.id, photo=open("content/переменные.png", 'rb'))
    variables_types = """
    Переменные бывают 5 видов:
    - Строка str
    - Число int
    - Список list
    - Словарь dict
    - Правда/Неправда bool
    """
    bot.send_message(call.message.chat.id, variables_types, reply_markup=complete_stage)


def course_print(call):
    bot.send_message(call.message.chat.id, "Теперь, когда мы знаем, что такое переменные, мы можем приступить к самому программированию!")
    bot.send_photo(call.message.chat.id, photo=open("content/Print.png", 'rb'))
    bot.send_message(call.message.chat.id, "Для начала мы познакомимся с командой 'print()'.")
    bot.send_message(call.message.chat.id, "Она выводит нужный нам текст в консоль")
    bot.send_message(call.message.chat.id, 'Так-же есть некие f-строки они выглядят так "print(f"{переменная} любой текст" ', reply_markup=complete_stage)


def course_print_practice(call):
    test_keyboard = types.InlineKeyboardMarkup()
    answer_1 = types.InlineKeyboardButton(text='3', callback_data='right')
    answer_2 = types.InlineKeyboardButton(text='+ 3', callback_data='wrong')
    answer_3 = types.InlineKeyboardButton(text='9', callback_data='wrong')
    test_keyboard.add(answer_1)
    test_keyboard.add(answer_2)
    test_keyboard.add(answer_3)
    bot.send_photo(call.message.chat.id, photo=open("content/print_test.png", 'rb'))
    bot.send_message(call.message.chat.id, "Какое число должно стоять вместо вопроса?", reply_markup=test_keyboard)


def course_hard_print_practice(call):
    hard_test_keyboard = types.InlineKeyboardMarkup()
    answer_1 = types.InlineKeyboardButton(text='Python', callback_data='right')
    answer_2 = types.InlineKeyboardButton(text='Py+th+on', callback_data='wrong')
    hard_test_keyboard.add(answer_1)
    hard_test_keyboard.add(answer_2)
    bot.send_photo(call.message.chat.id, photo=open("content/print_test2.png", 'rb'))
    bot.send_message(call.message.chat.id, "Как думаете, что выведет в консоле на этот раз?", reply_markup=hard_test_keyboard)


def course_python_logic(call):
    bot.send_message(call.message.chat.id, "Теперь мы знаем уже 1 крутую команду в питоне! 😉 ")
    bot.send_message(call.message.chat.id, "На этот раз мы познакомимся с логическими командами if, elif, else")
    bot.send_message(call.message.chat.id, 'if в переводе "Если". В питоне зачастую она используется так: "Если перемееная == чему-то, то выполняю это." ')
    bot.send_message(call.message.chat.id, 'elif использует, в другом 👉 КОНКРЕТНОМ 👈 случае')
    bot.send_message(call.message.chat.id, 'else используется, в другом 👉 ЛЮБОМ 👈 случае')
    bot.send_photo(call.message.chat.id, photo=open("content/Условие if.png", 'rb'), reply_markup=complete_stage)
    bot.send_message(call.message.chat.id, 'Попробуйте сами написать свой код с условиями 😉 ')


def course_cycles(call):
    bot.send_message(call.message.chat.id, "Мы уже узнали как работают логические команды в питоне! 🤯 ")
    bot.send_message(call.message.chat.id, "Настало время для циклов")
    bot.send_photo(call.message.chat.id, photo=open("content/Цикл for.png", 'rb'))
    bot.send_message(call.message.chat.id, "Цикл как бы бежит 🏃 по списку, перебирая его элементы и присвайвая их значения в нашем случаем переменной i")
    bot.send_photo(call.message.chat.id, photo=open("content/Цикл while.png", 'rb'))
    bot.send_message(call.message.chat.id, "Цикл while работает, пока не выполнит, то или иное условие", reply_markup=complete_stage)
    bot.send_photo(call.message.chat.id, photo=open("content/Шпаргалка1.png", 'rb'))
    bot.send_photo(call.message.chat.id, photo=open("content/Шпаргалка2.png", 'rb'))
    bot.send_message(call.message.chat.id, "Эти же равенства можно использовать и в условиях 😌 ")


def course_functions(call):
    bot.send_message(call.message.chat.id, "Вот мы уже почти изучили почти все базовые команды в Python 🐍 ")
    bot.send_message(call.message.chat.id, "Осталось узнать, что такой ФУНКЦИИ 👑 ")
    bot.send_message(call.message.chat.id, "Функции это некая большая коробка с командами, условиями, и переменными.")
    bot.send_message(call.message.chat.id, "Чтобы не повторять одни и те же действия используют чаще функции, чем циклы.")
    bot.send_photo(call.message.chat.id, photo=open("content/Функции.png", 'rb'), reply_markup=complete_stage)


def course_imports(call):
    bot.send_message(call.message.chat.id, "Мы уже подходим к концу нашего курса.")
    bot.send_message(call.message.chat.id, "Вы наверное скажете, что Python довольно лёгкий, но почему же он так популярен?...")
    sleep(5.5)
    bot.send_photo(call.message.chat.id, photo=open("content/Библиотеки.png", 'rb'))
    bot.send_message(call.message.chat.id, "Библиотеки от разных других пользователей! Их очень много и из-за этого Питон очень многофункционален 👍 ")
    bot.send_message(call.message.chat.id, "(pip можно использовать, только, если у вас установлен python на ПК)", reply_markup=complete_stage)


def course_clean_code(call):
    bot.send_message(call.message.chat.id, "На последок хочу рассказать как писать чистый и аккуратный код")
    bot.send_message(call.message.chat.id, "- Называйте пременные понятными названиями")
    bot.send_message(call.message.chat.id, "- Делайте отступы")
    bot.send_message(call.message.chat.id, "- Пользуйтесь сайтом PEP8 online (http://pep8online.com)")
    bot.send_message(call.message.chat.id, "- Пишите код по шаблону: в начале import'ы, потом глобальные константы, потом функции, потом переменные и использование функций", reply_markup=complete_stage)


def the_end(call):
    bot.send_message(call.message.chat.id, "Поздравляю, вы теперь короли Python'а! 👑 ")
    bot.send_message(call.message.chat.id, "Курс окончен, развивайтесь и стремить к своим высотам 💪 ")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Начать" or "начать":
        intro_keyboard = types.InlineKeyboardMarkup()
        start_intro = types.InlineKeyboardButton(text='Да, готов(-а)', callback_data='Yes')
        intro_keyboard.add(start_intro)
        bot.send_photo(message.from_user.id, photo=open("content/курс.png", 'rb'))
        bot.send_message(message.from_user.id, "Здравствуйте, готовы пройти небольшой курс по изучению языка программирования python?", reply_markup=intro_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Yes":
        course_keyboard = types.InlineKeyboardMarkup()
        start_course = types.InlineKeyboardButton(text='Начать программировать', callback_data='start_course')
        course_keyboard.add(start_course)
        bot.send_message(call.message.chat.id, 'Начнём! Для чего же вообще нужно програмирование?')
        bot.send_message(call.message.chat.id, 'Программиирование — процесс создания компьютерных программ, облегчающих нам жизнь. Например весь функцион государственных сайтов, это по сути программы.')
        bot.send_photo(call.message.chat.id, photo=open("content/программа.png", 'rb'), reply_markup=course_keyboard)

    elif call.data == "start_course":
        bot.send_message(call.message.chat.id, 'Для начала откроем сайт, где мы будем программировать и создавать наши проекты')
        bot.send_message(call.message.chat.id, 'https://www.online-python.com')
        bot.send_message(call.message.chat.id, 'И удалим всё ненужное')
        bot.send_photo(call.message.chat.id, photo=open("content/чистота.png", 'rb'), reply_markup=complete_stage)

    elif call.data == "complete_stage":
        def stage_promotion():
            global stage
            stage = stage + 1
        stage_promotion()
        if stage == 1:
            course_variables(call)
        elif stage == 2:
            course_variables_types(call)
        elif stage == 3:
            course_print(call)
        elif stage == 4:
            course_print_practice(call)
        elif stage == 5:
            course_hard_print_practice(call)
        elif stage == 6:
            course_python_logic(call)
        elif stage == 7:
            course_cycles(call)
        elif stage == 8:
            course_functions(call)
        elif stage == 9:
            course_imports(call)
        elif stage == 10:
            course_clean_code(call)
        elif stage == 11:
            the_end(call)
    elif call.data == 'wrong':
        bot.send_message(call.message.chat.id, "К сожалению это неверно 😢 ")
    elif call.data == 'right':
        bot.send_message(call.message.chat.id, "Отлично! Ответ верный 😃 ", reply_markup=complete_stage)
bot.polling(none_stop=True, interval=0)
