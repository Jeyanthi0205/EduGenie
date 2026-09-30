from quiz_module import generate_quiz


topic = "Python programming basics"

quiz = generate_quiz(topic)

print("QUIZ TEST SUCCESSFUL!")
print()
print("Topic:")
print(quiz.topic)
print()

for number, question in enumerate(quiz.questions, start=1):
    print(f"Question {number}:")
    print(question.question)

    for index, option in enumerate(question.options):
        print(f"  {chr(65 + index)}. {option}")

    print(f"Answer: {question.answer}")
    print(f"Explanation: {question.explanation}")
    print()