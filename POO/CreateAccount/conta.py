#Chegou a hora de criar a sua primeira classe, a classe Conta. Para tal, crie o arquivo conta.py e siga os passos abaixo:

#1 - Defina a classe, utilizando a palavra-chave class, e em seguida defina o seu nome.

#2 - Defina a função construtora da classe, recebendo uma referência do próprio objeto como argumento.

#3 - Receba também como argumento os valores dos atributos da classe, isto é, numero, titular, saldo e limite.

#4 - Através da referência do objeto, defina os atributos numero, titular, saldo e limite com os respectivos valores recebidos como argumento.

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite