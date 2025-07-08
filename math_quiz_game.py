import random
import time

def generator_question():
    num1=random.randint(0,10)
    num2=random.randint(0,10)
    opertion=random.choice(['+','-','*'])

    if opertion == '+':
        answer=num1+num2
    elif opertion == '-':
        answer=num1-num2
    else:
        answer=num1*num2
    return f"{num1} {opertion} {num2}",answer

def main_quiz():
    score=0
    round=5
    print("welcome to quiz game!!!")

    for i in range(round):
        question,crt_ans=generator_question()
        print(f"\n question {i+1}: {question} ")
        time.sleep(1)
        answer=int(input("enter the user value :"))
        if crt_ans==answer:
            print("correct")
            score=score+1
        else:
            print("wrong")
        print(f"{score}/{round}")
    print("----game over----")

    if score==round:
        print("you won the game !!!")
    else:
        print("keep it up try much !")

main_quiz()