import sys
import json
import gzip
from collections import OrderedDict
import pprint


args = sys.argv
args.append('jawiki-country.json.gz')


def read_wiki(file_name, title):

    with gzip.open(file_name, 'r', 'utf-8') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']


def main():
    file_name = args[1]
    print(read_wiki(file_name, 'イギリス'))


if __name__ == '__main__':
    main()
