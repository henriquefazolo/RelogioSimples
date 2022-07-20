"""
hora = int(input("Digite a hora do dia: "))
if hora < 0:
  print("hora inválida. Deve ser um valor maior ou igual a 0")
elif hora < 24:
  print("Boa noite")
elif hora < 6:
  print("Boa madrugada")
elif hora < 12:
  print("Bom dia")
elif hora < 18:
  print("Boa tarde")
else:
  print("hora inválida, deve ser menor que 24")

"""
# Solução


class Relogio:
    def __init__(self, hora):
        """
        Retorna uma saudação conforme o valor inserido de 0 a 24.

        :param hora: Valor inteiro para hora.
        """
        self.hora = hora

    def saudacao(self):
        """

        :return: Retorna uma saudação conforme a hora informada.
        """
        if self.hora in range(0, 7):
            return 'Boa Madrugada'
        elif self.hora in range(7, 13):
            return 'Bom dia'
        elif self.hora in range(13, 19):
            return 'Boa tarde'
        elif self.hora in range(19, 24):
            return 'Boa noite'
        else:
            return 'Hora inválida. Deve ser um valor entre 0 e 23'


r = Relogio(0)

print(r.saudacao())
