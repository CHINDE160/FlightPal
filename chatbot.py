
# Import necessary libraries
import pandas as pd

# Define flight data
flight_data = {
    "FlightID": [101, 102, 103, 104, 105, 106],
    "Airline": ["AirAsia", "IndiGo", "Vistara", "SpiceJet", "GoAir", "Air India"],
    "From": ["Delhi", "Mumbai", "Chennai", "Delhi", "Hyderabad", "Bangalore"],
    "To": ["Mumbai", "Bangalore", "Kolkata", "Bangalore", "Pune", "Delhi"],
    "Departure_Time": ["08:00 AM", "09:30 AM", "07:00 AM", "06:45 AM", "12:30 PM", "03:15 PM"],
    "Arrival_Time": ["10:00 AM", "11:30 AM", "10:00 AM", "09:45 AM", "02:00 PM", "05:45 PM"],
    "Price": [5000, 6000, 7000, 7500, 4500, 8000]
}

# Create a DataFrame from the flight data
df = pd.DataFrame(flight_data)

# Define seat options
seat_options = {
    "Economy": 1000,
    "Premium Economy": 2000,
    "Business Class": 5000
}

# Define meal options
meal_options = {
    "Vegetarian": 500,
    "Non-Vegetarian": 500,
    "Special Meal": 1000
}

# Define a function to book a flight
def book_flight(flight_id):
    result = df[df["FlightID"] == flight_id]
    if not result.empty:
        print("Flight booked successfully!")
        print(result)
        # Ask for seat preference
        print("\nSeat Options:")
        for seat, price in seat_options.items():
            print(f"{seat}: ${price}")
        seat_choice = input("Enter your seat preference: ")
        if seat_choice in seat_options:
            print(f"Seat preference: {seat_choice}")
        else:
            print("Invalid seat preference. Defaulting to Economy.")
            seat_choice = "Economy"
        # Ask for meal preference
        print("\nMeal Options:")
        for meal, price in meal_options.items():
            print(f"{meal}: ${price}")
        meal_choice = input("Enter your meal preference: ")
        if meal_choice in meal_options:
            print(f"Meal preference: {meal_choice}")
        else:
            print("Invalid meal preference. Defaulting to Vegetarian.")
            meal_choice = "Vegetarian"
        # Calculate total price
        total_price = result["Price"].values[0] + seat_options[seat_choice] + meal_options[meal_choice]
        print(f"\nTotal Price: ${total_price}")
    else:
        print("Flight not found!")

# Define a main function to interact with the user
def main():
    print("Welcome to the flight booking chatbot!")
    while True:
        print("\n1. Search for flights")
        print("2. Book a flight")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            from_city = input("Enter the departure city: ")
            to_city = input("Enter the arrival city: ")
            result = df[(df["From"] == from_city) & (df["To"] == to_city)]
            if not result.empty:
                print(result)
            else:
                print("No flights found!")
        elif choice == "2":
            flight_id = int(input("Enter the flight ID: "))
            book_flight(flight_id)
        elif choice == "3":
            print("Thank you for using the flight booking chatbot!")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()

