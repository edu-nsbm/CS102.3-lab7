def main() -> None:

    correct_pin: int = 1234
    n_max_attempts: int = 3

    initial_balance: float = 100_000.00

    for n_attempt in range(1, n_max_attempts + 1):
        input_pin: int = int(input("Enter PIN: "))

        if input_pin == correct_pin:
            while True:
                withdrawal_amount: float = float(input("\nEnter withdrawal amount: "))

                if initial_balance - withdrawal_amount >= 500:
                    initial_balance -= withdrawal_amount
                    print(f"Withdrawal of {withdrawal_amount} is successful!")
                    print(f"Balance: {initial_balance}")
                    break
                else:
                    print("Insufficient funds! Retry.")

            break

        else:
            n_attempts_left = n_max_attempts - n_attempt

            if n_attempts_left == 0:
                print("Incorrect PIN! Your account is locked!")
            else:
                print(
                    f"Incorrect PIN! You have {n_max_attempts - n_attempt} more attempts left and then your account's locked!"
                )


if __name__ == "__main__":
    main()
