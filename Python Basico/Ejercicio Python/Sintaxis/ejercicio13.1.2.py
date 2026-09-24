amount_seconds = int(input("Enter the time in seconds: "))
amount_seconds_remaining = 0

if amount_seconds > 600:
    print("Mayor")
elif amount_seconds < 600:
    amount_seconds_remaining = 600 - amount_seconds
    print(f"Seconds remaining to 10 minutes is: {amount_seconds_remaining}")
elif amount_seconds == 600:
    print("Igual")

