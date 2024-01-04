import logging
from django.shortcuts import render
import datetime

# Konfigurieren Sie das Logging für Ihre Anwendung
logger = logging.getLogger(__name__)

def hello_there(request, name):
    now = datetime.datetime.now()
    format_1 = now.strftime("%A, %d %B, %Y at %X")
    format_2 = now.strftime("%A, %d/%m/%y %B, %Y at %H:%M:%S")

    if "format" in request.GET and request.GET["format"] == "short":
        formatted_now = format_2
    else:
        formatted_now = format_1

    context = {
        'name': name,
        'date': formatted_now
    }

    # Loggen Sie den Aufruf der Funktion
    logger.info(f"hello_there view wurde aufgerufen mit {name} um {formatted_now}")
    
    return render(request, 'hello/hello_template.html', context)

def kontakt(request):
    # Loggen Sie den Aufruf der Funktion
    logger.info("Kontakt view wurde aufgerufen.")
    
    context = {
        'email': 'ihre-email@example.com'  # Ersetzen Sie dies durch Ihre tatsächliche E-Mail-Adresse
    }
    return render(request, 'hello/kontakt.html', context)




