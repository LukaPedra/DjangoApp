from cgitb import text
import django.db
import os
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters, ContextTypes
import json
import sqlite3

con = sqlite3.connect('/workspace/teste/db.sqlite3')
cur = con.cursor()
print("Conectado com sucesso ao sqlite")
JsonActive = False
UsersJSON = open("users.json")
UsersDict = json.load(UsersJSON)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
def registerUser(Nome, TelegramId, filename='users.json'):
	print(Nome)
	cur.execute("UPDATE G1oportunidades_user SET TelegramId = ? WHERE GloboId = ? ",(str(TelegramId), str(Nome)))
	con.commit()
	for row in cur.execute("SELECT * FROM G1oportunidades_user WHERE GloboId = ?",(str(Nome),)):
		print(row)
	if JsonActive == True:
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


def GetInfo(TelegramId):
	for row in cur.execute("SELECT * FROM G1oportunidades_user WHERE TelegramId = ?",(str(TelegramId))):
		return row

async def start(update: Update, context: CallbackContext):
    #registerUser(update.effective_user.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=UsersDict["WelcomeMessage"])

async def NewUser(update: Update, context: ContextTypes.DEFAULT_TYPE):
	"""Starts the conversation and asks the user about their name"""
	await update.message.reply_text(
		"Ótimo! Me manda o nome exatamente igual a como você inseriu no "
		"Formulário para eu registrar você no sistema"
	)
	nameToRegister = str(update.message.text)[9:]
	registerUser(nameToRegister, update.effective_user.id)
	await context.bot.send_message(chat_id=update.effective_chat.id, text="printed.")



async def AboutMe(update: Update, context: ContextTypes.DEFAULT_TYPE):
	print("About me entered")
	for row in cur.execute("SELECT * FROM G1oportunidades_user WHERE TelegramId = ?",(str(update.effective_chat.id),)):
		Message = ("Nome: %s\nTelegramId: %s\nExperiência Profissional: %s\nCidade de Interesse: %s\nPretensão Salarial: R$ %s.00\nÁrea de Interesse: %s\nCursos Extracurriculares: %s\nEscolaridade: %s"%(row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
		await context.bot.send_message(chat_id=update.effective_chat.id, text=Message)

if __name__ == '__main__':
	application = ApplicationBuilder().token('5425942873:AAFm-nzTWN_2yAA4ehvyGKD9-C9ozYOC49I').build()
	
	start_handler = CommandHandler('start', start)
	AboutMe_handler = CommandHandler('AboutMe',AboutMe)
	NewUser_handler = CommandHandler('NewUser', NewUser)
	application.add_handler(start_handler)
	application.add_handler(AboutMe_handler)
	application.add_handler(NewUser_handler)
	application.run_polling()