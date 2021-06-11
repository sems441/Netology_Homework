class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses =[]
        self.courses_in_progress = []
        self.grades = {}
        self.count_grades = 0

    def rate_lectors(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_attached:
                lecturer.courses_attached[course] += grade
            else:
                return
        else:
            return "Ошибка"

    def __str__(self):
        avg_score = 0
        learning = ""
        finish = ""
        for key, value in self.grades.items():
            avg_score += value
        avg_score = round (avg_score / self.count_grades, 2)
        for course in self.courses_in_progress:
            learning += course + " "
        for finised_courses in self.finished_courses:
            finish += finised_courses + " "
        # record = f"Имя: {self.name}\nФамилия {self.surname}\nСредняя оценка за домашние задания: {avg_score}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        record_1 = f"Имя: {self.name}\nФамилия {self.surname}\nСредняя оценка за домашние задания: {avg_score}"
        record_2 = f"\nКурсы в процессе изучения: {learning}"
        record_3 = f"\nЗавершенные курсы: {finish}"
        record = record_1 + record_2 + record_3
        return record
    
    def __lt__(self, other):
        if not isinstance (other, Student):
            print("Неверне сравнение")
            return
        avg_score = 0
        for key, value in self.grades.items():
            avg_score += value
        self.avg_score = round (avg_score / self.count_grades, 2)
        # print (self.avg_score, "->",  self.name)
        avg_score = 0
        for key, value in other.grades.items():
            avg_score += value
        other.avg_score = round (avg_score / other.count_grades, 2)
        # print(other.avg_score, "->", other.name)
        if self.avg_score > other.avg_score:
            return f"Оценка {self.name} больше оценки {other.name}"
        elif self.avg_score == other.avg_score:
            return f"{self.name} одинаковый средний бал  с {other.name}"
        else:
            return f"Оценка {self.name} меньше оценки {other.name}"
                

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = {}
        
    def __str__(self):
        avg_score = 0
        count = 0
        for key, value in self.courses_attached.items():
            avg_score += value
            count += 1
        avg_score = round (avg_score / count, 2)
        self.avg_score = f"Имя: {self.name}\nФамилия {self.surname}\nСредняя оценка лекции {avg_score}"
        return self.avg_score
    
    def __lt__(self, other):
        if not isinstance (other, Lecturer):
            print("Неверне сравнение")
            return
        avg_score = 0
        count = 0
        for key, value in self.courses_attached.items():
            avg_score += value
            count += 1
        self.avg_score = round (avg_score / count, 2)
        # print (self.avg_score, "->",  self.name)
        avg_score = 0
        count = 0
        for key, value in other.courses_attached.items():
            avg_score += value
            count += 1
        other.avg_score = round (avg_score / count, 2)
        # print(other.avg_score, "->", other.name)

        if self.avg_score > other.avg_score:
            return f"Оценка {self.name} больше оценки {other.name}"
        else:
            return f"Оценка {self.name} меньше оценки {other.name}"
        
        

class Reviewer (Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.count_grades += 1
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        record = f"Имя: {self.name}\nФамилия {self.surname}"
        return record


def avg_grade_course_students(name, course_name):
    total = 0
    count = 0
    for students in name:
        total += students.grades[course_name]
        count += 1
    total = total / count
    print (f"Средняя оценка студентов за курс {course_name} равна {total}")
        
def avg_grade_course_lectors(name, course_name):
    total = 0
    count = 0
    for lectors in name:
        total += lectors.courses_attached[course_name]
        count += 1
    total = total / count
    print (f"Средняя оценка лекторов за курс {course_name} равна {total}")


Ruoy_student = Student('Ruoy', 'Eman', 'male')
Ruoy_student.courses_in_progress += ['Python']
Jane_student = Student('Jane', 'Ebbot', 'female')
Jane_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(Ruoy_student, 'Python', 10)
cool_mentor.rate_hw(Ruoy_student, 'Python', 4)
cool_mentor.rate_hw(Jane_student, 'Python', 10)

Mike_lecture = Lecturer("Mike", "Mola")
Sem_lecture = Lecturer("Sem", "Cola")
Mike_lecture.courses_attached["Math"] = 0
Mike_lecture.courses_attached["Bio"] = 0
Sem_lecture.courses_attached["Math"] = 0
Sem_lecture.courses_attached["Bio"] = 0

Ruoy_student.courses_in_progress+=["Math"]
Ruoy_student.courses_in_progress+=["Bio"]
Ruoy_student.finished_courses += ["Chemestry"]


Ruoy_student.rate_lectors(Mike_lecture, "Math", 6)
Ruoy_student.rate_lectors(Mike_lecture, "Bio", 8)

Ruoy_student.rate_lectors(Sem_lecture, "Math", 4)
Ruoy_student.rate_lectors(Sem_lecture, "Bio", 6)

print(Ruoy_student.courses_in_progress)
print(Mike_lecture.courses_attached)
print(Ruoy_student.grades)

print("-" * 30)
jonh = Reviewer("Jonh", "Smith")
print(jonh)

print("-" * 30)
print(Mike_lecture)

print("-" * 30)
print(Ruoy_student)

print("-" * 30)
print(Mike_lecture > Sem_lecture)
print(Ruoy_student>Jane_student)

# задание №4
print("+" * 30)
all_students = [Ruoy_student, Jane_student]
avg_grade_course_students(all_students, 'Python')

all_lectors = [Mike_lecture, Sem_lecture]
avg_grade_course_lectors(all_lectors, "Bio")