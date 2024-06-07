class Tecnologia():
    def __init__(self, id, nome, imagem, descricao):
        self.id = id
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao


python = Tecnologia(1, "Python", 'img/tecnologias/python.png', "Python é uma linguagem de programação de alto nível, interpretada, conhecida por sua simplicidade e legibilidade.")
javascript = Tecnologia(2, "JavaScript", 'img/tecnologias/js.png', "JavaScript é uma linguagem de programação popular usada principalmente para construir aplicações web interativas.")
django = Tecnologia(3, "Django", 'img/tecnologias/django.png', "Django é um framework web de alto nível para Python que incentiva o desenvolvimento rápido e design limpo e pragmático.")
html = Tecnologia(4, "HTML", 'img/tecnologias/html.png', "HTML (Hypertext Markup Language) é a linguagem de marcação padrão para criar páginas da web e aplicações web.")
css = Tecnologia(5, "CSS", 'img/tecnologias/css.png', "CSS (Cascading Style Sheets) é uma linguagem de folha de estilo usada para descrever a apresentação de um documento escrito em HTML ou XML.")
docker = Tecnologia(6, "Docker", 'img/tecnologias/download.png', "Docker é uma plataforma para desenvolver, enviar e executar aplicativos em contêineres.")


lista_tecnologia = (django, docker,  python, javascript,  html, css, )
