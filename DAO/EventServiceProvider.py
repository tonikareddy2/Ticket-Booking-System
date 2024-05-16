from Util.DBconn import DBconnection
from Entity import Event


class EventServiceProvider(DBconnection):

    def create_event(
        self, event_name, date, time, total_seats, ticket_price, event_type, venue
    ):
        try:
            self.cursor.execute(
                """
                INSERT INTO Event (event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type, venue_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event_name,
                    date,
                    time,
                    total_seats,
                    total_seats,
                    ticket_price,
                    event_type,
                    venue.venue_id,
                ),
            )
            self.conn.commit()
            return Event(
                event_name,
                date,
                time,
                venue.venue_name,
                total_seats,
                total_seats,
                ticket_price,
                event_type,
            )
        except Exception as e:
            print(e)

    def getEventDetails(self):
        try:
            while True:
                print("Select the type of event details you want to see:")
                print("1. Movie event details")
                print("2. Concert event details")
                print("3. Sports event details")
                choice = int(input("Enter your choice (1/2/3): "))

                if choice == 1:
                    event_type = "Movie"
                    break
                elif choice == 2:
                    event_type = "Concert"
                    break
                elif choice == 3:
                    event_type = "Sports"
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

            self.cursor.execute(
                "SELECT * FROM Event WHERE event_type = ?", (event_type,)
            )
            events = []
            for row in self.cursor.fetchall():
                event = Event(*row)
                events.append(event)
            return events
        except Exception as e:
            print(e)

    def getAvailableNoOfTickets(self):
        try:
            self.cursor.execute("SELECT SUM(available_seats) FROM Event")
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(e)
