#pip install mysql-connector-python
#pip install tkinter
#pip install tkcalendar
#pip install python-dateutil

import os
import random
import mysql.connector

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

from datetime import datetime
from dateutil.relativedelta import relativedelta

#funzione per creare la finestra di connessione al database
def finestra_connessione():
    
    #funzione per effettuare la connessione al database
    def connessione():
        global db
        
        db_host = host_connection_entry.get()
        db_user = user_connection_entry.get()
        db_password = password_connection_entry.get()
        db_database = database_connection_entry.get()

        try:
            db = mysql.connector.connect(
                host = db_host,
                user = db_user,
                password = db_password,
                database = db_database,
                autocommit=True
            )
            messagebox.showinfo("Successo", "Connessione effettuata con successo")
            conn = TRUE
            if conn:
                connect_menu_btn.config(state=DISABLED)
                booking_menu_btn.config(state=NORMAL)
                ticket_menu_btn.config(state=NORMAL)
                flights_menu_btn.config(state=NORMAL)

            connection_wdw.destroy()
            
        except:
            messagebox.showerror("Errore", "Dati non validi")

    ##finestra per connessione al database
    connection_wdw = Tk()
    connection_wdw.title("ArovAIR: Connessione al database")
    connection_wdw.iconbitmap(os.path.dirname(__file__) + "\\ArovAIR_icon.ico")
    connection_wdw.geometry("400x230")


    #label connetti ad arovair
    connect_connection_lbl = Label(connection_wdw, text="Connetti ad ArovAIR", font="Times 20 italic bold")
    connect_connection_lbl.grid(row=0, column=0, columnspan=2)


    #frame per raccogliere campi riguardanti la connessione
    connection_frame = LabelFrame(connection_wdw, text="Inserisci i dati per la connessione al database")
    connection_frame.grid(row=1, column=0, padx=20)


    #labels per connessione al database
    host_connection_lbl = Label(connection_frame, text="Host")
    host_connection_lbl.grid(row=1, column=0, padx=20, pady=(10, 0), sticky=W)
    user_connection_lbl = Label(connection_frame, text="User")
    user_connection_lbl.grid(row=2, column=0, padx=20, sticky=W)
    password_connection_lbl = Label(connection_frame, text="Password")
    password_connection_lbl.grid(row=3, column=0, padx=20, sticky=W)
    database_connection_lbl = Label(connection_frame, text="Database")
    database_connection_lbl.grid(row=4, column=0, padx=20, pady=(0, 10), sticky=W)


    #entry fields per connessione al database
    host_connection_entry = Entry(connection_frame, width=30)
    host_connection_entry.grid(row=1, column=1, padx=(10, 50), pady=(10, 0))
    user_connection_entry = Entry(connection_frame, width=30)
    user_connection_entry.grid(row=2, column=1, padx=(10, 50))
    password_connection_entry = Entry(connection_frame, width=30)
    password_connection_entry.config(show="*")
    password_connection_entry.grid(row=3, column=1, padx=(10, 50))
    database_connection_entry = Entry(connection_frame, width=30)
    database_connection_entry.grid(row=4, column=1, padx=(10, 50), pady=(0, 10))


    #button per connessione al database
    connect_connection_btn = Button(connection_wdw, text="Connetti", command=connessione)
    connect_connection_btn.grid(row=2, column=0, columnspan=2, ipadx=50, pady=10)

def finestra_booking():

    def accedi(taxcode):
        global db
        
        def aggiorna(s):
            
            if s == "register":
                checkifempty_register = [len(TaxCode_register_entry.get()),
                                         len(PersonName_register_entry.get()),
                                         len(PersonSurame_register_entry.get()),
                                         len(BirthDate_register_dateentry.get()),
                                         len(Nationality_register_entry.get()),
                                         len(BirthPlace_register_entry.get()),
                                         len(Gender_register_combo.get()),
                                         len(ZipCode_register_entry.get()),
                                         len(StreetName_register_entry.get()),
                                         len(CivicNumber_register_entry.get())]

                flag1 = 0
                #print(checkifempty)
                for elem in checkifempty_register:
                    if elem != 0:
                        flag1 += 1
                #print(flag)

                if flag1==len(checkifempty_register):
                    Prenota_register_btn.config(state=NORMAL)
                else:
                    Prenota_register_btn.config(state=DISABLED)

            elif s == "booking":
                try:
                    FlightID_booking3_entry.config(state=NORMAL)
                    FlightID_booking3_entry.delete(0, END)
                    FlightID_booking3_entry.insert(END, flight_tree.item(flight_tree.focus())["values"][0])
                    FlightID_booking3_entry.config(state="readonly")
                except:
                    messagebox.showwarning("Errore", "Volo non selezionato")

                DocumentNumber_booking3_entry.config(state=NORMAL)
                DocumentNumber_booking3_entry.delete(0, END)
                DocumentNumber_booking3_entry.insert(END, SerialNumber_booking5_entry.get())
                DocumentNumber_booking3_entry.config(state="readonly")


                scadenza = Issuing_booking5_dateentry.get()
                scadenza = datetime.strptime(scadenza, "%Y-%m-%d").date()
                scadenza = scadenza + relativedelta(years=10)


                Expiry_booking5_entry.config(state=NORMAL)
                Expiry_booking5_entry.delete(0, END)
                Expiry_booking5_entry.insert(END, str(scadenza))
                Expiry_booking5_entry.config(state="readonly")


                checkifempty_booking = [len(flight_tree.item(flight_tree.focus())["values"]),
                                        len(SeatClass_booking3_combo.get()),
                                        len(SeatBoarding_booking3_combo.get()),
                                        len(SeatNumber_booking3_entry.get()),
                                        len(FlightID_booking3_entry.get()),
                                        len(DocumentNumber_booking3_entry.get()),
                                        len(NofTickets_booking4_entry.get()),
                                        len(PaymentMethod_booking4_combo.get()),
                                        len(SerialNumber_booking5_entry.get()),
                                        len(DocumentType_booking5_combo.get()),
                                        len(Municipality_booking5_entry.get()),
                                        len(Issuing_booking5_dateentry.get()),
                                        len(Expiry_booking5_entry.get()),
                                        len(BaggageType_booking6_combo.get()),
                                        len(Weight_booking6_entry.get())]

                flag2 = 0
                #print(checkifempty)
                for elem in checkifempty_booking:
                    if elem != 0:
                        flag2 += 1
                #print(flag)

                if flag2==len(checkifempty_booking):
                    Prenota_booking_btn.config(state=NORMAL)
                else:
                    Prenota_booking_btn.config(state=DISABLED)


        def insert(s):
            if s == "booking":
                mycursor.execute("INSERT INTO Booking_T (BookingID, BookingDate, BookingType, PaymentMethod, TicketCost, NofTickets, TaxCode) VALUES ('"
                                    + BookingID_booking4_entry.get() + "', '"
                                    + BookingDate_booking4_entry.get() + "', '"
                                    + BookingType_booking4_entry.get() + "', '"
                                    + PaymentMethod_booking4_combo.get() + "', '"
                                    + TicketCost_booking4_entry.get() + "', '"
                                    + NofTickets_booking4_entry.get() + "', '"
                                    + TaxCode_booking3_entry.get() + "')")
                
                mycursor.execute("INSERT INTO Document_T (SerialNumber, DocumentType, Municipality, Issuing, Expiry) VALUES ('"
                                    + SerialNumber_booking5_entry.get() + "', '"
                                    + DocumentType_booking5_combo.get() + "', '"
                                    + Municipality_booking5_entry.get() + "', '"
                                    + Issuing_booking5_dateentry.get() + "', '"
                                    + Expiry_booking5_entry.get() + "')")
                
                mycursor.execute("INSERT INTO Ticket_T (BarCode, SeatClass, SeatBoarding, SeatNumber, CheckIn, GateNumber, GateTerminal, GateClosingTime, TaxCode, FlightID, DocumentNumber, BookingID) VALUES ('"
                                    + BarCode_booking3_entry.get() + "', '"
                                    + SeatClass_booking3_combo.get() + "', '"
                                    + SeatBoarding_booking3_combo.get() + "', '"
                                    + SeatNumber_booking3_entry.get() + "', '"
                                    + CheckIn_booking3_entry.get() + "', '"
                                    + GateNumber_booking3_entry.get() + "', '"
                                    + GateTerminal_booking3_entry.get() + "', '"
                                    + GateClosingTime_booking3_entry.get() + "', '"
                                    + TaxCode_booking3_entry.get() + "', '"
                                    + FlightID_booking3_entry.get() + "', '"
                                    + DocumentNumber_booking3_entry.get() + "', '"
                                    + BookingID_booking3_entry.get() + "')")

                mycursor.execute("INSERT INTO Baggage_T (BaggageID, BaggageType, Weight, TicketBarCode) VALUES ('"
                                    + BaggageID_booking6_entry.get() + "', '"
                                    + BaggageType_booking6_combo.get() + "', '"
                                    + Weight_booking6_entry.get() + "', '"
                                    + BarCode_booking3_entry.get() + "')")

                messagebox.showinfo("Successo", "Prenotazione effettuata con successo")
                booking_wdw.destroy()

            elif s == "register":
                mycursor.execute("INSERT INTO Person_T (TaxCode, PersonName, PersonSurname, BirthDate, Nationality, BirthPlace, Gender, ZipCode, StreetName, CivicNumber, EmailAddress, PhoneNumber, Category) VALUES ('"
                                    + TaxCode_register_entry.get() + "', '"
                                    + PersonName_register_entry.get() + "', '"
                                    + PersonSurame_register_entry.get() + "', '"
                                    + BirthDate_register_dateentry.get() + "', '"
                                    + Nationality_register_entry.get() + "', '"
                                    + BirthPlace_register_entry.get() + "', '"
                                    + Gender_register_combo.get() + "', '"
                                    + ZipCode_register_entry.get() + "', '"
                                    + StreetName_register_entry.get() + "', '"
                                    + CivicNumber_register_entry.get() + "', '"
                                    + EmailAddress_register_entry.get() + "', '"
                                    + PhoneNumber_register_entry.get() + "', '"
                                    + Category_register_entry.get() + "')")
                
                mycursor.execute("INSERT INTO Passenger_T (PTaxCode) VALUES ('" + TaxCode_register_entry.get() + "')")
                
                messagebox.showinfo("Successo", "Registrazione effettuata con successo")
                booking_wdw.destroy()

        mycursor=db.cursor()
        
        mycursor.execute("SELECT COUNT(*) FROM Person_T WHERE TaxCode = '" + str(taxcode) + "'")
        supp = list()
        for x in mycursor:
            supp.append(x)

        if supp[0][0] == 0:
            res = messagebox.askyesno("Utente non registrato", "Desideri registrarti?")
            
            if res == True:            
                for widget in booking_wdw.winfo_children():
                    widget.destroy()

                booking_wdw.geometry("640x400")
                
                #frame registrazione
                register_frame = LabelFrame(booking_wdw, text="Registrati", width=620, height=320)
                register_frame.grid_propagate(0)
                register_frame.grid(row=0, column=0, padx=10)
            

                #label registrazione
                TaxCode_register_lbl = Label(register_frame, text="Codice fiscale")
                TaxCode_register_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)
                
                PersonName_register_lbl = Label(register_frame, text="Nome")
                PersonName_register_lbl.grid(row=1, column=0, padx=20, sticky=W)
                
                PersonSurame_register_lbl = Label(register_frame, text="Cognome")
                PersonSurame_register_lbl.grid(row=2, column=0, padx=20, sticky=W)
                
                BirthDate_register_lbl = Label(register_frame, text="Data di nascita")
                BirthDate_register_lbl.grid(row=3, column=0, padx=20, sticky=W)
                
                Nationality_register_lbl = Label(register_frame, text="Nazionalità")
                Nationality_register_lbl.grid(row=4, column=0, padx=20, sticky=W)
                
                BirthPlace_register_lbl = Label(register_frame, text="Luogo di nascita")
                BirthPlace_register_lbl.grid(row=5, column=0, padx=20, sticky=W)
                
                Gender_register_lbl = Label(register_frame, text="Sesso")
                Gender_register_lbl.grid(row=6, column=0, padx=20, sticky=W)
                
                ZipCode_register_lbl = Label(register_frame, text="CAP")
                ZipCode_register_lbl.grid(row=7, column=0, padx=20, sticky=W)
                
                StreetName_register_lbl = Label(register_frame, text="Via residenza")
                StreetName_register_lbl.grid(row=8, column=0, padx=20, sticky=W)
                
                CivicNumber_register_lbl = Label(register_frame, text="N° civico")
                CivicNumber_register_lbl.grid(row=9, column=0, padx=20, sticky=W)
                
                EmailAddress_register_lbl = Label(register_frame, text="Indirizzo email")
                EmailAddress_register_lbl.grid(row=10, column=0, padx=20, sticky=W)

                PhoneNumber_register_lbl = Label(register_frame, text="Numero di telefono")
                PhoneNumber_register_lbl.grid(row=11, column=0, padx=20, sticky=W)
                
                Category_register_lbl = Label(register_frame, text="Categoria")
                Category_register_lbl.grid(row=12, column=0, padx=20, pady=(0, 10), sticky=W)
                

                #entry fields e dateentry registrazione
                TaxCode_register_entry = Entry(register_frame, width=30)
                TaxCode_register_entry.grid(row=0, column=1, padx=20, pady=(10, 0))

                PersonName_register_entry = Entry(register_frame, width=30)
                PersonName_register_entry.grid(row=1, column=1, padx=20, sticky=W)
                
                PersonSurame_register_entry = Entry(register_frame, width=30)
                PersonSurame_register_entry.grid(row=2, column=1, padx=20, sticky=W)

                BirthDate_register_dateentry = DateEntry(register_frame, selectmode="day", state="readonly", date_pattern="yyyy-mm-dd", width=27)
                BirthDate_register_dateentry.grid(row=3, column=1, padx=20, sticky=W)

                Nationality_register_entry = Entry(register_frame, width=30)
                Nationality_register_entry.grid(row=4, column=1, padx=20, sticky=W)

                BirthPlace_register_entry = Entry(register_frame, width=30)
                BirthPlace_register_entry.grid(row=5, column=1, padx=20, sticky=W)
                
                genders = ["M", "F"]
                Gender_register_combo = ttk.Combobox(register_frame, values=genders, state="readonly", width=27)
                Gender_register_combo.grid(row=6, column=1, padx=20, sticky=W)

                ZipCode_register_entry = Entry(register_frame, width=30)
                ZipCode_register_entry.grid(row=7, column=1, padx=20, sticky=W)

                StreetName_register_entry = Entry(register_frame, width=30)
                StreetName_register_entry.grid(row=8, column=1, padx=20, sticky=W)

                CivicNumber_register_entry = Entry(register_frame, width=30)
                CivicNumber_register_entry.grid(row=9, column=1, padx=20, sticky=W)

                EmailAddress_register_entry = Entry(register_frame, width=30)
                EmailAddress_register_entry.grid(row=10, column=1, padx=20, sticky=W)

                PhoneNumber_register_entry = Entry(register_frame, width=30)
                PhoneNumber_register_entry.grid(row=11, column=1, padx=20, sticky=W)

                Category_register_entry = Entry(register_frame, width=30)
                Category_register_entry.insert(END, "P")
                Category_register_entry.config(state="readonly")
                Category_register_entry.grid(row=12, column=1, padx=20, pady=(0, 10), sticky=W)

                #buttons registrazione
                Aggiorna_register_btn = Button(booking_wdw, text="Aggiorna", command= lambda: aggiorna("register"))
                Aggiorna_register_btn.grid(row=2, column=0, columnspan=2, ipadx=30, pady=(10, 2))

                Prenota_register_btn = Button(booking_wdw, text="Registrati", command=lambda: insert("register"), state=DISABLED)
                Prenota_register_btn.grid(row=3, column=0, columnspan=2, ipadx=30, pady=(2, 10))

            else:
                booking_wdw.destroy()


        else:
            messagebox.showinfo("Successo", "Utente registrato")
            for widget in booking_wdw.winfo_children():
                widget.destroy()
            
            booking_wdw.geometry("1067x830")
            
            ############################################################ GENERAZIONE CODICI ############################################################
            
            #generazione casuale TicketBarCode
            mycursor.execute("SELECT BarCode FROM Ticket_T")

            supp = list()
            for x in mycursor:
                supp.append(x)

            used_barcodes = list()
            for i in range(len(supp)):
                used_barcodes.append(supp[i][0])


            ticketbarcode = "8 " + "" + str(random.randint(1000, 9999)) + " " + str(random.randint(10000, 99999))
            while True:
                if ticketbarcode in used_barcodes:
                    ticketbarcode = "8 " + "" + str(random.randint(1000, 9999)) + " " + str(random.randint(10000, 99999))        
                else:
                    break


            #generazione casuale BookingID
            mycursor.execute("SELECT BookingID FROM Booking_T")

            supp = list()
            for x in mycursor:
                supp.append(x)

            used_bookingids = list()
            for i in range(len(supp)):
                used_bookingids.append(supp[i][0])


            bookingid = str(random.randint(100000, 999999))
            while True:
                if bookingid in used_bookingids:
                    bookingid = str(random.randint(100000, 999999))
                else:
                    break


            #generazione casuale BaggageID
            mycursor.execute("SELECT BaggageID FROM Baggage_T")

            supp = list()
            for x in mycursor:
                supp.append(x)

            used_baggageids = list()
            for i in range(len(supp)):
                used_baggageids.append(supp[i][0])


            baggageid = "B-" + "" + str(random.randint(1000, 9999))
            while True:
                if baggageid in used_baggageids:
                    baggageid = "B-" + "" + str(random.randint(1000, 9999))
                else:
                    break

            ################################################################## FLIGHT ##################################################################

            mycursor = db.cursor()        
            mycursor.execute("SELECT FlightID, Departure, DepartureAirport, Arrival, ArrivalAirport FROM Flight_T WHERE Departure > " + "'" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "'" + "ORDER BY Departure")

            supp = list()
            for x in mycursor:
                supp.append(x)


            #frame prenotazione volo
            booking_frame2 = LabelFrame(booking_wdw, text="Prenota volo", width=1050, height=300)
            booking_frame2.grid_propagate(0)
            booking_frame2.grid(row=0, column=0, padx=10, columnspan=2)
            
            #tree prenotazione volo
            flight_tree = ttk.Treeview(booking_frame2)

            #definizione colonne
            flight_tree["columns"] = ("FlightID", "Departure", "DepartureAirport", "Arrival", "ArrivalAirport")

            #formattazione colonne
            flight_tree.column("#0", width=0, minwidth=0)
            flight_tree.column("FlightID", anchor=CENTER)
            flight_tree.column("Departure", anchor=CENTER)
            flight_tree.column("Arrival", anchor=CENTER)
            flight_tree.column("DepartureAirport", anchor=CENTER)
            flight_tree.column("ArrivalAirport", anchor=CENTER)

            #crea headings
            flight_tree.heading("#0", text="", anchor=CENTER)
            flight_tree.heading("FlightID", text="FlightID", anchor=CENTER)
            flight_tree.heading("Departure", text="Departure", anchor=CENTER)
            flight_tree.heading("Arrival", text="Arrival", anchor=CENTER)
            flight_tree.heading("DepartureAirport", text="DepartureAirport", anchor=CENTER)
            flight_tree.heading("ArrivalAirport", text="ArrivalAirport", anchor=CENTER)

            #aggiungi dati
            for i in range(len(supp)):
                flight_tree.insert(parent="", index="end", iid=i, text="", values=supp[i])

            flight_tree.grid(row=0, column=0, padx=20, pady=20)


            ############################################################## TICKET ##############################################################

            #frame dettagli biglietto
            booking_frame3 = LabelFrame(booking_wdw, text="Dettagli biglietto", width=520, height=450)
            booking_frame3.grid_propagate(0)
            booking_frame3.grid(row=1, column=0, rowspan=3, padx=(5, 0))

            #label dettagli biglietto
            BarCode_booking3_lbl = Label(booking_frame3, text="Codice biglietto")
            BarCode_booking3_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)

            SeatClass_booking3_lbl = Label(booking_frame3, text="Classe sedile")
            SeatClass_booking3_lbl.grid(row=1, column=0, padx=20, sticky=W)

            SeatBoarding_booking3_lbl = Label(booking_frame3, text="Lato sedile")
            SeatBoarding_booking3_lbl.grid(row=2, column=0, padx=20, sticky=W)

            SeatNumber_booking3_lbl = Label(booking_frame3, text="Numero sedile (1-75)")
            SeatNumber_booking3_lbl.grid(row=3, column=0, padx=20, sticky=W)

            CheckIn_booking3_lbl = Label(booking_frame3, text="Check-in")
            CheckIn_booking3_lbl.grid(row=4, column=0, padx=20, sticky=W)

            GateNumber_booking3_lbl = Label(booking_frame3, text="Numero gate")
            GateNumber_booking3_lbl.grid(row=5, column=0, padx=20, sticky=W)

            GateTerminal_booking3_lbl = Label(booking_frame3, text="Numero terminal")
            GateTerminal_booking3_lbl.grid(row=6, column=0, padx=20, sticky=W)

            GateClosingTime_booking3_lbl = Label(booking_frame3, text="Orario chiusura gate")
            GateClosingTime_booking3_lbl.grid(row=7, column=0, padx=20, sticky=W)

            TaxCode_booking3_lbl = Label(booking_frame3, text="Codice fiscale")
            TaxCode_booking3_lbl.grid(row=8, column=0, padx=20, sticky=W)

            FlightID_booking3_lbl = Label(booking_frame3, text="Codice volo")
            FlightID_booking3_lbl.grid(row=9, column=0, padx=20, sticky=W)

            DocumentNumber_booking3_lbl = Label(booking_frame3, text="Codice documento")
            DocumentNumber_booking3_lbl.grid(row=10, column=0, padx=20, sticky=W)

            BookingID_booking3_lbl = Label(booking_frame3, text="Codice prenotazione")
            BookingID_booking3_lbl.grid(row=11, column=0, padx=20, pady=(0, 10), sticky=W)

            #entry fields e combobox dettagli biglietto
            BarCode_booking3_entry = Entry(booking_frame3, width=30)
            BarCode_booking3_entry.insert(END, ticketbarcode)
            BarCode_booking3_entry.config(state="readonly")
            BarCode_booking3_entry.grid(row=0, column=1, padx=20, pady=(10, 0))

            seatclasses = ["First", "Business", "Economy"]
            SeatClass_booking3_combo = ttk.Combobox(booking_frame3, values=seatclasses, state="readonly", width=27)
            SeatClass_booking3_combo.grid(row=1, column=1, padx=20, sticky=W)

            seatboardings = ["Front", "Middle", "Back"]
            SeatBoarding_booking3_combo = ttk.Combobox(booking_frame3, values=seatboardings, state="readonly", width=27)
            SeatBoarding_booking3_combo.grid(row=2, column=1, padx=20, sticky=W)

            SeatNumber_booking3_entry = Entry(booking_frame3, width=30)
            SeatNumber_booking3_entry.grid(row=3, column=1, padx=20, sticky=W)
            
            CheckIn_booking3_entry = Entry(booking_frame3, width=30)
            CheckIn_booking3_entry.insert(END, "Online")
            CheckIn_booking3_entry.config(state="readonly")
            CheckIn_booking3_entry.grid(row=4, column=1, padx=20, sticky=W)

            GateNumber_booking3_entry = Entry(booking_frame3, width=30)
            GateNumber_booking3_entry.insert(END, "1")
            GateNumber_booking3_entry.config(state="readonly")
            GateNumber_booking3_entry.grid(row=5, column=1, padx=20, sticky=W)
            
            GateTerminal_booking3_entry = Entry(booking_frame3, width=30)
            GateTerminal_booking3_entry.insert(END, "1")
            GateTerminal_booking3_entry.config(state="readonly")
            GateTerminal_booking3_entry.grid(row=6, column=1, padx=20, sticky=W)
            
            GateClosingTime_booking3_entry = Entry(booking_frame3, width=30)
            GateClosingTime_booking3_entry.insert(END, "22:50")
            GateClosingTime_booking3_entry.config(state="readonly")
            GateClosingTime_booking3_entry.grid(row=7, column=1, padx=20, sticky=W)
            
            TaxCode_booking3_entry = Entry(booking_frame3, width=30)
            TaxCode_booking3_entry.insert(END, str(taxcode))
            TaxCode_booking3_entry.config(state="readonly")
            TaxCode_booking3_entry.grid(row=8, column=1, padx=20, sticky=W)
            
            FlightID_booking3_entry = Entry(booking_frame3, width=30, state="readonly")
            FlightID_booking3_entry.grid(row=9, column=1, padx=20, sticky=W)
            
            DocumentNumber_booking3_entry = Entry(booking_frame3, width=30, state="readonly")
            DocumentNumber_booking3_entry.grid(row=10, column=1, padx=20, sticky=W)
            
            BookingID_booking3_entry = Entry(booking_frame3, width=30)
            BookingID_booking3_entry.insert(END, str(bookingid))
            BookingID_booking3_entry.config(state="readonly")
            BookingID_booking3_entry.grid(row=11, column=1, padx=20, pady=(0, 10), sticky=W)


            ############################################################## BOOKING ##############################################################

            #frame inserimento dettagli booking
            booking_frame4 = LabelFrame(booking_wdw, text="Dettagli prenotazione", width=515, height=170)
            booking_frame4.grid_propagate(0)
            booking_frame4.grid(row=1, column=1)
            
            #label inserimento dettagli booking
            BookingID_booking4_lbl = Label(booking_frame4, text="Codice prenotazione")
            BookingID_booking4_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)

            BookingDate_booking4_lbl = Label(booking_frame4, text="Data prenotazione", anchor="w")
            BookingDate_booking4_lbl.grid(row=1, column=0, padx=20, sticky=W)

            BookingType_booking4_lbl = Label(booking_frame4, text="Tipo di prenotazione", anchor="w")
            BookingType_booking4_lbl.grid(row=2, column=0, padx=20, sticky=W)

            TicketCost_booking4_lbl = Label(booking_frame4, text="Prezzo biglietto", anchor="w")
            TicketCost_booking4_lbl.grid(row=3, column=0, padx=20, sticky=W)
            
            NofTickets_booking4_lbl = Label(booking_frame4, text="Numero di biglietti", anchor="w")
            NofTickets_booking4_lbl.grid(row=4, column=0, padx=20, sticky=W)

            PaymentMethod_booking4_lbl = Label(booking_frame4, text="Pagamento", anchor="w")
            PaymentMethod_booking4_lbl.grid(row=5, column=0, padx=20, pady=(0, 10), sticky=W)

            #entry fields dettagli booking
            BookingID_booking4_entry = Entry(booking_frame4, width=30)
            BookingID_booking4_entry.insert(END, bookingid)
            BookingID_booking4_entry.config(state="readonly")
            BookingID_booking4_entry.grid(row=0, column=1, padx=120, pady=(10, 0))
            
            BookingDate_booking4_entry = Entry(booking_frame4, width=30)
            BookingDate_booking4_entry.insert(END, str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            BookingDate_booking4_entry.config(state="readonly")
            BookingDate_booking4_entry.grid(row=1, column=1, padx=120)

            BookingType_booking4_entry = Entry(booking_frame4, width=30)
            BookingType_booking4_entry.insert(END, "Online")
            BookingType_booking4_entry.config(state="readonly")
            BookingType_booking4_entry.grid(row=2, column=1, padx=120)

            TicketCost_booking4_entry = Entry(booking_frame4, width=30)
            TicketCost_booking4_entry.insert(END, str(random.randrange(150, 300)))
            TicketCost_booking4_entry.config(state="readonly")
            TicketCost_booking4_entry.grid(row=3, column=1, padx=120)

            NofTickets_booking4_entry = Entry(booking_frame4, width=30)
            NofTickets_booking4_entry.grid(row=4, column=1, padx=120)
            
            paymentmethods = ["Credit Card", "Bank Transfer"]
            PaymentMethod_booking4_combo = ttk.Combobox(booking_frame4, values=paymentmethods, state="readonly", width=27)
            PaymentMethod_booking4_combo.grid(row=5, column=1, padx=120, pady=(0, 10), sticky=W)


            ############################################################## DOCUMENT ##############################################################

            #frame inserimento documento
            booking_frame5 = LabelFrame(booking_wdw, text="Inserisci documento", width=515, height=160)
            booking_frame5.grid_propagate(0)
            booking_frame5.grid(row=2, column=1)
            
            #label inserimento documento
            SerialNumber_booking5_lbl = Label(booking_frame5, text="Codice documento")
            SerialNumber_booking5_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)

            DocumentType_booking5_lbl = Label(booking_frame5, text="Tipo documento")
            DocumentType_booking5_lbl.grid(row=1, column=0, padx=20, sticky=W)
            
            Municipality_booking5_lbl = Label(booking_frame5, text="Comune di rilascio")
            Municipality_booking5_lbl.grid(row=2, column=0, padx=20, sticky=W)

            Issuing_booking5_lbl = Label(booking_frame5, text="Data di rilascio")
            Issuing_booking5_lbl.grid(row=3, column=0, padx=20, sticky=W)
            
            Expiry_booking5_lbl = Label(booking_frame5, text="Data di scadenza")
            Expiry_booking5_lbl.grid(row=4, column=0, padx=20, pady=(0, 10), sticky=W)
            
            #entry fields inserimento documento
            SerialNumber_booking5_entry = Entry(booking_frame5, width=30)
            SerialNumber_booking5_entry.grid(row=0, column=1, padx=127, pady=(10, 0))
            
            documenttypes = ["Passport", "Identity Card", "Driving License"]
            DocumentType_booking5_combo = ttk.Combobox(booking_frame5, values=documenttypes, state="readonly", width=27)
            DocumentType_booking5_combo.grid(row=1, column=1, padx=127, sticky=W)
            
            Municipality_booking5_entry = Entry(booking_frame5, width=30)
            Municipality_booking5_entry.grid(row=2, column=1, padx=127)

            Issuing_booking5_dateentry = DateEntry(booking_frame5, selectmode="day", state="readonly", date_pattern="yyyy-mm-dd", width=27)
            Issuing_booking5_dateentry.grid(row=3, column=1, padx=127)

            Expiry_booking5_entry = Entry(booking_frame5, state="readonly", width=30)
            Expiry_booking5_entry.grid(row=4, column=1, padx=127, pady=(0, 10))


            ############################################################## BAGGAGE ##############################################################

            #frame inserimento bagagli
            booking_frame6 = LabelFrame(booking_wdw, text="Inserisci bagagli", width=515, height=120)
            booking_frame6.grid_propagate(0)
            booking_frame6.grid(row=3, column=1)

            #label inserimento bagagli
            BaggageID_booking6_lbl = Label(booking_frame6, text="Codice bagaglio")
            BaggageID_booking6_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)
            
            BaggageType_booking6_lbl = Label(booking_frame6, text="Tipo di bagaglio")
            BaggageType_booking6_lbl.grid(row=1, column=0, padx=20, sticky=W)
            
            Weight_booking6_lbl = Label(booking_frame6, text="Peso del bagaglio (kg)")
            Weight_booking6_lbl.grid(row=2, column=0, padx=20, pady=(0, 10), sticky=W)

            #entry fields inserimento bagagli
            BaggageID_booking6_entry = Entry(booking_frame6, width=30)
            BaggageID_booking6_entry.insert(END, baggageid)
            BaggageID_booking6_entry.config(state="readonly")
            BaggageID_booking6_entry.grid(row=0, column=1, padx=137, pady=(10, 0))
            
            baggagetypes = ["Checked", "Carry-on"]
            BaggageType_booking6_combo = ttk.Combobox(booking_frame6, values=baggagetypes, state="readonly", width=27)
            BaggageType_booking6_combo.grid(row=1, column=1, padx=137, sticky=W)

            Weight_booking6_entry = Entry(booking_frame6, width=30)
            Weight_booking6_entry.grid(row=2, column=1, padx=137, pady=(0, 10))


            #############################################################################################################################################

            #button caricamento dati
            Aggiorna_booking_btn = Button(booking_wdw, text="Aggiorna", command=lambda: aggiorna("booking"))
            Aggiorna_booking_btn.grid(row=4, column=0, columnspan=2, ipadx=30, pady=(10, 2))

            Prenota_booking_btn = Button(booking_wdw, text="Prenota", command=lambda: insert("booking"), state=DISABLED)
            Prenota_booking_btn.grid(row=5, column=0, columnspan=2, ipadx=34, pady=(2, 10))

    booking_wdw = Tk()
    booking_wdw.title("ArovAIR: Prenota un volo")
    booking_wdw.iconbitmap(os.path.dirname(__file__) + "\\ArovAIR_icon.ico")
    booking_wdw.geometry("370x110")

    booking_frame = LabelFrame(booking_wdw, text="Sei già registrato?", width=350, height=70)
    booking_frame.grid_propagate(0)
    booking_frame.grid(row=0, column=0, padx=10)
    
    TaxCode_booking_frame_lbl = Label(booking_frame, text="Codice fiscale")
    TaxCode_booking_frame_lbl.grid(row=0, column=0, padx=20, sticky=W)

    TaxCode_booking_frame_entry = Entry(booking_frame, width=30)
    TaxCode_booking_frame_entry.grid(row=0, column=1, padx=20, pady=(10, 5))

    Check_booking_frame_btn = Button(booking_wdw, text="Accedi", command=lambda: accedi(TaxCode_booking_frame_entry.get()))
    Check_booking_frame_btn.grid(row=1, column=0, columnspan=2, pady=5, ipadx=10)

def finestra_ticket():

    def view_ticket(ticketbarcode):
        mycursor = db.cursor()

        mycursor.execute("SELECT BarCode FROM Ticket_T")

        supp = list()
        for x in mycursor:
            supp.append(x[0])
        
        if ticketbarcode in supp:
            for widget in ticket_wdw.winfo_children():
                widget.destroy()

            mycursor.execute('''SELECT BarCode AS TicketCode, Ticket_T.FlightID, PersonName AS 'Name', PersonSurname AS Surname, 
                                Departure, DepartureAirport, A1.City AS DepartureCity, A1.Nation AS DepartureNation, 
                                Arrival, ArrivalAirport, A2.City AS ArrivalCity, A2.Nation AS ArrivalNation, SeatClass, SeatBoarding, 
                                SeatNumber, GateNumber AS Gate, GateTerminal AS Terminal, GateClosingTime
	                                FROM Ticket_T INNER JOIN Person_T ON Ticket_T.TaxCode=Person_T.TaxCode
	                                    INNER JOIN Flight_T ON Ticket_T.FlightID=Flight_T.FlightID
                                        INNER JOIN Airport_T AS A1 ON Flight_T.DepartureAirport = A1.AirportCode
                                        INNER JOIN Airport_T AS A2 ON Flight_T.ArrivalAirport = A2.AirportCode
                                                WHERE BarCode=\'''' + ticketbarcode + "'")

            supp = list()
            for x in mycursor:
                supp.append(x)
            
            ticket_wdw.geometry("490x440")

            TicketDetails_frame = LabelFrame(ticket_wdw, text="Dettagli biglietto", width=470, height=400)
            TicketDetails_frame.grid_propagate(0)
            TicketDetails_frame.grid(row=0, column=0, padx=10)


            #label ticket details
            FlightID_ticket_lbl = Label(TicketDetails_frame, text="FlightID")
            FlightID_ticket_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)

            Name_ticket_lbl = Label(TicketDetails_frame, text="Nome")
            Name_ticket_lbl.grid(row=1, column=0, padx=20, sticky=W)

            Surname_ticket_lbl = Label(TicketDetails_frame, text="Cognome")
            Surname_ticket_lbl.grid(row=2, column=0, padx=20, sticky=W)

            DepartureDateTime_ticket_lbl = Label(TicketDetails_frame, text="Data e ora di partenza")
            DepartureDateTime_ticket_lbl.grid(row=3, column=0, padx=20, sticky=W)

            DepartureAirport_ticket_lbl = Label(TicketDetails_frame, text="Aereoporto di partenza")
            DepartureAirport_ticket_lbl.grid(row=4, column=0, padx=20, sticky=W)

            DepartureCity_ticket_lbl = Label(TicketDetails_frame, text="Città di partenza")
            DepartureCity_ticket_lbl.grid(row=5, column=0, padx=20, sticky=W)

            DepartureNation_ticket_lbl = Label(TicketDetails_frame, text="Nazione di partenza")
            DepartureNation_ticket_lbl.grid(row=6, column=0, padx=20, sticky=W)

            ArrivalDateTime_ticket_lbl = Label(TicketDetails_frame, text="Data e ora di partenza")
            ArrivalDateTime_ticket_lbl.grid(row=7, column=0, padx=20, sticky=W)

            ArrivalAirport_ticket_lbl = Label(TicketDetails_frame, text="Aereoporto di arrivo")
            ArrivalAirport_ticket_lbl.grid(row=8, column=0, padx=20, sticky=W)

            ArrivalCity_ticket_lbl = Label(TicketDetails_frame, text="Città di arrivo")
            ArrivalCity_ticket_lbl.grid(row=9, column=0, padx=20, sticky=W)

            ArrivalNation_ticket_lbl = Label(TicketDetails_frame, text="Nazione di arrivo")
            ArrivalNation_ticket_lbl.grid(row=10, column=0, padx=20, sticky=W)

            SeatClass_ticket_lbl = Label(TicketDetails_frame, text="Classe sedile")
            SeatClass_ticket_lbl.grid(row=11, column=0, padx=20, sticky=W)

            SeatBoarding_ticket_lbl = Label(TicketDetails_frame, text="Lato sedile")
            SeatBoarding_ticket_lbl.grid(row=12, column=0, padx=20, sticky=W)

            SeatNumber_ticket_lbl = Label(TicketDetails_frame, text="Numero sedile")
            SeatNumber_ticket_lbl.grid(row=13, column=0, padx=20, sticky=W)
            
            Gate_ticket_lbl = Label(TicketDetails_frame, text="Numero gate")
            Gate_ticket_lbl.grid(row=14, column=0, padx=20, sticky=W)

            Terminal_ticket_lbl = Label(TicketDetails_frame, text="Numero terminal")
            Terminal_ticket_lbl.grid(row=15, column=0, padx=20, sticky=W)

            GateClosingTime_ticket_lbl = Label(TicketDetails_frame, text="Orario di chiusura gate")
            GateClosingTime_ticket_lbl.grid(row=16, column=0, padx=20, pady=(0, 10), sticky=W)


            #entry fields ticket details
            FlightID_ticket_entry = Entry(TicketDetails_frame, width=30)
            FlightID_ticket_entry.insert(END, supp[0][1])
            FlightID_ticket_entry.config(state="readonly")
            FlightID_ticket_entry.grid(row=0, column=1, padx=20, pady=(10, 0))

            Name_ticket_entry = Entry(TicketDetails_frame, width=30)
            Name_ticket_entry.insert(END, supp[0][2])
            Name_ticket_entry.config(state="readonly")
            Name_ticket_entry.grid(row=1, column=1, padx=20)

            Surname_ticket_entry = Entry(TicketDetails_frame, width=30)
            Surname_ticket_entry.insert(END, supp[0][3])
            Surname_ticket_entry.config(state="readonly")
            Surname_ticket_entry.grid(row=2, column=1, padx=20)

            DepartureDateTime_ticket_entry = Entry(TicketDetails_frame, width=30)
            DepartureDateTime_ticket_entry.insert(END, supp[0][4])
            DepartureDateTime_ticket_entry.config(state="readonly")
            DepartureDateTime_ticket_entry.grid(row=3, column=1, padx=20)

            DepartureAirport_ticket_entry = Entry(TicketDetails_frame, width=30)
            DepartureAirport_ticket_entry.insert(END, supp[0][5])
            DepartureAirport_ticket_entry.config(state="readonly")
            DepartureAirport_ticket_entry.grid(row=4, column=1, padx=20)

            DepartureCity_ticket_entry = Entry(TicketDetails_frame, width=30)
            DepartureCity_ticket_entry.insert(END, supp[0][6])
            DepartureCity_ticket_entry.config(state="readonly")
            DepartureCity_ticket_entry.grid(row=5, column=1, padx=20)

            DepartureNation_ticket_entry = Entry(TicketDetails_frame, width=30)
            DepartureNation_ticket_entry.insert(END, supp[0][7])
            DepartureNation_ticket_entry.config(state="readonly")
            DepartureNation_ticket_entry.grid(row=6, column=1, padx=20)

            ArrivalDateTime_ticket_entry = Entry(TicketDetails_frame, width=30)
            ArrivalDateTime_ticket_entry.insert(END, supp[0][8])
            ArrivalDateTime_ticket_entry.config(state="readonly")
            ArrivalDateTime_ticket_entry.grid(row=7, column=1, padx=20)

            ArrivalAirport_ticket_entry = Entry(TicketDetails_frame, width=30)
            ArrivalAirport_ticket_entry.insert(END, supp[0][9])
            ArrivalAirport_ticket_entry.config(state="readonly")
            ArrivalAirport_ticket_entry.grid(row=8, column=1, padx=20)

            ArrivalCity_ticket_entry = Entry(TicketDetails_frame, width=30)
            ArrivalCity_ticket_entry.insert(END, supp[0][10])
            ArrivalCity_ticket_entry.config(state="readonly")
            ArrivalCity_ticket_entry.grid(row=9, column=1, padx=20)

            ArrivalNation_ticket_entry = Entry(TicketDetails_frame, width=30)
            ArrivalNation_ticket_entry.insert(END, supp[0][11])
            ArrivalNation_ticket_entry.config(state="readonly")
            ArrivalNation_ticket_entry.grid(row=10, column=1, padx=20)

            SeatClass_ticket_entry = Entry(TicketDetails_frame, width=30)
            SeatClass_ticket_entry.insert(END, supp[0][12])
            SeatClass_ticket_entry.config(state="readonly")
            SeatClass_ticket_entry.grid(row=11, column=1, padx=20)

            SeatBoarding_ticket_entry = Entry(TicketDetails_frame, width=30)
            SeatBoarding_ticket_entry.insert(END, supp[0][13])
            SeatBoarding_ticket_entry.config(state="readonly")
            SeatBoarding_ticket_entry.grid(row=12, column=1, padx=20)

            SeatNumber_ticket_entry = Entry(TicketDetails_frame, width=30)
            SeatNumber_ticket_entry.insert(END, supp[0][14])
            SeatNumber_ticket_entry.config(state="readonly")
            SeatNumber_ticket_entry.grid(row=13, column=1, padx=20)

            Gate_ticket_entry = Entry(TicketDetails_frame, width=30)
            Gate_ticket_entry.insert(END, supp[0][15])
            Gate_ticket_entry.config(state="readonly")
            Gate_ticket_entry.grid(row=14, column=1, padx=20)

            Terminal_ticket_entry = Entry(TicketDetails_frame, width=30)
            Terminal_ticket_entry.insert(END, supp[0][16])
            Terminal_ticket_entry.config(state="readonly")
            Terminal_ticket_entry.grid(row=15, column=1, padx=20)

            GateClosingTime_ticket_entry = Entry(TicketDetails_frame, width=30)
            GateClosingTime_ticket_entry.insert(END, supp[0][17])
            GateClosingTime_ticket_entry.config(state="readonly")
            GateClosingTime_ticket_entry.grid(row=16, column=1, padx=20, pady=(0, 10))
            

            #button per chiudere la finestra
            close_ticket_wdw_btn = Button(ticket_wdw, text="Esci", command=ticket_wdw.destroy)
            close_ticket_wdw_btn.grid(row=1, column=0, ipadx=25, pady=(0, 10))

        else:
            messagebox.showerror("Errore", "Biglietto inesistente")
        

    ticket_wdw = Tk()
    ticket_wdw.title("ArovAIR: Visualizza biglietto")
    ticket_wdw.iconbitmap(os.path.dirname(__file__) + "\\ArovAIR_icon.ico")
    ticket_wdw.geometry("370x110")

    ticket_frame = LabelFrame(ticket_wdw, text="Inserisci il codice biglietto", width=350, height=70)
    ticket_frame.grid_propagate(0)
    ticket_frame.grid(row=0, column=0, padx=10)

    TicketCode_ticket_lbl = Label(ticket_frame, text="Codice biglietto")
    TicketCode_ticket_lbl.grid(row=0, column=0, padx=20, sticky=W)

    TicketCode_ticket_entry = Entry(ticket_frame, width=30)
    TicketCode_ticket_entry.grid(row=0, column=1, padx=20, pady=10)

    Visualizza_btn = Button(ticket_wdw, text="Visualizza", command=lambda: view_ticket(TicketCode_ticket_entry.get()))
    Visualizza_btn.grid(row=1, column=0, padx=20, pady=5, columnspan=2)


def finestra_flight():
    mycursor = db.cursor()
    
    mycursor.execute("SELECT FlightID, Departure, DepartureAirport, Arrival, ArrivalAirport FROM Flight_T WHERE Departure > " + "'" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "'" + "ORDER BY Departure")

    supp = list()
    for x in mycursor:
        supp.append(x)

    flight_wdw = Tk()
    flight_wdw.title("ArovAIR: Visualizza voli")
    flight_wdw.iconbitmap(os.path.dirname(__file__) + "\\ArovAIR_icon.ico")
    flight_wdw.geometry("1055x290")

    flight_tree = ttk.Treeview(flight_wdw)

    #definizione colonne
    flight_tree["columns"] = ("FlightID", "Departure", "DepartureAirport", "Arrival", "ArrivalAirport")

    #formattazione colonne
    flight_tree.column("#0", width=0, minwidth=0)
    flight_tree.column("FlightID", anchor=CENTER)
    flight_tree.column("Departure", anchor=CENTER)
    flight_tree.column("Arrival", anchor=CENTER)
    flight_tree.column("DepartureAirport", anchor=CENTER)
    flight_tree.column("ArrivalAirport", anchor=CENTER)

    #crea headings
    flight_tree.heading("#0", text="", anchor=CENTER)
    flight_tree.heading("FlightID", text="FlightID", anchor=CENTER)
    flight_tree.heading("Departure", text="Departure", anchor=CENTER)
    flight_tree.heading("Arrival", text="Arrival", anchor=CENTER)
    flight_tree.heading("DepartureAirport", text="DepartureAirport", anchor=CENTER)
    flight_tree.heading("ArrivalAirport", text="ArrivalAirport", anchor=CENTER)

    #aggiungi dati
    for i in range(len(supp)):
        flight_tree.insert(parent="", index="end", iid=i, text="", values=supp[i])

    flight_tree.grid(row=0, column=0, padx=20, pady=10)
    close_flight_wdw_btn = Button(flight_wdw, text="Esci", command=flight_wdw.destroy)
    close_flight_wdw_btn.grid(row=1, column=0, ipadx=25, pady=(0, 10))

###########################################################################################################################################################################
#finestra per menu principale
menu_wdw = Tk()
menu_wdw.title("ArovAIR: Menu")
menu_wdw.iconbitmap(os.path.dirname(__file__) + "\\ArovAIR_icon.ico")
menu_wdw.geometry("320x240")


conn = BooleanVar()
conn = FALSE


welcome_connection_lbl = Label(menu_wdw, text="Benvenuto su ArovAIR", font="Times 20 italic bold")
welcome_connection_lbl.grid(row=0, column=0, columnspan=2, padx=10)

#frame scelta menu
menu_frame = LabelFrame(menu_wdw, text="Cosa vuoi fare?", width=280, height=160)
menu_frame.grid_propagate(0)
menu_frame.grid(row=1, column=0, padx=20)

#label scelta menu
connect_menu_lbl = Label(menu_frame, text="Connetti al database")
connect_menu_lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky=W)
booking_menu_lbl = Label(menu_frame, text="Prenota un volo")
booking_menu_lbl.grid(row=1, column=0, padx=20, sticky=W)
ticket_menu_lbl = Label(menu_frame, text="Visualizza biglietto")
ticket_menu_lbl.grid(row=2, column=0, padx=20, sticky=W)
flights_menu_lbl = Label(menu_frame, text="Visualizza voli")
flights_menu_lbl.grid(row=3, column=0, padx=20, pady=(0, 10), sticky=W)

#button scelta menu
connect_menu_btn = Button(menu_frame, text="Connetti", command=finestra_connessione)
connect_menu_btn.grid(row=0, column=1, padx=20, pady=(10, 2), ipadx=1)
booking_menu_btn = Button(menu_frame, text="Prenota", command=finestra_booking, state=DISABLED)
booking_menu_btn.grid(row=1, column=1, padx=20, pady=2, ipadx=4)
ticket_menu_btn = Button(menu_frame, text="Visualizza", command=finestra_ticket, state=DISABLED)
ticket_menu_btn.grid(row=2, column=1, padx=20, pady=2)
flights_menu_btn = Button(menu_frame, text="Visualizza", command=finestra_flight, state=DISABLED)
flights_menu_btn.grid(row=3, column=1, padx=20, pady=(2, 10))

#button chiudi programma
close_menu_btn = Button(menu_wdw, text="Esci", command=menu_wdw.quit)
close_menu_btn.grid(row=2, column=0, pady=5, ipadx=25)


menu_wdw.mainloop()