import shutil
def write_file(text):
    directory = 'C:/Users/Naara Felix/PycharmProjects/test.txt'
    archive = open(directory, 'w')
    archive.write(text)
    archive.close()

def update_file(name_archive, text):
    archive = open(name_archive, 'a')
    archive.write(text)
    archive.close()

def read_archive(name_archive):
    archive = open(name_archive, 'r')
    text = archive.read()
    print(text)

def average_grades(name_archive):
    archive = open(name_archive, 'r')
    student_grade = archive.read()
    #print(student_grade)
    student_grade = student_grade.split('\n')
    #print(student_grade)
    lista_average = []
    for x in student_grade:
        lista_grades = x.split(',')
        student = lista_grades[0]
        lista_grades.pop(0)
        print(student)
        print(lista_grades)
        average = lambda grades: sum([int(i) for i in grades]) / 4
        print(average(lista_grades))
        lista_average.append({student: average(lista_grades)})
    return lista_average

def copy_archive(name_archive):
    shutil.copy(name_archive, 'C:/Users/Naara Felix/PycharmProjects/grades.student')

def move_archive(name_archive):
    shutil.move(name_archive, 'C:/Users/Naara Felix/PycharmProjects/')

if __name__ == '__main__':
    move_archive('test.txt')
    #copy_archive('grades.txt')
    #lista_average = average_grades('Grades.txt')
    #print(lista_average)
    #write_file('First line.\n')
    #student = 'Cesar, 7, 8, 5, 6\n'
    #update_file('Grades.txt', student)
    #update_file('Third line.\n')
    #read_archive('test.txt')
