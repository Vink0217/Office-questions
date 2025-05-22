'''
Q18) Simple Quiz App 
Create a console-based quiz app with questions and multiple-choice answers. 
'''
questions = [
    {
        'question': 'Who is the current President of the USA?',
        'options': ['a) John F. Kennedy', 'b) George Bush', 'c) Donald Trump', 'd) None of the above'],
        'answer': 'c'
    },
    {
        'question': '''If a = 10 and b = 15, what is the output of the following code?
        c = a % b
        print(c)''',
        'options': ['a) 5', 'b) 10', 'c) 15', 'd) None of the above'],
        'answer': 'b'
    },
    {
        'question': 'What is the capital of France?',
        'options': ['a) Paris', 'b) London', 'c) Berlin', 'd) Madrid'],
        'answer': 'a'   
    },
    {
        'question': 'Which data type is used to store True or False values in Python?',
        'options': ['a) int', 'b) str', 'c) bool', 'd) float'],
        'answer': 'c'
    },
    {
        'question': 'What will be the output of: print(2 ** 3)?',
        'options': ['a) 6', 'b) 8', 'c) 9', 'd) None of the above'],
        'answer': 'b'
    }
]

result = 0
for question in questions:
    print("\n" + question['question'])
    for option in question['options']:
        print(option)
    user_answer = input('Enter your answer (a/b/c/d): ').strip().lower()

    if user_answer == question['answer']:
        result += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

print(f"\nYour final score is {result}/{len(questions)}")
