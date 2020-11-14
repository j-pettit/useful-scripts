''' Convert a currency to another currency'''

import argparse
import json
from urllib import request

parser = argparse.ArgumentParser(description='find the conversion rate between two currencies')
parser.add_argument('base', help='the currency to convert from')
parser.add_argument('target', help='the currency to convert to')
parser.add_argument('-v', '--value', metavar='value', type=float, default=1.0, help='the amount of base currency to be converted')
args = parser.parse_args()

base = args.base.upper()
target = args.target.upper()

url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + args.target + "&f=" + args.base + "&v=1&s=cbr"
r = request.urlopen(url)
obj = json.loads(r.read())
res = obj[target] * args.value
res_f = '{:,.2f}'.format(res)
val_f = '{:,.2f}'.format(args.value)

print(f'{val_f} {base} has a value of {res_f} {target}')