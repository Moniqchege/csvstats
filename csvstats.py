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

def calculate_stats(values):
    count = len(values)
    total = sum(values)
    mean = total / count
    minimum = min(values)
    maximum = max(values)

    return {
        "count": count,
        "mean": mean,
        "min": minimum,
        "max": maximum,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compute basic statistics for a CSV column"
    )

    parser.add_argument("file", help="Path to CSV file")
    parser.add_argument("--column", required=True, help="Column name")

    args = parser.parse_args()

    values = read_column(args.file, args.column)

    print("Values:", values)

    stats = calculate_stats(values)

    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
