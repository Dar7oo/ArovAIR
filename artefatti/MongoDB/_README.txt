Per l'esportazione dei dati in formato json ed il loro caricamento in MongoDB, è stato effettuato l'embedding delle tabelle Person_T, Employee_T e Passenger_T.

I seguenti file contengono le seguenti informazioni:
	- Person_T_EMB:				clienti e passeggeri
	- Flight_Personnel_T_EMB: 		personale di volo
	- Land_Personnel_T_EMB: 		personale di terra

Per effetto della denormalizzazione provocata dall'embedding effettuato su queste tabelle, gli attributi della tabella Employee_T si trovano in Flight_Personnel_T_EMB ed Land_Personnel_T_EMB quindi Employee_T viene eliminata.