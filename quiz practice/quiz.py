questions = {"Q1. What is your name?": "B",
             "Q2. How old are you?": "A",
             "Q3. Place of birth?": "D",
             "Q4. What do you like to play?": "C"
             }

options = [["A. Kwabena", "B. Julian", "C. Mariatu", "D. Francis"],
           ["A. 90", "B. 30", "C. 35", "D. 25"],
           ["A. Bo", "B. Kenema", "C. Makeni", "D. Freetown"],
           ["A. Tennis", "B. Cricket", "C. Football", "D. Basket ball"]
           ]
objectives = ["A", "B", "C", "D"]
total_questions = 0
total = 0
for question, answer in questions.items():
    print(question)
    for option in options[total_questions]:
        print(option, end=" ")
    print("\n")

    response = input("Answer: ")
    if response.upper() not in objectives:
        response = input("Enter A through D")
    total_questions += 1
    if response.upper() == answer:
        print("correct answer" + "\n")
        total += 1
    else:
        print("wrong answer" + "\n")
total = str(total)
total_questions = str(total_questions)
print(f"final score = {total}/{total_questions}")
