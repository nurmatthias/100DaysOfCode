class QuizBrain:

    def __init__(self, qList):
        self.questionNumber = 0
        self.questionList = qList
        self.score = 0
    

    def nextQuestion(self):
        question = self.questionList[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber}: {question.text} (True/False): ")
        self.checkAnswer(answer, question.answer)


    def checkAnswer(self, user_answer, correct_aswer):
        if user_answer.lower() == correct_aswer.lower():
            print("Thats correct")
            self.score += 1
        else:
            print("nope, thats wrong")

    def printScore(self):
        print(f"Your actual score is {self.score}/{self.questionNumber}")

    def moreQuestions(self):
        return self.questionNumber < len(self.questionList)