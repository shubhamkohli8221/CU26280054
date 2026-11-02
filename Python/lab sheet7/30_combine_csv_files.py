# Program 30: Combine multiple CSV files into one CSV file.
import csv
from pathlib import Path

input_files = ["students.csv", "students_extra.csv"]
output_file = "combined_students.csv"

try:
    with open(output_file, "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        header_written = False

        for filename in input_files:
            path = Path(filename)
            if not path.exists():
                print(f"Skipping missing file: {filename}")
                continue

            with path.open("r", newline="", encoding="utf-8") as source:
                reader = csv.reader(source)
                header = next(reader, None)
                if header is None:
                    continue
                if not header_written:
                    writer.writerow(header)
                    header_written = True
                for row in reader:
                    writer.writerow(row)

    print("Combined data saved to", output_file)
except OSError as error:
    print("File error:", error)
