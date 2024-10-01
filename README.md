# Raspagem de dados Campeonato Brasileiro

## Sobre
Este projeto é uma automação para a coleta de dados por Web Scraping no site do GE, no qual é extraído o nome do clube e os pontos, há também esses mesmos dados sendo coletados por uma API pública. A coleta de dados é feita em segundos.

## Funcionalidades
### Web Scraping
- **DADOS COLETADOS:** Os dados coletados são adicionados ao arquivo "Classificação_brasileirao" com a extensão ".csv"
- **ELEMENTO A SER PESQUISADO:** O elemento a ser pesquisado é pela TAGNAME e pela propriedade INNERHTML para acessar o valor. E para os pontos, foi necessário ser acessado pelo CSS_SELECTOR e também acessadno a propriedade de INNERHTML para acessar o valor.
### API
- **DADOS COLETADOS:** Os dados coletados são adicionados ao arquivo "tabela_campeonato" com a extensão ".csv"
- **ELEMENTO A SER PESQUISADO:** Os elementos a serem pesquisaddos são através da API, porém são coletados diversas estatísticas por essa API, então há um filtro para pegar somente os elementos de "nome" e de "pontos"



É necessário instalar o webdriver, o pandas e requests para conseguir utilizar o código.
