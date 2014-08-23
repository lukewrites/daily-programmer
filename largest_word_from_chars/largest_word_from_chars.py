"""
Given a string of words and a string of letters. Find the largest string(s) that
are in the 1st string of words that can be formed from the letters in the 2nd
string.
  Letters can be only used once. So if the string has "a b c" then words like
     "aaa" and "bbb" do not work because there is only 1 "a" or "b" to be used.
  If you have tie for the longest strings then output all the possible strings.
  If you find no words at all then output "No Words Found"


Challenge input 1:
hello yyyyyyy yzyzyzyzyzyz mellow well yo kellow lellow abcdefhijkl hi is yellow just here to add strings fellow lellow llleow
l e l o h m f y z a b w

Challenge input 2:
sad das day mad den foot ball down touch pass play
z a d f o n


"""

def word_checker(words, chars):
    # make the chars into a sorted list of letters
    letters = chars.join(' ').sort()
    # take each of the words and sort them
    
    # check to see if each of the sorted words is in the sorted list of letters

    # look @ the list of words that are in the sorted list of letters.
    # find the longest one(s)

    # return longest word(s)

