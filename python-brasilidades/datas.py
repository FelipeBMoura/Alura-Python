from datetime import datetime, timedelta
from datas_br import DatasBr


print(datetime.today())

cadastro = DatasBr()

print(cadastro.momento_cadastro)

print(cadastro.mes_cadastro())

print(cadastro.dia_da_semana())

hoje = datetime.today()

hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M:%S")

print(hoje_formatada)
print(type(hoje_formatada))
print(cadastro)

numero = 1
string = "um"

print(len(string))
# print(len(numero))

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1)

print(amanha-hoje)

hoje = DatasBr()

print(hoje.tempo_cadastro())
