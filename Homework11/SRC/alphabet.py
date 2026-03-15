class Alphabet:
    def __init__(self, lang, letters):
        # Зберігаємо мову та список літер
        self.lang = lang
        self.letters = letters

    def print(self):
        # Виводимо всі літери
        print("".join(self.letters))

    def letters_num(self):
        # Повертаємо кількість літер
        return len(self.letters)


if __name__ == "__main__":
    # Створюємо алфавіт англійської мови
    eng = Alphabet("English", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    # Викликаємо методи
    eng.print()
    print("Number of letters:", eng.letters_num())
