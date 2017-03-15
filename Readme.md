# Time Based Priority Queue - Python Implementation

## Problem: Implement a time-based priority queue.

Write a module to implement a queue based on time and priority. <br>
This program can be used to schedule tasks at a given time.<br>

## Rules:<br>
- Don't use any third party queue libraries<br>
- You can use list or hash libraries<br>

## Running<br>
Pass filename & starttime as parameters to program<br>


## E.g <br>
Let's say file name is "queueProcess" <br>
Let's say input file name is "inputs_events.csv" <br>

` ./queueProcess input_events.csv  "2017/02/10 4:59" ` <br>

## Input <br>
`event_name, time_to_expire , priority`<br>
`"Task_#501", "2017/02/10 5:01"`<br>
`"Task_#500", "2017/02/10 5:00"`<br>
`"Task_#500", "2017/02/10 5:00" , 1`<br>

## Output <br>
![alt tag](https://github.com/lordzuko/Time-Based-Priority-Queue/blob/master/Data/output_inputs_events0.PNG)
