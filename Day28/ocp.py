class Greeter:
    def __init__(self, language):
        self.language = language

    def greet(self):
        if self.language == 'english':
           return 'Hello!'
        elif self.language == 'spanish':
           return '¡Hola!'
        elif self.language == 'french':
           return 'Bonjour!'
        else:
            return 'Language not supported.'