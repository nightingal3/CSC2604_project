from get_syn_2 import *
import matplotlib.pyplot as plt

def collapse_same_len(g_dict):
    new_dict = {}
    for group in g_dict:
        if group not in new_dict:
            new_dict[group] = {}
        for elem in g_dict[group]:
            length = len(elem)
            if length not in new_dict[group]:
                new_dict[group][length] = 0
            new_dict[group][length] += g_dict[group][elem]
    return new_dict





if __name__ == "__main__":
    f = open("syn_group.pickle", "rb")
    syn_group = pickle.load(f)
    f.close()
    # the syn group where the frequencies are now
    #normal_syn_group = {}
    """for group in syn_group:
        # s is the sum
        s = 0
        for elem in syn_group[group]:
            s+= syn[group][elem]
        for elem in syn_group[group]:
            try:
                 normal_syn_group[group][elem] = syn_group[group][elem]/float(s)
            except KeyError:
                normal_syn_group[group] = {}                
                normal_syn_group[group][elem] = syn_group[group][elem]/float(s)
    """



    syn_group = OrderedDict(syn_group)


    # keep track of the syn groups with indices
    syn_index = {}
    i = 1
    for group in syn_group:
	syn_index[group] = i
	i+=1


    
    letter_linear_results  = np.zeros((len(syn_group), 3))
    for group in syn_group:
        r, p = calc_pearson_r(syn_group[group] , "length", "linear")
	    letter_linear_results[syn_index[group]-1] =[syn_index[group], r, p]
        print("%s has r=%f and p=%f" % (syn_index[group], r, p))

    #letter_linear_results.sort(axis=0)

    print(letter_linear_results)
    fig, ax = plt.subplots()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    col_label = ("synonym group", "r", "p")
    ax.title("Word Length and Frequency Linear Regressions")
    ax.table(cellText=letter_linear_results, colLabels=col_label, loc='center')
    
    fig.savefig("length_linear_results", bbox_inches='tight')

    # ~~~~ LETTER EXP REGRESSION

     
    letter_exp_results  = np.zeros((len(syn_group), 3))
    for group in syn_group:
        r, p = calc_pearson_r(syn_group[group] , "length", "exp")
	    letter_exp_results[syn_index[group]-1] =[syn_index[group], r, p]
        print("%s has r=%f and p=%f" % (syn_index[group], r, p))

        fig, ax = plt.subplots()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    col_label = ("synonym group", "r", "p")
    ax.title("Word Length and Frequency Exponential Regressions")
    ax.table(cellText=letter_exp_results, colLabels=col_label, loc='center')
    
    fig.savefig("length_exp_results", bbox_inches='tight')



    #~~~ COLLAPSED LINEAR REG
    collapsed = collapse_same_len(syn_group)

    collapsed_letter_linear_results  = np.zeros((len(collapsed), 3))
    for group in collapsed:
        r, p = calc_pearson_r(collapsed[group] , "length", "linear")
        collapsed_letter_linear_results[syn_index[group] - 1] = [syn_index[group], r, p]
        print("%s has r=%f and p=%f" % (group, r, p))

    fig, ax = plt.subplots()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    col_label = ("synonym group", "r", "p")
    ax.title("Collapsed Word Length and Frequency Linear Regressions")
    ax.table(cellText=collapsed_letter_linear_results, colLabels=col_label, loc='center')
    
    fig.savefig("collapsed_length_linear_results", bbox_inches='tight')

    #~~~COLLAPSED EXP REG


    collapsed_letter_exp_results  = np.zeros((len(collapsed), 3))
    for group in collapsed:
        r, p = calc_pearson_r(collapsed[group] , "length", "exp")
        collapsed_letter_exp_results[syn_index[group] - 1] = [syn_index[group], r, p]
        print("%s has r=%f and p=%f" % (group, r, p))

    fig, ax = plt.subplots()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    col_label = ("synonym group", "r", "p")
    ax.title("Collapsed Word Length and Frequency Exp Regressions")
    ax.table(cellText=collapsed_letter_exp_results, colLabels=col_label, loc='center')
    
    fig.savefig("collapsed_length_exp_results", bbox_inches='tight')



    #~~~ ALL DATA POINTS WITH RELATIVE FREQUENCIES
    normal_syn_group = {}
    for group in syn_group:
        # s is the sum
        s = 0
        for elem in syn_group[group]:
            s+= syn[group][elem]
        for elem in syn_group[group]:
            normal_syn_group[elem] = (syn_group[group][elem]/float(s)) * 100

    

    #~~~ ALL DATA  NORMALIZED EXP REG
    #normal_exp_reg = np.zeros((len(normal_syn_group), 3))
    r, p = calc_pearson_r(normal_syn_group, "length", "exp")
    print("r=%f, p=%f" % (r, p))

    #~~~~~ TABLE FOR THE SYN GROUP INDEXES
    synonym_indexes = []
    for group in syn_index:
        synonym_indexes.append([syn_index[group], group])

    fig, ax = plt.subplots()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    col_label = ("synonym group", "index")
    ax.title("Synonym Group indices")
    ax.table(cellText=syn_indexes, colLabels=col_label, loc='center')
    
    fig.savefig("synonym_group_indexes", bbox_inches='tight')
