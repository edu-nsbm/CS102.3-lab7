def main() -> None:

    n_units: int = 0
    total: float = 0

    for count in range(1, 5):
        n_curr_units: int = int(input(f"Enter month {count}'s units: "))

        n_units += n_curr_units

    if n_units <= 100:
        total = 10 * n_units
    elif n_units <= 200:
        total = 10 * 100 + 15 * (n_units - 100)
    else:
        total = 10 * 100 + 15 * 100 + 20 * (n_units - 200)

    print(f"\n{total = }")
    print("High Usage" if n_units > 400 else "Low Usage")


if __name__ == "__main__":
    main()
