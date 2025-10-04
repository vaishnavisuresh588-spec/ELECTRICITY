# Electricity Bill Calculator Program with Discount

# Input: number of units consumed
units = int(input("Enter the number of units consumed: "))

# Rate per unit
rate = 5  

# Calculate bill
bill = units * rate

# Apply discount if bill exceeds 1000
if bill > 1000:
    discount = bill * 0.10
    bill -= discount
    print(f"\nYou got a discount of ₹{discount:.2f} (10% off)")

# Display result
print("\n--- Electricity Bill ---")
print(f"Units Consumed: {units}")
print(f"Rate per Unit: ₹{rate}")
print(f"Total Bill: ₹{bill:.2f}")