#!/usr/bin/env python3

import sys
import signal

# Dictionary to store status code counts
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0

def print_statistics():
    global total_file_size
    global line_count
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
    print()

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) == 7:
        ip, _, _, status_code, file_size = parts[0], parts[3], parts[5], int(parts[6]), int(parts[-1])
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_counts:
                status_counts[status_code] += 1
        total_file_size += file_size
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
