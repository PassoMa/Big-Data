nomes = ["Kevinlyn", "Karolayne", "Ryan", "Miguel", "Marcella"]
senhas = ["Keka14", "Karol10", "Ryan08", "Miguel03", "Marcella33"]

nome_usu = input("Informe o nome de usuário: ")
for i in range(len(nomes)):
    if nomes [i] == nome_usu:
        resp = input("Informe a senha: ")
        break
    else:
        resp = "Usuario não Encontrado" 
for i in range(len(senhas)):
    if senhas [i] == resp:
        resp = "Senha correta"
        break
    else:
        resp =  "Senha incorreta"          
print(resp) 


