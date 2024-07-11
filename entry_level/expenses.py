num_expenses = int(input("Enter # of expenses:"))
expenses = []

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)
print("you spent £", total, sep = '')