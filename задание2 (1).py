class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def list_students(self):
        print(f"Преподаватель: {self.name} по предмету: {self.subject}")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")


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

   
    s1 = Student("Маша", 101)
    s2 = Student("Петя", 102)

    s1.add_grade(8)
    s1.add_grade(9)

    s2.add_grade(7)
    s2.add_grade(6)

    teacher = Teacher("Петрова Анна", 35, "Математика")
    teacher.add_student(s1)
    teacher.add_student(s2)
    teacher.list_students()

    print("\nИнформация о студентах:")
    for student in teacher.students:
        student.display_info()
