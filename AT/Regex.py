import pytest
import re
def verEmail(email):
    x = re.search("^[a-z0-9]+[\.'\-a-z0-9_]*[a-z0-9]+@(gmail|googlemail)\.com$", email)
    ret = False
    if x:
        ret = True
    else:
        ret = False
    return ret
    
class TestStringMethods():
    def test_one(self):
        assert verEmail("admin@gmail.com") == True
    def test_two(self):
        assert verEmail("john.smith@googlemail.com") == True
    def test_three(self):
        assert verEmail("john5.a.smith@gmail.com") == True
    def test_four(self):
        assert verEmail("jane_doe@googlemail.com") == True
    def test_five(self):
        assert verEmail("patrick.o'reilly@gmail.com") == True
    def test_six(self):
        assert verEmail(".admin@gmail.com") == False
    def test_seven(self):
        assert verEmail("postmaster.@gmail.com") == False
    def test_eight(self):
        assert verEmail("patrick.o'reilly.@gmail.com") == False
    def test_nine(self):
        assert verEmail("admin@@gmail.com") == False
    def test_ten(self):
        assert verEmail("admin@gmail..com") == False  
        
if __name__ == '__main__':
    TestStringMethods()
