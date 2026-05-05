def main() -> None:

    n_high_temp: int = 0
    n_normal_temp: int = 0
    n_low_temp = 0

    while True:
        curr_temp: float = float(input("Enter current temperature | -1 to exit: "))

        if curr_temp == -1:
            break
        elif curr_temp > 35:
            n_high_temp += 1
        elif curr_temp > 20:
            n_normal_temp += 1
        else:
            n_low_temp += 1

    print(f"{n_high_temp = }")
    print(f"{n_normal_temp = }")
    print(f"{n_low_temp = }")


if __name__ == "__main__":
    main()
