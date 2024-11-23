from classes import Question, QuizBrain
from data import question_data

if __name__ == "__main__":
    question_bank = [Question(question["text"], question["answer"]) for question in question_data]

    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.quiz()
        quiz_brain.next()

    total_score = quiz_brain.question_index
    user_score = quiz_brain.score
    print("You've completed the quiz.")
    print(f"Your final score was: {user_score}/{total_score}")

    # TODO: checking if the answer is correct
    # TODO: checking if we're at the end of the quiz
