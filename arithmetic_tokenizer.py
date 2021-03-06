# Tokenizer module
from operators import *

# Takes a source string and returns an array of tokens
token_map = {
	'+': ADD,
	'-': SUBTRACT,
	'*': MULTIPLY,
	'/': DIVIDE
}

def tokenize(expr):

		res = []

		split_expr = expr.split()

		for string_expr in split_expr:
			try:
				num = float(string_expr)
				res.append({ 'type': 'number', 'value': num })
				
			except:
				res.append({ 'type': 'operator', 'value': token_map[string_expr] })
		
		return res

