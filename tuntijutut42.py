try:
    number = input("Anna numero:\n")
    number = int(number)
    divided = 100 / number
    print(f"Numerosi: {number}, jakotulos: {divided}")
except Exception as e:
    print("Virhe: " + str(e))
    print("Virhe! Ole yhteydessä ohjelman kehittäjään.")
    