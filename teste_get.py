import requests

headers = {'Authorization': 'Token 7af16ad81aa270528cf0f7a567a0d2c7b2788524'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

#print(resultado.json())

# Testando se o endpoint está correto

assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 6

# Testando o título do primeiro curso:
assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'


