"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def process_report():
    def clean_line(line):
        return re.sub(r'\s+', ' ', line.strip())

    def format_header(header):
        return [col.lower().replace(' ', '_') for col in header]

    def handle_row(line, current_row):
        parts = re.split(r'\s{2,}', line)
        if parts[0].isdigit():
            if current_row:
                data.append(current_row[:])
            current_row.clear()
            current_row.extend([int(parts[0]), int(parts[1]), float(parts[2].replace(',', '.'))])
            current_row.append(clean_line(' '.join(parts[3:])))
        else:
            current_row[-1] += ' ' + clean_line(line)

    with open('files/input/clusters_report.txt') as file:
        lines = [line.strip() for line in file.readlines() if '---' not in line]

    header = re.split(r'\s{2,}', lines[0])
    header = format_header(header)

    data = []
    current_row = []

    for line in lines[2:]:
        handle_row(line, current_row)

    if current_row:
        data.append(current_row)

    df = pd.DataFrame(data, columns=header)
    return df

df = process_report()
print(df)
