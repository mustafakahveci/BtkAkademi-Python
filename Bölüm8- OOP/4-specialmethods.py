import random

class Question:
    def __init__(self,text,options,answer):
        self.text = text
        self.options = options
        self.answer = answer

    def checkUserAnswer(self,userAnswer):
        return self.answer == userAnswer
    
q1 = Question('en iyi programalama dili hangisidir ? ',['Python','Javascript','JAVA','C#'],"Python")
q2 = Question('en popüler programalama dili hangisidir ? ',['JAVA','Javascript','Python','C#'],"Python")
q3 = Question('en çok kazandıran programalama dili hangisidir ? ',['C#','Javascript','JAVA','Python'],"Python")
q4 = Question('en çok sevilen programalama dili hangisidir ? ',['Python','JAVA','Javascript','C#'],"Python")
q5 = Question('en kolay programalama dili hangisidir ? ',['Python','Javascript','C#','JAVA'],"Python")
questions_list = [q1,q2,q3,q4,q5]

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0 

    def viewQuiz(self): 

        for index,question in enumerate(self.questions):
            print(f"Soru {index+1} : " + question.text)
            for index,item in enumerate(question.options):
                print("- "+item)
            answer = input("cevabınız : ")
            if(question.checkUserAnswer(answer)):
                self.score += 1
        print(f"Skorunuz : {self.score}")
            
quiz = Quiz(random.choice(questions_list) for i in range(2)) #rastgele 2 sorulu quiz oluşturduk.
quiz.viewQuiz()