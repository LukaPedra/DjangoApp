import json

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
 
    # python object to be appended

     
registerUser(55)
'''
usersJSON = open("users.json")
usersDict = json.load(usersJSON)

#Check if user is new or already exists in JSON
StartUser = 4444
if StartUser not in usersDict:
	appendNewUser={
		"GloboId":"",
		"TelegramId":StartUser,
		"Escolaridade":"",
		"ExperienciaProfissional":"",
		"CidadedeInteresse":"",
		"PretensaoSalarial":"",
		"AreasdeInteresse":"",
		"CursosExtracurriculares":""
	}
	usersDict["Users"].append(appendNewUser)
	usersJSON.seek(0)

	json.dump(usersDict,usersJSON,indent=4)'''