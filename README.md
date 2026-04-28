# Mājasdarbu Pārvaldības Sistēma 

Lietotne, kas izstrādāta ar Flask ietvaru, lai palīdzētu skolēniem un studentiem organizēt savus mājasdarbus. Projekts ietver lietotāju reģistrāciju, uzdevumu pievienošanu, prioritāšu noteikšanu un termiņu kontroli[cite: 1, 2].

## Galvenās Funkcijas 
- **Lietotāju Autentifikācija**: Droša reģistrācija un pieteikšanās ar paroļu hešēšanu[cite: 1, 2].
- **Uzdevumu Pārvaldība (CRUD)**: Pievieno, apskati, rediģē un dzēs mājasdarbus[cite: 1, 2].
- **Datu Apstrāde un Loģika**:
  - Automātiska termiņu kontrole (kavēto darbu izcelšana)[cite: 1, 2].
  - Uzdevumu filtrēšana pēc statusa (Visi, Aktīvie, Izpildītie)[cite: 1, 2].
  - Meklēšanas funkcija pēc priekšmeta vai uzdevuma[cite: 1, 2].
- **Prioritātes**: Iespēja atzīmēt svarīgus darbus ar ⭐ simbolu[cite: 1, 2].
- **Dizains**: Moderna saskarne ar Gaišo un Tumšo režīmu (tēmas saglabāšana pārlūkā)[cite: 1, 2].
- **Admin Panelis**: Sistēmas statistikas pārskats administratoriem[cite: 1, 2].

## Projekta struktūra un failu apraksts
- **app.py**: Galvenais servera puses fails, kas nodrošina maršrutēšanu un datu apstrādes loģiku.
- **database.db**: SQLite datubāze, kurā tiek glabāti lietotāju konti un uzdevumi.
- **static/**: Mape ar statiskajiem failiem:
    - **style_2.css**: Definē vizuālo izskatu un tumšās tēmas loģiku.
    - **script.js**: JavaScript kods interaktīvai tēmu pārslēgšanai.
- **templates/**: HTML veidnes (base.html, index.html, login.html, register.html).

## Tehnoloģijas 
- **Python / Flask**: Servera puses loģika[cite: 1, 2].
- **SQLite**: Relāciju datubāze datu glabāšanai[cite: 1, 2].
- **HTML5 / CSS3**: Responsīvs dizains ar CSS mainīgajiem[cite: 1, 2].
- **JavaScript**: Dinamiska tēmu pārslēgšana[cite: 1, 2].

## Uzstādīšana 
1. Instalējiet nepieciešamās bibliotēkas:
   ```bash
   pip install flask werkzeug
