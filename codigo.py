import mysql.connector
import PySimpleGUI as sg

mydb = mysql.connector.connect (
	host = "localhost", 
	user = "root",
	password = "1915691",
	database = "loja_sollaris2"
)

def inserir():
	mycursor = mydb.cursor()
	a = 0
	while (a < vezes):
		sql = "INSERT INTO produtos (codigo, descrição) VALUES (%s,%s)"
		val = (nome, curso)
		mycursor.execute(sql, val)
		mydb.commit()
		a = a + 1
	print("registro(s) inserido")


#=================================================================
#Criando tema
sg.theme("DarkPurple")

#Layout
layout = [
	[sg.Text("Digite o Código do Produto:")],
	[sg.Input(key = '-CODIGO-')],
	[sg.Text("Descrição do Produto:")],
	[sg.Input(key = '-DESCRICAO-')],
	[sg.Text("Digite a Quantidade do Produto:")],
	[sg.Input(key = '-VEZES-')],
	[sg.Text(size=(40,1), key='-OUTPUT-')],
	[sg.Button('Inserir'), sg.Button('Sair')]
]

#Janela
window = sg.Window('Loja Sollaris', layout)

while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Sair':
		break
	elif event == 'Inserir':
		nome = values['-CODIGO-']
		curso = values['-DESCRICAO-']
		vezes1 = values['-VEZES-']
		vezes = int(vezes1)
		inserir()
		window['-OUTPUT-'].update('Dados inseridos!')
window.close()
