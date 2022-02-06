from random import shuffle
from statistics import mean
from nerdledict import nerdleDict



verbose = True

def setVerbose(b):
  global verbose
  verbose=b


def bitmap(word):
  return sum( 2**(ord(c)) for c in set(word) )

def possibles(startlist, green, grey, yellow):
  wordlist = []
  for word in startlist:

    if nerdleDict[word] & grey :
      continue

    yellowpass = True
    for y in yellow:
      if any ( y[i] != '.' and (y[i] not in word or y[i] == word[i])
               for i in range(8) ):
        yellowpass = False
        break
    if not yellowpass:
      continue
    
    if green != '........':
      if any(green[i] != '.' and word[i] != green[i]
             for i in range(8) ):
        continue


    wordlist.append(word)
  return wordlist  
#---------------------------------------------------------------------------  

def best(wordlist, green, grey, yellow):

  
  if len(wordlist)==2:
    if verbose: print("only two options:", wordlist)
    return wordlist[0]
  
  if len(wordlist)==1:
    if verbose: print("only one option:", wordlist)
    return wordlist[0]
  
  if len(wordlist)==0:
    raise Exception("empty wordlist encountered")

  bestword=''
  bestlen = (1000000, 1000000.0)

  for word in nerdleDict:

    worstlen = 0
    slens = []
    for solution in wordlist:

      newgreen = green
      for i in range(8):
        if solution[i]==word[i]:
          newgreen = newgreen[:i] + word[i] +newgreen[i+1:]
          assert len(newgreen)==8

      newgrey = grey
      newyellow = list(yellow)
      
      for i,c in enumerate(word):
        if c not in solution:
          newgrey |= 2**(ord(c))
        else:
          if c != newgreen[i]  :
            ny = '........'
            newyellow.append( ny[:i] + c + ny[i+1:] )
            
      newwordlist = possibles(wordlist, newgreen, newgrey, newyellow)
      slens.append( len(newwordlist) )
      if len(newwordlist) > worstlen:
          worstlen = len(newwordlist)
      if worstlen > bestlen[0]:
        break

    worstavg = ( worstlen, mean(slens) )

    #if worstavg[1] < bestlen[1] and worstavg[0] > bestlen[0]:
    #  print("not considering ", worstavg , "as better than ", bestlen)

    if worstavg < bestlen or (worstavg==bestlen and word in wordlist):
      bestlen = worstavg
      bestword = word
      if verbose: print(bestword, bestlen)
      
  if verbose: print( '"'+bestword+'"', "has a worst case of", bestlen,"options")
  return bestword
  
# ------------------------------------------------------------------------        

if __name__ == '__main__':
  from time import perf_counter

  # green is a single 8 character string that indicate the
  # positions of green squares
  green = '......=.'
 
  # yellow is a list of 8 character strings that indicate the
  # positions of yellow squares.
  yellow = ['9...7=..']

  # grey is just a bitmap of the grey characters, without
  # regard to their position
  grey = bitmap('*8-65')

  wordlist = possibles(nerdleDict, green, grey, yellow)

  print("Starting equation list: ", len(wordlist), wordlist )
  starttime= perf_counter()
  best(wordlist, green, grey, yellow)
  endtime= perf_counter()
  print(round(endtime-starttime,1),"sec")
