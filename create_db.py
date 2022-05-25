import json
from quiz_pkg.models import *
from quiz_pkg.print_to_term import print_success

# TODO Rename to Models?

db = SqliteDatabase('quiz_app.db')


def create_tables():
    db.connect()
    db.create_tables([User, Category, Question, Answer])


"""
DB Seeding
"""


def seed_database():
    # Create Category
    category = Category.create(name="Python")

    # Load the JSON file containing questions and answers
    json_file = open("questions_answers.json")
    questions_answers = json.load(json_file)

    # Iterative over the Questions and Answers to seed the tables
    for question_answer in questions_answers:
        question = Question.create(
            category=category,
            question=question_answer["question"].strip()
        )
        for answer in question_answer['answers']:
            Answer.create(
                question=question,
                text=answer["text"].strip(),
                is_correct=bool(answer["is_correct"])
            )


if __name__ == '__main__':
    create_tables()
    seed_database()

    print_success("SUCCESS!", "The database has been created! Please run [bold]quizapp.py[/bold] to play!")
