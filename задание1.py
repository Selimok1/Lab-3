class Student:
    """
    Класс для представления студента с именем, ID и оценками.
    """

    def __init__(self, name, student_id):
        """
        Инициализация объекта Student.
        :param name: Имя студента (строка).
        :param student_id: ID студента (строка или число).
        """
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """
        Добавляет оценку в список с проверкой диапазона 0-10.
        :param grade: Оценка (число).
        """
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Ошибка: Оценка должна быть в диапазоне 0-10.")

    def get_average(self):
        """
        Вычисляет средний балл.
        :return: Средний балл (число).
        """
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def display_info(self):
        """
        Выводит информацию о студенте.
        """
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")

if __name__ == "__main__":
    # Пример использования
    student = Student("Иван Иванов", 12345)
    student.add_grade(8)
    student.add_grade(9)
    student.display_info()