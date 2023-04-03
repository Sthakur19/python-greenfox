# Personal finance

# We are going to represent our expenses in a list containing integers.

# - Create a list with the following items:
#   - 500, 1000, 1250, 175, 800 and 120
# - Create an application which prints out the answers to the following
#   questions:
#   - How much did we spend?
#   - Which was our greatest expense?
#   - Which was our cheapest spending?
#   - What was the average amount of our spendings? (print this as a float value)

# The full output of your `main` method should be the following:

# ```text
# 3845
# 1250
# 120
# 640.8333
# ```

print("```text")
personal_finance = [500,1000,1250,175,800,120]
total_spend = sum(personal_finance)
print(total_spend)
max_spend = max(personal_finance)
print(max_spend)
min_spend = min(personal_finance)
print(min_spend)
average_spend = sum(personal_finance) / len(personal_finance)
print(round(average_spend,4))
print("```")