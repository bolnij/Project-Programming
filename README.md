# Mājasdarbu Pārvaldības Sistēma 

Lietotne, kas izstrādāta ar Flask ietvaru, lai palīdzētu skolēniem un studentiem organizēt savus mājasdarbus. Projekts ietver lietotāju reģistrāciju, uzdevumu pievienošanu, prioritāšu noteikšanu un termiņu kontroli.

## Galvenās Funkcijas 
- **Lietotāju Autentifikācija**: Droša reģistrācija un pieteikšanās ar paroļu hešēšanu.
- **Uzdevumu Pārvaldība (CRUD)**: Pievieno, apskati, rediģē un dzēs mājasdarbus.
- **Datu Apstrāde un Loģika**:
  - Automātiska termiņu kontrole (kavēto darbu izcelšana).
  - Uzdevumu filtrēšana pēc statusa (Visi, Aktīvie, Izpildītie).
  - Meklēšanas funkcija pēc priekšmeta vai uzdevuma.
- **Prioritātes**: Iespēja atzīmēt svarīgus darbus ar ⭐ simbolu.
- **Dizains**: Moderna saskarne ar Gaišo un Tumšo režīmu (tēmas saglabāšana pārlūkā).
- **Admin Panelis**: Sistēmas statistikas pārskats administratoriem.

## Tehnoloģijas 
- **Python / Flask**: Servera puses loģika.
- **SQLite**: Relāciju datubāze lietotāju un darbu glabāšanai.
- **HTML5 / CSS3**: Responsīvs dizains ar mainīgajiem (CSS variables).
- **JavaScript**: Dinamiska tēmu pārslēgšana.

## Uzstādīšana 
1. Instalējiet Python bibliotēkas:
   ```bash
   pip install flask werkzeug
