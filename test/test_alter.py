import unittest
def alternatingCharacters(s):
    alt = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            alt += 1
    
    return alt
class TestAlter(unittest.TestCase):
    def test_one(self):
     assert alternatingCharacters("ABAB") == 0
     assert alternatingCharacters("AAABBB") == 1
     assert alternatingCharacters("AAABBBAABB") == 4
     assert alternatingCharacters("") == 0
     assert alternatingCharacters("A") == 0
     assert alternatingCharacters("AB") == 0
     assert alternatingCharacters("AA") == 1
     assert alternatingCharacters("ABABAB") == 0
     assert alternatingCharacters("CCCCCC") == 5
     assert alternatingCharacters("AaAaAa") == 0
     assert alternatingCharacters("AaAaAaa") == 1
    pass

if __name__ == '__main__':
    unittest.main()