def main() -> None:
    total_salary_payout: float = 0
    total_bonus_given: float = 0

    for count in range(1, 6):
        curr_salary: float = float(input(f"Enter employee {count}'s salary: "))
        bonus_p: float = 0

        if curr_salary >= 100_000:
            bonus_p = 20
        elif curr_salary >= 50_000:
            bonus_p = 10
        else:
            bonus_p = 5

        bonus: float = curr_salary * bonus_p / 100
        print(f"{bonus = }\n")

        total_salary_payout += curr_salary + bonus
        total_bonus_given += bonus

    print(f"{total_salary_payout = }")
    print(f"{total_bonus_given = }")


if __name__ == "__main__":
    main()
