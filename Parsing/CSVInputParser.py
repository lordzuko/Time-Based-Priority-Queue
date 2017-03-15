'''
MIT License

Copyright (c) 2017 Himanshu Maurya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import csv
from datetime import datetime


class InputParser:
    """
        Parses the given CSV of Input Events.
    """

    def __init__(self, path):
        self.path = path

    def convert_to_datetime(self, tte):
        """
            Convert time from given format to acceptable datetimeformat
        """
        date, time = tte.split()
        year, month, day = date.split('/')
        date = '/'.join([year, month, day])
        tte = " ".join([date, time])
        return datetime.strptime(tte, '%Y/%m/%d %H:%M')

    def parse_clean_csv(self):
        """
            Clean the csv data and create a dictionary to be used
            in HeapPriorityQueue
        """
        cleaned_data = []
        with open(self.path, 'r') as csvfile:
            rows = csv.DictReader(csvfile, delimiter=',')
            for row in rows:
                temp = dict()
                temp['event_name'] = row['event_name']
                tte = row[' time_to_expire '].strip().replace('"', '')
                temp['time_to_expire'] = self.convert_to_datetime(tte)
                if row[' priority']:
                    temp['priority'] = int(row[' priority'])
                else:
                    temp['priority'] = 0

                cleaned_data.append(temp)
        return cleaned_data


