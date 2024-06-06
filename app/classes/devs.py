class Dev():
    def __init__(self, id, nome, descricao, image, complemento):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.image = image
        self.complemento = complemento

heloisa = Dev(1, 'Heloisa Cabral', 'Software Engineer - DMS LOGISTIC', 'img/dev/dev-heloisa.png', 'complemento teste')
pedro = Dev(2, 'Pedro Coelho', 'Software Engineer - GT GROUP', 'img/dev/dev-pedro.png', 'complemento pedro')
gabriel = Dev(3, 'Gabriel Fernandes', 'Software Engineer - DMS LOGISTIC', 'img/dev/dev-gabriel.png', 'complemento gabriel ')

dev_list = (heloisa, pedro, gabriel)