from cgitb import text
import django.db
import os
import random
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import json
import sqlite3


materias = ["https://g1.globo.com/jornal-hoje/noticia/2016/07/dinamica-de-grupo-dicas-para-conseguir-uma-vaga-de-emprego.html","https://g1.globo.com/concursos-e-emprego/noticia/2013/07/veja-como-montar-um-curriculo-para-conseguir-o-primeiro-emprego.html","https://g1.globo.com/jornal-hoje/noticia/2016/06/curso-tecnico-e-opcao-para-entrar-no-mercado-de-trabalho-mais-rapido.html","https://g1.globo.com/jornal-hoje/noticia/2016/05/vagas-de-emprego-veja-dicas-para-conseguir-se-recolocar-no-mercado.html","https://g1.globo.com/sp/sao-carlos-regiao/noticia/2022/05/25/pats-anunciam-empregos-mas-empresas-nunca-te-chamam-veja-porque-vagas-nao-sao-preenchidas-e-dicas-para-ser-contratado.ghtml"]
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
	'''if JsonActive == True:
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
			json.dump(file_data, file, indent = 4)'''


def GetInfo(TelegramId):
	for row in cur.execute("SELECT * FROM G1oportunidades_user WHERE TelegramId = ?",(str(TelegramId),)):
		return row

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #registerUser(update.effective_user.id)
	await context.bot.send_message(chat_id=update.effective_chat.id, text=UsersDict["WelcomeMessage"])

async def NewUser(update: Update, context: ContextTypes.DEFAULT_TYPE):
	"""Starts the conversation and asks the user about their name"""
	nameToRegister = str(update.message.text)[9:]
	registerUser(nameToRegister, update.effective_user.id)
	await context.bot.send_message(chat_id=update.effective_chat.id, text="Registrado!")


async def AboutMe(update: Update, context: ContextTypes.DEFAULT_TYPE):
	print("About me entered")
	for row in cur.execute("SELECT * FROM G1oportunidades_user WHERE TelegramId = ?",(str(update.effective_chat.id),)):
		Message = ("Nome: %s\nTelegramId: %s\nExperiência Profissional: %s\nCidade de Interesse: %s\nPretensão Salarial: R$ %s.00\nÁrea de Interesse: %s\nCursos Extracurriculares: %s\nEscolaridade: %s"%(row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
		await context.bot.send_message(chat_id=update.effective_chat.id, text=Message)

async def Vaga(update: Update, context: ContextTypes.DEFAULT_TYPE):
	profile = GetInfo(update.effective_user.id)
	cur.execute("SELECT * FROM G1oportunidades_vaga")
	rows = cur.fetchall()
	if not rows:
		await update.message.reply_text("Não conseguimos encontrar uma vaga :(")
		return
	vaga = random.choice(rows)
	text = ("⚠Encontramos esta vaga em %s.\nSegue o link: %s"%(vaga[4],vaga[7]))
	await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def Materias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    materiaTeste = random.choice(materias)
    text = ("Confira essas dicas para se qualificar: \n%s"%materiaTeste)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def Empregado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Status alterado!")

async def Desempregado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Status alterado!")
    
if __name__ == '__main__':
	application = ApplicationBuilder().token(os.getenv('Token')).build()
	
	start_handler = CommandHandler('start', start)
	AboutMe_handler = CommandHandler('AboutMe',AboutMe)
	NewUser_handler = CommandHandler('NewUser', NewUser)
	Vaga_handler = CommandHandler('Vaga', Vaga)
	Materias_handler = CommandHandler('Materias',Materias)
	Empregado_handler = CommandHandler('Empregado',Empregado)
	Desempregado_handler = CommandHandler('Desempregado', Desempregado)
	application.add_handler(start_handler)
	application.add_handler(AboutMe_handler)
	application.add_handler(NewUser_handler)
	application.add_handler(Vaga_handler)
	application.add_handler(Materias_handler)
	application.add_handler(Empregado_handler)
	application.add_handler(Desempregado_handler)
	application.run_polling()