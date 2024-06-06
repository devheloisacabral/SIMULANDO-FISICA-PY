class Card():
    def __init__(self, id, nome, descricao, image, complemento):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.image = image
        self.complemento = complemento

card1 = Card(1, 'Movimento Uniforme', 'teste', 'img/teste.png', 'mu')
card2 = Card(2, 'M. Uniformemente Variado', 'teste2', 'img/teste.png', 'muv')
card3 = Card(3, 'Lançamento Horizontal', 'teste3', 'img/teste.png', 'lh')
card4 = Card(4, 'Lançamento Oblíquo', 'teste4', 'img/teste.png', 'lo')
card5 = Card(5, 'Movimento Circular', 'teste5', 'img/teste.png', 'mc')

cards_list = (card1, card2, card3, card4, card5)