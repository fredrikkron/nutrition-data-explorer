# Affärsidé

I en vardag fylld av stress och höga krav söker allt fler sätt att upprätthålla energinivån för att känna sig stark genom hela dagen. Många vet att maten är en avgörande faktor men det är svårt att förstå vad som faktiskt är bra eller dåligt för hälsan. Informationsdjungeln gör det komplicerat och innehållsförteckningar är svårlästa vilket gör besluten överväldigande.
Näringsportalen samlar och visualiserar näringsvärden på ett informativt sätt för användaren. Det ska vara lätt att välja livsmedel som gynnar hälsan och smakar gott för att bygga en fungerande vardag.

<br>

# Projektmålet

Att skapa en dashboard som visualiserar och förenklar förståelsen av livsmedels näringsvärden. Genom smarta filter hittas livsmedels näringsprofil som ger förutsättningar för användaren att forma sitt eget kostschema som är nyttigt och njutbart.

<br>

# Tekniker & metoder
Projektet byggdes med en modern data- och visualiseringsstack där verktygen hade definierade roller för varje steg i utvecklingen. Python användes som programmeringsspråk för databehandling, API-anrop och integration av olika bibliotek samt verktyg. Jupyter Notebook som plattform för EDA (Exploratory Data Analysis) med hjälp av Pandas där grundläggande datavalidering gjorts på rådata. Datan laddades in i en DuckDB databas. dbt användes för SQL-baserad rensning, transformationer, datamodellering samt tester och dokumentation. Dbdiagram kompletterade med visualisering av databasstrukturen. För att skapa dashboarden användes Taipy som ramverk och Plotly/Matplotlib för att bygga interaktiva visualiseringar.

- Python (Projekt, requests)
- Jupyter Notebook/Pandas/DuckDB (EDA + grundläggande validering)
- DuckDB (Databas)
- dbt (Rensning, transformation, tester, dokumentation)
- Dbdiagram (Datamodellvisualisering)
- Taipy (Dashboard)
- Plotly/Matplotlib (Visualisering)
- Kanban Board (Utvecklingsdokumentation)

<br>

# Avgränsningar

Projektet avgränsas på flera sätt för att tydliggöra omfattning och fokus. Prisuppgifter inkluderas inte eftersom fokus ligger på att analysera näringsvärden snarare än ekonomiska aspekter. Användaren får verktygen att forma sin egna matkasse efter personlig ekonomisk situation.

Vidare begränsas projektet till att visualisera näringsdata som stöd för användaren utan att ge rekommendationer baserat på individens hälsostatus. Dashboarden ger en tydlig överblick av näringsvärden och enkla jämförelser men omfattar inte funktioner för fullständig måltidsplanering med recept eller shoppinglistor.

Projektet utvecklas lokalt och inte molnbaserat vilket minskar komplexiteten.

<br>

# Setup

*All commands are based from root folder*

### Initialize project

    Sync with this project using 
    uv sync

### Create database

    uv run create_ingest_db/create_database.py

### Get data from API

    uv run API/save_api_to_csv.py

    The API calls will take a while to retrieve all data from Livsmedelsverkets API.

### Ingestion with dbt

    cd dbt_nutrition

    dbt deps
    
    dbt run

    For testing/validation:
    dbt test

### DuckDB UI
    Open database for exploration with SQL
    Make sure you have duckdb installed on your device
        https://duckdb.org/#quickinstall

    duckdb -ui database/näringsportalen.duckdb


### Taipy Dashboard
    To start:
    uv run main.py