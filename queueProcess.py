import sys

from PriorityQueue.HeapPriorityQueue import HeapPriorityQueue
from Parsing.CSVInputParser import InputParser

def main(path_to_csv, starttime):
    input_parser = InputParser(path_to_csv)
    input_events = input_parser.parse_clean_csv()
    start_datetime = input_parser.convert_to_datetime(starttime)
    list_key_value = []
    for event in input_events:
        k = (event['time_to_expire'],event['priority'],event['time_to_expire'] - start_datetime)
        v = event['event_name']
        list_key_value.append((k, v))

    heapq = HeapPriorityQueue(list_key_value)
    while heapq:
        date_time, event = heapq.remove_min()
        date = date_time[0].strftime('%Y/%m/%d')
        time = date_time[0].strftime('%H:%M')
        date_time = ' '.join([str(date), str(time)])
        print("Current time [ {0} ] , Event \"{1}\"".format(date_time, event))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
