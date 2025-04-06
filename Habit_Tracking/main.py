from datetime import datetime
from time import strftime

import requests
import json
import datetime as dt


USERNAME = "vasanthji"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "abcdefghij"
GRAPH_ID = "graph1"
parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

graph_parameter = {
"id":GRAPH_ID,
"name":"dailyschedule",
"unit":"km",
"type":"float",
"color":"ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=pixela_endpoint, json=parameter)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

# response_graph = requests.post(url=graph_endpoint,json=graph_parameter, headers=header)
# print(response_graph.text)
date = dt.datetime.now()
date1 = datetime(year=2024 , day=12,month=11)
post_graph = f"{graph_endpoint}/{GRAPH_ID}"
post_graph_parameter ={
    "date": date1.strftime("%Y%m%d"),
    "quantity":"9.0",

}

response_graph = requests.post(url=post_graph,json=post_graph_parameter,headers=header)
print(response_graph.text)

put = f"{post_graph}"
new_graph_parameter ={
    "date": date1.strftime("%Y%m%d"),
    "quantity":"15.0",
    "color":"momiji"

}
response_put= requests.put(url=post_graph,json=new_graph_parameter,headers=header)

print(response_put.text)
del1=f"{post_graph}/{date.strftime("%Y%m%d")}"
response_del= requests.delete(url=del1,headers=header)
print(response_del.text)