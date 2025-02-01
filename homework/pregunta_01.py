"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    def clean_line(line):
        return re.sub(r'\s+', ' ', line.strip()).replace('.', '').strip()

    def clean_header(headers):
        return [header.lower().replace(" ", "_") for header in headers]

    def process_value(line, current_val):
        parts = re.split(r'\s{2,}', line)
        if parts[0].isdigit():
            rows.append(current_val[:])
            current_val.clear()
            current_val.extend([
                int(parts[0]),
                int(parts[1]),
                float(parts[2].split()[0].replace(',', '.'))
            ])
            percent_idx = line.find('%')
            current_val.append(clean_line(line[percent_idx + 1:]))
        else:
            current_val[-1] += " " + clean_line(line)

    with open("files/input/clusters_report.txt") as f:
        lines = [line.strip() for line in f.readlines() if "---" not in line]

    header = re.split(r"\s{2,}", lines[0])
    header[1] += " palabras clave"
    header[2] += " palabras clave"

    rows = []
    current_val = header

    for line in lines[2:]:
        if line:
            process_value(line, current_val)

    rows.append(current_val)
    rows[0] = clean_header(rows[0])

    df = pd.DataFrame(data=rows[1:], columns=rows[0])
    return df

