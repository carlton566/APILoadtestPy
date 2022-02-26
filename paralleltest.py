import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import json


url = input("Enter URL to do a load test on api")


def callAPI_single(url,json_line):
    print(json_line)
    try:
        html = requests.post(url,json=json_line,stream=True)
        return html.json()
    except requests.exceptions.RequestException as e:
       return e
total1=0
def runner():
    totAPIRequests = 0

    global url
    beginTime = time.time()
    threads= []
    with ThreadPoolExecutor(max_workers=1000) as executor:#change the max workers to required number of load or stress you want to test
        with open('json.txt') as f:
            for jsonObj in f:                
                json_line = json.loads(jsonObj)
                threads.append(executor.submit(callAPI_single, url,json_line))
                totAPIRequests+=1
                   
        for task in as_completed(threads):
           print(task.result())
           task.result()
           print() 
    endTime = time.time()
    print('\nRecords processed = '+str(totAPIRequests))   
    print(f"[Mulithread] Runtime of the program is {endTime - beginTime} seconds")  
runner()