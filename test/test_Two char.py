import unittest
def alternate(s):
    max_length = 0
    for char1 in set(s):
        for char2 in set(s):
            if char1 != char2:
                filtered_str = ''.join(c for c in s if c == char1 or c == char2)
                if all(filtered_str[i] != filtered_str[i+1] for i in range(len(filtered_str)-1)):
                    max_length = max(max_length, len(filtered_str))
    
    return max_length
    
    return alt
class Tes_twochar(unittest.TestCase):
    def test_two(self):
     assert alternate("A") == 0
     assert alternate("") == 0
     assert alternate("AB") == 0

    pass

if __name__ == '__main__':
    unittest.main()