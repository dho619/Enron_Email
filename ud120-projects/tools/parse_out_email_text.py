from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()
    
    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        ### project part 2: comment out the line below
        #words = text_string
        stemmer = SnowballStemmer("english")
        
        words = text_string.split()
        
        for i, palavra in enumerate(words):
            words[i] = stemmer.stem(palavra)
        '''
        aux = ""
        for i, palavra in enumerate(words):
            #print(i, " : ", palavra)
            if aux == "":
                aux = palavra
            else:
                aux = aux + " " + palavra
                    
        words = aux
        '''
        words = ' '.join(words)
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        




    return words

    

def main():
    ff = open("..\maildir/jones-t/all_documents/4056.", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

