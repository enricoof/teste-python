import requests
import csv

header = {
    "Authorization": "Bearer live_2e54e1a0fb36149c851707bd2b51e8"
}

response = requests.get(
    "https://api.api-futebol.com.br/v1/campeonatos/10/tabela", 
    headers=header,
    timeout=60
)

data = response.json()
print(data)
with open('tabela_campeonato.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Time', 'Pontos'])

    for team in data:
        nome = team["time"]["nome_popular"]
        pontos = team["pontos"]
        
        writer.writerow([nome, pontos])

print("Dados exportados com sucesso para 'tabela_campeonato.csv'")