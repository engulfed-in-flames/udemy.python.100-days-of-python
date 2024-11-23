class Question:

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer


class QuizBrain:

    def __init__(self, question_list: list[Question]) -> None:
        self.score: int = 0
        self.question_index: int = 0
        self.question_list: list[Question] = question_list

    def still_has_questions(self) -> bool:
        return self.question_index < len(self.question_list)

    def next(self) -> None:
        self.question_index += 1

    def quiz(self) -> None:
        question_index = self.question_index
        question = self.question_list[question_index].text

        answer = input(f"Q.{question_index + 1}: {question} (True/False)?: ")
        self.check_answer(answer)

    def check_answer(self, answer: str) -> None:
        correct_answer = self.question_list[self.question_index].answer
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_index + 1}\n")
