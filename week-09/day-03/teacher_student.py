class Student:
    def learn(self):
        print(f"the student is actually learning")
    
    def question(self, teacher):
        teacher.giveAnswer()

class Teacher:
    def teach(self, student):
        student.learn()

    def giveAnswer(self):
        print(f"the teacher is answering a question")

student = Student()
teacher = Teacher()

student.question(teacher)
teacher.teach(student)


