import argparse

def main():
    parser = argparse.ArgumentParser(
        description = "Compute basic statistsics for a CSV column"
    )

    parser.add_argument("file", help="Path to CSV file")
    parser.add_argument("--column", required=True, help="Column name")

    args = parser.parse_args()

    print("File", args.file)
    print("Column", args.column)

    if __name__ == "__main__":
        main()