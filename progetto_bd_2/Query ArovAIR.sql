USE ArovAIR;

#1. Durata di un volo:
SELECT FlightID, Departure, Arrival, TIMEDIFF(Arrival, Departure) AS Duration
	FROM Flight_T
		WHERE FlightID = 'XW2288';

#2. Voli disponibili:
SELECT FlightID, Departure, DepartureAirport, Arrival, ArrivalAirport
	FROM Flight_T
		WHERE Departure > current_timestamp()
			ORDER BY Departure;
            
#3. Informazioni su un volo prenotato:
SELECT BarCode AS TicketCode, Ticket_T.FlightID, PersonName AS 'Name', PersonSurname AS Surname, 
Departure, DepartureAirport, A1.City AS DepartureCity, A1.Nation AS DepartureNation, 
Arrival, ArrivalAirport, A2.City AS ArrivalCity, A2.Nation AS ArrivalNation, SeatClass, SeatBoarding, 
SeatNumber, GateNumber AS Gate, GateTerminal AS Terminal, GateClosingTime
	FROM Ticket_T INNER JOIN Person_T ON Ticket_T.TaxCode=Person_T.TaxCode
		INNER JOIN Flight_T ON Ticket_T.FlightID=Flight_T.FlightID
		INNER JOIN Airport_T AS A1 ON Flight_T.DepartureAirport = A1.AirportCode
		INNER JOIN Airport_T AS A2 ON Flight_T.ArrivalAirport = A2.AirportCode
			WHERE BarCode='8 2288 98577';

#4. Informazioni sul contratto di un dipendente:
SELECT TaxCode, PersonName AS 'Name', PersonSurname AS Surname, ContractType, Wage, Employee_T.Category
	FROM Person_T INNER JOIN Employee_T ON Person_T.TaxCode=Employee_T.ETaxCode
     WHERE TaxCode='CNKSZY57R26L605V';

#5. Aereoporti per nazione:
SELECT Nation, COUNT(AirportCode) AS NOfAirports
	FROM Airport_T
		GROUP BY Nation
        ORDER BY Nation;

#6. Tabellone dei voli in base al tempo atmosferico:
CREATE VIEW FlightBoard(FlightCode, DepartureAir,ArrivalAir,FlightStatus,cnt) AS
SELECT DISTINCT Detection_T.FlightID, DepartureAirport, ArrivalAirport,
	CASE 
		WHEN Forecast = 'stormy' or (Temperature NOT BETWEEN 2 AND 40) or Humidity > 55 THEN 'Cancelled'
		ELSE (SELECT Departure FROM Flight_T WHERE Flight_T.FlightID = Detection_T.FlightID)
	END AS "Status", COUNT(Detection_T.FlightID) AS Cnt
	FROM Weather_T INNER JOIN Detection_T ON Weather_T.DetectionNumber=Detection_T.DetectionNumber
		INNER JOIN Flight_T ON Flight_T.FlightID=Detection_T.FlightID
			GROUP BY FlightID
			ORDER BY FlightID;

SELECT DISTINCT FlightCode, DepartureAir, ArrivalAir, 
CASE WHEN cnt = 1 THEN FlightBoard.FlightStatus
	ELSE "Cancelled" 
    END AS FlightStatus 
FROM FlightBoard;

#7. Costo totale di una prenotazione:
SELECT BookingID, TicketCost, NofTickets, (TicketCost*NofTickets) AS TotalCost
	FROM Booking_T
		WHERE BookingID = '087426';

#8. Elenco dei dipendenti (pensionati e non) e calcolo dei contributi:
SELECT PersonName AS 'Name', PersonSurname AS Surname, BirthDate, (YEAR(CURDATE())-YEAR(BirthDate)) AS Age, DateEmployed, Wage, 
Employee_T.Category, ROUND((Wage*(YEAR(CURDATE())-YEAR(DateEmployed)))/100*30, 2) AS 'Contributions',
	CASE
		WHEN (YEAR(CURDATE())-YEAR(BirthDate)) < 65 THEN "Waged"
        WHEN (YEAR(CURDATE())-YEAR(BirthDate)) = 65 THEN "Retiring"
        ELSE "Retired"
    END AS "Status"
	FROM Person_T INNER JOIN Employee_T ON Person_T.TaxCode=Employee_T.ETaxCode;

#9. Documenti scaduti:
#a) Verificare chi viaggia con un documento scaduto rispetto alla data attuale: 
SELECT Passenger_T.PTaxCode,Flight_T.FlightID,SerialNumber,DocumentType, PersonName,PersonSurname
	FROM Document_T,Person_T,Passenger_T,Ticket_T,Flight_T
		WHERE Passenger_T.PTaxCode=Person_T.TaxCode 
			AND Ticket_T.DocumentNumber=Document_T.SerialNumber
			AND Ticket_T.FlightID=Flight_T.FlightID 
            AND Passenger_T.PTaxCode=Ticket_T.TaxCode 
            AND Expiry<CURDATE();

#b) Conteggio dei documenti scaduti: 
SELECT COUNT(*) AS NofExpiredDocuments
	FROM Document_T
		WHERE Expiry<CURDATE();

#10. Differenza temporale tra la data di prenotazione e la data di partenza del volo: 
SELECT Flight_T.FlightID, Booking_T.BookingID, Flight_T.Departure, BookingDate, DATEDIFF(Departure,BookingDate) AS DaysDiffernce
	FROM Booking_T,Flight_T,Ticket_T
		WHERE Flight_T.FlightID=Ticket_T.FlightID 
			AND Ticket_T.BookingID=Booking_t.BookingID
				ORDER BY FlightID;

#11. Posti disponibili su un volo:
SELECT Flight_T.FlightID, Departure, DepartureAirport, Arrival, ArrivalAirport, (NofSeats-COUNT(BarCode)) AS AvailableSeats, NofSeats
	FROM Flight_T JOIN Airplane_T ON Flight_T.AirplaneID = Airplane_T.SerialNumber
		INNER JOIN Ticket_T ON Flight_T.FlightID = Ticket_T.FlightID
			GROUP BY FlightID
			ORDER BY FlightID;

#12. Ricavo annuale dalla vendita dei biglietti:
SELECT YEAR(BooKingDate) AS Year, SUM(TicketCost*NofTickets) AS Earnings
	FROM Booking_T
		GROUP BY Year
        ORDER BY Year;
        
#13. Caratteristiche aeroporto di arrivo e partenza:
SELECT DepartureAirport, A1.City AS DepartureCity, A1.Nation AS DepartureNation, CASE WHEN A1.Parking = 0 THEN "No" ELSE "Yes" END AS "DParking", 
CASE WHEN A1.Metro = 0 THEN "No" ELSE "Yes" END AS "DMetro", CASE WHEN A1.BusStation = 0 THEN "No" ELSE "Yes" END AS "DBusStation",
A2.City AS ArrivalCity, A2.Nation AS ArrivalNation, CASE WHEN A2.Parking = 0 THEN "No" ELSE "Yes" END AS "AParking", 
CASE WHEN A2.Metro = 0 THEN "No" ELSE "Yes" END AS "AMetro", CASE WHEN A2.BusStation = 0 THEN "No" ELSE "Yes" END AS "ABusStation"
	FROM Ticket_T INNER JOIN Flight_T ON Ticket_T.FlightID=Flight_T.FlightID
    INNER JOIN Airport_T AS A1 ON Flight_T.DepartureAirport = A1.AirportCode
    INNER JOIN Airport_T AS A2 ON Flight_T.ArrivalAirport = A2.AirportCode
			WHERE BarCode='8 6994 99991';
            
#14. Recensioni medie per volo:
SELECT FlightID, ROUND(AVG(Cleanliness), 1) AS Cleanliness, ROUND(AVG(onboardExperience),1) AS OnBoardExperience, ROUND(AVG(Service),1) AS Service
	FROM Review_T
		GROUP BY FlightID
		ORDER BY FlightID;

#15. Numero di biglietti venduti per ogni destinazione:
SELECT Nation, COUNT(BarCode) AS NofTickets
	FROM Ticket_T INNER JOIN Flight_T ON Ticket_T.FlightID = Flight_T.FlightID
		INNER JOIN Airport_T ON Flight_T.ArrivalAirport = Airport_T.AirportCode
			GROUP BY Nation
            ORDER BY Nation;

#16. Storico dei voli in un intervallo di tempo:
SELECT FlightID, Departure, DepartureAirport, Arrival, ArrivalAirport
	FROM Flight_T
		WHERE Departure BETWEEN '2017-05-18' AND '2017-07-18'
			ORDER BY Departure;

#17. Numero di biglietti acquistati per nazionalità:
SELECT Nationality, COUNT(BarCode) AS TicketsSold
	FROM Ticket_T INNER JOIN Person_T ON Ticket_T.TaxCode = Person_T.TaxCode
		GROUP BY Nationality
		ORDER BY Nationality;