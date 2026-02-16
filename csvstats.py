import argparse
import csv


def read_column(file_path, column_name):
    values = []

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        if column_name not in reader.fieldnames:
            raise ValueError(f"Column '{column_name}' not found.")

        for row in reader:
            try:
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                # Skip non-numeric values
                continue

    return values


def main():
    parser = argparse.ArgumentParser(
        description="Compute basic statistics for a CSV column"
    )

    parser.add_argument("file", help="Path to CSV file")
    parser.add_argument("--column", required=True, help="Column name")

    args = parser.parse_args()

    values = read_column(args.file, args.column)

    print("Values:", values)


if __name__ == "__main__":
    main()
