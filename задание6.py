class Temperature:
    """
    Класс для хранения температуры в Цельсиях и получения в Фаренгейтах.
    """

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if isinstance(value, (int, float)):
            self._celsius = value
        else:
            print("Значение должно быть числом.")

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


# Пример использования
if __name__ == "__main__":
    temp = Temperature(20)
    print(f"Цельсий: {temp.celsius}")
    print(f"Фаренгейт: {temp.fahrenheit}")

    temp.celsius = 25
    print(f"Обновленная температура в Цельсиях: {temp.celsius}")
    print(f"Температура в Фаренгейтах: {temp.fahrenheit}")