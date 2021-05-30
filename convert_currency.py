''' Convert a currency to another currency'''

import argparse
import json
from urllib import request

parser = argparse.ArgumentParser(description='find the conversion rate between two currencies')
parser.add_argument('base', help='the currency to convert from')
parser.add_argument('target', help='the currency to convert to')
parser.add_argument('-v', '--value', metavar='value', type=float, default=1.0, help='the amount of base currency to be converted')
parser.add_argument('-p', '--precision', metavar='precision', type=int, default=2, help='precision of the currency conversion')
args = parser.parse_args()

base = args.base.upper()
target = args.target.upper()

url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + args.target + "&f=" + args.base + "&v=1&s=cbr"
r = request.urlopen(url)
obj = json.loads(r.read())
res = obj[target] * args.value
res_f = '{:,.{prec}f}'.format(res, prec=args.precision)
val_f = '{:,.{prec}f}'.format(args.value, prec=args.precision)

print(f'{val_f} {base} has a value of {res_f} {target}')