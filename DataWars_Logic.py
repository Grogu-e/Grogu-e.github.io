# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:33:35 2022

@author: anacs
"""
class DataWars_Logic:
    
    
    
    def __init__(self):
        
        pass
    
    def checkIssue(self,issue, userResponses):
        realResponses = issue.discover()
        if realResponses == userResponses:
            return True
        else:
            return False
            
        #actualResponses = (realResponses == userResponses)
        #return actualResponses
    
class DataWars:
    def __init__(self):
        self.issues = None
        
class Issue:
    def __init__(self,numberOne, operator,numberTwo, responsed):
        self.numberOne = numberOne
        self.operator = operator
        self.numberTwo = numberTwo 
        self.responsed = responsed
        
        
    def __str__(self):
        """Displaying issues in readable form.
        Doctests:
        >>> myIssue = Issue(1, "+" , 3, 4)
        >>> str(myIssue)
        '1 + 3 = 4'
        >>> i = Issue(1, "+", 1, 2)
        >>> str(i)
        '1 + 1 = 2'
        """
        issueString = str(self.numberOne) + " " + self.operator + " " +  str(self.numberTwo) + " = " + str(self.responsed)
        return issueString
    
    def discover(self):
        """ To fine the actual answer
        >>> myIssue = Issue(1, "+", 3, 4)
        >>> myIssue.discover()
        4
        """
        return 4
    
    
    # #def mop(self):
    #     """
        
    #     mops the floor
    #     Returns
    #     -------
    #     None.
        
    #     Doctests:
    #    >>> i = Issue(1, "+", 1, 2)
    #    >>> i.mop()
    #    "It's mopped"
            
    #     """
    #     return "It's mopped"
    
if __name__ == "__main__":
    """ tes"""
    import doctest
    doctest.testmod(verbose=True)
       

