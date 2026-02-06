name = input(" Enter your name:")

age = int(input("enter your age:"))

age = age + 4

print("hey", name, ",you will be", age, "years old in 2023!")

total_bill = float(input("enter total bill amount:"))
people =int (input("Enter number of people:"))

share_per_person = total_bill / people

print("Total Bill:", total_bill, ",\nEach person pays:", share_per_person)

print(type(total_bill))
print(type(people))
print(type(share_per_person))

item_name = "Laptop"
quantity = 4
price = 2999.99
in_stock = True

print("Item:", item_name, ",Qty:", quantity, ", price:", price, ", Available:", in_stock)

total_cost = quantity * price

print("Total Cost:", total_cost)