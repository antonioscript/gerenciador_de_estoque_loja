import mysql.connector
import PySimpleGUI as sg

mydb = mysql.connector.connect (
	host = "localhost", 
	user = "seu_usuario",
	password = "sua_senha",
	database = "seu_banco"
)

#=================================================================
#Criando tema
sg.theme("Lightgrey1")
#DarkTeal, DarkTeal12, DarkBlue10, DarkBlue1, Lightgrey1

def inicial():
	layout = [
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("")],
		[sg.Text("Digite o Nome do Usuário", font='Courier 16')],
		[sg.Input(key = '-USUARIO-', size=30, font='Courier 14')],
		[sg.Text("Digite a Senha", font='Courier 16')],
		[sg.Input(key = '-SENHA-', size=30, font='Courier 14', password_char="*")],
		[sg.Button("Entrar",font='Courier 18', size=7), sg.Button("Sair",font='Courier 18', size=7) ],
]

#Janela
	window = sg.Window('Sistema de Gerenciamento de Estoque', layout, size=(700,500), element_justification='center'  )
	
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Sair':
		exit()
	elif event == "Entrar":
		usuario = values['-USUARIO-']
		senha = values['-SENHA-']
		if usuario == "seu_usuario" and senha == "sua_senha":
			window.close()
			front()
		else:
			inicial()
#====================================================================
#Função de Entrada Inicial
def front():
	layout = [
		[sg.Text("Seja Bem Vindo!", font='Courier 50')],
		[sg.Text("Escolha o Que Deseja Fazer", font='Courier 26')],
		[sg.Button("Cadastrar Produtos", key="cadastrar", font='Courier 18', size=30)],
		[sg.Button("Remover Produtos", key="remover" , font='Courier 18', size=30)],
		[sg.Button("Visualizar Produtos", key="visualizar", font='Courier 18', size=30)],
		[sg.Button("Sair", key="sair", font='Courier 18', size=30)],
]
	#Janela
	window = sg.Window('Sistema de Gerenciamento de Estoque', layout, size=(700,500), element_justification='center')
	
	#Execução
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'sair':
		exit()
	elif event == "cadastrar":
		window.close()
		pagina_cadastro()
	elif event == "remover":
		window.close()
		pagina_remover()
	elif event == "visualizar":
		window.close()
		pagina_visualizar()
	elif event == "calcular":
		window.close()
		pagina_quantidade()
	
#=====================Página de Cadastro===========================
def pagina_cadastro():
	
	layout = [
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("Digite o Código do Produto:", font='Courier 18', size=30)],
			[sg.Input(key = '-CODIGO-', size=60)],
			[sg.Text("Descrição do Produto:", font='Courier 18', size=30)],
			[sg.Input(key = '-DESCRICAO-', size=60)],
			[sg.Text("Digite a Quantidade do Produto:", font='Courier 18', size=30), sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],key='-VEZES-', size=4)],
			[sg.Text("")],
			[sg.Text(size=(40,1), font='Courier 18', justification='center', key='-OUTPUT-'), ],
			[sg.Button('Inserir', font='Courier 18', size=7),sg.Button('Voltar', font='Courier 18', size=7), sg.Button('Sair', font='Courier 18', size=7)],
]
	#Janela
	window = sg.Window('Sistema de Gerenciamento de Estoque', layout, size=(700,500), element_justification='center')

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == 'Inserir':
			nome = values['-CODIGO-']
			curso = values['-DESCRICAO-']
			vezes1 = values['-VEZES-' or 'dest']
			vezes = int(vezes1)
			mycursor = mydb.cursor()
			a = 0
			while (a < vezes):
				sql = "INSERT INTO produtos (codigo, descrição) VALUES (%s,%s)"
				val = (nome, curso)
				mycursor.execute(sql, val)
				mydb.commit()
				a = a + 1
				window['-OUTPUT-'].update('Dados inseridos!')
				window['-CODIGO-'].update('')
				window['-DESCRICAO-'].update('')
				window['-VEZES-'].update('')
			print("registro(s) inserido")
		elif event == 'Voltar':
			window.close()
			front()
#====================Página de Remoção===========================
def pagina_remover():
	
	layout = [
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("")],
			[sg.Text("Digite o ID do Produto que será Removido:", font='Courier 18', size=60)],
			[sg.Input(key = '-ID-', size=60),],
			[sg.Text("")],
			[sg.Text(size=(60,1), font='Courier 18', justification='center', key='-OUTPUT-'), ],
			[sg.Button('Remover', font='Courier 18', size=7),sg.Button('Voltar', font='Courier 18', size=7), sg.Button('Sair', font='Courier 18', size=7)]
]
	#Janela
	window = sg.Window('Sistema de Gerenciamento de Estoque', layout, size=(700,500), element_justification='center')

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == 'Remover':
			identificador = values['-ID-']
			mycursor = mydb.cursor()
			sql = "DELETE FROM produtos WHERE id = %s"
			mycursor.execute(sql,(identificador,))
			mydb.commit()
			window['-OUTPUT-'].update('Dados Removidos!')
			window['-ID-'].update("")
			print("registro(s) removidos!")
		elif event == 'Voltar':
			window.close()
			front()
#================Página de Visualização===========================
def pagina_visualizar():
	layout = [
		[sg.Text("Produtos Cadastrados",font='Courier 20', size=60)],
		[sg.Output(size=(60,10),font='Courier 18' )],
		[sg.Button("Visualizar", key="ver", font='Courier 18', size=10), sg.Button("Voltar", font='Courier 18', size=10)],
]
	window = sg.Window('Sistema de Gerenciamento de Estoque', layout,layout, size=(700,500), element_justification='center')
	
	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Sair':
			break
		elif event == 'ver':
			mycursor = mydb.cursor()
			mycursor.execute("SELECT * FROM produtos")
			myresult = mycursor.fetchall()
			print("ID / Código / Descrição")
			print()
			for row in myresult:
				print(row)
		elif event == 'Voltar':
			window.close()
			front()
			
inicial()
