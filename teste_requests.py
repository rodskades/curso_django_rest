import requests

# GET Avaliações
# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando os resultados desta página
# print(avaliacoes.json()['results'])

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando somente o nome da pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')

# print(avaliacao.json())

# GET Cursos
headers = {'Authorization': 'Token 7af16ad81aa270528cf0f7a567a0d2c7b2788524'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
