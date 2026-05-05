def main() -> None:

    total: float = 0
    discount_p: float = 0

    for count in range(1, 6):
        curr_item_price: float = float(input(f"Enter item {count} price: "))
        curr_item_quantity: int = int(input(f"Enter item {count} quantity: "))

        curr_total: float = curr_item_price * curr_item_quantity
        total += curr_total

    if total > 10_000:
        discount_p = 25
    elif total > 5_000:
        discount_p = 15

    discount: float = total * discount_p / 100

    print(f"{total = }")
    print(f"{discount_p = }")
    print(f"{discount = }")
    print(f"final_amount = {total - discount}")


if __name__ == "__main__":
    main()
