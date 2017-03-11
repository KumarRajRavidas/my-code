
def semordnilap1(str1):
    if len(str1) == 1:
        return True
    if str1[0] ==str1[1] :
        return True
    if str1[0] == str1[-1]:
        return semordnilap1(str1[1:-1])
    else:
        return False
print semordnilap1("rajjar")  
print ''


def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) #1 and -1 not includ ex= rajkumar  ajkuma.
    return isPal(toChars(s))
print isPalindrome('qwertyuuytrewq')
print ''





def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilapWrapper(str1, str2)




def semordnilap2(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # If strings aren't the same length, they cannot be semordnilap
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter
    # of str2
    if str1[0] == str2[-1]:
        return semordnilap2(str1[1:], str2[:-1])
    else:
        return False
print semordnilap2("r", "r")    


def reversestr(strr):
    revers=''
    if len(strr)==1:
        return strr
    for i in range(1,len(strr)+1):
            revers= revers + strr[-i]
    return revers    

strr='rajkumarravidas * sadivarramukjar'
print reversestr(strr)












    