# custom_wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Setzen der Umgebungsvariablen für die Django-Einstellungen
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

# Erstellen der WSGI-Anwendung
application = get_wsgi_application()

# Hier kann ich zusätzliche Anpassungen vornehmen.

# Beispiel: Logging-Konfiguration
# Wenn ich Logging in meiner Anwendung konfigurieren möchte, kann ich dies hier tun.
# Hier ist ein Beispiel, wie Sie ein einfaches Logging auf INFO-Ebene aktivieren können:

import logging

# # Legen Sie das gewünschte Logging-Level fest (z.B. INFO).
logging.basicConfig(level=logging.INFO)

# Ich kann jetzt in meinem Code Lognachrichten erstellen, z.B.:
logging.info("Dies ist eine Lognachricht auf INFO-Ebene.")

# Hier kann ich spezielle Middleware hinzufügen oder weitere Anpassungen vornehmen.
# Dies ist nur ein Beispiel, und ich soll entsprechend meinen Anforderungen anpassen.

