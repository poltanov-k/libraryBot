import telebot

bot = telebot.TeleBot('6029798849:AAEgoG36QpnD17PWLCkRlsN-FrHpy6bZcnI')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добрейший вечерочек! Выбираем тематику, не стесняемся!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет! Пора чему-нибудь научиться! /start")

    # МЕНЮ ГАЙДОВ

    elif message.text == "Интернет-маркетинг 💰":
        bot.send_message(message.from_user.id, "Отличный выбор, юный манипулятор! Теперь сузим твою выборку",reply_markup=keyboard2);
    elif message.text == "Социальные сети":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n <b>Нейромаркетинг социальных сетей </b> \n Скачать - /download1 \n\n<b>Продвижение В Инстаграм</b>\n Скачать - /download2\n\n<b>Быстрый старт в Telegram</b>\nСкачать - /download3\n\n<b>Заработок в telegram [Трафик]</b>\nСкачать - /download4\n\n<b>Как раскрутить канал в Telegram за копейки</b>\nСкачать - /download5",  parse_mode="HTML",reply_markup=keyboard8)
    elif message.text == "Продажи":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Продажи и лидогенерация</b>\nСкачать - /download6 \n\n<b>Взрывные продажи 2.0: лучшие практики\nСкачать - /download7 \n\n<b>БМ - Продажи как система</b>\nСкачать - /download8 \n\n<b>Эффективные продажи по телефону</b>\nСкачать - /download9 \n\n<b>Как продавать неприлично много с помощью email рассылок</b>\nСкачать - /download10 \n\n", parse_mode="HTML",reply_markup=keyboard8)
    elif message.text == "CEO-продвижение":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Оптимизация и продвижение сайтов</b>\nСкачать - /download47", parse_mode="HTML", reply_markup=keyboard8)

    elif message.text == "Психология 💆":
        bot.send_message(message.from_user.id, "Думаешь, что достаточно знаешь себя или других? Поверь, все не так просто. Начни разбираться в людях с помощью наших гайдов!",reply_markup=keyboard3);
    elif message.text == "Мотивация":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Как мотивировать себя на тренировки и достигать целей</b>\nСкачать - /download11 \n\n", parse_mode="HTML",reply_markup=keyboard9)
    elif message.text == "Общение":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Секреты общения. Магия слов</b>\nСкачать - /download12 \n\n", parse_mode="HTML",reply_markup=keyboard9)
    elif message.text == "Нужно больше гайдов!":
                bot.send_sticker(message.from_user.id, 'CAADAgADLQADW46KBtt3vZkY7m8NFgQ')

    elif message.text == "Программирование 💻":
        bot.send_message(message.from_user.id, "Выучить любой язык программирования можно и в одиночку. Наши курсы разработаны как для новичков, так и для профессионалов!",reply_markup=keyboard4);
    elif message.text == "Python":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Изучение python, tkinter и django</b>\nСкачать - /download13 \n\n<b>Полное руководство по Python 3: от новичка до специалиста</b>\nСкачать - /download14 \n\n<b>Мастер этического взлома с Python</b>\nСкачать - /download15 \n\n",parse_mode="HTML",reply_markup=keyboard10)
    elif message.text == "Java":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Программирование на Java с нуля до гуру</b>\nСкачать - /download16 \n\n",parse_mode="HTML",reply_markup=keyboard10)
    elif message.text == "1C":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Программирование в системе 1С:Предприятие 8.3</b>\nСкачать - /download17 \n\n<b>Ускорение и оптимизация систем на 1С:Предприятие 8.3</b>\nСкачать - /download18",parse_mode="HTML",reply_markup=keyboard10)
    elif message.text == "C#":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Изучение C# от новичка до профи</b>\nСкачать - /download19 \n\n",parse_mode="HTML",reply_markup=keyboard10)
    elif message.text == "PHP":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Основы PHP</b>\nСкачать - /download20 \n\n",parse_mode="HTML",reply_markup=keyboard10)
    elif message.text == "JavaScript":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Интенсивный онлайн курс Продвинутый JavaScript</b>\nСкачать - /download21\n\n<b>JavaScript. Полное руководство для современной веб-разработки</b>\nСкачать - /download22",parse_mode="HTML",reply_markup=keyboard10)
    elif message.text == "Допольнительно":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Программирование начинающим</b>\nСкачать - /download23\n\n<b>Создание чат-ботов без программирования за 1 час</b>\nСкачать - /download24\n\n<b>Чат бот WhatsApp на миллион. Научись за 5 минут</b>\nСкачать - /download25\n\n<b>Создание чат-бот для бизнеса с нуля</b>\nСкачать - /download26",parse_mode="HTML",reply_markup=keyboard10)

    elif message.text == "Здоровье 🌽":
        bot.send_message(message.from_user.id, "Хочешь подтянуть свою фигуру? С нашими гайдами это проще простого!",reply_markup=keyboard5);
    elif message.text == "Фитнесс":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Как быстро сесть на шпагат</b>\nСкачать - /download27\n\n<b>Как увеличить кол-во отжиманий с 10 до 100 за 1 месяц</b>\nСкачать - /download28\n\n<b>Улучшаем физическую форму без специальных тренажеров</b>\nСкачать - /download29\n\n<b>4.	Анатомия силовых упражнений с использованием собственного веса</b>\nСкачать - /download30",parse_mode="HTML",reply_markup=keyboard11)
    elif message.text == "Здоровое питание":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>ОСНОВЫ ЗДОРОВОГО ПИТАНИЯ</b>\nСкачать - /download45",parse_mode="HTML",reply_markup=keyboard11)
    elif message.text == "Йога":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Новая книга по Йоге</b>\nСкачать - /download46",parse_mode="HTML",reply_markup=keyboard11)

    elif message.text == "Дизайн-программирование 🎨":
        bot.send_message(message.from_user.id, "Фотошоп, афтер эффектс и много других программ, которые ты знаешь, но в которые не умеешь. Мы научим, только выбери что:",reply_markup=keyboard6);
    elif message.text == "Photoshop":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>HDR Photoshop Actions</b>\nСкачать - /download31\n\n<b>SoPainted Photoshop Action</b>\nСкачать - /download32\n\n<b>Dark Action I - Photoshop Action</b>\nСкачать - /download33\n\n<b>Poster Painting Photoshop Action</b>\nСкачать - /download34\n\n<b>Universal Comic Book Effect Photoshop Action</b>\nСкачать - /download38",parse_mode="HTML",reply_markup=keyboard12)
    elif message.text == "Adobe After Effects":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Cinema 4D & AfterEffects</b>\nСкачать - /download35\n\n<b>Adobe After Effects Продвинутый уровень</b>\nСкачать - /download36\n\n<b>Крутая база After Effects [5-ый поток] + 3200 шаблонов Videohive + Бонусы</b>\nСкачать - /download37",parse_mode="HTML",reply_markup=keyboard12)
    elif message.text == "Дизайн ВКонтакте":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Марафон По Дизайну В Вконтакте</b>\nСкачать - /download39\n\n<b>Дизайнер В Вконтакте 4.0</b>\nСкачать - /download40",parse_mode="HTML",reply_markup=keyboard12)
    elif message.text == "Моушен дизайн":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Курс по моушн дизайну</b>\nСкачать - /download41",parse_mode="HTML",reply_markup=keyboard12)

    elif message.text == "Изучение языков 🇬🇧":
        bot.send_message(message.from_user.id, "Ду ю файнд изи вей то лерн форейн ленгвич? Кам хир енд чуз:",reply_markup=keyboard7);
    elif message.text == "Английский язык":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Оганян Ж.Л. - Экспресс - курс английского языка</b>\nСкачать - /download42",parse_mode="HTML",reply_markup=keyboard13)
    elif message.text == "Испанский язык":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Самоучитель испанского языка. Don Manual</b>\nСкачать - /download43",parse_mode="HTML",reply_markup=keyboard13)
    elif message.text == "Французский язык":
                bot.send_message(message.from_user.id, "Доступные гайды:\n\n<b>Современный французский язык</b>\nСкачать - /download44",parse_mode="HTML",reply_markup=keyboard13)

        # КОМАНДЫ СКАЧАТЬ
    elif message.text == "/download1":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup=markup1)
    elif message.text == "/download2":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup2)
    elif message.text == "/download3":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup=markup3)
    elif message.text == "/download4":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup4)
    elif message.text == "/download5":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup5)
    elif message.text == "/download6":
        bot.send_message(download.from_user.id, "Ссылка на скачивание:", reply_markup= markup6)
    elif message.text == "/download7":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup7)
    elif message.text == "/download8":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup8)
    elif message.text == "/download9":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup9)
    elif message.text == "/download10":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup=markup10)
    elif message.text == "/download11":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup11)
    elif message.text == "/download12":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup12)
    elif message.text == "/download13":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup13)
    elif message.text == "/download14":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup14)
    elif message.text == "/download15":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup15)
    elif message.text == "/download16":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup16)
    elif message.text == "/download17":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup17)
    elif message.text == "/download18":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup18)
    elif message.text == "/download19":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup19)
    elif message.text == "/download20":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup20)
    elif message.text == "/download21":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup21)
    elif message.text == "/download22":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup22)
    elif message.text == "/download23":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup23)
    elif message.text == "/download24":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup=markup24)
    elif message.text == "/download25":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup25)
    elif message.text == "/download26":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup26)
    elif message.text == "/download27":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup27)
    elif message.text == "/download28":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup28)
    elif message.text == "/download29":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup29)
    elif message.text == "/download30":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup30)
    elif message.text == "/download31":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup=markup31)
    elif message.text == "/download32":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup33)
    elif message.text == "/download34":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup34)
    elif message.text == "/download35":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup35)
    elif message.text == "/download36":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup36)
    elif message.text == "/download37":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup37)
    elif message.text == "/download38":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup38)
    elif message.text == "/download39":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup=markup39)
    elif message.text == "/download40":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup40)
    elif message.text == "/download41":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup41)
    elif message.text == "/download42":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup42)
    elif message.text == "/download43":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup43)
    elif message.text == "/download44":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup44)
    elif message.text == "/download45":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup45)
    elif message.text == "/download46":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup46)
    elif message.text == "/download47":
        bot.send_message(message.from_user.id, "Ссылка на скачивание:", reply_markup= markup47)

    # ВЕРНУТЬСЯ В МЕНЮ

    elif message.text == "В главное меню ☝":
        bot.send_message(message.from_user.id, "В начало!", reply_markup=keyboard1)
    elif message.text == "Назад ↩":
        bot.send_message(message.from_user.id, "Назад в меню!", reply_markup=keyboard2)
    elif message.text == "Назад⁣ ↩":
        bot.send_message(message.from_user.id, "Назад в меню!", reply_markup=keyboard3)
    elif message.text == "Назад ↩⁣⁣":
        bot.send_message(message.from_user.id, "Назад в меню!", reply_markup=keyboard4)
    elif message.text == "Назад ↩⁣⁣⁣":
        bot.send_message(message.from_user.id, "Назад в меню!", reply_markup=keyboard5)
    elif message.text == "Назад ↩⁣⁣⁣⁣":
        bot.send_message(message.from_user.id, "Назад в меню!", reply_markup=keyboard6)
    elif message.text == "Назад ↩⁣⁣⁣⁣⁣":
        bot.send_message(message.from_user.id, "Назад в меню!", reply_markup=keyboard7)

    else:
        bot.send_message(message.from_user.id, "Нужна помощь? Напиши /help.")

@bot.message_handler(content_types=['sticker'])
def send_text(message):
    print(message)

@bot.message_handler(content_types=['photo'])
def photo_messages(message):
    if message.content_type == 'photo':
        bot.send_sticker(message.from_user.id, 'CAADAgAD2QIAAtGzAgABXgFV1s')

# КЛАВИАТУРА РЕПЛАЙ

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.add('Интернет-маркетинг 💰')
keyboard1.add('Психология 💆')
keyboard1.add('Программирование 💻')
keyboard1.add('Здоровье 🌽')
keyboard1.add('Дизайн-программирование 🎨')
keyboard1.add('Изучение языков 🇬🇧')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard2.add('Социальные сети')
keyboard2.add("Продажи")
keyboard2.add("CEO-продвижение")
keyboard2.add("В главное меню ☝")

keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard3.add('Мотивация')
keyboard3.add("Общение")
keyboard3.add("Нужно больше гайдов!")
keyboard3.add("В главное меню ☝")

keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard4.add('Python')
keyboard4.add("Java")
keyboard4.add("1C")
keyboard4.add("C#")
keyboard4.add("PHP")
keyboard4.add("JavaScript")
keyboard4.add("Допольнительно")
keyboard4.add("В главное меню ☝")

keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard5.add('Фитнесс')
keyboard5.add("Здоровое питание")
keyboard5.add("Йога")
keyboard5.add("В главное меню ☝")

keyboard6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard6.add('Photoshop')
keyboard6.add("Adobe After Effects")
keyboard6.add("Дизайн ВКонтакте")
keyboard6.add("Моушен дизайн")
keyboard6.add("В главное меню ☝")

keyboard7 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard7.add('Английский язык')
keyboard7.add("Испанский язык")
keyboard7.add("Французский язык")
keyboard7.add("В главное меню ☝")

# КЛАВА НАЗАД

keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard8.add('Назад ↩')
keyboard8.add("В главное меню ☝")

keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard9.add('Назад⁣ ↩')
keyboard9.add("В главное меню ☝")

keyboard10 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard10.add('Назад ↩⁣⁣')
keyboard10.add("В главное меню ☝")

keyboard11 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard11.add('Назад ↩⁣⁣⁣')
keyboard11.add("В главное меню ☝")

keyboard12 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard12.add('Назад ↩⁣⁣⁣⁣')
keyboard12.add("В главное меню ☝")

keyboard13 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard13.add('Назад ↩⁣⁣⁣⁣⁣')
keyboard13.add("В главное меню ☝")





# КЛАВИАТУРА ИНЛАЙН

markup1 = telebot.types.InlineKeyboardMarkup()
inlinekey1 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9uxr')
markup1.add(inlinekey1)

markup2 = telebot.types.InlineKeyboardMarkup()
inlinekey2 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wyp')
markup2.add(inlinekey2)

markup3 = telebot.types.InlineKeyboardMarkup()
inlinekey3 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wyq')
markup3.add(inlinekey3)

markup4 = telebot.types.InlineKeyboardMarkup()
inlinekey4 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wyr')
markup4.add(inlinekey4)

markup5 = telebot.types.InlineKeyboardMarkup()
inlinekey5 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s144myt.storage.yandex.net/rdisk/9a9aca7bc6343697baf6470b2e96239500d9ad7743066024b3e1d988bb687f23/5de25772/lhrGPxjgD96j86dmCsxhrgp8zeqBL7XntJYzDUoJeucPDgsSCFY0TB5QmnRasSss_BIRjgUy2XLVs4QlELDmkA==?uid=0&filename=%D0%9A%D0%B0%D0%BA%20%D1%80%D0%B0%D1%81%D0%BA%D1%80%D1%83%D1%82%D0%B8%D1%82%D1%8C%20%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%20%D0%B2%20%D0%A2%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%20%D0%B7%D0%B0%20%D0%BA%D0%BE%D0%BF%D0%B5%D0%B9%D0%BA%D0%B8%20-%20%D1%81%20%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC%20%D0%B1%D1%8E%D0%B4%D0%B6%D0%B5%D1%82%D0%BE%D0%BC.docx&disposition=attachment&hash=cTGnpaanIHmE9Jl/Bgm3VtZIM3BLbUnncSeMFIjNHr4%3D&limit=0&content_type=application%2Fvnd.openxmlformats-officedocument.wordprocessingml.document&owner_uid=541703102&fsize=189049&hid=abe24e7c4160869d661334237c254523&media_type=document&tknv=v2&rtoken=HumozV7RkV5Z&force_default=no&ycrid=na-fcc6ee0c82f5cbed1517e075cfc49cbc-downloader20f&ts=5988ef2cf4080&s=4de82824e876dfeb962cc553ae40a109ceb76a54921a92096e7eafa2f28f0c5c&pb=U2FsdGVkX18N_xHqDaT2E0SHKVdvJZfLZpxA6tcNYXpPYRmEkfANBspyDzYGlLnXwH_suG7bBlYmQYqwfQXoX3rW7HHq4VONMhGY8WbpeVw')
markup5.add(inlinekey5)

markup6 = telebot.types.InlineKeyboardMarkup()
inlinekey6 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s447sas.storage.yandex.net/rdisk/2162c075555d070ab411bcbe61a743ccf1139775ab4212b06f4272bb70bde45a/5de263f3/OBXdzocGHhHCWvRt7oYw6OyIQSmGB_XF3FuxZT2stc6UP8RorUnAr965EBeqM0VYzcvXuK65cI5S4CxTbkFbgQ==?uid=0&filename=%5BInfosklad.org%5D%20%D0%91%D0%B8%D0%B7%D0%BA%D0%BE%D0%BD%20-%20%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B8%20%D0%B8%20%D0%BB%D0%B8%D0%B4%D0%BE%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%282015%29.rar&disposition=attachment&hash=oE9I/NccTXwmiDvgXKBaOMPl5Td2ZBnK7a8CXGiop2w%3D%3A/%5BInfosklad.org%5D%20%D0%91%D0%B8%D0%B7%D0%BA%D0%BE%D0%BD%20-%20%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B8%20%D0%B8%20%D0%BB%D0%B8%D0%B4%D0%BE%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%282015%29.rar&limit=0&content_type=application%2Fx-rar&owner_uid=444853684&fsize=330602452&hid=d3caf91f698ed368dfea3119b447cc0b&media_type=compressed&tknv=v2&rtoken=ftKm1kQT5x6v&force_default=no&ycrid=na-a3f4b1e9e60fc145323115be8a33801b-downloader18h&ts=5988fb19aa2c0&s=60ede155c20ef8e7cfabafdb6666b9dd03cf240426c2fd7235bab12aec67b8f7&pb=U2FsdGVkX18WVOQNQYkJHeacjmTYQFDHAZ_8EAuCy0UM_aD0ejARyiRf6eMnVi30EX6aBeSN9-4E4pws06_iW3ykN8sQ5al8vSvnRXffTIM')
markup6.add(inlinekey6)

markup7 = telebot.types.InlineKeyboardMarkup()
inlinekey7 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s167i.storage.yandex.net/rdisk/690ef32dc9bf6b2388401cc73a1067abc0e842e1a9c9346d463f98d0fad606ae/5de25878/_hmqyItL7UCNPd_8uCQWrPT8Uuf1qivhEY9kpU3gi1l8zovSUO9TlT9AuUzgV8qUX8ShndHBaM_8gAXT3_3WEQ==?uid=0&filename=%D0%B2%D0%B7%D1%80%D1%8B%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B8%202.0.avi&disposition=attachment&hash=NTTPsIfm0JHp8xNaCq9rrIcBVezE10l1E4c3Z4G9ciM%3D&limit=0&content_type=video%2Favi&owner_uid=378244782&fsize=3389393328&hid=d0b1284cd83686ff3d9209e0ccb56154&media_type=video&tknv=v2&rtoken=ln67dWKL9QAq&force_default=no&ycrid=na-f73b27df5d0cd8d8383f7bc865aaa8d8-downloader21f&ts=5988f026d0e00&s=018c06f39bb82280a858b06b9f118f65ab512500d8012d02a5becf1c6f5e8c2e&pb=U2FsdGVkX1-5Sy8CfojUNaj3kCV1V7P5iPYC7Tlizti5LuuiPgxqr3WNyGsRdsKPD24kSe23-YL9ypmfHA4rKsRGgVQRTrBCHCVmRzFUp8M')
markup7.add(inlinekey7)

markup8 = telebot.types.InlineKeyboardMarkup()
inlinekey8 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s231sas.storage.yandex.net/rdisk/d23486df37d743de4165f59f6600f122be82932cd70639533b71ddbd5716c30c/5de26434/W7tUHT7IOW_m438xu3moqjbLzMS3hpgIVuUTjRApGkpJ2-u4Q4zc-VJkZGluWYSSZwXfNcxXb6i0BwH8L-7okw==?uid=0&filename=1%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5.mp4&disposition=attachment&hash=KHts1VM4knVIkhCBCVyeNROr0Q016APkJ9jxIIkNSDE%3D%3A/%D0%A3%D1%80%D0%BE%D0%BA%201%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/1%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5.mp4&limit=0&content_type=video%2Fmp4&owner_uid=156363096&fsize=151105952&hid=3a55b8630df0396174d2daef0858316d&media_type=video&tknv=v2&rtoken=i5Gsbtf6QNi9&force_default=no&ycrid=na-122e8a0147072c6e22c66c98f49e212e-downloader18h&ts=5988fb57a7500&s=6854e05dc2a3ffd8d9dc0d6b1e9db25743467e7fd8e86c92e4a0216634d90bdf&pb=U2FsdGVkX18T9NM3R994a36ALBU2lRGriqQBkIKsFmt1kS2P-a4GHR354Lh72I60Yk4RsjZp3rbjb9w5Yhtbv_cZ84GvzRO0vgaqjBeUC0E')
markup8.add(inlinekey8)

markup9 = telebot.types.InlineKeyboardMarkup()
inlinekey9 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wyw')
markup9.add(inlinekey9)

markup10 = telebot.types.InlineKeyboardMarkup()
inlinekey10 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wyx')
markup10.add(inlinekey10)

markup11 = telebot.types.InlineKeyboardMarkup()
inlinekey11 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://psv4.userapi.com/c856228/u64851044/docs/d3/35e0dcbecd6a/Kak_motivirovat_sebya.pdf?extra=0R3fv9kbUc4J12ycVIpnoWS9TTtF22-4bnKzMhEFLBqI_O0xmkVuur2cf96kWFJpwAE20lFIkQBVRePxHl_PPi7_mIfMsnIzvXesnHon9m29WDwJXrwwOUGl_72LZiSy8x-7x7SrbpEsA7RCVRy6Hg&dl=1')
markup11.add(inlinekey11)

markup12 = telebot.types.InlineKeyboardMarkup()
inlinekey12 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s473sas.storage.yandex.net/rdisk/577f976a14e8bc55eefb62321067f23859fab7c7b782e94bb18bd058a3a8d79d/5de26493/2UCa1r0kdpJav96fD2gVvMJlIeIub_2TMe21TD7moDLH-fg8WmGU0BAakfOBcTXjJmZojfWdhTGz329tHN9xEw==?uid=0&filename=%5BInfosklad.org%5D%20%D0%A1%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D1%8B%20%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F.%20%D0%9C%D0%B0%D0%B3%D0%B8%D1%8F%20%D1%81%D0%BB%D0%BE%D0%B2%20-%20%D0%94%D0%B6%D0%B5%D0%B9%D0%BC%D1%81%20%D0%91%D0%BE%D1%80%D0%B3.rar&disposition=attachment&hash=CeEa9zcQqU4PzBFPzm1KFG6NrtsdMjbvb3XuYYtuE8Y%3D%3A%2F%5BInfosklad.org%5D%20%D0%A1%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D1%8B%20%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F.%20%D0%9C%D0%B0%D0%B3%D0%B8%D1%8F%20%D1%81%D0%BB%D0%BE%D0%B2%20-%20%D0%94%D0%B6%D0%B5%D0%B9%D0%BC%D1%81%20%D0%91%D0%BE%D1%80%D0%B3.rar&limit=0&content_type=application%2Fx-rar&owner_uid=430390144&fsize=2347920&hid=e6c87382f907c5f31e3a536eb9628a3a&media_type=compressed&tknv=v2&rtoken=GJhqRivLUTRq&force_default=no&ycrid=na-6d43ba0d1b30ca66e1d573f71593961c-downloader18f&ts=5988fbb240ac0&s=e1cd97afb912ee575eeacfeb2f0fdcc8f1acc50171fac3c2c36f2656800395ed&pb=U2FsdGVkX1_oJmWE3rfg6e2qvtFgcKyZiWM5RJQXXOhbZWh2joVto-b4HkD0j05MpQIhn8vS132uLTJww130gfPvEvx-yZFolWs-l5DBDF0')
markup12.add(inlinekey12)

markup13 = telebot.types.InlineKeyboardMarkup()
inlinekey13 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s142vla.storage.yandex.net/rdisk/1917673ed08a7018de86da9b9ec3f304ace34c5bcac6c0409a9bde3bc7ba8054/5de25ccc/SDjyGN7tNo3FzQf1lCCNyQ-JRX08SLiokQ16F1XuEmoJWFRbndFWNUiAvBbwk9hfbKA-TzGMSonfVzPQWDE0jg==?uid=0&filename=%5Bslivysklad.com%5D%20%231%20-%20%D0%97%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE%20%D1%81%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%BE%D0%B9%20TKinter.mp4&disposition=attachment&hash=6ZLrOEEZQdQpFMNZl62B2O2%2BIFKSYL6/z3DYgZdYRB5MvOvr1VbTmIjurvJ7nqh9q/J6bpmRyOJonT3VoXnDag%3D%3D%3A/%5Bslivysklad.com%5D%20%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0%20TKinter/%5Bslivysklad.com%5D%20%231%20-%20%D0%97%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE%20%D1%81%20%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%BE%D0%B9%20TKinter.mp4&limit=0&content_type=video%2Fmp4&owner_uid=651445697&fsize=146495168&hid=ed5282e70d15d3f3abe13bfd95042bfa&media_type=video&tknv=v2&rtoken=CqZlyUHpe1Vs&force_default=no&ycrid=na-d87bd56443829fdeb69ed0b3fed38e35-downloader5f&ts=5988f4477cb00&s=afef7aa2c57e29a99f1eee8cc47e1153e8da58fdbd8d7fa85d2d6eb7929b00b5&pb=U2FsdGVkX1-AJQe2PZcI-y2wwJ5s0VzJ_zr_3w2-13KD-HNW0aQwUZyBHF1Cwvz3B03pdjKX82N8Sbfy6cwuvEqlsUmf6Jbb2Rq874LiUL4')
markup13.add(inlinekey13)

markup14 = telebot.types.InlineKeyboardMarkup()
inlinekey14 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo1.cldmail.ru/2buR5k5UsGxLt3gSnaGK/G/2fyM/s7t5wibDv/%5Bsharewood.biz%5D%20JavaScript.%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D0%B5%20%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9%20%D0%B2%D0%B5%D0%B1-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%282019%29.part1.rar?key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2&key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2')
markup14.add(inlinekey14)

markup15 = telebot.types.InlineKeyboardMarkup()
inlinekey15 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo20.datacloudmail.ru/zip/296uXvjQenQTDALaVNxkiSorxzJxJQt4xLSbvfHYrpSj2NMTSw9twtPTFM73A4iL6SnEVxH1DbxGtaNH/01%20Introduction%20and%20Setup.zip?key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2&key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2')
markup15.add(inlinekey15)

markup16 = telebot.types.InlineKeyboardMarkup()
inlinekey16 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo2.datacloudmail.ru/zip/MeJhrsmgDgnxSxTUjbnx6BDjGhmQsuWkhVZuUx8XHatgawLkXr2rmysqdBqRbFHc3aNsXhDVwF5CJqc/%D0%91%D0%BE%D0%BD%D1%83%D1%81%201.%20%D0%9F%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D1%8B%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.zip?key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2&key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2')
markup16.add(inlinekey16)

markup17 = telebot.types.InlineKeyboardMarkup()
inlinekey17 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo5.cldmail.ru/2aUbSexD78yo5VCm8jqX/G/JUe1/5NPS2jDca/%5Bsupersliv.biz%5D%201-1%D0%A1%20%D0%9F%D1%80%D0%B5%D0%B4%D0%BF%D1%80%D0%B8%D1%8F%D1%82%D0%B8%D0%B5%208.3.%20%D0%9F%D0%B5%D1%80%D0%B2%D1%8B%D0%B5%20%D1%88%D0%B0%D0%B3%D0%B8%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0/1-1%D0%A1%20%D0%9F%D1%80%D0%B5%D0%B4%D0%BF%D1%80%D0%B8%D1%8F%D1%82%D0%B8%D0%B5%208.3.%20%D0%9F%D0%B5%D1%80%D0%B2%D1%8B%D0%B5%20%D1%88%D0%B0%D0%B3%D0%B8%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0.part1.rar?key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2&key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2')
markup17.add(inlinekey17)

markup18 = telebot.types.InlineKeyboardMarkup()
inlinekey18 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s470sas.storage.yandex.net/rdisk/167db985e500c6da20f0ad520119b76638da05d2ff7f7aabe06aca0bfe969b5f/5de25d09/uLJuegx1NoJ-3pL_E-jKa1ZlJ6qetRyKzd6ppMC4ItQkHGDfmAMWc7_Iuie_ZPkdn0FREdVvw2yCHxMQZk4PtA==?uid=0&filename=%5BInfosklad.org%5D%202016%20%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5.rar&disposition=attachment&hash=b0KV6dEXzFgDNXyVOA6nidLyuhC9f9KKvzpcMK/V2Hc%3D&limit=0&content_type=application%2Fx-rar&owner_uid=540352966&fsize=3677813582&hid=cea9f97ab6d810a754882eb7731f1959&media_type=compressed&tknv=v2&rtoken=i3wkApku64dP&force_default=no&ycrid=na-ae8052b68c50ccd28dbfec8e436924c8-downloader10e&ts=5988f481a9440&s=e3e51bb08604eca118e0185f339b0c20203613d24b8db24f91888c982ad02ba1&pb=U2FsdGVkX1-e4u7IPMtPdD1_E3vtMaZ59Cez2IxSeSiggwBz7LNm2J--PzPeuXupQNwp9uA22FVvZEIeIoNsP4RXWOPF0j-J3Xce8fq3Pos')
markup18.add(inlinekey18)

markup19 = telebot.types.InlineKeyboardMarkup()
inlinekey19 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo23.datacloudmail.ru/zip/qwyawc93XQzJCPyYdEdnJ1qh3uxkCyzDWocxXuJRUS2MFFtrJrn6CghgSuKjku48BJoJqDGouvrFjbh/%231%20-%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D1%8F%D0%B7%D1%8B%D0%BA%20C%23.%20%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%B2%D1%81%D0%B5%D0%B3%D0%BE%20%D0%BD%D0%B5%D0%BE%D0%B1%D1%85%D0%BE%D0%B4%D0%B8%D0%BC%D0%BE%D0%B3%D0%BE.zip?key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2&key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2')
markup19.add(inlinekey19)

markup20 = telebot.types.InlineKeyboardMarkup()
inlinekey20 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s267iva.storage.yandex.net/rdisk/3699751cff91b9a4dc0452cf6fcd4e4cea12194eb9000b0951124aacd8643135/5de25d2c/iYfkVu7jsbeWdp4CzDtGwnPKaScYIgY2FC7vZUX0oRN7KilMwU_sdgKmBpxHSzh78B5yQp3YksgZVz31CY2u3g==?uid=0&filename=Lesson_01.mp4&disposition=attachment&hash=%2BugvhPnQRcT6mzh4MGnQJC0ZftoKleZeE7f2sGI/QKs%3D%3A/PHP%20Laravel/lesson_1/Lesson_01.mp4&limit=0&content_type=video%2Fmp4&owner_uid=568619793&fsize=335008769&hid=25e1ece05f4f89ad62ea01630bcb0d5e&media_type=video&tknv=v2&rtoken=H8zSD5g6LG1Q&force_default=no&ycrid=na-724888b8ffaa5e9a6964345a2134e1e8-downloader21f&ts=5988f4a30a300&s=004b00bce641f8a084943e41e70a52f7f801d673dbd345f398c61fc7aea31656&pb=U2FsdGVkX1-rj6I4rotUFj5b7t4drvJHIo_0_-EFsiZ62VEWYxzDt7U2yt7i1_3Hy121WDP1ix6_F0y6yjR3Y1C7LL2YT2WS3Vz5yMVYIEE')
markup20.add(inlinekey20)

markup21 = telebot.types.InlineKeyboardMarkup()
inlinekey21 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo21.datacloudmail.ru/zip/2UYRAeeEd7Q9zbDaEMWbCGkC7oQXsSuXGjFEbvM1SyDaVcR5A5dsvhgrkPumvP43jGZf62LmJHmBeaEX/1.zip?key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2&key=174b9b31913a296ba92cff7f812f7ab78ec7c8e2')
markup21.add(inlinekey21)

markup22 = telebot.types.InlineKeyboardMarkup()
inlinekey22 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s204i.storage.yandex.net/rdisk/087a9e5187f9c8a4a98d2d4ac05bd6cd10be36315b799ab8e67359d935028347/5de25d83/XXgrKoy155FMY1lPFRiFPOUouIyXcias0gIvdFnDg4zeH5kJOm5clHl56vvHApi3RQjhxTGDlFxhYH-rESqbLw==?uid=0&filename=001%20%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B5%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0.mp4&disposition=attachment&hash=X2TOphpqUGaJsPLjGy0oFW9b/7laILchkxF23Y%2B7pNvUeUkh0Xm4rYodMTq2XuBPq/J6bpmRyOJonT3VoXnDag%3D%3D%3A/%5B%40slivytg%5D%2001%20%D0%9F%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%BA%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B5/001%20%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%20%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B5%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0.mp4&limit=0&content_type=video%2Fmp4&owner_uid=774604460&fsize=99245740&hid=efdb6f5a59d84b8cd2ef0b4ea072b988&media_type=video&tknv=v2&rtoken=KNKUeRqIKzXf&force_default=no&ycrid=na-e76a2c64c8b736a02b7e1752cfdfb9fd-downloader22e&ts=5988f4f6026c0&s=617f47d91b0ff24e9c92f05387e7d2971f763906b265a00211c8b14822f9e376&pb=U2FsdGVkX1-F12e_UM5gUEdwZ74pnLbJBgS_iOjqKwiXqVwmaTdCGxnz22nlI7BaxfXsn5S-vzBSnyAAzpVWoHTEDc6tFbRuBNrG2NlmnbU')
markup22.add(inlinekey22)

markup23 = telebot.types.InlineKeyboardMarkup()
inlinekey23 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s191myt.storage.yandex.net/rdisk/03dd6f90bf8e26d7d14e0a3f9a8044239ee34f5f9f997fed929a62218005dcc6/5de25d54/nLVAUnMWUbchWFcRkueNN2j35BKf81GWIz5QM-GCgRCE_p0a2ESyfwVApJoQnp6sHIlhtaFCCtlanDcl5sJfhw==?uid=0&filename=%5BInfosklad.org%5D%201.%20%D0%90%20%D0%B2%D1%8B%20%D1%82%D0%BE%D1%87%D0%BD%D0%BE%20%D1%83%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D1%8B%2C%20%D1%87%D1%82%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%B0%D1%88%D0%B5%20%D0%BF%D1%80%D0%B8%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.mp4&disposition=attachment&hash=iGh%2BRVcxNFHUajd7pBH0d8ifi5WOBFgDO6MCZhmbi/M%3D%3A/%5BInfosklad.org%5D%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/%5BInfosklad.org%5D%201.%20%D0%90%20%D0%B2%D1%8B%20%D1%82%D0%BE%D1%87%D0%BD%D0%BE%20%D1%83%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D1%8B%2C%20%D1%87%D1%82%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%8D%D1%82%D0%BE%20%D0%B2%D0%B0%D1%88%D0%B5%20%D0%BF%D1%80%D0%B8%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.mp4&limit=0&content_type=video%2Fmp4&owner_uid=614602731&fsize=58013775&hid=d00c714c269bdeed544f7e578c3b2b5f&media_type=video&tknv=v2&rtoken=UIC85H6LNQgE&force_default=no&ycrid=na-a5ed58c3d86a45288ba31501fd07376a-downloader5f&ts=5988f4c92fd00&s=7eaa43775c33ea733a0244cbb510da0bba6a15a99ce262261b244f63c1579f02&pb=U2FsdGVkX1_BGcOCvuPdxycyR0j3wwo1_i-cO5h8HiSbslLSU3moeXvIw40Rw9ut-QW1wVDsrlGz94SeljpVdMios-4LyqzVdg_n4CgJvMw')
markup23.add(inlinekey23)

markup24 = telebot.types.InlineKeyboardMarkup()
inlinekey24 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wz8')
markup24.add(inlinekey24)

markup25 = telebot.types.InlineKeyboardMarkup()
inlinekey25 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wz9')
markup25.add(inlinekey25)

markup26 = telebot.types.InlineKeyboardMarkup()
inlinekey26 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wza')
markup26.add(inlinekey26)

markup27 = telebot.types.InlineKeyboardMarkup()
inlinekey27 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s187vla.storage.yandex.net/rdisk/1bf0aa6c7f3be8bd7fd1dd0cf2d4b09d8537ce6bfbb79f853d2d2b1450c0a860/5de264da/LA4fDMcIr0YP5dfNQ-1q8dAhEDMGjDf6YWllfU5Pfx2cRBXlnIFoDIDJRSob0XiZDKBK-f_kwp-ixoEdJsqp6A==?uid=0&filename=%5BInfosklad.org%5D%201.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5.mp4&disposition=attachment&hash=vhJxjXuHz8g6wvg3vqn7WtLkv0bX8sIqO1V9/nZnxC8%3D%3A/%5BInfosklad.org%5D%201.%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5.mp4&limit=0&content_type=video%2Fmp4&owner_uid=678116424&fsize=93971854&hid=3d0170c49820f0f6138e5de20a89d614&media_type=video&tknv=v2&rtoken=d7iSLhmYoSU0&force_default=no&ycrid=na-70cf693ba3dd477ac225a3e8cfb4789b-downloader14e&ts=5988fbf5f6a80&s=b785393caf424e5281789f736ceba8cf8b0eba46f64d0025708ad69557e40a7b&pb=U2FsdGVkX1-916FFO1vrwTHSdU5XeGCOOK5KpZw2cBRHKwzJN3a4bZ1Fk2ltkeYbDHIsCE4lZikywn0Afyp7SnDbkvm5cveGi5-wwJN3Vbg')
markup27.add(inlinekey27)

markup28 = telebot.types.InlineKeyboardMarkup()
inlinekey28 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/n9wzd')
markup28.add(inlinekey28)

markup29 = telebot.types.InlineKeyboardMarkup()
inlinekey29 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wzf')
markup29.add(inlinekey2)

markup30 = telebot.types.InlineKeyboardMarkup()
inlinekey30 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s159man.storage.yandex.net/rdisk/2cb493fdd9c33b1650e8f0018030583024540af8f2bda76b717a323b25fed450/5de25dfe/7YOVLxR3psCRX8y9dCKdgNGiz_CASK2n1RRggANZ4-6dJfahNNlLgpNskwtmdF7s40_mjYhBghDSsopQjT3f1A==?uid=0&filename=%D0%90%D0%BD%D0%B0%D1%82%D0%BE%D0%BC%D0%B8%D1%8F%D0%A1%D0%B8%D0%BB%D0%BE%D0%B2%D1%8B%D1%85%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%BD%D0%B8%D0%B9.pdf&disposition=attachment&hash=tcj46k%2B1m3kBetRgsf2RXnaI7RD66f6%2B4/HwrmKGmuo%3D&limit=0&content_type=application%2Fpdf&owner_uid=232423554&fsize=78081007&hid=eb5092c0151e066ea0deb36e4debda33&media_type=document&tknv=v2&rtoken=JR8nxa5xxlys&force_default=no&ycrid=na-36d839058d72a0667c1986c063aaa234-downloader2f&ts=5988f56b4fb80&s=83028d705dac140b886b69160c1c5ebe01d5135ea6e440d00373d49fdf3aab29&pb=U2FsdGVkX19okj46PPePk8kMKNb3tTqZ-iAFtAkX88LdSfrqdpP4XEVboWULBWxxzfbVJM92FBb0rmDIt9bFMYO87GRNOOGte6erqzKvW84')
markup30.add(inlinekey30)

markup31 = telebot.types.InlineKeyboardMarkup()
inlinekey31 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s205sas.storage.yandex.net/rdisk/663151b10d9dfd315273a8ae764ba0291860771352b55e394c6e5241a140b681/5de25e9d/hSlkR1KSBPWJAJF0fAAZREeC3k7LOWdDAu3EIywL0f3BZ9hctNj4BEDTqcC4mouzOwpDIZhy94h_IH59ry7XlQ==?uid=0&filename=%5BInfosklad.org%5D%20hdr-photoshop-actions.rar&disposition=attachment&hash=kvzkNuZ54crnqFoLkgDeQYZ1JxDE1Y4BY384GvOnV7g%3D&limit=0&content_type=application%2Fx-rar&owner_uid=581292648&fsize=7386&hid=20a59063aac748976434c0b11248d0ca&media_type=compressed&tknv=v2&rtoken=VvzkAvPoZbIy&force_default=no&ycrid=na-3266f0d0436dc89cf94e1721453e737d-downloader18h&ts=5988f602f2140&s=4373c420e02b0a8e6baa539c708a86bdc516ee183049b6a2ac7f6df7cf58bdb3&pb=U2FsdGVkX1-83DkIpT79zqyrSXnjTBYPFaxyvdHDHltI-Y2s9XZKYeyfLNMAEruoyO3mmqT28lW8Ahjjo2416DZnUgOjXFJujhdX3zEC4S8')
markup31.add(inlinekey31)

markup32 = telebot.types.InlineKeyboardMarkup()
inlinekey32 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s307sas.storage.yandex.net/rdisk/0d2b37cb4ee9abdf2dc741bbc252734096c430c086a7b426423e6575982e79c1/5de25ee8/QnvCiksl5IVeYSLvoPDf94EKaIO6VTetfCFOLs6nX9mXfNWbDiFzvMvPVI4Mucnc1Lgg57YoXGKdCqTwHgbsbA==?uid=0&filename=%5BInfosklad.org%5D%20SoPainted.Photoshop.Action.zip&disposition=attachment&hash=zOGMrpGCMugjKLLj7FyLsJ8gM7g9PnUFYYuRIn63ook%3D&limit=0&content_type=application%2Fzip&owner_uid=681534599&fsize=79063974&hid=526011c679f0be076be7a9ee0bffc192&media_type=compressed&tknv=v2&rtoken=YNTmFTmydKoP&force_default=no&ycrid=na-dfe3053fa5c97a06c8f9865b7fbbcfc0-downloader6f&ts=5988f64a78a00&s=7ff97daf6df6de61cf1e1a617fecb639662cd6a04895c8f2772ea9f2c3fe6e8c&pb=U2FsdGVkX1_X8_PgV9rFCgO1YTs7pFR3ANPcpxx7ATmOrLxvLqfX0gKCrXHuLbTYbMNcK0wSwWCWB8C2Mgq9zHOFAuMEzAIFR_jzKjqQ5kg')
markup32.add(inlinekey32)

markup33 = telebot.types.InlineKeyboardMarkup()
inlinekey33 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s144vla.storage.yandex.net/rdisk/7fa4f8c75757502f326f90812c425c940acf1d4a6a6a39f8816cb7edcd727da5/5de25efc/vJbOvaR8GbZNR7yyp0U9DgLdJtg5DBomFzElarR5w66EZRu8Vibfh46ckYSQQ1cnAryKoI6V_RKzpststCZgeQ==?uid=0&filename=%5BInfosklad.org%5D%20Dark_Action_I.zip&disposition=attachment&hash=s5GdNhjgGgC4l3xciZF57eEpBx9%2BxQbljSWSmI5HwJ0%3D&limit=0&content_type=application%2Fzip&owner_uid=684338110&fsize=127718&hid=c2faaf07a19e5647cb6f7349393329fb&media_type=compressed&tknv=v2&rtoken=1OjOMPRsDMn4&force_default=no&ycrid=na-148121ed43ca5d9c096219aad2d157d6-downloader13e&ts=5988f65d8b700&s=299fc82d9507046654eadfa1cd7c2d570ad7725c940476d82d8e18820d36728f&pb=U2FsdGVkX19X0v0P4kzCzkxBlIyRYS3HMgNFXqwihxx4wGsJPSJgSj1kNh6A9rxDiA0vf8U8TWldJ8GxIR2ERRAKDqlPmy9LL68ILoAHh6Q')
markup33.add(inlinekey33)

markup34 = telebot.types.InlineKeyboardMarkup()
inlinekey34 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s241sas.storage.yandex.net/rdisk/a73911ea096ff57b404007277ab1f8d6029ba4c29f4e5bd59a5d7696d43b6c99/5de25f49/NesbyHk8QkH_o2O5DMUcHznwCaf22HcgP4rl3Md0sVge24ZLWBQTQmjaQfg7PohhzII4hWG5kh5dQwjO1Vg_bg==?uid=0&filename=%5BInfosklad.org%5D%20poster-painting-photoshop-action.zip&disposition=attachment&hash=%2BymHI/yHmVUVK1%2B0oOs8HEgAkNIr1Jfo8OQjRV8p3E8%3D&limit=0&content_type=application%2Fzip&owner_uid=678818984&fsize=94274&hid=5556ba69352beaa0293a93a31b8bc562&media_type=compressed&tknv=v2&rtoken=NtkV2tN05Yeq&force_default=no&ycrid=na-2b1739139997a7153c810d43caf7d7a0-downloader12h&ts=5988f6a6fa440&s=0625fe91384b57645a343d79d7851ea575b009e93294c6312ce5f4b0807d8de1&pb=U2FsdGVkX18VYaEVKpl5i8V5GwO6WlWEmr_n7X-buErj2Zf9pW7dnfv9V8geyXqk3M6kZsI5eOsUT1KzhUE_mzWs9x4gDllv5029FfGk3pY')
markup34.add(inlinekey34)

markup35 = telebot.types.InlineKeyboardMarkup()
inlinekey35 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo22.datacloudmail.ru/zip/mNQ8cRYNcqJXZAsgxa48eKcdtBhHnuKd4VEzGHiaaWwDxSLjpkdvLxqhoDo2Mb3Q4eYdq3gHsFvjXYz/1.%20%D0%91%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9%20%D1%81%D1%82%D0%B0%D1%80%D1%82.zip?key=d8decdc1780486057ce38f968eea99e9fed11c17&key=d8decdc1780486057ce38f968eea99e9fed11c17')
markup35.add(inlinekey35)

markup36 = telebot.types.InlineKeyboardMarkup()
inlinekey36 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo23.cldmail.ru/27DhA1oE4Zc3wicL7Xd4/G/9upP/oNrqBWed7/%5Bslivysklad.com%5D%201%20%D1%83%D1%80%D0%BE%D0%BA/%5Bslivysklad.com%5D%201%20%D1%87%D0%B0%D1%81%D1%82%D1%8C.mp4?key=d8decdc1780486057ce38f968eea99e9fed11c17&key=d8decdc1780486057ce38f968eea99e9fed11c17')
markup36.add(inlinekey36)

markup37 = telebot.types.InlineKeyboardMarkup()
inlinekey37 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/g9wzr')
markup37.add(inlinekey37)

markup38 = telebot.types.InlineKeyboardMarkup()
inlinekey38 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s429sas.storage.yandex.net/rdisk/92504cc4056d02a247e08dfe901e0fcf55bed3404651cd7087685b2d6f71fc61/5de26397/6b9X2bXHutMwDbgt296whdd6Nc-8RIQ4gS9T_Sf7QccLZUgDyVYqXVzWALoXymrrc-MwGNUVO83KA_gWn5NtPA==?uid=0&filename=%5BInfosklad.org%5D%20universal_comic_book_effect_photoshop_action.rar&disposition=attachment&hash=/tcyBqvG3sMWQx%2B3fEextjoMN1m6fqztyCHytYIqT4g%3D&limit=0&content_type=application%2Fx-rar&owner_uid=540384171&fsize=9984721&hid=436771af0fafb9389486d1ba9b82ffb2&media_type=compressed&tknv=v2&rtoken=wpmW5HM3Rwfs&force_default=no&ycrid=na-306fbe6d018a5b19489447529138aab3-downloader3f&ts=5988fac1ed3c0&s=e667ab3115273c9944ca3dbc14d9af96c210339349e1a52a44e176f73a821323&pb=U2FsdGVkX18twwVj3L7YdN9VDUgQUjqY_qUsOmOQKvJc0j9AGZNwhYH0gkc3pjCmzY7C8AfRUyf-8qOk-aH9zNNhsMLRRak275qWWboZdGQ')
markup38.add(inlinekey38)

markup39 = telebot.types.InlineKeyboardMarkup()
inlinekey39 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wzj')
markup39.add(inlinekey39)

markup40 = telebot.types.InlineKeyboardMarkup()
inlinekey40 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://cloclo15.cldmail.ru/H8YiKnNFMHStVQwvHMH/G/CocY/5zddU3adp/%5BInfosklad.org%5D%20diz.vk.part01.rar?key=d8decdc1780486057ce38f968eea99e9fed11c17&key=d8decdc1780486057ce38f968eea99e9fed11c17')
markup40.add(inlinekey40)

markup41 = telebot.types.InlineKeyboardMarkup()
inlinekey41 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://rocld.com/m9wz')
markup41.add(inlinekey41)

markup42 = telebot.types.InlineKeyboardMarkup()
inlinekey42 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://psv4.userapi.com/c856324/u266946354/docs/d8/8b2a026a9a35/Oganyan_Zh_L_-_Express_-_kurs_angliyskogo_yazyka_-_2016.pdf?extra=3K6Ltzgd5FDGObSFuhuRES-FHOwKF2VFxDQKEeOlaFA9Q6l83RK3hFbdL9ejGtn1252b4kuKBvgFRhVdebNskrAmVA-HiBi7y60JeBs2i-00_PUxGXGRRExfx4CpJoqYKFK_Psm5uNK3Q8IM8X7ecFE&dl=1')
markup42.add(inlinekey42)

markup43 = telebot.types.InlineKeyboardMarkup()
inlinekey43 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s306man.storage.yandex.net/rdisk/82ad2ef88d09d21d1635b6790be63726be269bbec2edae12054f573e90405a84/5de25b94/c43Y1Zx9xnD3BO3vyHd8wcH5xH7Towd0bzLPO8p-ypSeDR3o9JCNorYsHs0CT6yxS0LpdegimQYFiMuE1fzvzQ==?uid=0&filename=%D0%A1%D0%B0%D0%BC%D0%BE%D1%83%D1%87%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%20%D0%B8%D1%81%D0%BF%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0.%20Don%20Manual._%D0%A5%D0%B5%D1%81%D1%83%D1%81%20%D0%92%D0%B8%D1%81%D0%B5%D0%BD%D1%82%D0%B5_2012%20-153%D1%81.doc&disposition=attachment&hash=r0enNQdqvv6/WTzsMGYWYjA/D2W8fQhF7JtWLodCxGI%3D&limit=0&content_type=application%2Fmsword&owner_uid=400758827&fsize=8041984&hid=8a62886a0ef4f4a06e357077e472cea7&media_type=document&tknv=v2&rtoken=odLSWvpY4G8j&force_default=no&ycrid=na-e286053d815ee18d660756e0d35e2978-downloader7e&ts=5988f31df0d00&s=3ad10c26b5a15c9f8997350359a72ef71ac414331f5c1b537e9608758abec18c&pb=U2FsdGVkX1-GFTJ49i_7PnESNiSHGl47oj1JtHUbVZw3J0rL3vf2snOcWlp6MMtXrspt0maG28z_RCwt2VGcgJnpKpAx5T13eMOwpHrXmjU')
markup43.add(inlinekey43)

markup44 = telebot.types.InlineKeyboardMarkup()
inlinekey44 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://s30vla.storage.yandex.net/rdisk/8dc1f747e8c7a6da3173f2be01dc04388d903b4ffc2c26ed0ad45e898c464180/5de25e18/HkOmzIzOdVPz8fznTj6-t98cSzIhS0khNTOFQmY9RZDUcmugsOBxK21Fnd0AXD5CF--2_Etnrr8sMJuqQ1Hy5Q==?uid=0&filename=modern-french-grammar-lang-perez.rar&disposition=attachment&hash=i4YbajQdRXTBof9PB/4KjBuFfv6or2u4yH8wEoETdyfCq7ZvgtqdsAakfPgrPqi7q/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-rar&owner_uid=90552338&fsize=1606733&hid=5c2cdf327f96d879b23cc9264c935a65&media_type=compressed&tknv=v2&rtoken=G6GaN1TFFU01&force_default=no&ycrid=na-25e82d381fe2b8a77898d8a57b13eff7-downloader22h&ts=5988f5841b600&s=566ae6bbbbe3bb6ae350aab3d9cec4b893f0d97abf6cec43737e02c1a4163c90&pb=U2FsdGVkX18tRGsKXxVciGy9ihQj0eCpNZLlPjFK5MCUet9Y--yr8JBCXuXZR6E3zvXBExQIk49GvNp13rbw2vctnj2jCRI4fHN8GwtWtNs')
markup44.add(inlinekey44)

markup45 = telebot.types.InlineKeyboardMarkup()
inlinekey45 = telebot.types.InlineKeyboardButton(text='Скачать!', url='http://window.edu.ru/resource/665/19665/files/metod644.pdf')
markup45.add(inlinekey45)

markup46 = telebot.types.InlineKeyboardMarkup()
inlinekey46 = telebot.types.InlineKeyboardButton(text='Скачать!', url='http://www.abhidharma.ru/A/Ioga/Content/0013.pdf')
markup46.add(inlinekey46)

markup47 = telebot.types.InlineKeyboardMarkup()
inlinekey47 = telebot.types.InlineKeyboardButton(text='Скачать!', url='https://site-ok.ua/download/ashmanov.pdf')
markup47.add(inlinekey47)

# КОНЕЦ
bot.polling(none_stop=True, interval=0)
