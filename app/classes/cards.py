class Card():
    def __init__(self, id, nome, descricao, image, complemento):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.image = image
        self.complemento = complemento


card3 = Card(3, 'Lançamento Vertical', 'teste3', 'img/teste.png', 'lh')
card4 = Card(4, 'Lançamento Oblíquo', 'teste4', 'img/teste.png', 'lo')


cards_list = (card3, card4)