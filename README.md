# BDD Bankkonto Demo

Dieses Repository zeigt eine **BDD-Demo mit `behave`**, in der ein einfaches **Bankkonto** getestet wird.

## 📦 Installation & Vorbereitung

1. Stelle sicher, dass **Python 3.7+** installiert ist.
2. Installiere `behave` mit:

   ```sh
   pip install behave
   ```

3. Klone dieses Repository oder lade es als ZIP herunter.
4. Navigiere in das Projektverzeichnis.

## 🚀 Nutzung

Um die Tests auszuführen, gib folgenden Befehl ein:

```sh
behave
```

Falls alles erfolgreich ist, solltest du eine Ausgabe wie diese sehen:

```
Feature: Bankkonto
  Scenario: Einzahlung auf das Konto ✔
  Scenario: Abhebung vom Konto ✔
  Scenario: Abhebung mit unzureichendem Guthaben ✔
```

## 🛠 Erweiterungsideen

- Implementiere weitere Bankfunktionen (Überweisungen, Zinsen)
- Teste Grenzwerte für minimale/maximale Einzahlungen
- Simuliere verschiedene Benutzerkonten

Viel Spaß beim Behavior-Driven Development! 🚀
