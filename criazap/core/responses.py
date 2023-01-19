from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Olá, Sou seu Corretor Virtual, para iniciar a busca digite yep")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("Até mais!")

class OneResponse(GenericRandomResponse):
    choices = ("Qual seu endereço de e-mail?")

class TwoResponse(GenericRandomResponse):
    choices = ("Procura um Imóvel pronto ou na planta?")

class ThreeResponse(GenericRandomResponse):
    choices = ("O que é importante em um imóvel para você?")

class FourResponse(GenericRandomResponse):
    choices = ("Em qual cidade ?")

class FiveResponse(GenericRandomResponse):
    choices = ("Em qual região?")

class SixResponse(GenericRandomResponse):
    choices = ("Em que bairro ?")

class SevenResponse(GenericRandomResponse):
    choices = ("Está a quanto tempo procurando um imóvel?")

class FinalResponse(GenericRandomResponse):
    choices = ("OK! Bora continuar essa mensagem no WhatsApp!")

