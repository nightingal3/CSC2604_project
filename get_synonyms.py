import re
import pickle
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

    syn_dict = {}
    for i in range(len(syn_header)):
        syn_dict[syn_header[i]] = syn_body[i]

    f = open("syn_dict.pickle", 'wb')

    # remember to run/load with python3
    pickle.dump(syn_dict, f, pickle.HIGHEST_PROTOCOL)
    f.close()




if __name__ == "__main__":
    rahmGetSyn()
    #print(get_sgynonyms("test.txt"))

