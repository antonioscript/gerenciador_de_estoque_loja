import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost", 
	user = "root",
	password = "sua_senha",
	database = "seu_banco"
)
mycursor = mydb.cursor()


#Função Inserir
def inserir():
	a = 0
	codigo = int(input("Digite o Código do Produto: "))
	descricao = input("Descrição do Produto: ")
	vezes = int(input("Digite a quantida do Produto: "))
	while (a < vezes):
		sql = "INSERT INTO produtos (codigo, descrição) VALUES (%s,%s)"
		val = (codigo, descricao)
		mycursor.execute(sql, val)
		mydb.commit()
		a = a + 1		
	print("Registros inseridos!")
	print("-" * 50)
	print()
	apresentacao()

#Função Remover
def remover():
	codigo1 = input("Digite o ID do Produto Que Será Removido: ")
	sql = "DELETE FROM produtos WHERE id = %s"
	mycursor.execute(sql,(codigo1,))
	mydb.commit()
	print(mycursor.rowcount, "registro(s) deletado")
	print()
	apresentacao()
	
#Função Mostrar Quantidade do Produto
def quantidade():
	codigo2 = input("Digite o Código do Produto: ")
	sql = "SELECT * FROM produtos WHERE codigo = %s"
	mycursor.execute(sql,(codigo2,))

	myresult = mycursor.fetchall()
	
	print("Quantidade de Produtos: ", mycursor.rowcount)
	print("-"*50)
	print()
	apresentacao()

#Função Tabela (Mostra Tudo)
def tabela():
	mycursor.execute("SELECT * FROM produtos")
	myresult = mycursor.fetchall()

	for x in myresult:
		print(x)
	print()
	apresentacao()

#Função de Apresentação Inicial
def apresentacao():
	print("============CONTROLE DE ESTOQUE=============")
	print("Digite: ")
	print("[1] - Adcionar Mercadoria")
	print("[2] - Remover Mercadoria")
	print("[3] - Mostrar Quantidade de um Produto")
	print("[4] - Mostrar todo o estoque")
	print("[5] - Sair")
	entrada = int(input("Digite uma opção: "))
	if entrada == 1:
		inserir()
	elif entrada == 2:
		remover()
	elif entrada == 3:
		quantidade()
	elif entrada == 4:
		tabela()
	elif entrada == 5:
		exit()
	else:
		print("ATENÇÃO!")
		print("Comando Inválido! Tente novamente")
		print()
		apresentacao()

#Programa começa aqui
apresentacao()

