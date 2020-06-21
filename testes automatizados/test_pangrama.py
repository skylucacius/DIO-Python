from unittest import TestCase
from pangrama import pangrama

# classe de teste sendo extensão de TestCase usando Arrange-Act-Assert
class PangramaTest(TestCase):
    def test_metodo_de_teste(self):
        # arrange
        frase = 'Zebras caolhas de Java querem mandar fax para moça gigante de New York'
        # act
        testaFrase = pangrama(frase)
        # assert
        self.assertTrue(testaFrase,'deu erro mano...')
