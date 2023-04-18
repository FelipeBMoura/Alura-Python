import re

from telefonesBr import TelefonesBr

padrao = "[0-9][a-z][0-9]"  # padrão número letra número
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)

print(resposta)
print(resposta.group())

padra_email = "\w{5,50}@\w[a-z]{3,10}.\w{2,3}.\w{2,3}"

texto = "aaabbbccc rodrigo123@gmail.com.br ihgsufyufyf"

resposta = re.search(padra_email, texto)

print(resposta)
print(resposta.group())

padrao_molde = "(xx)aaaa-wwww"

padrao_telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

texto = "eu gosto do numero 2126451234 e gosto também do 2136431234"

resposta = re.search(padrao_telefone, texto)

print(resposta)
print(resposta.group())

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)

padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
resposta = re.search(padrao, telefone)
print(resposta)
print(resposta.group(2))

print(telefone_objeto)
