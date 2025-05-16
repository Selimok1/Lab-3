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

if __name__ == "__main__":
    student = Student("Иван Иванов", 12345)
    student.add_grade(8)
    student.add_grade(9)
    student.display_info()
