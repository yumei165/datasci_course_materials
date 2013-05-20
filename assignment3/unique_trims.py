import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: share same key
    # value: string of nucleotides after trimming
    value = record[1]
    mr.emit_intermediate(1,value[0:-10])
   

def reducer(key, list_of_values):
    # key: common key
    # value: list of trimmed string
    s = set()
    for unit in list_of_values:
      if unit not in s:
         s.add(unit)
         mr.emit(unit)
      

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
