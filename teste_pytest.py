import requests


class TestCursos:
    headers = {'Authorization': 'Token 344450ffd7443c85b61340eb37443ffd82d626eb'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}6/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby",
            "url": "http://www.geekuniversity.com.br/cpr"
        }
        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby",
            "url": "http://www.geekuniversity.com.br/ncpr"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}9/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0

