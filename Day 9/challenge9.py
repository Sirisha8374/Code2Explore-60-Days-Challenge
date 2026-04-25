import copy

def create_inventory():
    inventory = [
        {"item": "Laptop", "details": {"price":50000, "stock": 10, "rating": 4.5}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "rating": 4.2}}
    ]
    return inventory

def apply_discount(data, roll_no):
    index = roll_no % len(data)

    for i in range(len(data)):
        if i == index:
            data[i]["details"]["price"] *= 0.9
            data[i]["details"]["stock"] += 5
    return data

def compare_data(original, modified):
    changed = 0
    unchanged = 0
    for i in range(len(original)):
        if original[i]["details"] != modified[i]["details"]:
            changed += 1
        else:
            unchanged += 1
    return (changed, unchanged)

inventory = create_inventory()
roll_no = int(input("Enter roll number: "))

shallow_copy = inventory.copy()
deep_copy = copy.deepcopy(inventory)

apply_discount(shallow_copy, roll_no)
apply_discount(inventory, roll_no)

shallow_result = compare_data(inventory, shallow_copy)
deep_result = compare_data(inventory, deep_copy)

def print_inventory(title, data):
    print(f"\n===== {title} =====")
    for i in range(len(data)):
        item = data[i]
        print("\nItem ", i+1)
        print("Name: ", item["item"])
        print("Price: ", item["details"]["price"])
        print("Stock: ", item["details"]["stock"])
        print("Rating: ", item["details"]["rating"])

print_inventory("Original Inventory", inventory)
print_inventory("Shallow Copy", shallow_copy)
print_inventory("Deep Copy", deep_copy)

print("\n===== Comparison =====")
print("\nShallow Comparison (changed, unchanged): ", shallow_result)
print("Deep Comparison (changed, unchanged): ", deep_result)
