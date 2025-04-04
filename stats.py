def word_count(string):
    word_list=string.split()
    return len(word_list)


def char_count(text):
    char_dict={}
    text=text.lower()
    for i in text:
        if i in char_dict:
            char_dict[i]+=1
        else:
            char_dict[i]=1
    
    return char_dict

def sort_on(dict):
    return dict["count"]

def dict_sort(dict):
    dict_to_list=[]
    for i in dict:
        new_dict={}
        new_dict["char"] = i
        new_dict["count"] = dict[i]
        dict_to_list.append(new_dict)
    
    dict_to_list.sort(reverse=True, key=sort_on)
    return dict_to_list