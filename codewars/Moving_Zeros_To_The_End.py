'''
codewars.Moving_Zeros_To_The_End의 Docstring

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

# w/o numpy
def move_zeros(lst):
    cnt = lst.count(0)
    
    for i in range(cnt):
        lst.remove(0)
        
    lst.extend([0] * cnt)
        
    return lst
