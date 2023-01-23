import requests

headers = {'Authorization': 'Token 344450ffd7443c85b61340eb37443ffd82d626eb'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}8/', headers=headers)

# Testando código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0
