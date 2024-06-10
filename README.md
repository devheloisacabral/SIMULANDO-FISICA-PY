# Simulando Física 🚀

Este repositório contém um simulador de lançamento oblíquo e vertical desenvolvido em Python com Pygame, utilizando Django na web com HTML, CSS e JavaScript. O foi projeto está dockerizado para facilitar a configuração e execução. 🐳

## Funcionalidades

- Simulação de lançamento oblíquo e vertical baseada em fórmulas da física.
- Interface gráfica utilizando Pygame para visualização da simulação.
- Interface web para interação com o simulador.

## Requisitos

- Docker
- Git

O arquivo `requirements.txt` está presente no projeto, não se preocupe com os outros requisitos. Quando executarem `docker-compose up --build`, o container está configurado para instalar automaticamente as dependências necessárias. Os usuários só precisam alterar o arquivo requirements.txt caso desejem adicionar novas dependências. Nesse caso, devem inserir as novas dependências no arquivo e executar `docker-compose up --build` para reconstruir o container com as novas dependências. 📦

## Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/devheloisacabral/SIMULANDO-FISICA-PY.git
```

2. Navegue até o diretório clonado:


3. Crie e ative um ambiente virtual (opcional, mas recomendado):

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```
Windows

```bash
python3 -m venv venv
cd venv/Scripts/activate
```

4. Execute o Docker Compose para construir e iniciar os containers:

```bash
docker-compose up --build
```

Acesse a interface web em [http://localhost:8000](http://localhost:8000) para interagir com o simulador. 🌐

## Como usar

1. Na interface web, escolha o tipo de lançamento (oblíquo ou vertical) e insira os parâmetros relevantes.
2. Clique em qualquer lugar da tela para executar a simulação.
3. Visualize o resultado da simulação na tela.
4. Repita conforme necessário, ajustando os parâmetros conforme desejado. 🔄

## Contribuição

Este projeto foi desenvolvido por [Heloisa Cabral](https://github.com/devheloisacabral), [Pedro Coelho](https://github.com/pedro-coelho1604) e [Gabriel Fernandes](https://github.com/GabrielFernandes05). Contribuições são bem-vindas! Sinta-se à vontade para abrir issues relatando problemas encontrados ou para enviar pull requests com melhorias. 🤝
