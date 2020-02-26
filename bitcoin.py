import requests

def main():
    dollars = get_dollar_amount()
    rate_float = request_bitcoin_rate(dollars)
    bit_rate = do_math(dollars, rate_float)
    display(dollars, bit_rate)

def get_dollar_amount():
    number = float(input('Enter amount of dollars to convert: '))
    return number

def request_bitcoin_rate(dollars):
    bitcoin_rate = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    bpi = bitcoin_rate['bpi']
    usd = bpi['USD']
    rate_float = usd['rate_float']
    return rate_float

def do_math(dollars, rate_float):
    bit_rate = dollars * rate_float
    return bit_rate

def display(dollars, bit_rate):
    print(f'${dollars} is {bit_rate} bitcoins.')