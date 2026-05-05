def main() -> None:
    count: int = 1

    balance: float = 100_000.00

    while True:
        curr_transaction: float = float(input(f"Enter transaction {count}: "))

        if curr_transaction == 0:
            break
        elif curr_transaction > 0:
            balance += curr_transaction
            print(f"Deposit of {curr_transaction} is successful")
        else:
            balance -= curr_transaction
            print(f"Withdrawal of {curr_transaction} is succesfull")

        count += 1

    print(f"Final balance: {balance}")

    print("Active" if balance >= 0 else "Overdrawn")


if __name__ == "__main__":
    main()
