import mysql.connector
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lerovisk@1112",
    database = "inf_usuario"
)
cursor = conexao.cursor()

print("Bem vindo! Realize seu cadastro abaixo.")
endereco = ""
numero = ""
idade = 0
cpf = ""
email = ""

while True:
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            print("Você não possui a idade mínima exigida.")
            break

        endereco = input("Digite seu endereço: ")
        numero = input("Digite seu numero de celular: ")
        email = input("Digite seu endereço de e-mail (exemplo123@gmail.com): ")
        cpf = input("Digite seu CPF: ")

        print("\nConfirme se seus dados estão corretos (Sim/Não): ")
        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Endereço: ", endereco)
        print("Número: ", numero)
        print("Email: ", email)
        print("CPF: ", cpf)

        resposta = input("S/N: ")
        if resposta.upper()  == "N":
            print("Preencha seus dados novamente.")
            continue
        if resposta.upper() == "S":
            print("Finalizando...")
            try:
                sql = "INSERT INTO dados (nome, idade, endereco, numero, email, cpf) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (nome, idade, endereco, numero, email, cpf)

                cursor.execute(sql, valores)
                conexao.commit()
                break

            except mysql.connector.IntegrityError as erro:
                if "email" or "cpf" in str(erro):
                    print("Já existe um usuário com esse cadastro")
            continue

    except ValueError:
        print("ERRO, tente novamente!")

cursor.close()
conexao.close()
