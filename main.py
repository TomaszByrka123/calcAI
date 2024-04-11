from sympy import sympify

def main():
    expression = input("Podaj działanie matematyczne: ")
    try:
        result = sympify(expression)
        print("Wynik:", result)
    except Exception as e:
        print("Wystąpił błąd:", e)

if __name__ == "__main__":
    main()
