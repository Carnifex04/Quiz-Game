from data import question_data as questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in questions:
    question_text = question["text"]
    question_answer = question["answer"]
    quiz_question = Question(question_text, question_answer)
    question_bank.append(quiz_question)

print("Welcome to the True/False Quiz...")
print("The rules are simple: You will be provided with a question, each having either True or False as its answer")
print("You can enter 'exit' to leave the quiz and get your final score")
print("Have Fun!!!\n")
quiz = QuizBrain(question_bank)
while quiz.still_has_question() and not quiz.end_game:
    quiz.next_question()
print("\nYou completed the quiz.")
print(f"Final score: {quiz.score}/{quiz.question_number}")
