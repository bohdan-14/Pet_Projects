#10.1

def som_gen (begin, end, func):
     for i in range (end):
          yield begin
          begin = func (begin)


#10.2

def first_word (text):
     text_cleared = text.replace (".", "").replace(",", "")
     text_word = text_cleared.split()
     result = text_word[0]
     return result

#10.3

def is_even (digit):
     if digit % 2 == 0:
          return True
     else:
          return False