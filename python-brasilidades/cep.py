from acesso_cep import BuscaEndereco
import requests

cep = '01001000'

objeto_cep = BuscaEndereco(cep)

print(objeto_cep)

r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

print(r.text)

print(objeto_cep.acessa_via_cep())

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
