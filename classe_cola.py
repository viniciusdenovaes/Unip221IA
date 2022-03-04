# circular import para verificacao de tipos


class Classe:

    def __init__(self, coisa: str, estruct: dict):
        self.coisa: str = coisa
        self.estruct: dict = estruct

    def __repr__(self):
        res = '\n'
        for field, value in self.__dict__.items():
            res += str(field) + ':\n\t' + str(value).replace('\n', '\n\t')
            res += '\n'
        res += '\n'
        return res


class Chave:

    def __init__(self, coisa: str):
        self.coisa: str = coisa

    def __hash__(self):
        return hash((self.coisa, ))

    def __eq__(self, o: 'Classe') -> bool:
        return (self.coisa, ) == (o.coisa, )

    def __repr__(self):
        res = '\n'
        for field, value in self.__dict__.items():
            res += str(field) + ':\n\t' + str(value).replace('\n', '\n\t')
            res += '\n'
        res += '\n'
        return res

if __name__ == '__main__':
    coisa: Classe = Classe('meu objeto', {1: 5, 'a': 9, 'coisa': 10})
    coisa2: Classe = Classe('meu objeto', {1: 5, 'a': 9, 'coisa': 11})

    chave1 = Chave('1')
    chave2 = Chave('2')
    chave3 = Chave('3')

    print({
        chave1: 1,
        chave2: 2,
        chave3: 3,
    })


