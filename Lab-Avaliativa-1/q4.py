
class Televisao:

    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.__volume = 0
        self.__canal = ''

    def aumentar_volume(self, valor: int) -> None:
        self.__volume += valor

    def diminuir_volume(self, valor: int) -> None:
        self.__volume -= valor

    def trocar_canal(self, canal: str) -> None:
        self.__canal = canal

    def current_state(self) -> None:
        print('#' * 20)
        print(f"Modelo: {self.modelo}")
        print(f"Volume: {self.__volume}, Canal: {self.__canal}")


class SmartTV(Televisao):

    def __init__(self, modelo: str, internet: bool) -> None:
        super().__init__(modelo)
        self.internet = internet

    def conectar_internet(self) -> None:
        self.internet = not self.internet

    def current_state(self) -> None:
        super().current_state()
        print(f"Internet: {self.internet}")


televisao = Televisao("LG")
televisao.aumentar_volume(70)
televisao.diminuir_volume(27)
televisao.trocar_canal("Canal #1")
televisao.current_state()

smart = SmartTV("Samsung", False)
smart.aumentar_volume(70)
smart.diminuir_volume(27)
smart.trocar_canal("Canal #1")
smart.conectar_internet()
smart.current_state()
