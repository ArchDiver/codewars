def justLetterOnly(string):
    """This version only flips letters. It won't effect numbers"""
    ans, word = '', []
    for val in string:
        if val.isalpha():
            word.insert(0, val)
        else:
            ans += ''.join(word) + val
            word = []
    
    return ans

def justLetterNum(string):
    """This version flips letters AND numbers. In case there is leet code."""
    ans, word = '', []
    for val in string:
        if val.isalpha() or val.isnumeric():
            word.insert(0, val)
        else:
            ans += ''.join(word) + val
            word = []
    
    return ans



print(justLetter("Hello  world!"))
print(justLetterNum("He110  !W0R1*"))