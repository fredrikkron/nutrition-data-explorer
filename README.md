# Affärsidé

I en vardag fylld av stress och höga krav söker allt fler sätt att upprätthålla energinivån för att känna sig stark genom hela dagen. Många vet att maten är en avgörande faktor men det är svårt att förstå vad som faktiskt är bra eller dåligt för hälsan. Informationsdjungeln gör det komplicerat och innehållsförteckningar är svårlästa vilket gör besluten överväldigande.
Näringsportalen samlar och visualiserar näringsvärden på ett informativt sätt som med filtreringar anpassar sig till användarens mål. Det ska vara lätt att välja livsmedel som gynnar hälsan och smakar gott för att bygga en fungerande vardag.

<br>

# Projektmål

Att skapa en dashboard som visualiserar och förenklar förståelsen av livsmedels näringsvärden. Genom smarta filter hittas livsmedel som stärker hälsan, undviker de som dränerar energi och bygger förutsättningar för användaren att forma sitt eget kostschema som är nyttigt och njutbart.

<br>

# Tekniker & metoder
Projektet byggs med en modern data- och visualiseringsstack. Python används som huvudspråk för databehandling och analys. Jupyter Notebook fungerar som plattform för EDA (Exploratory Data Analysis) och dokumentation av processer. Pandas för datarensning och transformation medan DuckDB tillsammans med dbdiagram använts för SQL-baserad modellering och visualisering av databasstrukturen. För att skapa dashboarden används Taipy som ramverk och Plotly/Matplotlib för att bygga interaktiva visualiseringar. Arbetet organiseras i en Kanban Board, där issues och tasks dokumenteras för att strukturera projektets utveckling.

- Python (Projekt)
- Jupyter Notebook (EDA)
- Pandas (Datarensning)
- Taipy (Dashboard)
- Plotly/Matplotlib (Visualisering)
- KanbanBoard (Dokumentera utvecklingen)
- Duckdb (SQL/datamodellering)
- Dbdiagram (Datamodellvisualisering)

<br>

# Avgränsningar

Projektet avgränsas på flera sätt för att tydliggöra omfattning och fokus i enlighet med estimeringsplan.
Datan hämtas enbart från Livsmedelsverket för att säkerställa tillförlitlighet och hålla projektet hanterbart baserat på en statisk excelfil snarare än ett realtids-API. Prisuppgifter inkluderas inte, eftersom fokus ligger på att analysera näringsvärden snarare än ekonomiska aspekter. 
Vidare begränsas projektet till att visualisera näringsdata och erbjuda filtreringar som stöd för användaren utan att ge rekommendationer baserat på individens hälsostatus. Dashboarden ger en tydlig överblick av näringsvärden och enkla jämförelser men omfattar inte funktioner för fullständig måltidsplanering med recept eller shoppinglistor.
Projektet utvecklas lokalt och inte molnbaserat vilket minskar komplexiteten.