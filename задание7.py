class Student:
    """
    Класс для хранения информации о студенте.
    """
    def __init__(self, name):
        self.name = name

class Teacher:
    """
    Класс для хранения информации о преподавателе.
    """
    def __init__(self, subject):
        self.subject = subject

class Assistant(Student, Teacher):
    """
    Класс ассистент, наследует от Student и Teacher.
    """
    def __init__(self, name, subject):
        Student.__init__(self, name)
        Teacher.__init__(self, subject)

    def help_student(self):
        """
        Метод помощи студентам.
        """
        print(f"{self.name} помогает студентам по предмету {self.subject}.")

if __name__ == "__main__":
    assistant = Assistant("Иван", "Математика")
    print(f"Ассистент: {assistant.name}")
    print(f"Преподает предмет: {assistant.subject}")
    assistant.help_student()