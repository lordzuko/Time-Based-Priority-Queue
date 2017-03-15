import sys
import time

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
    prev_time = start_datetime
    first_time = True
    while heapq:
        date_time, event = heapq.remove_min()
        date = date_time[0].strftime('%Y/%m/%d')
        time_ = date_time[0].strftime('%H:%M')
        date_time_str = ' '.join([str(date), str(time_)])
        seconds_difference = (date_time[0] - prev_time).total_seconds()
        minute_difference = int(seconds_difference//60)
        time.sleep(seconds_difference)
        if prev_time == date_time[0]:
            print("Current time [ {0} ] , Event \"{1}\" Processed".format(date_time_str, event))
        else:
            if first_time:
                print("-- After {} minute --".format(str(minute_difference)))
                first_time = False
            else:
                print("-- After another {} minute --".format(str(minute_difference)))
            print("Current time [ {0} ] , Event \"{1}\" Processed".format(date_time_str, event))
            prev_time = date_time[0]

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
