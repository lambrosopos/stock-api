import os
import sys
import csv

def get_file_content(filepath):
    try:
        with open(filepath, 'r') as f:
            content = [r for r in csv.reader(f, delimiter=',')]
    except IOError as e:
        print('IO Error occured')
        print(e)
    except:
        print('Unexpected error:', sys.exc_info()[0])

    return content


def write_content(filepath, data):
    try:
        with open(filepath, 'w'), as f:
            csv_writer = csv.writer(f, delimiter=',', qutoechar='"',
                                    qutoing=csv.QUOTE_MINIMAL)

            csv_writer.writerows(data)
        print('Write successful')
    except IOError as e:
        print('IO Error occured')
        print(e)
    except:
        print('Unexpected error:', sys.exc_info()[0])

    return True
