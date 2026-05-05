def main() -> None:

    n_low_stock: int = 0
    n_normal_stock: int = 0
    n_high_stock: int = 0

    for count in range(1, 7):
        curr_quantity: int = int(input(f"Enter product {count}'s quantity: "))

        if curr_quantity < 10:
            n_low_stock += 1
        elif curr_quantity < 50:
            n_normal_stock += 1
        else:
            n_high_stock += 1

    print(f"{n_low_stock = }")
    print(f"{n_normal_stock = }")
    print(f"{n_high_stock = }")


if __name__ == "__main__":
    main()
