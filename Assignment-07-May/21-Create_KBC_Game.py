# Q21.Create Your Own KBC Game
# Design and implement a quiz game inspired by the popular Kaun Banega Crorepati (KBC)
# game show. The aim of this assignment is to test the user's knowledge through a series of
# multiple-choice questions, track their score, and display statistics at the end of the game. The
# game also provides the flexibility to skip any question.

# KBC Quiz Game

score = 0
correct = 0
wrong = 0
skipped = 0

start = input("Do you want to start the KBC Game? (yes/no): ")

if start.lower() == "yes":

    # Question 1
    print("\nQuestion 1 for 1000 points")
    print("What is the capital of India?")
    print("A. Mumbai")
    print("B. Delhi")
    print("C. Kolkata")
    print("D. Chennai")

    ans = input("Enter your answer (A/B/C/D) or type skip: ")

    if ans.lower() == "skip":
        skipped += 1

    elif ans.upper() == "B":
        print("Correct Answer")
        score += 1000
        correct += 1

    else:
        print("Wrong Answer")
        wrong += 1


    # Question 2
    print("\nQuestion 2 for 2000 points")
    print("Which language is used for Python programming?")
    print("A. Hindi")
    print("B. Java")
    print("C. English")
    print("D. Python")

    ans = input("Enter your answer (A/B/C/D) or type skip: ")

    if ans.lower() == "skip":
        skipped += 1

    elif ans.upper() == "D":
        print("Correct Answer")
        score += 2000
        correct += 1

    else:
        print("Wrong Answer")
        wrong += 1


    # Question 3
    print("\nQuestion 3 for 3000 points")
    print("Which planet is known as the Red Planet?")
    print("A. Mars")
    print("B. Earth")
    print("C. Venus")
    print("D. Jupiter")

    ans = input("Enter your answer (A/B/C/D) or type skip: ")

    if ans.lower() == "skip":
        skipped += 1

    elif ans.upper() == "A":
        print("Correct Answer")
        score += 3000
        correct += 1

    else:
        print("Wrong Answer")
        wrong += 1


    # Question 4
    print("\nQuestion 4 for 5000 points")
    print("Who is known as the Father of Computer?")
    print("A. Newton")
    print("B. Charles Babbage")
    print("C. Einstein")
    print("D. Tesla")

    ans = input("Enter your answer (A/B/C/D) or type skip: ")

    if ans.lower() == "skip":
        skipped += 1

    elif ans.upper() == "B":
        print("Correct Answer")
        score += 5000
        correct += 1

    else:
        print("Wrong Answer")
        wrong += 1


    # Question 5
    print("\nQuestion 5 for 10000 points")
    print("Which keyword is used to define a function in Python?")
    print("A. define")
    print("B. fun")
    print("C. def")
    print("D. function")

    ans = input("Enter your answer (A/B/C/D) or type skip: ")

    if ans.lower() == "skip":
        skipped += 1

    elif ans.upper() == "C":
        print("Correct Answer")
        score += 10000
        correct += 1

    else:
        print("Wrong Answer")
        wrong += 1


    # Final Result
    print("\n===== GAME OVER =====")
    print("Total Score:", score)
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skipped)

else:
    print("Game Cancelled")