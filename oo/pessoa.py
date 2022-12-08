class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_calsse(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    pedro = Pessoa(renzo, nome='Pedro')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Gomes'
    del pedro.filhos
    pedro.olhos = 1
    del pedro.olhos
    print(pedro.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(pedro.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(pedro.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), pedro.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_calsse(), pedro.nome_e_atributos_de_calsse())