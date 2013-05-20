import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person identifier
    # value: null
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: person identifier
    # value: list of occurrence counts of key
    
    mr.emit((key,len(list_of_values)))
      

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
