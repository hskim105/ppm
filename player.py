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
    
    def add_to(randBit, pos, four_bits):
        """
        This function will add the passed random bit to the value in the position
        
        Args:
            randBit (int): current random bit
            pos (int): position in the four_bit. Has to be [0|1|2|3]
            four_bit (int[]): the four bit number in the LED
        
        Returns:
            randBit: randBit + four_bit[pos]
            pos: [0|1|2|3]
        """
        randBit += four_bit[pos]
        return randbit, pos
        
    def replace_to(randBit, pos, four_bits):
        """
        This function will replace the value in the position with the rand bit
        
        Args:
            randBit (int): current random bit
            pos (int): position in the four_bit. Has to be [0|1|2|3]
            four_bit (int[]): the four bit number in the LED
        
        Returns:
            randBit: randBit + four_bit[pos]
            pos: [0|1|2|3]
        """
        four_bit[pos] = randBit
        return randBit, pos
        
    def find_code_digits(randBit):
        """
        This function will find if the passed in random bit can
        add or replace an existing bit to become the code digit
        
        Args:
            randBit (int): current random bit
        Returns:
            operation: [self.add | self.replace]
            selected: [0|1|2|3]
        """
        
    
    
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
        
        operation = self.skip
    	selected = 0
    	#Your Code is Here
        """
        Logic:
        1.  Check if the random bit can be add/replace bits in position 2 | 3
            If it can, then replace the highest one
        """
        if next_randoms[0] == 
    	return operation, selected
