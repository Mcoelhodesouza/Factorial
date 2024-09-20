def factorial(num):
    print("Numero attuale: ", num)
    if num == 1:
        print("Terminato")
        return num
    else:
        print("Nuova chiamata della funzione")
        return factorial(num-1) * num


if __name__ == "__main__":
    n = int(input("Please, insert a positive integer number:"))
    print("The factorial of", str(n), "is:", str(factorial(n)))