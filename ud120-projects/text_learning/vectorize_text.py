#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText
from sklearn.feature_extraction.text import TfidfVectorizer

from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []
count = 0

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        #if count==200:
        #    break
        #count +=1
        path = os.path.join('..', path[:-1])
        #print path
        email = open(path, "r")
            
        temp = parseOutText(email)

        signature_words = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]
        for signature_word in signature_words:
            temp = temp.replace(signature_word, "")
           
        word_data.append(temp)			
        if name == "sara":
            from_data.append(0)
        else:
            from_data.append(1)
        
        email.close()


#print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit(word_data)
vectorizer.transform(word_data)
vocab_list = vectorizer.get_feature_names()
print(len(vocab_list))
print(vocab_list[34597])

