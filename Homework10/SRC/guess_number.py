import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 5

    print("Вгадайте число від 1 до 100. У вас є 5 спроб.")

    for i in range(attempts):
        guess = int(input(f"Спроба {i+1}: "))
        if guess == number:
            print("Вітаємо! Ви вгадали правильне число.")
            return
        elif guess > number:
            print("Занадто високо.")
        else:
            print("Занадто низько.")

    print(f"Вибачте, у вас закінчилися спроби. Правильний номер був {number}")

if __name__ == "__main__":
    guess_number()
