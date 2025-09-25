def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    main()
