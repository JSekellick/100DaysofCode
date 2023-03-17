print("Math Game!")
print()

print("Name your multiples!!!")
number = int(input("Pick an integer for the multiplication table: "))
correct_answers = 0

for i in range(1, 11):
    question = int(input(f"{i} X {number} = "))
    answer = (i * number)
    if question == (i * number):
        correct_answers += 1
        print("Awesome!")
    else:
        print(f"Nope. The answer is {answer}")
    print(f"Your score is {correct_answers}")
if correct_answers > 7:
    print(f"🥳 Congratulations, you scored {correct_answers} out of 10!!! 🎉🎉🎉")
elif correct_answers > 5:
    print(f"You scored {correct_answers} out of 10. You can do better.")
else:
    print(f"You scored {correct_answers} out of 10. Very disappointing...")