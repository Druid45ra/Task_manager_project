import os
import sys
from django.core.management import execute_from_command_line

def main():
    """Punct de intrare pentru aplicație."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_project.settings')
    try:
        execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000'])
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == '__main__':
    main()
