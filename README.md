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

Neuer Stand (API-Implementierung)

Im aktuellen Schritt wurde der erste vollständige API-Endpunkt implementiert:

POST /companies

Damit ist es nun möglich, Firmen über die API zu erstellen und direkt in der Datenbank zu speichern.

Umsetzung:

• Einführung von Pydantic-Schemas:
  CompanyCreate → für eingehende Requests (Validierung)
  CompanyRead → für ausgehende Responses
• Einführung einer Service-Schicht:
  create_company(...) übernimmt die Erstellung und Speicherung in der Datenbank
• Einführung einer Datenbank-Session:
   zentrale Bereitstellung über get_db()
• Implementierung des Endpunkts:
  POST /companies
  Speicherung der Daten über SQLAlchemy
  Rückgabe der gespeicherten Firma inkl. ID und Zeitstempel

Ergebnis:

• End-to-End-Datenfluss funktioniert:
  Request → Validierung → Service → Datenbank → Response
• Daten werden erfolgreich in PostgreSQL gespeichert
• API kann über Swagger (/docs) getestet werden

Beispiel:
Request:
{
  "name": "Muster GmbH",
  "legal_form": "GmbH",
  "registration_country": "DE",
  "registration_number": "HRB 12345"
}
Response:
{
  "id": 1,
  "name": "Muster GmbH",
  "legal_form": "GmbH",
  "registration_country": "DE",
  "registration_number": "HRB 12345",
  "created_at": "...",
  "updated_at": "..."
}
Aktueller Stand
Der aktuelle Entwicklungsstand umfasst:
•	Docker-basierte Entwicklungsumgebung
•	FastAPI-Backend
•	React-Frontend
•	PostgreSQL-Datenbank
•	SQLAlchemy-Datenmodell für Firmen
•	Alembic erfolgreich integriert
•	Tabelle companies erstellt
•	POST /companies API-Endpunkt implementiert
•	End-to-End-Datenfluss (API → Service → Datenbank → Response) funktioniert
•	Pydantic-Schemas für Request und Response integriert
•	Service-Schicht für Datenverarbeitung eingeführt
•	Daten können erfolgreich über die API gespeichert werden

Nächste Schritte
•	GET /companies implementieren (Abruf von Firmen)
•	Speicherung und Abruf von Daten weiter testen
•	API-Struktur weiter ausbauen (z. B. Trennung in Router)
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
