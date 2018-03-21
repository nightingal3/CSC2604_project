import re
import pickle
import os
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

def get_synonyms(filename): #This is meant to be used on "English Synonyms and Antonyms" by James Champlin Fernald
    f = open(filename, "r")
    lines = f.readlines()[460:]
    synonym_dict = {}
    word_pattern = "[A-Z]+\."
    syn = r"Synonyms"
    syn_pattern = "([a-z]+(,|.|\s)+)+"
    for i in range(len(lines)-1):
        matchObj = re.search(word_pattern, lines[i])
        #print(lines[i])
    if matchObj:
        synonym_dict[matchObj.group()] = []
        j = i + 1
        if re.search(syn, lines[j]):
            j = i + 2
            #syn_match = re.findall(syn_pattern, lines[j]
            while True:
                syn_match = re.findall(syn_pattern, lines[j])
                print(syn_match)
                if not syn_match:
                    break
                synonym_dict[matchObj.group()].extend(syn_match)
                print(synonym_dict[matchObj.group()])
                #assert False
                j += 1
        i += j - i
  
    f.close() 

    return synonym_dict
"""
def rahmGetSyn():
    # only works for test.txt
    f = open("test.txt", 'r')
    data = f.readlines()
    syn = "".join(data[456:21986])
    raw_syn = re.findall('(?<=Synonyms:)\n\n.*?\n\n', syn,re.DOTALL)
    syn_body = [i.replace(',', "").replace('.', "").split() for i in raw_syn]
    syn_body = [i.lower() for i in syn_body]

    raw_syn_header = re.findall('(?<=\*).*?(?=Synonyms:)', syn, re.DOTALL)
    syn_header = [i.replace('*', "").replace('.', "").strip() for i in raw_syn_header]

    print(syn_body)
    syn_header = [i.lower() for i in syn_header]

    syn_dict = {}
    for i in range(len(syn_header)):
        syn_dict[syn_header[i]] = syn_body[i]

    f = open("syn_dict.pickle", 'wb')

    # remember to run/load with python3
    pickle.dump(syn_dict, f, pickle.HIGHEST_PROTOCOL)
    f.close()
"""

def five_grams_read():
    """im deciding to do all the counting and file opening in one function, so that we can one by one open the files. Otherwise i think the string/list of all lines from all ngrams would crash something.
    Also note, initially, im attempting to get context for every word in the synonym dictioinary, we'll see how it goes."""
	
    # import synonyms
    syn_file = open("syn_dict.pickle", 'rb')
    syn_dict = pickle.load(syn_file)
    syn_file.close()

    # dict of each header synonym, where the value will be a set of contexts
    context_dict = {}
    # initialize with syn_dict keys
    for key in syn_dict:
        context_dict[key] = set([])

    wnet_pos = {

    "NOUN":'n',
    "VERB":'v',
    "ADJ": 'a',
    "ADV": 'r'

    }

    wnet_lemtzr = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))


	# changes current working directory to the previos directory, where the 5gram data is
    
    #os.chdir("/./../") # just going to test on the 5grams that are NOT in the downloads dir.
	# uncomment the above chdir to test on the actual 5 gram set
   

	#~~~~~~~set up done

    print(os.getcwd())
	# iterate over each file in the 5gram directory, with checking if it is a 5 gram file.
    for fname in os.listdir("./../../../data/downloads/google_ngrams/5/"):
        print("opening %s" % fname)
        if fname[:6] != "google":
            continue
        full_path = os.path.join("./../../../data/downloads/google_ngrams/5/", fname)
        curr_file = open(full_path,'r')
        print(curr_file)
        print(full_path)
        #data = curr_file.readlines()
        curr_file.close()
	
        with open(full_path, "r") as data:
        	for unformat_line in data:
        		unformat_line.replace("", '\n')
        		line = unformat_line.split()
                	print(line)
        		# im assuming that target word is the first word in the 5gram
        		# not sure if i should lemmatize the target word tbh
			if len(line) <= 4:
			    continue
        		word = line[4].lower().split("_") # splits potential POS tagging
        		#[0] element should be the word without any POS tagging, regardless of
        		if word[0] in context_dict:
        			""" tests for a word to be a useful context word,  not necessarily in order """
        		# first must be lemmatize
        		# is alphabetical only
        		# is not a function word, determiner/article, pronoun, pre and postpositions, conjunction, auxilliary verbs, interjections, particles, expletives, 	prosentences
        		# using stop word set for the above^

        		# iterate over every context word
				print(word[0])
        			for context in [line[1], line[2], line[3], line[4]]:
        			#pos split
        				new_context = context.split("_")
					print(new_context)
					
        				if new_context[0].isalpha():
        				#new_context = new_context.lower()
        					if new_context[0].lower() not in stopWords:
        						if len(new_context) == 2 and new_context[1] in wnet_pos: # because dog_NOUN = [dog,NOUN]
								print("New context found")
                                                                print(new_context)
			  
        							final_context = wnet_lemtzr.lemmatize(new_context[0], wnet_pos[new_context[1]])
        						else:
        							final_context = wnet_lemtzr.lemmatize(new_context[0])
							print(final_context)
        					# update the set at the correct key-value
        						context_dict[word[0]].add(final_context)
							print(context_dict[word[0]])
						
		print(context_dict)
    f = open("context_dict.p", "w")
    pickle.dump(context_dict, f, 2)
    f.close()


def common_context(w1, w2, context_dict):
	return context_dict[w1].intersection(context_dict[w2])


if __name__ == "__main__":
    #rahmGetSyn()
    five_grams_read()
    #print(get_synonyms("test.txt"))

