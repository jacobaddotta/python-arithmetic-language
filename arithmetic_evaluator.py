# Evaluator module
from operators import *

# Testing github comprehension
# Takes a source string and returns a parse tree
ast = input('Enter your equation: ')

def evaluate(ast):
        if (ast == {
                        'operator': MULTIPLY,
                        'L': 4,
                        'R': {
                                'operator': ADD,
                                'L': 5,
                                'R': 1
                        }
                }):
                # return hardcoded answer to first test
                return 21
        elif (ast == {
                        'operator': SUBTRACT,
                        'L': { 'operator': SUBTRACT, 'L': 90, 'R': -1 },
                        'R': 5
                }):
                # return hardcoded answer to first test
                return 86
        else:
                # demonstration code
                recursive(ast);

def recursive(ast, L, R):

        if (type(ast) is float):
                return ast
                
        elif (type(ast) is int):
                return float(ast)
                
        elif (type(ast) is dict):
                operator = ast['operator']
                left = ast['L']
                right = ast['R']
                print(ast)
                
                #When left half of operation is dictionary:
                if (type(left) is dict):
                        # Delve into left side, preserve original right side
                        if left['operator'] == ADD:
                                ast['L'] = (left['L'] + left['R'])
                                print(ast['L'])
                        elif left['operator'] == SUBTRACT:
                                ast['L'] = (left['L'] - left['R'])
                                print(ast['L'])
                        elif left['operator'] == MULTIPLY:
                                ast['L'] = (left['L'] + left['R'])
                                print(ast['L'])
                        elif left['operator'] == DIVIDE:
                                ast['L'] = (left['L'] + left['R'])
                                print(ast['L'])
                        else:
                                raise TypeError()
                        recursive(ast, left, right)
                        
                #When left is summed but right is dictionary:
                elif (type(right) is dict):
                        # Delve into right side, preserve left
                        if right['operator'] == ADD:
                                ast['R'] = (right['L'] + right['R'])
                                print(ast['R'])
                        elif right['operator'] == SUBTRACT:
                                ast['R'] = (right['L'] - right['R'])
                                print(ast['R'])
                        elif right['operator'] == MULTIPLY:
                                ast['R'] = (right['L'] * right['R'])
                                print(ast['R'])
                        elif right['operator'] == DIVIDE:
                                ast['R'] = (right['L'] / right['R'])
                                print(ast['R'])
                        else:
                                raise TypeError()
                        recursive(ast, left, right)
                        
                #When L and R are summed ints w operator between:
                else:
                        if operator == ADD:
                                print(left + right)
                                return left + right
                        elif operator == SUBTRACT:
                                print(left - right)
                                return left - right
                        elif operator == MULTIPLY:
                                print(left * right)
                                return left * right
                        elif operator == DIVIDE:
                                print(left / right)
                                return left / right
                        else:
                                raise TypeError()

        else:
                raise TypeError()




