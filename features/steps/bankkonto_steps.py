from behave import given, when, then
from bankkonto import Bankkonto

@given('das Konto hat ein Startguthaben von {betrag:d}€')
def step_set_startguthaben(context, betrag):
    context.konto = Bankkonto(startguthaben=betrag)

@when('der Nutzer {betrag:d}€ einzahlt')
def step_einzahlen(context, betrag):
    context.konto.einzahlen(betrag)

@when('der Nutzer {betrag:d}€ abhebt')
def step_abheben(context, betrag):
    context.erfolg = context.konto.abheben(betrag)

@then('beträgt das Guthaben {betrag:d}€')
def step_check_guthaben(context, betrag):
    assert context.konto.guthaben == betrag, f"Erwartet: {betrag}€, aber erhalten: {context.konto.guthaben}€"

@then('wird die Abhebung abgelehnt')
def step_check_abgelehnt(context):
    assert context.erfolg is False, "Die Abhebung wurde nicht abgelehnt!"
