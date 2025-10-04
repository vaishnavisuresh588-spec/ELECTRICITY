# Electricity Bill Calculator Program

# Input: number of units consumed
units = int(input("Enter the number of units consumed: "))

# Rate per unit
rate = 5  

# Calculate bill
bill = units * rate

# Display result
print("\n--- Electricity Bill ---")
print(f"Units Consumed: {units}")
print(f"Rate per Unit: ₹{rate}")
print(f"Total Bill: ₹{bill}")
