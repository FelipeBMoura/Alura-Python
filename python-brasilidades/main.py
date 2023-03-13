from cpf_cnpj import Documento
from validate_docbr import CNPJ


# cpf_um = Cpf("97686085015")#
# print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"

# cnpj = CNPJ()#
# print(cnpj.validate(exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
