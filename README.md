# Mājasdarbu Pārvaldības Sistēma 

Lietotne, kas izstrādāta ar Flask ietvaru, lai palīdzētu skolēniem un studentiem organizēt savus mājasdarbus. Projekts ietver lietotāju reģistrāciju, uzdevumu pievienošanu, prioritāšu noteikšanu un termiņu kontroli.

## Galvenās Funkcijas 
- **Lietotāju Autentifikācija**: Droša reģistrācija un pieteikšanās ar paroļu hešēšanu.
- **Uzdevumu Pārvaldība (CRUD)**: Pievieno, apskati, rediģē un dzēs mājasdarbus.
- **Datu Apstrāde un Loģika**:
  - Automātiska termiņu kontrole (kavēto darbu izcelšana).
  - Uzdevumu filtrēšana pēc statusa (Visi, Aktīvie, Izpildītie).
  - Mekлēšanas funkcija pēc priekšmeta vai uzdevuma.
- **Prioritātes**: Iespēja atzīmēt svarīgus darbus ar ⭐ simbolu.
- **Dizains**: Moderna saskarne ar Gaišo un Tumšo režīmu.
- **Admin Panelis**: Sistēmas statistikas pārskats administratoriem.

## Projekta struktūra un failu apraksts
- **app.py**: Galvenais servera puses fails, kas nodrošina maršrutēšanu un datu apstrādes loģiku.
- **database.db**: SQLite datubāze, kurā tiek glabāti lietotāju konti un uzdevumi.
- **static/**: Mape ar statiskajiem failiem:
    - **style_2.css**: Definē vizuālo izskatu un tumšās tēmas loģiku.
    - **script.js**: JavaScript kods interaktīvai tēmu pārslēgšanai.
- **templates/**: HTML veidnes (base.html, index.html, login.html, register.html).

## Tehnoloģijas 
- **Python / Flask**: Servera puses loģika.
- **SQLite**: Relāciju datubāze datu glabāšanai.
- **HTML5 / CSS3**: Responsīvs dizains ar CSS mainīgajiem.
- **JavaScript**: Dinamiska tēmu pārslēgšana.

## Uzstādīšana 
1. Instalējiet nepieciešamās bibliotēkas:
   ```bash
   pip install flask werkzeug
