Feature: Bankkonto

  Scenario: Einzahlung auf das Konto
    Given das Konto hat ein Startguthaben von 100€
    When der Nutzer 50€ einzahlt
    Then beträgt das Guthaben 150€

  Scenario: Abhebung vom Konto
    Given das Konto hat ein Startguthaben von 100€
    When der Nutzer 30€ abhebt
    Then beträgt das Guthaben 70€

  Scenario: Abhebung mit unzureichendem Guthaben
    Given das Konto hat ein Startguthaben von 50€
    When der Nutzer 100€ abhebt
    Then wird die Abhebung abgelehnt
