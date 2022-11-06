import requests

url = 'http://localhost:9696/predict'

customer = {
    'age' : 25,
    'bill_amt1 ' : 490,
    'bill_amt2' : -10,
    'bill_amt3' : 0,
    'bill_amt4' : 0,
    'bill_amt5' : 0,
    'bill_amt6' : 1000,
    'education' : 'university',
    'limit_bal' : 170000,
    'marriage'  :'married',
    'pay_1' : 0,
    'pay_2' : 5,
    'pay_3' : 0,
    'pay_4' : 3,
    'pay_5' : -1,
    'pay_6' : 0,
    'pay_amt1' : 0,
    'pay_amt2' : 4920,
    'pay_amt3' : 500,
    'pay_amt4' : 30000,
    'pay_amt5' : 1000,
    'pay_amt6' : 1030,
    'sex' : 'male'
}


response = requests.post(url, json = customer)

result = response.json()

print(result)

if result['result']:
    print('Default Payment')

elif result['result'] == False:
    print('Not Default Payment')



