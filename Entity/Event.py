class Event:
    def __init__(
        self,
        event_id,
        event_name,
        event_date,
        event_time,
        venue_id,
        total_seats,
        available_seats,
        ticket_price,
        event_type,
    ):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def display_event_details(self):
        print(f"Event ID: {self.event_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Event Time: {self.event_time}")
        print(f"Venue ID: {self.venue_id}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")
