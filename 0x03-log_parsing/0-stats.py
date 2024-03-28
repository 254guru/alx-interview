#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re


def extract_info(log_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {'status_code': 0, 'file_size': 0}
    log_format = '{}\\-{}{}{}{}\\s*'.format(*pattern)
    match = re.fullmatch(log_format, log_line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_stats(total_size, status_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('Total file size:', total_size, flush=True)
    for status_code in sorted(status_stats.keys()):
        num = status_stats.get(status_code, 0)
        if num > 0:
            print(status_code, ':', num, flush=True)


def update_metrics(line, total_size, status_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_info(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_stats:
        status_stats[status_code] += 1
    return total_size + line_info['file_size']

def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_size = 0
    status_stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0,
    }
    try:
        while True:
            line = input()
            total_size = update_metrics(
                line, total_size, status_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_size, status_stats)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_size, status_stats)


if __name__ == '__main__':
    run()
