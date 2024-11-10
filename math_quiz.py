import random


def random_number_generator(min_val, max_val): #it will generate random integer for mentioned range
    """
    Random integer.
    """
    return random.randint(min_val, max_val)


def operator_selection(): #selects random mathematical operator eg. + , - , *.
    return random.choice(['+', '-', '*'])


def math_problem_generator(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2   #appropriate operator changes
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    points = 0
    total_questions_provided = 3 #integers only

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions_provided):
        n1 = random_number_generator(1, 10) 
        n2 = random_number_generator(1, 5)  #integer value only
        o = operator_selection()

        PROBLEM, right_answer = math_problem_generator(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == right_answer:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {right_answer}.")

    print(f"\nGame over! Your score is: {points}/{total_questions_provided}")

if __name__ == "__main__":
    math_quiz()