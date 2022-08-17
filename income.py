from math import pow
def compute_income(deposit, interest_rate, amount_months):
    # вычислить прибыль
    z = deposit * pow((1+interest_rate/(12*100)),amount_months) - deposit
    return z

k = float(input())

n = int(input())

s = 703
# вычислить прибыль с помощью функции

for x in range(1000, 30000):
    income = compute_income(x, k, n )
    if round(income,0) == s:
        print(x)    


