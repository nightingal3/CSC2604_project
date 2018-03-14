import re

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


if __name__ == "__main__":
    print(get_synonyms("test.txt"))
