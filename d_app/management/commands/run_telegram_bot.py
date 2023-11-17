from django.core.management.base import BaseCommand

import telebot
from d_app.models import Product
# from d_app.models import YourModel


bot = telebot.TeleBot("6572171052:AAHfjzVdwkCSJruqiQVecH92vc7x0kSgWZk")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        bot.send_message(message.chat.id, product.name)

# @bot.message_handler(commands=['pic'])
# def pics(message):
#     pics = YourModel.objects.all()
#     for pic in pics:
#         bot.send_message(message.chat.id, pic.image)
        


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")