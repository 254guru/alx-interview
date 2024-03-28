import sys
from collections import defaultdict


def print_statistics(file_sizes, status_codes):
    print("File size:", sum(file_sizes))
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    file_sizes = []
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) != 7:
                continue

            status_code = parts[-2]
            if status_code.isdigit():
                status_codes[int(status_code)] += 1

            file_sizes.append(int(parts[-1]))

            if line_count % 10 == 0:
                print_statistics(file_sizes, status_codes)
                file_sizes.clear()
                status_codes.clear()
    except KeyboardInterrupt:
        print_statistics(file_sizes, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
