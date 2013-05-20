import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i,j) element in product matrix
    # value: kth contribution value
    key = record[1]
    for j in range(0,5):
      if record[0] == 'a':
         mr.emit_intermediate((record[1],j), (record[2],record[3]))
      else:
         mr.emit_intermediate((j,record[2]),(record[1],record[3]))
def reducer(key, list_of_values):
    # key: (i,j) entry information
    # value: list of (i,k) in 'a' and (k,j) in 'b' values
    tmp = {}
    value = 0
    for item in list_of_values:
        if item[0] in tmp:
           value += tmp[item[0]]*item[1]
        else:
           tmp[item[0]] = item[1]   
    mr.emit((key[0],key[1],value))
      

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
