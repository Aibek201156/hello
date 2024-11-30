import telebot

# Укажите токен вашего бота
TOKEN = "7709268116:AAFDeoJxsEra7UrHnhdtvjMuKZRH-iQt24Y"
bot = telebot.TeleBot(TOKEN)

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    bot.reply_to(message, "Hello, World!")

# Запуск бота
print("Бот запущен. Нажмите Ctrl+C для остановки.")
bot.infinity_polling()
