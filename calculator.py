import argparse


def validate_args(loan_amount, interest_rate, term, typ):
    if loan_amount <= 0:
        raise ValueError("Loan amount should be more than 0")
    if not (0 <= interest_rate <= 100):
        raise ValueError("Interest rate has to be between 0 and 100")
    if term <= 0:
        raise ValueError("Term should be more than 0")
    if typ not in ["fixed", "variable"]:
        raise ValueError("Type should be either fixed or variable")


def calculate_payments(loan_amount, interest_rate, term, typ):
    months = 12
    payments = term * months
    if typ == "fixed":
        q = 1 + (interest_rate / months / 100)
        return payments * [
            loan_amount * (q ** payments) * (q - 1) / (q ** payments - 1)
        ]
    else:
        capital_installment = loan_amount / payments
        interest_instalments = [
            ((loan_amount - i * capital_installment) * interest_rate / 100) / 12
            for i in range(payments)
        ]
        return [capital_installment + ii for ii in interest_instalments]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple mortgage calculator")
    parser.add_argument("-l", "--loan", help="Total amount of loan")
    parser.add_argument("-i", "--interest", help="Interest rate (annual)")
    parser.add_argument("-t", "--term", help="Number of years")
    parser.add_argument("-T", "--type", help="Type of loan")
    args = parser.parse_args()

    loan = int(args.loan)
    interest = int(args.interest)
    term = int(args.term)

    validate_args(loan, interest, term, args.type)
    payments = calculate_payments(loan, interest, term, args.type)
    print("Your monthly payments are:")
    for i, payment in enumerate(payments, 1):
        print(f"{i}. {round(payment, 2)}")
