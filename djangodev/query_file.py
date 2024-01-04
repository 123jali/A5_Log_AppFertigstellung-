# In jamila_mini_app/query_file.py

from .models import JamilaModel  # Stellen Sie sicher, dass der Pfad zu Ihrem Modell korrekt ist

def get_all_entries():
    """
    Gibt alle Einträge aus der Datenbank zurück.
    """
    return JamilaModel.objects.all()

def get_entries_by_age(age):
    """
    Gibt Einträge zurück, deren 'age' größer als der angegebene Wert ist.
    """
    return JamilaModel.objects.filter(age__gt=age)