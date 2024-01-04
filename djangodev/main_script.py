# In jamila_mini_app/main_script.py
import sys
sys.path.append('C:\Users\jamil\OneDrive\Desktop\Gruber_Infi\.virtualvenvs\djangodev\source')
from django.core.management import setup_environ
from web_project import settings  # Stellen Sie sicher, dass Sie Ihr Projekt korrekt importieren

setup_environ(settings)

from .query_file import get_all_entries, get_entries_by_age

if __name__ == "__main__":
    # Beispielaufrufe der erstellten Funktionen
    all_entries = get_all_entries()
    print("Alle Einträge:")
    for entry in all_entries:
        print(entry)

    age_threshold = 25
    entries_above_age = get_entries_by_age(age_threshold)
    print(f"Einträge mit 'age' größer als {age_threshold}:")
    for entry in entries_above_age:
        print(entry)