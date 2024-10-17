#add import

from question_d import get_bonus_pay_amount


def main():

    try:
        sales = float(input("Enter the sales amount: "))

        bonus = get_bonus_pay_amount(sales)

        print(f"The bonus pay amount is: {bonus}")

    except ValueError:
        print("Invalid. Please enter a number.")


main()