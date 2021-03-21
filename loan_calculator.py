import argparse
import math
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
if args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
    exit()
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
    exit()
elif not args.interest:
    print("Incorrect parameters")
    exit()
elif len(sys.argv) < 5:
    print("Incorrect parameters")
    exit()
elif float(args.interest) < 0:
    print("Incorrect parameters")
    exit()
elif args.payment and float(args.payment) < 0:
    print("Incorrect parameters")
    exit()
elif args.principal and float(args.principal) < 0:
    print("Incorrect parameters")
    exit()
elif args.periods and float(args.periods) < 0:
    print("Incorrect parameters")
    exit()
i = float(args.interest) / 1200
if args.type == "diff":
    P = float(args.principal)
    n = int(args.periods)
    overpayment = 0
    for m in range(1, int(args.periods) + 1):
        print("Month {}: payment is {}".format(m, math.ceil(P / n + i * (P - P * (m - 1) / n))))
        overpayment += math.ceil(P / n + i * (P - P * (m - 1) / n))
    overpayment -= P
    print("\nOverpayment = " + f"{math.ceil(overpayment)}")
elif not args.principal:
    n = int(args.periods)
    P = round(float(args.payment)) * ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    print("Your loan principal = " + f"{round(P)}" + "!")
    print("Overpayment = " + f"{math.ceil(n * float(args.payment) - P)}")
elif not args.periods:
    monthly_payment = float(args.payment)
    P = round(float(args.principal))
    n = math.ceil(math.log(monthly_payment / (monthly_payment - i * P), i + 1))
    print("It will take " + f"{str(n // 12) + ' years' if n >= 12 else ''}" +
          f"{' and ' + str(n % 12) + ' month' if n % 12 else ''}" + f"{'s' if n % 12 > 1 else ''}"
                                                                    " to repay this loan!")
    print("Overpayment = " + f"{math.ceil(n * monthly_payment - P)}")
elif not args.payment:
    P = float(args.principal)
    n = int(args.periods)
    monthly_payment = P * i * (1 + i) ** n / ((1 + i) ** n - 1)
    print("Your monthly payment = " + f'{math.ceil(monthly_payment)}' + "!")
    print("Overpayment = " + f"{int(n * math.ceil(monthly_payment) - P)}")
