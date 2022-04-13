import requests,json

url = "https://api.postalpincode.in/pincode/110001"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# response_txt=json.loads(response.text.encode('utf8'))
# #print(response_txt)

# # x= [sub["PostOffice"]for sub in response_txt ]
# # z=[y["Circle"] for y in x ]
# # print(z)
# # r = requests.get("https://api.postalpincode.in/pincode/110001")
# print(response_txt[0]['PostOffice'][0]['Country'])
# # state=response_txt([0]['PostOffice'][0]['State'])
# city=response_txt([0]['PostOffice'][0]['Circle'])
# print(city)
# x=r.json()

# print(x[0])
def get_city(pincode:int):
    response_txt=json.loads(response.text.encode('utf8'))
    return {"city": response_txt[0]['PostOffice'][0]['Circle'],"state":response_txt[0]['PostOffice'][0]['State'],"country":response_txt[0]['PostOffice'][0]['Country']}

x=get_city(110001)
print(x["city"])