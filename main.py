import telebot

bot = telebot.TeleBot('6989288490:AAHa1jf8OnsAA_qQtLVxKsSy4RCfVRXigaI')

store_1 = '*Репка*\nПосадил дед репку. Выросла репка большая-пребольшая.\nПошел дед репку рвать: тянет-потянет, вытянуть не может!\nПозвал дед бабку:бабка за дедку,дедка за репку — тянут-потянут, вытянуть не могут!\nПозвала бабка внучку:внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!\nПозвала внучка Жучку:Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!\nПозвала Жучка кошку: кошка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!\nПозвала кошка мышку: мышка за кошку, кошка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, — вытянули репку!'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуй! Хочешь расскажу сказку?\nКоманды:\n /story - Рассказать сказку\n /other - Прочитать еще сказки', parse_mode='Markdown')

@bot.message_handler(commands=['story'])
def story(message):
    bot.send_message(message.chat.id, store_1, parse_mode='Markdown')


@bot.message_handler(commands=['other'])
def ofher(message):
    bot.send_message(message.chat.id, '[Тут](https://nukadeti.ru/skazki/korotkie-skazki-na-noch) ты можешь прочитать еще другие сказки', parse_mode='Markdown')
    bot.stop_polling()

bot.infinity_polling()