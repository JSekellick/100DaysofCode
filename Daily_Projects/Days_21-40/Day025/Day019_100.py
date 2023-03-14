# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1

# for counter in range(10):
#   print(counter)

# total = 0
# for number in range(100):
#   total += 1
#   print(total)

# for day in range(7):
#   print("Day", day)

# total = 10
# for counter in range(100):
#   total += 10
#   print("total")

loan = 1000
year = 0
for interest in range(5):
    loan *= 1.05
    year += 1
    print(f"Year {year} is {loan}")

# Provided solution
# loan = 1000
# apr = 0.05
# for i in range(10):
#   loan+=(loan*apr)
#   print("Year", i+1, "is", round(loan,2))
