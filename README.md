# ClientServerApp
Implementare aplicatie de tip client-server, in care clientul itereaza directoare/subdirectoare/fisiere si trimite o lista cu toate path-urile fisierelor gasite catre server. Serverul preia aceasta informatie si ulterior transmite date despre fiecare fisier regasit in acea lista. 
Repo-ul conține două scripturi - `server.py` și `client.py` - care permit transferul de informații despre fișiere prin sockets între client si server t utilizând conexiunea TCP/IP. Serverul primește lista de paths către fișiere de la client, prelucrează fiecare fișier și trimite înapoi detalii despre fiecare fișier.

## Server (`server.py`)

`server.py` este responsabil pentru gestionarea conexiunii și prelucrarea fișierelor trimise de la client. Detaliile fiecărui fișier, cum ar fi numele, dimensiunea, hash-ul MD5 și datele de creare sau modificare vor fi afisate in output

## Client (`client.py`)

`client.py` este responsabil pentru trimiterea listei cu path-ul fișierelor către server.

### Instrucțiuni de rulare

1. Deschide un terminal și navigheaza la directorul în care se află scriptul `server.py`.
2. Asigura-te ca toate dependintele din server.py si client.py sunt instalate, altfel deschide un terminal si instaleaza-le folosind comanda 'pip install' . Ex: " pip install psutil"
3. Executa comanda: `python server.py`.
4. Serverul va asculta pe adresa IP `127.0.0.1` și portul `555` (in cazul de fata serverul si clientul sunt in aceeasi retea), in cazul in care sunt in retele   
   diferite trebuie adaugate IP-urile si porturile specifice. 
5. Deschide un al doilea terminal și navigheaza la directorul în care se află scriptul `client.py`.
6. Modifica variabila `iterare_path` în codul `client.py` pentru a specifica directorul de unde se itereaza fișierele.
7. Executa comanda: `python client.py`.
8. Output-ul din terminalul serverului va contine informatiile descrise mai sus, apoi se inchide sesiunea cu clientul. 
