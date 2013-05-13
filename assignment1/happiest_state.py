from __future__ import division
import sys
import json
import string,re

def clean(tweet):
       # tweet = tweet.lower()
        tweet = re.sub('[%s]'%(re.escape(string.punctuation)),'',tweet)
        words = tweet.split()
        return words

def main():
   #get tweet data and sentiment dict
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #initialize result
   result = {}
   
   #set up scores dict
   scores = {}
   for line in sent_file.readlines():
        term, score = line.split('\t')
        scores[term] = int(score)
  
   #get tweets and calculate scores
   for line in tweet_file.readlines():
        tweet_line = json.loads(line)
        eachtweet= tweet_line.get('text', '')
        place = tweet_line.get('place', '')
        if eachtweet and place and place['country_code'] == 'US': 
           state = place['full_name'].split()[-1]
           words = clean(eachtweet)
           score = 0
           for word in words:
               word = word.encode('utf-8')
               score += scores.get(word,0)
           if score > 0 :
               updatescore = 1
           elif score < 0:
               updatescore = -1
           else:
               updatescore = 0

           result[state] = float(updatescore) + result.get(state,0)
                
   print max(result, key = result.get)
   
#    
if __name__ == '__main__':
    main() 
