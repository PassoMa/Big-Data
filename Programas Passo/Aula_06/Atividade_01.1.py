#Corrigido
nomes = ["Kevinlyn", "Karolayne", "Ryan", "Miguel", "Marcella"]
senhas = ["Keka14", "Karol10", "Ryan08", "Miguel03", "Marcella33"]

nome_usu = input("Informe o nome de usuário: ")
for i in range(len(nomes)):
    if nomes [i] == nome_usu:
        senha =input("Informe a senha: ")
        if senhas[i] == senha:
            resp = "Acesso Liberado"
        else:
            resp = "Senha não confere"
        break
    else:
        resp = "Usuario não Encontrado" 
print(resp)        
    