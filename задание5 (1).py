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

    def __str__(self):
        return f"Студент {self.name} (ID: {self.student_id})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades)


if __name__ == "__main__":
    s1 = Student("Аня", 1)
    s1.add_grade(9)
    s1.add_grade(10)
    print(s1)
    print(f"Количество оценок: {len(s1)}")
    s2 = Student("Боря", 2)
    s2.add_grade(8)
    print(s1 == s2)
