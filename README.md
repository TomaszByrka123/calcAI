# Silesian Phoenix - Platforma Edukacyjna

## Instrukcja

### Instalacja

Utworzenie wirtualnego środowiska:

```sh
$ python3 -m venv venv
```

Aktywacja wirtualnego środowiska:

```sh
$ source venv/bin/activate
```

Instalacja wymaganych pakietów z wykorzystaniem pliku _requirements.txt_:

```sh
(venv) $ pip install -r requirements.txt
```

### Inicjalizacja bazy danych

W celu poprawnego działania aplikacji wymagane jest utworzenie bazy danych SQLite oraz dodanie dwóch rekordów

```sh
(venv) $ flask init_db
(venv) $ flask basic_user
```

### Aktywacja aplikacji

Aktywacja serwera aplikacji w trybie deweloperskim:

```sh
(venv) $ flask --app app --debug run
```

Aplikacja będzie dostępna pod adresem http://127.0.0.1:5000.

---

Aktywacja serwera aplikacji w trybie deweloperskim z dostępem z poziomu sieci lokalnej LAN:

```sh
(venv) $ flask --app app --debug run --host 0.0.0.0
```

Aplikacja będzie dostępna pod adresem http://127.0.0.1:5000 oraz http://<lokalny_adres_hosta>:5000

## Użyte pakiety

* **Flask** — mikro-framework do tworzenia aplikacji sieciowych, wraz z następującymi zależnościami:
  * click — pakiet do tworzenia interfejsów wiersza poleceń
  * itsdangerous — kryptograficzne podpisywanie danych
  * Jinja2 — silnik szablonów
  * MarkupSafe — zamiana znaczenia znaków w celu zwiększenia bezpieczeństwa danych przekazywanych od użytkownika
  * Werkzeug — zbiór narzędzi do tworzenia aplikacji, która może komunikować się z serwerem WSGI
  * Flask-CORS - dodatek umożliwiający pracę z CORS (ang. _Cross Origin Resource Sharing_)
  * Flask-OpenID - dodatek umożliwiający wykorzystanie OpenID do autoryzacji
  * Flask-QRcode - dodatek pozwalający na łatwe generowanie kodów QR
  * Flask-Login - obsługa zarządzania użytkownikami (logowanie/wylogowanie) w Flask
  * Flask-WTF - uproszczenie formularzy w Flask
  * Flask-SQLAlchemy - ORM (ang. _Object Relational Mapper_) dla obsługi bazy danych
* **pytest** — framework do testowania projektów w Pythonie
* **flake8** — narzędzie do analizy statycznej
* **pdfkit** — dodatek do narzędzia wkhtmltopdf do konwersji HTML na PDF za pomocą Webkit
* **pytest-cov** — generowanie raportów typu _coverage_
* **email_validator** — dodatek umożliwiający walidację adresu Email
* **pyflakes** — prosta paczka do sprawdzania programu pod kątem błędów
* **websauna** — zestaw narzędzi do obsługi aplikacji webowych

Aplikacja została napisana z wykorzystaniem Pythona 3.10, ale jest wstecznie kompatybilna do wersji 3.8.

## Autorzy

- [Tomasz Byrka](https://gitlab.com/tombyrka123)

## Status projektu

Projekt jest aktualnie w stanie rozwoju.

---
