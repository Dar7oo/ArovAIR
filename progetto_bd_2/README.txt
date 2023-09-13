Il programma python chiamato "main.py" utilizza le seguenti librerie:
	- mysql-connector-python, per l'interazione con sql
	- tkinter, per implementare le funzionalità grafiche
	- tkcalendar
	- python-dateutil

Per la loro installazione, eseguire le seguenti istruzioni nel prompt dei comandi
	- pip install mysql-connector-python
	- pip install tkinter
	- pip install tkcalendar
	- pip install python-dateutil




Le query eseguite dal programma python sono le seguenti:
	- inserimento prenotazione					(righe 183...190)
	- inserimento documento						(righe 192...197)
	- inserimento biglietto						(righe 199...211)
	- inserimento bagaglio						(righe 213...217)
	- inserimento persona						(righe 223...236)
	- inserimento passeggeto					(riga 238)
	- conteggio passeggero con codice fiscale			(riga 245)
	- selezione codici biglietti					(riga 370, 729)
	- selezione codici prenotazioni					(riga 390)
	- selezione codici bagagli					(riga 410)
	- selezione voli disponibili					(riga 431, 930)
	- selezione informazioni biglietto				(righe 739...747)



Nota: nel seguire la procedura di esportazione del database descritta nel documento presentato, le clausole insert per l'inserimento dei dati non venivano generate. Per questo motivo, abbiamo inserito manualmente le nostre insert alla fine dello script project_db_2.sql. Inoltre, qualora questo non fosse necessario, abbiamo caricato separatamente il file con le insert, chiamato "Inserimento dati Arovair.sql".

Nota: nel programma python non sono stati effettuati controlli sugli input inseriti dagli utenti. Si consiglia di inserire dati appropriati (ad esempio, non inserire cifre in un campo che richiede lettere oppure non inserire stringhe di testo eccessivamente lunghe).

Nota: prima di confermare la prenotazione del volo nel programma python, copiare il codice ticket in modo da poterlo usare per la funzionalità che visualizza le informazioni del biglietto
