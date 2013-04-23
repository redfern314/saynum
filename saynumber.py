# saynumber.py
#
# Contains code that takes in an int from the command line 
#   and plays back the verbal representation of the number
#
# Requires an updated version of Linux and appropriate .wav
#   files stored in the same directory as this script
#
# Possible future improvements: add functionality for reading
#   the word "and" at appropriate places in the number
#
# Written by Derek Redfern
# 10/26/12

import sys
import os

def numtotext(num,level):
    ''' Converts a number in a string to the textual equivalent.
        i.e. '12' becomes 'twelve'.

        Operates by splitting the string into groups of 3 characters ('triples')
            and recursing on the triples

        Args:
            num: string representing a number between 0 and 999999999, inclusive
            level: level of recursion (0 represents the 'ones' triple, 1 represents 'thousands', etc)

        Returns: string containing a textual representation of num
    '''
    result="" #accumulates the textual representation 
    if len(num)==0 or int(num)==0:
        return("") #return empty string
    while len(num)>3: #split into triples; recurse on newly created triples
        result=numtotext(num[-3:],level)+result
        level+=1
        num=num[:-3]

    #take the last remaining segment of size <=3 and use it as a base case for the recursive function

    #if num is less than 3 digits, prepend an appropriate number of '0's
    if len(num)==1:
        num='00'+num
    if len(num)==2:
        num='0'+num

    temp="" #temp accumulates the values for this triple
    if not num[0]=='0': #handle hundreds place
        temp+=numtotext('00'+num[0],0)
        temp+="hundred "

    if not num[1]=='1':
        #handle tens place
        if num[1]=='2':
            temp+="twenty "
        elif num[1]=='3':
            temp+="thirty "
        elif num[1]=='4':
            temp+="forty "
        elif num[1]=='5':
            temp+="fifty "
        elif num[1]=='6':
            temp+="sixty "
        elif num[1]=='7':
            temp+="seventy "
        elif num[1]=='8':
            temp+="eighty "
        elif num[1]=='9':
            temp+="ninety "

        #handle ones place
        if num[2]=='1':
            temp+="one "
        elif num[2]=='2':
            temp+="two "
        elif num[2]=='3':
            temp+="three "
        elif num[2]=='4':
            temp+="four "
        elif num[2]=='5':
            temp+="five "
        elif num[2]=='6':
            temp+="six "
        elif num[2]=='7':
            temp+="seven "
        elif num[2]=='8':
            temp+="eight "
        elif num[2]=='9':
            temp+="nine "
    else: #where num[1]==0
        if num[2]=='0':
            temp+="ten "
        elif num[2]=='1':
            temp+="eleven "
        elif num[2]=='2':
            temp+="twelve "
        elif num[2]=='3':
            temp+="thirteen "
        elif num[2]=='4':
            temp+="fourteen "
        elif num[2]=='5':
            temp+="fifteen "
        elif num[2]=='6':
            temp+="sixteen "
        elif num[2]=='7':
            temp+="seventeen "
        elif num[2]=='8':
            temp+="eighteen "
        elif num[2]=='9':
            temp+="nineteen "

    #append string corresponding to tuple level
    if level==1:
        temp+="thousand "
    elif level==2:
        temp+="million "

    result=temp+result
    return(result) #return textual string

def saystr(text):
    ''' Reads out a string of number words (i.e. ten, hundred, five, etc)
        Uses a call to the Linux function aplay to play corresponding wav files

        Args:
            text: string containing number words
        Returns:
            nothing
    '''
    words=text.split() #split into list of words
    for word in words:
        os.system("aplay audio/"+word+".wav") #play corresponding wav file

#===============================MAIN CODE===============================

numstr=sys.argv[1] #get number from cmd-line
try:
    num=int(numstr) #try a cast in case of invalid input
except ValueError:
    sys.exit("Invalid number")
finally:
    if num>=1000000000 or num<0: #number is negative or too large
        sys.exit("Number not currently handled.")

text = numtotext(numstr,0) #convert to textual string
print '\n'+text+'\n' #print string to standard output
saystr(text) #read textual string