# Digital Notice Board using Python

notices = []

def add_notice():
notice = input("Enter the new notice: ").strip()

```
if notice:
    notices.append(notice)
    print("Notice added successfully!")
else:
    print("Notice cannot be empty.")
```

def view_notices():
print("\n===== DIGITAL NOTICE BOARD =====")

```
if not notices:
    print("No notices available.")
    return

for number, notice in enumerate(notices, start=1):
    print(f"{number}. {notice}")
```

def delete_notice():
view_notices()

```
if not notices:
    return

try:
    number = int(input("Enter notice number to delete: "))

    if 1 <= number <= len(notices):
        removed = notices.pop(number - 1)
        print(f"Notice deleted: {removed}")
    else:
        print("Invalid notice number.")

except ValueError:
    print("Please enter a valid number.")
```

while True:
print("\n===== DIGITAL NOTICE BOARD =====")
print("1. Add Notice")
print("2. View Notices")
print("3. Delete Notice")
print("4. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    add_notice()

elif choice == "2":
    view_notices()

elif choice == "3":
    delete_notice()

elif choice == "4":
    print("Digital Notice Board Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```

