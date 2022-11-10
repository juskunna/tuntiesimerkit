try:
    number = input("Anna numero:\n")
    number = int(number)
    divided = 100 / number
    print(f"Numerosi: {number}, jakotulos: {divided})
except ValueError:
    print("Annoit tekstiä! Aja ohjelma uudestaan.")

except ZeroDivisionError:
    print("Nollalla ei voi jakaa, anna muu numero")
