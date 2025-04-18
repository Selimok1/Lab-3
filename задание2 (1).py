class Person:
    """
    Базовый класс человека с атрибутами name и age.
    """

    def __init__(self, name, age):
        """
        Инициализация Person.
        :param name: Имя человека.
        :param age: Возраст человека.
        """
        self.name = name
        self.age = age


class Teacher(Person):
    """
    Класс преподавателя, наследует от Person.
    """

    def __init__(self, name, age, subject):
        """
        Инициализация преподавателя.
        :param name: Имя.
        :param age: Возраст.
        :param subject: Предмет, который преподает.
        """
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        """
        Добавляет студента в список.
        :param student: Объект Student.
        """
        self.students.append(student)

    def remove_student(self, student_id):
        """
        Удаляет студента по student_id.
        :param student_id: ID студента.
        """
        self.students = [s for s in self.students if s.student_id != student_id]

    def list_students(self):
        """
        Выводит список студентов.
        """
        print(f"Преподаватель: {self.name} по предмету: {self.subject}")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")


# Пример использования
if __name__ == "__main__":
    class Student:
        def __init__(self, name, student_id):
            self.name = name
            self.student_id = student_id
            self.grades = []

        def add_grade(self, grade):
            if 0 <= grade <= 10:
                self.grades.append(grade)
            else:
                print("Ошибка: Оценка должна быть в диапазоне 0-10.")

        def get_average(self):
            if self.grades:
                return sum(self.grades) / len(self.grades)
            return 0

        def display_info(self):
            print(f"Студент: {self.name}")
            print(f"ID: {self.student_id}")
            print(f"Оценки: {self.grades}")
            print(f"Средний балл: {self.get_average():.2f}")

    # Создаем студентов
    s1 = Student("Маша", 101)
    s2 = Student("Петя", 102)

    s1.add_grade(8)
    s1.add_grade(9)

    s2.add_grade(7)
    s2.add_grade(6)

    # Создаем преподавателя
    teacher = Teacher("Петрова Анна", 35, "Математика")
    # Добавляем студентов
    teacher.add_student(s1)
    teacher.add_student(s2)

    # Выводим список студентов
    teacher.list_students()

    # Информация о студентах
    print("\nИнформация о студентах:")
    for student in teacher.students:
        student.display_info()