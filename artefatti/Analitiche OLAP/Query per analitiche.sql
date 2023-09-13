#Popular_Destinations:
SELECT Flight_T.FlightID, MONTH(Flight_T.Arrival) AS Month, Airport_T.City, Flight_T.ArrivalAirport
	FROM Airport_T, Flight_T 
		WHERE Flight_T.ArrivalAirport = Airport_T.AirportCode;

#Passenger_Rewiews:
SELECT Flight_T.FlightID, Passenger_T.PTaxCode, Cleanliness, OnBoardexperience, Service, Nationality, Gender
	FROM Flight_T, Review_T, Passenger_T, Person_T
		WHERE Flight_T.FlightID = Review_T.FlightID 
			AND Passenger_T.PTaxCode = Person_T.TaxCode
			AND Review_T.TaxCode = Passenger_T.PTaxCode;

#Buggage_Study:
SELECT Gender, BaggageType, Weight
	FROM Flight_T,Passenger_T, Person_T, Ticket_T, Baggage_T
		WHERE Flight_T.FlightID = Ticket_T.FlightID 
			AND Person_T.TaxCode = Passenger_T.PTaxCode 
			AND Baggage_T.TicketBarCode = Ticket_T.BarCode 
			AND Ticket_T.TaxCode = Passenger_T.PTaxCode;

#Average_Ticket_Cost:
SELECT Flight_T.FlightID, Booking_T.BookingID, Ticket_T.BarCode, ArrivalAirport, TicketCost
	FROM Flight_T, Booking_T, Ticket_T
		WHERE Flight_T.FlightID = Ticket_T.FlightID 
			AND Booking_T.BookingID = Ticket_T.BookingID;