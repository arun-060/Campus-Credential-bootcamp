import sys

class Question:
    def __init__(self):
        self.question = []
        self.option_1 = []
        self.option_2 = []
        self.option_3 = []
        self.option_4 = []
        self.correct_answer = []
        self.countRightAns = 0
        self.countWrongAns = 0
        self.scorePerQues = 5
        self.totalScore = 0
        self.fullName = None
        self.studentId = None
        
    def addStudent(self):
        self.fullName = input("Enter name : ")
        self.studentId = int(input("Enter the student id : "))
        
    def addQuestion(self):
        question = input("Enter the question : ")
        op1 = input("Enter option 1 : ")
        op2 = input("Enter option 2 : ")
        op3 = input("Enter option 3 : ")
        op4 = input("Enter option 4 : ")
        
        self.question.append(question)
        self.option_1.append(op1)
        self.option_2.append(op2)
        self.option_3.append(op3)
        self.option_4.append(op4)
        
        correct_ans = input("Enter the correct answer : ")
        self.correct_answer.append(correct_ans)
    
    def askQuestionAndCheckAnswer(self):
        for i in range(len(self.question)):
            print("Question:",self.question[i])
            print("1:",self.option_1[i])
            print("2:",self.option_2[i])
            print("3:",self.option_3[i])
            print("4:",self.option_4[i])
            
            answer = None
            user_answer = int(input("Enter your answer from above options 1,2,3,4 : "))
            if user_answer == 1:
                answer = self.option_1[i]
            elif user_answer == 2:
                answer = self.option_2[i]
            elif user_answer == 3:
                answer = self.option_3[i]
            else:
                answer = self.option_1[i]
            
            if answer == self.correct_answer[i]:
                self.countRightAns += 1
            else:
                self.countWrongAns +=1
                
    def showResult(self):
        print("Student name: ", self.fullName)
        print("correct answers: ", self.countRightAns)
        print("wrong answers: ", self.countWrongAns)
        print("final score : ", self.countRightAns*self.scorePerQues)
    
if __name__ == "__main__":
    
    q = Question()
    while True:
        
        print("1.Add Student\n2.Add Question\n3.Take Test\n4.Show result\n5.Exit")
        ch = int(input("Enter your choice : "))
        if ch == 1:
            q.addStudent()
        elif ch == 2:
            q.addQuestion()
        elif ch == 3:
            q.askQuestionAndCheckAnswer()
        elif ch == 4:
            q.showResult()
        elif ch == 5:
            sys.exit()
        
    