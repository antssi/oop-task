import self as self


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade <= 10:
                if course in lecturer.grades_from_student:
                    lecturer.grades_from_student[course] += [grade]
                else:
                    lecturer.grades_from_student[course] = [grade]
            else:
                return 'Error'

    def average_grade(self):
        average_grade = []
        for values in self.grades.values():
            i = 0
            while i < len(values):
                average_grade.append(values[i])
                i += 1
        average_grade_total = round((sum(average_grade)) / len(average_grade), 1)
        return average_grade_total


    def __str__(self):
        res = f'Студент \n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {self.average_grade()} \n Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка! Сравнивать разрешается только студентов.")
            return
        res = f'Средний балл {self.name} хуже, чем у {other.name}? - {self.average_grade() < other.average_grade()}'
        return res

    def __le__(self, other):
        if not isinstance(other, Student):
            print("Ошибка! Сравнивать разрешается только студентов.")
            return
        res = f'Средний балл {self.name} хуже или такой же как у {other.name}? - {self.average_grade() <= other.average_grade()}'
        return res

def student_avg_grade_course(students, course):
    all_grades = []
    for student in students:
        for courses, grade in student.grades.items():
            if courses in course:
                i = 0
                while i < len(grade):
                    all_grades.append(grade[i])
                    i += 1
    avg_grade_course = sum(all_grades) / len(all_grades)
    res = f'Средний балл всех студентов на курсе {course} - {avg_grade_course}'
    return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_student = {}

    def average_rate(self):
        average_rate = []
        for values in self.grades_from_student.values():
            i = 0
            while i < len(values):
                average_rate.append(values[i])
                i += 1
        average_rating = round((sum(average_rate)) / len(average_rate) , 1)
        return average_rating

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка! Сравнивать разрешается только лекторов")
            return
        res = f'Средний балл {self.name} хуже, чем у {other.name}? - {self.average_rate() < other.average_rate()}'
        return res

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка! Сравнивать разрешается только лекторов")
            return
        res = f'Средний балл {self.name} хуже или такой же как у {other.name}? - {self.average_rate() <= other.average_rate()}'
        return res


    def __str__(self):
        res = f'Лектор \n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.average_rate()}'
        return res

def avg_grade_course(lecturers):
    all_grades = []
    for lecture in lecturers:
        for grade in lecture.grades_from_student.values():
            i = 0
            while i < len(grade):
                all_grades.append(grade[i])
                i += 1
    avg_grade_course = sum(all_grades) / len(all_grades)
    res = f'Средний балл всех лекторов - {avg_grade_course}'
    return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Проверяющий \n Имя: {self.name} \n Фамилия: {self.surname}'
        return res


first_student = Student('Vadim', 'Andronov', 'Male')
first_student.courses_in_progress += ['Python', 'Java', 'С++', 'PHP']
first_student.finished_courses += ['Основы программирования на Python', 'Английский язык для программистов', 'Базы данных']

second_student = Student('Anna', 'Ivanova', 'Female')
second_student.courses_in_progress += ['Python', 'Java', 'C++', 'Swift']
second_student.finished_courses += ['Основы программирования на Python', 'Английкий язык для программистов', 'Основы Java', 'Знакомство со Swift']

students_list = [first_student, second_student]

first_reviewer = Reviewer('Anton', 'Korskov')
first_reviewer.courses_attached += ['Python', 'Java', 'C++', 'PHP']

second_reviewer = Reviewer('Tim', 'Kolenko')
second_reviewer.courses_attached += ['Python', 'Java', 'C++', 'PHP']

first_lecturer = Lecturer('Dan', 'Izotov')
first_lecturer.courses_attached += ['Python', 'Java', 'C++', 'PHP', 'Swift']

second_lecturer = Lecturer('John', 'Zhukov')
second_lecturer.courses_attached += ['Python', 'Java', 'C++', 'PHP']

lecturer_list = [first_lecturer, second_lecturer]

#Оценки студентам
first_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Java', 6)
second_reviewer.rate_hw(first_student, 'C++', 8)
first_reviewer.rate_hw(first_student, 'PHP', 4)
first_reviewer.rate_hw(second_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Java', 6)
first_reviewer.rate_hw(second_student, 'C++', 10)

#Оценки лекторам
first_student.lecturer_grade(first_lecturer, 'Python', 9)
first_student.lecturer_grade(first_lecturer, 'Java', 6)
first_student.lecturer_grade(second_lecturer, 'C++', 4)
second_student.lecturer_grade(first_lecturer, 'Swift', 10)
second_student.lecturer_grade(second_lecturer, 'Java', 8)
second_student.lecturer_grade(second_lecturer, 'PHP', 10)

print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviewer)
print(second_reviewer)

print(student_avg_grade_course(students_list, 'Python'))
print(avg_grade_course(lecturer_list))


print(first_lecturer > second_lecturer)
print(first_lecturer >= second_lecturer)
print(first_student > second_student)
