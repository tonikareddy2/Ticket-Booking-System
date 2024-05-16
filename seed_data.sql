-- VENUE TABLE

INSERT INTO Venue (venue_id,venue_name, address)
VALUES (1,'RK Beach', 'Visakhapatnam'),
       (2,'Tirumala', 'Tirupati'),
       (3,'Nagarjuna Sagar Dam', 'Nalgonda district'),
       (4,'Undavalli Caves', 'Guntur'),
       (5,'Amaravati', 'Vijayawada'),
       (6,'Bhavani Island', 'Vijayawada'),
       (7,'Kanaka Durga Temple', 'Vijayawada'),
       (8,'Pulicat Lake', 'Nellore'),
       (9,'Kolleru Lake', 'West Godavari'),
       (10,'Lepakshi Temple', 'Anantapur');

-- EVENT TABLE

INSERT INTO Event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type)
VALUES 
('Event 1', '2024-05-01', '18:00:00', 1, 100, 100, 1500.00, 'Movie'),
('Event 2', '2024-05-02', '19:00:00', 2, 150, 150, 2000.00, 'Concert'),
('Event 3', '2024-05-03', '20:00:00', 3, 200, 200, 1800.00, 'Sports'),
('Event 4', '2024-05-04', '17:00:00', 4, 120, 120, 2200.00, 'Movie'),
('Event 5', '2024-05-05', '21:00:00', 5, 180, 180, 2500.00, 'Concert'),
('Event 6', '2024-05-06', '19:30:00', 6, 90, 90, 1700.00, 'Movie'),
('Event 7', '2024-05-07', '20:30:00', 7, 160, 160, 2100.00, 'Concert'),
('Event 8', '2024-05-08', '18:30:00', 8, 130, 130, 1900.00, 'Sports'),
('Event 9', '2024-05-09', '19:00:00', 9, 110, 110, 2300.00, 'Movie'),
('Event 10', '2024-05-10', '20:00:00', 10, 140, 140, 2600.00, 'Concert');

-- CUSTOMER TABLE

INSERT INTO Customer (customer_id,customer_name, email, phone_number)
VALUES 
(1,'John Doe', 'john.doe@example.com', '1234567890'),
(2,'Jane Smith', 'jane.smith@example.com', '9876543210'),
(3,'Michael Johnson', 'michael.johnson@example.com', '4567890123'),
(4,'Emily Brown', 'emily.brown@example.com', '7890123456'),
(5,'William Taylor', 'william.taylor@example.com', '2345678901'),
(6,'Olivia Wilson', 'olivia.wilson@example.com', '8901234567'),
(7,'James Anderson', 'james.anderson@example.com', '5678901234'),
(8,'Emma Martinez', 'emma.martinez@example.com', '9012345678'),
(9,'Alexander Garcia', 'alexander.garcia@example.com', '3456789012'),
(10,'Sophia Lopez', 'sophia.lopez@example.com', '6789012345');

-- BOOKING TABLE

INSERT INTO Booking (booking_id, customer_id, event_id, num_tickets, total_cost, booking_date)
VALUES 
(1, 1, 1, 2, 3000.00, '2007-08-09'),
(2, 2, 2, 3, 6000.00, '2007-08-10'),
(3, 3, 3, 4, 7200.00, '2008-08-11'),
(4, 4, 4, 1, 2200.00, '2006-09-08'),
(5, 5, 5, 2, 5000.00, '2016-05-02'),
(6, 6, 6, 3, 5100.00, '2012-06-05'),
(7, 7, 7, 2, 4200.00, '2023-11-24'),
(8, 8, 8, 4, 7600.00, '2011-12-13'),
(9, 9, 9, 1, 2300.00, '2016-06-25'),
(10, 10, 10, 3, 7800.00, '2020-04-30');



SELECT * FROM Booking;
SELECT * FROM Customer;
SELECT * FROM Event;
SELECT * FROM Venue;