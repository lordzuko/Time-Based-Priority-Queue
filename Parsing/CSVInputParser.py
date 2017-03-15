import csv
from datetime import datetime


class InputParser:
    """
        Parses the given CSV of Input Events.
    """

    def __init__(self, path):
        self.path = path

    def convert_to_datetime(self, tte):
        date, time = tte.split()
        year, month, day = date.split('/')
        date = '/'.join([year, month, day])
        tte = " ".join([date, time])
        return datetime.strptime(tte, '%Y/%m/%d %H:%M')

    def parse_clean_csv(self):
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


