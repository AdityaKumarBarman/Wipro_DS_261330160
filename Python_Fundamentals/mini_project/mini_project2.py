cost_per_hour = 0.51
budget = 918

# calulate costs
cost_per_day = cost_per_hour*24
cost_per_week = cost_per_day*7
cost_per_month = cost_per_day*30

# bugdet will last till
days = budget/cost_per_day

# Print results
print("Cost per day ", cost_per_day)
print("Cost per week ", cost_per_week)
print("Cost per month ", cost_per_month)
print("Days the server can run ", int(days))