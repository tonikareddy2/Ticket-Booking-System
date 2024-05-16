from Entity import Booking, Customer, Event, Venue
from DAO import event_Service_Provider, BookingSystemProvider


def main():
    event_service_provider = event_Service_Provider()
    booking_service_provider = BookingSystemProvider()

    while True:
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. Get Available Seats")
        print("5. Get Event Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event_name = input("Enter event name: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM:SS): ")
            total_seats = int(input("Enter total number of seats: "))
            available_seats = int(input("Enter the available seats:"))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie/Sports/Concert): ")
            Venue.venue_id = input("Enter venue id:")
            created_event = Event(
                event_name,
                event_date,
                event_time,
                total_seats,
                available_seats,
                ticket_price,
                event_type,
                Venue.venue_id,
            )
            event_service_provider.create_event(created_event)
        elif choice == "2":
            # Implement logic to book tickets
            pass
        elif choice == "3":
            # Implement logic to cancel booking
            pass
        elif choice == "4":
            try:
                available_seats = event_service_provider.getAvailableNoOfTickets()
                if available_seats:
                    print("\nTotal Available Seats:", available_seats)
                else:
                    print("No available seats found.")
            except Exception as e:
                print("Error fetching available seats:", e)
        elif choice == "5":
            try:
                event_service_provider.getEventDetails()
            except Exception as e:
                print("Error fetching event details:", e)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
