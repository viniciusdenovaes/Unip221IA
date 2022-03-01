# circular import para verificacao de tipos


class Classe:

    def __init__(self):
        self.coisa: str = None


    def __repr__(self):
        res = '\n'
        for field, value in self.__dict__.items():
            res += str(field) + ':\n\t' + str(value).replace('\n', '\n\t')
            res += '\n'
        res += '\n'
        return res


