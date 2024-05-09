# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(num):
    str_num = str(num)
    return [int(n) for n in str_num[::-1]]
