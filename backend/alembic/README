Überwachungssoftware für Firmenprüfung
Ziel des Projekts
Dieses Projekt dient dem Aufbau einer Plattform zur Prüfung von Firmenkunden im Bereich Compliance und Geldwäscheprävention.
Langfristiges Ziel ist es, Unternehmen automatisiert darauf zu prüfen:
•	Verbindungen zu sanktionierten Entitäten
•	Risiken im Kontext von Geldwäsche (AML)
•	weitere Compliance-relevante Auffälligkeiten
In der aktuellen Version wird die technische Grundlage geschaffen, um:
•	Firmen strukturiert zu speichern
•	Daten konsistent zu verwalten
•	eine stabile und erweiterbare Architektur aufzubauen

Tech Stack
Backend
•	Python
•	FastAPI
•	SQLAlchemy
•	Alembic
Frontend
•	React (TypeScript)
Datenbank
•	PostgreSQL
Infrastruktur
•	Docker & Docker Compose

Lokale Entwicklungsumgebung
Zur Sicherstellung einer konsistenten Entwicklungsumgebung wird Docker verwendet.
Vorteile
•	identische Umgebung für alle Entwickler
•	keine lokale Installation von PostgreSQL notwendig
•	einfache Reproduzierbarkeit
Start der Anwendung
docker compose up --build
Verfügbare Services
Service	URL
Backend	http://localhost:8000

API Docs	http://localhost:8000/docs

Frontend	http://localhost:5173

Database	localhost:5432

 
Datenbank
Die Datenbank wird über einen PostgreSQL-Container bereitgestellt.
Konfiguration (docker-compose.yml)
POSTGRES_DB: ueberwachungssoftware
POSTGRES_USER: postgres
POSTGRES_PASSWORD: postgres


Datenmodellierung
Die Datenbankstruktur wird mit SQLAlchemy definiert.
Beispiel: Company-Modell
class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    legal_form: Mapped[str | None] = mapped_column(String(100), nullable=True)
    registration_country: Mapped[str] = mapped_column(String(2), nullable=False)
    registration_number: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
Ziel
•	klare Strukturierung von Firmendaten
•	Trennung zwischen Datenbank und Fachlogik
•	Erweiterbarkeit für zukünftige Module

Datenbank-Migrationen (Alembic)
Zur Versionierung von Datenbankänderungen wird Alembic verwendet.
Initialisierung
python -m alembic init alembic
Migration erstellen
python -m alembic revision --autogenerate -m "create companies table"
Migration anwenden
python -m alembic upgrade head

Aktueller Stand
Der aktuelle Entwicklungsstand umfasst:
•	Docker-basierte Entwicklungsumgebung
•	FastAPI-Backend
•	React-Frontend
•	PostgreSQL-Datenbank
•	SQLAlchemy-Datenmodell für Firmen
•	Alembic erfolgreich integriert
•	Tabelle companies erstellt

Nächste Schritte
•	API-Endpunkte für Firmen erstellen
o	POST /companies
o	GET /companies
•	Speicherung und Abruf von Daten testen
•	Erweiterung um:
o	Personen
o	Beteiligungen
o	Prüf-Fälle
•	Einführung von Audit-Logs

 Architekturprinzipien
•	einfacher, stabiler Start (kein Overengineering)
•	modularer Monolith
•	klare Trennung von:
o	API
o	Fachlogik
o	Datenzugriff
•	Nachvollziehbarkeit durch Migrationen und Logs

Hinweis
Dieses Projekt wird schrittweise aufgebaut.
Der Fokus liegt zunächst auf einer sauberen technischen Grundlage, bevor komplexe fachliche Logik implementiert wird.
