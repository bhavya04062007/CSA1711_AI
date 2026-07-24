# Vacuum Cleaner Problem

# Initial state
roomA = input("Enter state of Room A (clean/dirty): ")
roomB = input("Enter state of Room B (clean/dirty): ")

# Vacuum starts in Room A
vacuum_position = "A"

print("\nInitial State:")
print("Room A:", roomA)
print("Room B:", roomB)

# If vacuum in Room A
if vacuum_position == "A":
    if roomA == "dirty":
        print("Vacuum cleans Room A")
        roomA = "clean"

    print("Vacuum moves to Room B")
    vacuum_position = "B"

# If vacuum in Room B
if vacuum_position == "B":
    if roomB == "dirty":
        print("Vacuum cleans Room B")
        roomB = "clean"

print("\nFinal State:")
print("Room A:", roomA)
print("Room B:", roomB)

print("\nBoth rooms are clean. Task completed.")
