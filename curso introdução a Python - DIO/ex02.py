class Televisao:
    def __init__(self):
        self.ligada = True
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
print(televisao.ligada)
