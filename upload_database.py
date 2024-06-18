import argparse

def main():
    parser = argparse.ArgumentParser(description="Upload database command")
    parser.add_argument('--file', type=str, required=True, help='CSV file containing database')

    args = parser.parse_args()
    csv_file = args.file
    print(csv_file)


if __name__ == '__main__':
    main()