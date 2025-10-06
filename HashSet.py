import re
import argparse
import random

parser = argparse.ArgumentParser(description='Find lines containing a consecutive word pair in a text file.')
parser.add_argument('hashTableSize', type=int)
parser.add_argument('word1')
parser.add_argument('word2')

args = parser.parse_args()

filename = "data-assgn-6.txt"
hashTableSize = args.hashTableSize
word1 = args.word1
word2 = args.word2
pair_key = word1 + ' ' + word2


sentences = []
try:
  with open(filename, 'r') as file:
    for line in file:
      sentences.append(line.strip()) 


  print(f"Number of sentences read: {len(sentences)}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")



    import random

def hashFunction(key, a, b, p, m):
  
  numericalKey = sum(ord(char) for char in key)
  return ((a * numericalKey + b) % p) % m


p = 999999937
a = random.randint(1, p - 1)
b = random.randint(0, p - 1)


class HashTable:
    def __init__(self, size) :   
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def insert(self, key, value) :
        hash_value = hashFunction(key, a, b, p, self.size)
        
        for i, (existing_key, value_list) in enumerate(self.table[hash_value]):
            if existing_key == key and value not in value_list:
                self.table[hash_value][i] = (existing_key, value_list + [value])
                return
        
        self.table[hash_value].append((key, [value]))

    def get(self, key) :
       hash_val = hashFunction(key, a, b, p, self.size)
       for prevKey, valList in self.table[hash_val] :
          if prevKey == key:
             return valList
       return []
    
hashTable = HashTable(args.hashTableSize)

for lineID, sentence in enumerate(sentences) :
   words = re.findall(r'\b\w+\b', sentence.lower())
   
   for i in range(len(words)-1) :
    if words[i] == word1 and words[i+1] == word2 : 
      hashTable.insert(pair_key,(lineID, i))
   

resultIDs = hashTable.get(pair_key)
results_by_line = {}

for lineID, pos in resultIDs:
    if lineID not in results_by_line:
        results_by_line[lineID] = []
    results_by_line[lineID].append(pos + 1)  

for lineID in sorted(results_by_line):
    positions_str = ', '.join(str(p) for p in results_by_line[lineID])
    print(f"ID: {lineID + 1} Position: {positions_str}")


print(f"There are total {len(resultIDs)} occurences of Key: '{pair_key}'")