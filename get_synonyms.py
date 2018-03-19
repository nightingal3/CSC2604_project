import re
import pickle
import os
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

def rahmGetSyn():
    # only works for test.txt
    f = open("test.txt", 'r')
    data = f.readlines()
    syn = "".join(data[456:21986])
    raw_syn = re.findall('(?<=Synonyms:)\n\n.*?\n\n', syn,re.DOTALL)
    syn_body = [i.replace(',', "").replace('.', "").split() for i in raw_syn]

    raw_syn_header = re.findall('(?<=\*).*?(?=Synonyms:)', syn, re.DOTALL)
    syn_header = [i.replace('*', "").replace('.', "").strip() for i in raw_syn_header]
    print(syn_body)
    syn_dict = {}
    for i in range(len(syn_header)):
        syn_dict[syn_header[i]] = syn_body[i]

    f = open("syn_dict.pickle", 'wb')

    # remember to run/load with python3
    pickle.dump(syn_dict, f, pickle.HIGHEST_PROTOCOL)
    f.close()


def find_common_context(syn_set, five_grams):
	print("Bla")

def five_grams_read():
    """im deciding to do all the counting and file opening in one function, so that we can one by one open the files. Otherwise i think the string/list of all lines from all ngrams would crash something """
	
    # import synonyms
    syn_file = open("syn_dict.pickle", 'rb')
    syn_dict = pickle.load(syn_file)
    syn_file.close()

    # dict of each header synonym, where the value will be a set of contexts
    context_dict = {}
    # initialize with syn_dict keys
    for key in syn_dict:
        context_dict[key] = set([])



	# changes current working directory to the previos directory, where the 5gram data is
	os.chdir("/./../downloads/google_ngrams/5/")
	# iterate over each file in the 5gram directory, with checking if it is a 5 gram file.
	for fname in os.listdir():
		if fname[:7] != "google":
			continue
        curr_file = open(fname, 'r')
        data = curr_file.readlines()
        curr_file.close()

        



if __name__ == "__main__":
    #five_grams_read()
    rahmGetSyn()
    #print(get_synonyms("test.txt"))

