zeros = []

def do_the_list(alist):
    for i in alist:
        if alist[i] == "0":
            zeros.append(i)
            alist.pop(i)
            alist.extend(zeros)
    print(alist)


mylist = ["1", "0", "2"]

do_the_list(mylist)


