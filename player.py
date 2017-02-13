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
        
    def findMaxOpPos(currentMax, oldOp, oldPos, newVal, op, pos):
        """
        This function finds the operation and position that will yield the maximum value of points

        Args:
            currentMax (int): The current max value
            oldOp: [self.add | self.replace]
            oldPos (int): [0|1|2|3]

            newVal (int): New value that will be compared to the current max
            op: [self.add | self.replace]
            pos (int): [0|1|2|3]

        Returns:
            newMax (int)
            operation: [self.skip | self.add | self.replace]
            selected: [0|1|2|3]
        """
        #If current max is less than the new value; return new value and its op and pos
        if currentMax < newVal:
            return newVal, op, pos
        #Current max is greater than the new value; return the current max and its op and pos
        else:
            return currentMax, oldOp, oldPos
        
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
        
        #The sum of randBit and values that are in the array
        sumBitOne = randBit + bitOne
        sumBitTwo = randBit + bitTwo
        sumBitThree = randBit + bitThree
        sumBitFour = randBit + bitFour 
        
        """
        Logic:
        1.  Check if the random bit can add/replace bits in position 2 | 3
            If it can, then replace the highest one
        
        2.  Check all possible adjacency and pick the max value
        """
        #Checks if the random bit can add/replace bits in position 2 | 3
        if randBit == codeOne or sumBitThree == codeOne or randBit == codeTwo or sumBitFour == codeTwo:
            #Checks if the random bit is equal to the value of the first code digit (pos 2)
            if randBit == codeOne:
                operation = self.replace
                selected = 2
            #Checks if the random bit plus the value of the third bit is equal to the first code digit
            elif sumBitThree == codeOne:
                operation = self.add
                selected = 2
            #Checks if the random bit is equal to the value of the second code digit (pos 3)
            elif randBit == codeTwo:
                operation = self.replace
                selected = 3
            #Checks if the random bit plus the value of the fourth bit is equal to the second code digit
            elif sumBitFour == codeTwo:
                operation = self.add
                selected = 3
        
        #Checks if there are any adjacency in the list
        #FIXME: WRONG LOGIC
        elif randBit in four_bits or sumBitOne in four_bits or sumBitTwo in four_bits or sumBitThree in four_bits or sumBitFour in four_bits:
            #Default values. Will be changed after for loop
            currentMax = 0
            operation = self.skip
            selected = 0
            
            #Looping through each bit in the four_bits array
            for index in (0, 4):
                #Checking all possible adjacency at position 0
                if index == 0:
                    #Check 3 adjacency with replacement
                    if randBit == bitTwo and randBit == bitThree and randBit == bitFour:
                        #Compute the total points earned
                        totalPoints = 8 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 0)
                    #Check 3 adjacency with addition
                    if sumBitOne == bitTwo and sumBitOne == bitThree and sumBitOne == bitFour:
                        #Compute the total points earned
                        totalPoints = 8 * sumBitOne
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 0)
                        
                    #Check 2 adjacency with replacement
                    if randBit == bitTwo and randBit == bitThree:
                        #Compute the total points earned
                        totalPoints = 4 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 0)
                    #Check 2 adjacency with addition
                    if sumBitOne == bitTwo and sumBitOne == bitThree:
                        #Compute the total points earned
                        totalPoints = 4 * sumBitOne
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 0)
                    
                    #Check 1 adjacency with replacement
                    if randBit == bitTwo:
                        #Compute the total points earned
                        totalPoints = 2 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 0)
                    #Check 1 adjacency with addition
                    if sumBitOne == bitTwo:
                        #Compute the total points earned
                        totalPoints = 2 * sumBitOne
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 0)

                #Checking all possible adjacency at position 1
                elif index == 1:
                    #Check 3 adjacency with replacement
                    if randBit == bitOne and randBit == bitThree and randBit == bitFour:
                        #Compute the total points earned
                        totalPoints = 8 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 1)
                    #Check 3 adjacency with addition
                    if sumBitTwo == bitOne and sumBitTwo == bitThree and sumBitTwo == bitFour:
                        #Compute the total points earned
                        totalPoints = 8 * sumBitTwo
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 1)

                    #Check 2 adjacency with replacement
                    if randBit == bitThree and (randBit == bitOne or randBit == bitFour):
                        #Compute the total points earned
                        totalPoints = 4 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 1)
                    #Check 2 adjacency with addition
                    if sumBitTwo == bitThree and (sumBitTwo == bitOne or sumBitTwo == bitFour):
                        #Compute the total points earned
                        totalPoints = 4 * sumBitTwo
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 1)
                        
                    #Check 1 adjacency with replacement
                    if randBit == bitOne or randBit == bitThree:
                        #Compute the total points earned
                        totalPoints = 2 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 1)
                    #Check 1 adjacency with addition
                    if sumBitTwo == bitOne or sumBitTwo == bitThree:
                        #Compute the total points earned
                        totalPoints = 2 * sumBitTwo
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 1)
                        
                #Checking all possible adjacency at position 2
                elif index == 2:
                    #Check 3 adjacency with replacement
                    if randBit == bitOne and randBit == bitTwo and randBit == bitFour:
                        #Compute the total points earned
                        totalPoints = 8 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 2)
                    #Check 3 adjacency with addition
                    if sumBitThree == bitOne and sumBitThree == bitTwo and sumBitThree == bitFour:
                        #Compute the total points earned
                        totalPoints = 8 * sumBitThree
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 2)
                    
                    #Check 2 adjacency with replacement
                    if randBit == bitTwo and (randBit == bitOne or randBit == bitFour):
                        #Compute the total points earned
                        totalPoints = 4 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 2)
                    #Check 2 adjacency with addition
                    if sumBitThree == bitTwo and (sumBitThree == bitOne or sumBitThree == bitFour):
                        #Compute the total points earned
                        totalPoints = 4 * sumBitThree
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 2)
                    #Check 1 adjacency with replacement
                    if randBit == bitTwo or randBit == bitFour:
                        #Compute the total points earned
                        totalPoints = 2 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 2)
                    #Check 1 adjacency with addition
                    if sumBitThree == bitTwo or sumBitThree == bitFour:
                        #Compute the total points earned
                        totalPoints = 2 * sumBitThree
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 2)
                        
                #Checking all possible adjacency at position 3
                elif index == 3:
                    #Check 3 adjacency with replacement
                    if randBit == bitOne and randBit == bitTwo and randBit == bitThree:
                        #Compute the total points earned
                        totalPoints = 8 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 3)
                    #Check 3 adjacency with addition
                    if sumBitFour == bitOne and sumBitFour == bitTwo and sumBitFour == bitThree:
                        #Compute the total points earned
                        totalPoints = 8 * sumBitFour
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 3)
                        
                    #Check 2 adjacency with replacement
                    if randBit == bitTwo and randBit == bitThree:
                        #Compute the total points earned
                        totalPoints = 4 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 3)
                    #Check 2 adjacency with addition
                    if sumBitFour == bitTwo and sumBitFour == bitThree:
                        #Compute the total points earned
                        totalPoints = 4 * sumBitFour
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 3)
                    
                    #Check 1 adjacency with replacement
                    if randBit == bitThree:
                        #Compute the total points earned
                        totalPoints = 2 * randBit
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 3)
                    #Check 1 adjacency with addition
                    if sumBitFour == bitThree:
                        #Compute the total points earned
                        totalPoints = 2 * sumBitFour
                        #Compare with current max
                        currentMax, operation, selected = findMaxOpPos(currentMax, operation, selected, totalPoints, self.replace, 3)
        
        else:
            operation = self.replace
            selected = 0
    	return operation, selected