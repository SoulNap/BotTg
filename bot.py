import pytube as pytube
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
import time
import requests
import config
from config import TOKEN
import urllib.request
import os
bot = telebot.TeleBot(config.TOKEN)


# Команда start, выводящая кнопки
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем объект InlineKeyboardMarkup для вывода кнопок
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки
    news_button = types.InlineKeyboardButton('Новостная лента', callback_data='news_feed')
    materials_button = types.InlineKeyboardButton('Материалы', callback_data='materials')
    philosophers_button = types.InlineKeyboardButton('Философы', callback_data='philosophers')

    # Добавляем кнопки в разметку
    markup.add(news_button, materials_button, philosophers_button)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'news_feed')
def handle_news_feed(callback_query):
    # создаем список новостей
    news_list = [
        {
            'title': 'Джон Локк',
            'text': 'Человек рождается свободным, но всюду скован цепями',
            'photo': 'https://www.cumhuriyet.com.tr/Archive/2022/8/29/122915965-ic5.jpg'
        },
        {
            'title': 'Карл Маркс',
            'text': 'Новая эра отличается от старой эры главным образом тем, что плеть начинает воображать, будто она гениальна.',
            'photo': 'https://eponym.ru/GaleryImages/JG5H0FS5QLSHJGP8QJVBNCYUQ.jpg'
        },
        {
            'title': 'Фридрих Ницше',
            'text': 'Жизнь без музыки — сплошная ошибка',
            'photo': 'https://sun6-20.userapi.com/s/v1/ig2/s5Y25p3rt0xRTS32lxnZUZA564Iv-gRF-MWCI1jUMQ0nMFnk9xR88OwtZn4nq8DvkXB1Zc5HiFQhp96__Ejzulvk.jpg?size=1272x1288&quality=95&crop=0,0,1272,1288&ava=1'
        },
        {
            'title': 'Рене Декарт',
            'text': 'И мы не заблуждаемся, доколе просто утверждаем, что это так кажется. ',
            'photo': 'https://avatars.mds.yandex.net/i?id=32f245b03c63575658e20306f50f98a10ae51d5f-8200828-images-thumbs&n=13'
        },
        {
            'title': 'Фрэнсис Бэкон',
            'text': 'Самое лучшее из всех доказательств есть опыт',
            'photo': 'https://avatars.mds.yandex.net/i?id=f5191c178d95aba49d8ccf0eec9cb96b6006bc07-8567399-images-thumbs&n=13'
        }
    ]

    # создаем список сообщений в виде новостной ленты
    news_feed = []
    for news in news_list:
        message = f"<b>{news['title']}</b>\n\n{news['text']}"
        if news['photo']:
            bot.send_photo(callback_query.message.chat.id, news['photo'], caption=message, parse_mode='HTML')
        else:
            bot.send_message(callback_query.message.chat.id, message, parse_mode='HTML')

    # отправляем список сообщений с новостной лентой
    for message in news_feed:
        bot.send_message(callback_query.message.chat.id, message, parse_mode='HTML')

# Обработка нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data =='philosophers':
        # Создаем объект InlineKeyboardMarkup для вывода кнопок
        markup = types.InlineKeyboardMarkup()

        # Создаем кнопки
        platon_button = types.InlineKeyboardButton('Платон', callback_data='platon')
        aristotel_button = types.InlineKeyboardButton('Аристотель', callback_data='aristotel')
        socrat_button = types.InlineKeyboardButton('Сократ', callback_data='socrat')
        # Добавляем кнопки в разметку
        markup.add(platon_button, aristotel_button, socrat_button)
        # Отправляем сообщение с кнопками
        bot.send_message(call.message.chat.id, 'Выберите философа, по которому хотите получить более подробную информацию:', reply_markup=markup)
    elif call.data == 'platon':
        photo_url = 'https://avatars.dzeninfra.ru/get-zen_doc/5375671/pub_619499fbaa94705cb302170a_6194a1fb8cfd647b4bd6c8ae/scale_1200'
        # Здесь можно заполнить текстовую информацию, которую хотите отправить пользователю
        text = 'Платон (427/428 до н. э. — 347 до н. э.) — древнегреческий философ, ' \
               'ученик Сократа и основатель Академии. Он известен как автор ряда диалогов,' \
               ' в которых он выражает свои взгляды на различные философские проблемы.'
        bot.send_photo(call.message.chat.id, photo_url)
        bot.send_message(call.message.chat.id, text)
    elif call.data == 'aristotel':
        photo_url = 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Aristotle_Altemps_Inv8575.jpg'
        # Здесь можно заполнить текстовую информацию, которую хотите отправить пользователю
        text = 'Аристотель (384 до н. э. — 322 до н. э.) — древнегреческий философ, ' \
               'ученик Платона и учитель Александра Македонского. ' \
               'Он является автором трудов по метафизике, этике, политике, физике, биологии и логике.'
        bot.send_photo(call.message.chat.id, photo_url)
        bot.send_message(call.message.chat.id, text)
    elif call.data == 'socrat':
        photo_url = 'https://interesnyefakty.org/wp-content/uploads/portret-sokrata.jpg'  # URL изображения
        # Здесь можно заполнить текстовую информацию, которую хотите отправить пользователю
        text = 'Сократ (469/470 до н. э. — 399 до н. э.) — древнегреческий философ, ' \
               'создатель западной философской традиции. Он является основателем ' \
               'софистики и сократического метода, который заключается в проведении диалога с целью выявления истины.'
        bot.send_photo(call.message.chat.id, photo_url)
        bot.send_message(call.message.chat.id, text)
    elif call.data =='materials':
        # Создаем объект InlineKeyboardMarkup для вывода кнопок
        markup = types.InlineKeyboardMarkup()
        # Создаем кнопки
        text_button = types.InlineKeyboardButton('Текст', callback_data='text')
        video_button = types.InlineKeyboardButton('Видео', callback_data='video')
        #audio_button = types.InlineKeyboardButton('', callback_data='audio')
        # Добавляем кнопки в разметку
        markup.add(text_button, video_button)
        # Отправляем сообщение с кнопками
        bot.send_message(call.message.chat.id, 'Выберите тип материала по философии:', reply_markup=markup)
    #текст-материал
    elif call.data == 'text':
        photo_url = 'https://absolutera.ru/uploads/photo/file/32660/upl_1638790525_215529_p57hk.jpg'
        # Здесь можно заполнить текстовую информацию, которую хотите отправить пользователю
        text = 'В философии идеальное и материальное являются двумя фундаментальными понятиями, ' \
               'которые помогают объяснить и понять мир и нашу жизнь в нем. Идеальное обычно ассоциируется с духовным, ' \
               'нематериальным и духовным миром. Представители этой философской концепции, такие как Платон, считали, что идеи или формы ' \
               '(как они их называли) являются реальными сущностями, которые существуют вне нашего мира вечных идей. Идеи считаются источник' \
               'ом всех вещей и нашего знания о них. С другой стороны, Гегель в своей философии развития считал идею высшим началом реальности,' \
               ' которая определяет развитие всего мира. Материальное, с другой стороны, связано с тем, что может быть воспринято через наши чувства,' \
               ' то есть с физическим миром. Представители этой философской концепции, такие как Демокрит, считали, что мир состоит из атомов и пустоты,' \
               ' и что все вещи могут быть объяснены на основе материальных причин и законов. В современной философии материальное считается реальностью,' \
               ' которая может быть объяснена и описана с помощью науки. Таким образом, идеальное и материальное являются двумя основными понятиями в философии, ' \
               'которые помогают объяснить мир. Представители идеалистической философии, такие как Платон и Гегель, считают, что идеи являются реальными сущностями,' \
               ' а материальный мир проистекает из них. Представители материалистической философии, такие как Демокрит, считают, что мир состоит из материальных вещей,' \
               ' которые могут быть объяснены на основе материальных причин и законов.'
        bot.send_photo(call.message.chat.id, photo_url)
        bot.send_message(call.message.chat.id, text)
    #видео-материал
    elif call.data == 'video':
        video_url = 'https://youtu.be/PP8Uf-CxxhU'
        youtube = pytube.YouTube(video_url)
        text='https://youtu.be/PP8Uf-CxxhU'
        video = youtube.streams.get_highest_resolution()
        bot.send_message(call.message.chat.id, text)
        bot.send_video(call.message.chat.id, video.url)



    # текст-аудио
    elif call.data == 'audio':
        # Здесь можно указать ссылку на аудио, которое хотите отправить пользователю
        audio_url = 'https://youtu.be/CT5ub18UkrE'
        bot.send_audio(call.message.chat.id, audio_url)

    # Отвечаем на нажатие кнопки, чтобы не подсвечивалась
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: True)
def dialog(message):
    # генерируем случайную тему из списка
    topic = random.choice(topics)
    message_text, reply_markup = get_dialog_message(topic)
    bot.send_message(message.chat.id, message_text, reply_markup=reply_markup)

# список философских тем
topics = [
    'Какой главный вопрос философи?',
    'Свобода и ответственность',
    'Человек и общество',
    'Древнегреческое представление о сознании',
    'Идеальное по Марксу',
    'Искусство и красота',
    'Религия и метафизика',
]
video_path = os.path.join(os.getcwd(), 'videos', 'video.mp4')
# функция, которая генерирует сообщение с кнопкой "Закончить диалог"
def get_dialog_message(topic):
    message_new = 'Спасибо за диалог! Если захочешь продолжить обсуждение, напиши мне еще раз, а для того, чтобы вернуть меню напишите команду "/start"'
    message = f'Давай поговорим о теме "{topic}". Что ты об этом думаешь? Для вызова меню используйте /start'
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Закончить диалог')
    return message, markup

# Запускаем бота
bot.polling(none_stop=True)