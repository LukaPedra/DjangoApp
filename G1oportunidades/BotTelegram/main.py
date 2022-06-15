from cgitb import text
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
import json

UsersJSON = open("users.json")
UsersDict = json.load(UsersJSON)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
def registerUser(TelegramId,filename='users.json'):
	with open(filename,'r+') as file:
		appendNewUser={
			"GloboId":"",
			"TelegramId":TelegramId,
			"Escolaridade":"",
			"ExperienciaProfissional":"",
			"CidadedeInteresse":"",
			"PretensaoSalarial":"",
			"AreasdeInteresse":"",
			"CursosExtracurriculares":""
		}
		# First we load existing data into a dict.
		file_data = json.load(file)
		for User in file_data["Users"]:
			if User['TelegramId'] == TelegramId:
				return
        # Join new_data with file_data inside emp_details
		file_data["Users"].append(appendNewUser)
		# Sets file's current position at offset.
		file.seek(0)
		# convert back to json.
		json.dump(file_data, file, indent = 4)


async def start(update: Update, context: CallbackContext):
    registerUser(update.effective_user.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=UsersDict["WelcomeMessage"])



async def AboutMe(update: Update, context: CallbackContext):
    for User in UsersDict['Users']:
        if User['TelegramId'] == update.effective_user.id:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=str(User))
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Não conseguimos encontrar informações sobre você :(")

if __name__ == '__main__':
    application = ApplicationBuilder().token('5425942873:AAFm-nzTWN_2yAA4ehvyGKD9-C9ozYOC49I').build()
    
    start_handler = CommandHandler('start', start)
    AboutMe_handler = CommandHandler('AboutMe',AboutMe)
    application.add_handler(start_handler)
    application.add_handler(AboutMe_handler)
    application.run_polling()