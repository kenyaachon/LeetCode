def findSimilarities(source, newWord):
  #check to make sure the words are the same size
  if len(source) != len(newWord):
    return False
  
  size = len(source)
  similarities = 0
  #traverse through both strings
  for i in range(0, size):
    if source[i] == newWord[i]:
      similarities += 1
    
    
  #check the similarities counter to see whether the words are similar enough
  if similarities == size - 1:
    return True
  else:
    return False
  
    
def shortestWordEditPath(source, target, words):
  #traverse through the string
  transitions = 0
  for word in words:
    if findSimilarities(source, word):   #check to make sure that only letter has been changed
      source = word
      transitions += 1
      print(source)
      
    if source == target:    #check if the current source is same as target word
      return transitions
  #automatically return -1 if it is not possible to change the word
  return -1