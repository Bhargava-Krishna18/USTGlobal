
# generator to print the numbers which can be divisible by 5 and 7 between 0 and given number n
def div_5_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
            
            
def print_div_5_7(n):
    result = ','.join(str(num) for num in div_5_7(n))
    print(result)
    return result


#unitest

import unittest

class Test(unittest.TestCase):
    def test_div_5_7(self):
        result = list(div_5_7(100))
        self.assertEqual(result, [0, 35, 70])

    def test_print_div_5_7(self):
        self.assertEqual(print_div_5_7(100), "0,35,70")

if __name__ == "__main__":
    unittest.main()


# function that interleaves 2 strings

def inters(str_1, str_2):
    inter = ''.join(s1 + s2 for s1, s2 in zip(str_1, str_2))
    if len(str_1) > len(str_2):
        inter += str_1[len(str_2):]
    elif len(str_1) < len(str_2):
        inter += str_2[len(str_1):]
    return inter


str_1 = "AAAA"
str_2 = "1234567"
inter = inters(str_1, str_2)
print(inter)



import unittest

def inters(str_1, str_2):
    inter = ''.join(s1 + s2 for s1, s2 in zip(str_1, str_2))
    if len(str_1) > len(str_2):
        inter += str_1[len(str_2):]
    elif len(str_1) < len(str_2):
        inter += str_2[len(str_1):]
    return inter

class TestIntersFunction(unittest.TestCase):
    def test_inters(self):
        result = inters("AAAA", "1234567")
        self.assertEqual(result, "A1A2A3A4567")

    def test_inters_with_empty_string(self):
        result = inters("", "1234567")
        self.assertEqual(result, "1234567")

    def test_inters_with_different_length(self):
        result = inters("AAAA", "123")
        self.assertEqual(result, "A1A2A3A")

if __name__ == "__main__":
    unittest.main()
