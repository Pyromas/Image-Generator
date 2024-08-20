import telebot
from config import TOKEN
from logic import Text2ImageAPI
from config import API_TOKEN, SECRET_KEY, TOKEN


bot = telebot.TeleBot(TOKEN)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.send_message(message, 'Please write your prompt and i generate an image')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text 
    api = Text2ImageAPI('', API_TOKEN, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]

    api.save_image(images, 'decoded_image.jpg')
   
    with open('decoded_image.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
        
bot.polling()
