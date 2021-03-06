import MapReduce
import json
import sys

mr = MapReduce.MapReduce()
# Map function
# record - json object formatted as a string
def mapper(record):
    key = record[0]
    value = record[1]
    visited = []
    for word in value.split():
        # output (key, value) pair (only for mapper)
        if word not in visited:
             visited.append(word)
             mr.emit_intermediate(word, key)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    # output item (only for reducer)
    mr.emit((key,list_of_values))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
