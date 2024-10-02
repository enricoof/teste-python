# Raspagem de dados Campeonato Brasileiro

## Sobre
Este projeto é uma automação para a coleta de dados por Web Scraping no site do GE, no qual é extraído o nome do clube e os pontos, há também esses mesmos dados sendo coletados por uma API pública. A coleta de dados é feita em segundos.

### Funcionalidades
#### Web Scraping
- **DADOS COLETADOS:** Os dados coletados são adicionados ao arquivo "Classificação_brasileirao" com a extensão ".csv"
- **ELEMENTO A SER PESQUISADO:** O elemento a ser pesquisado é pela TAGNAME e pela propriedade INNERHTML para acessar o valor. E para os pontos, foi necessário ser acessado pelo CSS_SELECTOR e também acessadno a propriedade de INNERHTML para acessar o valor.
#### API
- **DADOS COLETADOS:** Os dados coletados são adicionados ao arquivo "tabela_campeonato" com a extensão ".csv"
- **ELEMENTO A SER PESQUISADO:** Os elementos a serem pesquisaddos são através da API, porém são coletados diversas estatísticas por essa API, então há um filtro para pegar somente os elementos de "nome" e de "pontos"

## Inicio

Passo a passo para rodar a aplicação

### Pré-Requisitos

É necessário ter instalado em seu computador:
- Python 3.12.6

### Instalação

Siga abaixo para a instalação do projeto:

1. Clone o repositório:
```bash
git clone https://github.com/enricoof/teste-python.git
```
2. Crie um Ambiente Virtual (venv) e ative:
```bash
Windows: python -m venv venv
         venv/scripts/activate

Linux/Mac: python3 -m venv venv
           source venv/bin/activate
```

3. Instale as dependências necessárias após ativar a venv:
```bash
pip install -r requirements.txt
```

### Dependências
```bash
attrs==24.2.0
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
h11==0.14.0
idna==3.10
numpy==2.1.1
outcome==1.3.0.post0
pandas==2.2.3
pycparser==2.22
PySocks==1.7.1
python-dateutil==2.9.0.post0
pytz==2024.2
requests==2.32.3
selenium==4.25.0
six==1.16.0
sniffio==1.3.1
sortedcontainers==2.4.0
trio==0.26.2
trio-websocket==0.11.1
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
websocket-client==1.8.0
wsproto==1.2.0
```

## Uso 
Após todos os passos, é só rodar o projeto!

## Contato
Meu nome é Enrico Folheni

Linked In - [Meu perfil!](www.linkedin.com/in/enrico-folheni)
