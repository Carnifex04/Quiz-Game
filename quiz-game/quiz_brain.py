class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.end_game = False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ").lower()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, q_answer):
        if u_answer == "exit":
            self.end_game = True
            self.question_number -= 1
            return
        elif u_answer != "true" and u_answer != "false":
            print("Enter a valid answer")
            self.question_number -= 1
            return
        elif u_answer == q_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You answered wrong :(")

        print(f"The correct answer was: {q_answer}")
        print(f"The current score: {self.score}/{self.question_number}\n")
