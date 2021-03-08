from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


questionBank = []
for data in question_data:
    questionBank.append(Question(data["question"], data["correct_answer"]))

quiz = QuizBrain(questionBank)

while quiz.moreQuestions():

    quiz.printScore()
    question = quiz.nextQuestion()

print(f"You've completed the quiz with {quiz.score}/{quiz.questionNumber}")