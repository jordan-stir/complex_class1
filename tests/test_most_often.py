from lib.most_often import *

#list needs creating
#is there anything contained in the list
#check the list for unique items
#return highest count and highest items frequency
#return unique highest count item

def test_add_new_item():
    mostoften = MostOften([1, 3, 3, 5])
    mostoften.add_new(7)
    assert mostoften.starting_list == ([1, 3, 3, 5, 7])

def test_checklist():
    mostoften = MostOften([])
    assert mostoften.starting_list == ([])

def test_get_most_often():
    mostoften = MostOften([1, 3, 3, 5])
    assert mostoften.get_most_often() == 3

def test_no_clear_winner():
    mostoften = MostOften(["a", "a", "b", "b", "c"])  
    assert mostoften.get_most_often() == "no clear winner" 

def test_clear_winner():
    mostoften = MostOften(["a", "a", "b", "b", "b"])  
    assert mostoften.get_most_often() == "b" 

def test_equally_high_count():
    mostoften = MostOften(["a", "a", "b", "b"])
    assert mostoften.get_most_often() == "no clear winner" 