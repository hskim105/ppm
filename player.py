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
        
    # def findMaxOpPos(currentMax, newVal, op, pos):
 #        """
 #        This function finds the operation and position that will yield the maximum value of points
 #
 #        Args:
 #            currentMax (int): The current max value
 #            newVal (int): New value that will be compared to the current max
 #            op: [self.add | self.replace]
 #            pos (int): [0|1|2|3]
 #
 #        Returns:
 #            newMax (int)
 #            operation: [self.skip | self.add | self.replace]
 #            selected: [0|1|2|3]
 #        """
 #
        
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
        
        #The random bit
        randBit = next_randoms[0]
        
        #Two code digits placed on position 2 (codeOne) and position 3 (codeTwo)
        codeOne = code_digits[0]
        codeTwo = code_digits[1]
        
        #The values that are in the array
        bitOne = four_bits[0]
        bitTwo = four_bits[1]
        bitThree = four_bits[2]
        bitFour = four_bits[3]
        
        """
        Logic:
        1.  Check if the random bit can add/replace bits in position 2 | 3
            If it can, then replace the highest one
        
        2.  Check all possible adjacency and pick the max value
        """
        #Checks if the random bit can add/replace bits in position 2 | 3
        if randBit == codeOne or (randBit + bitThree) == codeOne or randBit == codeTwo or (randBit + bitFour) == codeTwo:
            #Checks if the random bit is equal to the value of the first code digit (pos 2)
            if randBit == codeOne:
                operation = self.replace
                selected = 2
            #Checks if the random bit plus the value of the third bit is equal to the first code digit
            elif randBit + bitThree == codeOne:
                operation = self.add
                selected = 2
            #Checks if the random bit is equal to the value of the second code digit (pos 3)
            elif randBit == codeTwo:
                operation = self.replace
                selected = 3
            #Checks if the random bit plus the value of the fourth bit is equal to the second code digit
            elif randBit + bitFour == codeTwo:
                operation = self.add
                selected = 3
                
        #Checks if there are any adjacency in the list
        elif randBit in four_bits or (randBit + bitOne) in four_bits or (randBit + bitTwo) in four_bits or (randBit + bitThree) in four_bits or (randBit + bitFour) in four_bits:
            
            #Default values. Will be changed after for loop
            currentMax = 0
            operation = self.skip
            selected = 0
            
            #Looping through each bit in the four_bits array
            for index in four_bits:
                #Checking all possible adjacency at position 0
                if index == bitOne:
                    #Check 3 adjacency with replacement
                    #Check 3 adjacency with addition
                    
                    #Check 2 adjacency with replacement
                    #Check 2 adjacency with addition
                    
                    #Check 1 adjacency with replacement
                    #Check 1 adjacency with addition
                    print "HI"
                #Checking all possible adjacency at position 1
                elif index == bitTwo:
                    #Check 3 adjacency with replacement
                    #Check 3 adjacency with addition
                    
                    #Check 2 adjacency with replacement
                    #Check 2 adjacency with addition
                    
                    #Check 1 adjacency with replacement
                    #Check 1 adjacency with addition
                    print "HI"
                #Checking all possible adjacency at position 2
                elif index == bitThree:
                    #Check 3 adjacency with replacement
                    #Check 3 adjacency with addition
                    
                    #Check 2 adjacency with replacement
                    #Check 2 adjacency with addition
                    
                    #Check 1 adjacency with replacement
                    #Check 1 adjacency with addition
                    print "HI"
                #Checking all possible adjacency at position 3
                elif index == bitFour:
                    #Check 3 adjacency with replacement
                    #Check 3 adjacency with addition
                    
                    #Check 2 adjacency with replacement
                    #Check 2 adjacency with addition
                    
                    #Check 1 adjacency with replacement
                    #Check 1 adjacency with addition
                    print "HI"
        
        else:
            operation = self.replace
            selected = 0
    	return operation, selected