"""
setup_data.py — Creates the required Excel file for storing game statistics.

Run this script ONCE before playing for the first time:
    python setup_data.py

By default it creates the file at the path expected by menu_principal.py.
You can pass a custom path as a command-line argument:
    python setup_data.py /my/custom/path/stats.xlsx
"""

import sys
import os
import openpyxl

DEFAULT_PATH = "TAREA.xlsx"

def create_stats_file(path: str) -> None:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Estadisticas"
    headers = ["Nombre", "Resultado", "Intentos_realizados", "Dificultad", "Rango", "Modalidad"]
    sheet.append(headers)

    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True) if os.path.dirname(path) else None
    workbook.save(path)
    print(f"✅  Stats file created at: {os.path.abspath(path)}")
    print("You can now run:  python menu_principal.py")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH
    create_stats_file(target)
