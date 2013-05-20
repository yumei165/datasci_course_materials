import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friend tuple concatenated as a string
    # value: null
      key = record[0]+' '+record[1]
      mr.emit_intermediate(key,1)
   

def reducer(key, list_of_values):
    # key: friend tuple
    # value: list of occurrence counts of key
    if len(list_of_values) == 1:
      elem = key.split() 
      mr.emit((elem[1],elem[0]))
      mr.emit(tuple(elem))
      

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
