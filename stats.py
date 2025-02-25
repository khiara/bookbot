def get_num_words(file):
        count = 0
        words = file.split()
        for word in words:
                count +=1
        return count

def char_count(file):
        counts = {}
        for i in file:
                i = i.lower()
                if i in counts:
                        counts[i] +=1
                else:
                        counts[i] =1
        return counts

def sorter(dict):
        for k,v in dict.items():
                return v

def sort_list(dict):
        lst = []
        for k,v in dict.items():
                lst.append({k: v})
        lst.sort(reverse = True, key = sorter)
        return lst
