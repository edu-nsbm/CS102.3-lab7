def main() -> None:

    total: float = 0
    n_failed: int = 0

    for count in range(1, 7):
        curr_mark: float = float(input(f"Enter mark {count}: "))

        total += curr_mark

        if curr_mark < 50:
            n_failed += 1

    average: float = total / 5

    if average >= 60 and n_failed == 0:
        print("Excellent Performance.")
    elif average >= 50:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    main()
