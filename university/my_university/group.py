from .errors import GroupLimitError

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError("Не можна додати бiльше 10 студентiв!", len(self.group))
        self.group.add(student)
        print(f"Додано студента: {student}")

    def delete_student(self, last_name):
        for student in list(self.group):
            if student.last_name == last_name:
                self.group.remove(student)
                return

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'
