from my_university.student import Student
from my_university.group import Group
from my_university.errors import GroupLimitError

gr = Group('PD1')
try:
    for i in range(11):
        gender = 'Male' if i % 2 == 0 else 'Female'
        student = Student(gender, 20 + i, f'Name{i+1}', f'Lastname{i+1}', f'AN{i+1}')
        gr.add_student(student)
except GroupLimitError as e:
    print(f'Помилка: {e} Поточна кількість студентів: {e.current_count}')

gr.group.clear()
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student), 'Метод поиска должен возвращать экземпляр'
gr.delete_student('Taylor')
print(gr)
gr.delete_student('Taylor')
assert gr.find_student('Jobs') == st1
