from util import *

class Player(object):
    """
    player class. 
    
    To test your own machine player strategy, you should implement the ```make_decision()``` method. 
    To test your implementation, you should modify the configy.py to set one or two player(s) as 'machine' 
    """

    def __init__(self, id, name=None):
        self.points=0
        self.id=id
        self.name=name if name else 'player'+str(id)
        self.add = lambda val,rand: (val+rand) % 16
        self.replace = lambda val,rand: rand % 16
        self.skip = lambda val, rand: val
    
    def make_decision(self, four_bits, next_randoms, code_digits):
        """
        This function decide next move of the machine player.

        You should only modify '#Your Code is Here' to define your own machine player.
        To enable your machine player, please check & modify the configuration in config.py.

        Args:
            four_bits (int[]): the four bit number in the LED 
            next_randoms (int[]): the next 3 random digits
            code_digits(int[]): 2 code digits.
        Returns:
            operation: [self.skip | self.add | self.replace]
        	selected: [0|1|2|3]
        """
        
        """
        Logic:
        1.  Check if the random bit can be add/replace bits in position 2 | 3
            If it can, then replace the highest one
        
        2.  Check all possible adjacency and pick the max value
        """
        
        if next_randoms[0] == code_digits[0] or next_randoms[0] + four_bits[2] == code_digits[0] or next_randoms[0] == code_digits[1] or next_randoms[0] + four_bits[3] == code_digits[1]:
            if next_randoms[0] == code_digits[0]:
                operation = self.replace
                selected = 2
            elif next_randoms[0] + four_bits[2] == code_digits[0]:
                operation = self.add
                selected = 2
            elif next_randoms[0] == code_digits[1]:
                operation = self.replace
                selected = 3
            elif next_randoms[0] + four_bits[3] == code_digits[1]:
                operation = self.add
                selected = 3
        else:
            operation = self.replace
            selected = 0
    	return operation, selected
