test_array: list[int] = [0,0,1,5]
# =>[1,5,0,0]
#move to left
i = 0
while i < len(test_array):
  if test_array[i] == 0:
    j = i + 1
    while j < len(test_array):
      if test_array[j] != 0:
        test_array[i] = test_array[j]
        test_array[j] = 0
        
      j = j + 1
  
  i = i +1
  
print (test_array)
  