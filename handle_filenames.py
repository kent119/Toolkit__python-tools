import os

def add_number(path, start_num = 1, steps = 0):
    # Get file list
    file_list = os.listdir(path)
    # For every file in the list, rename
    i = start_num
    for each in file_list:
        if each == "Thumbs.db":
            print "It's Thumbs.db"
        else:
            src = path+"\\"+each
            dest, ext = split_extension(src)
            dest = dest + "_" + str(i) + ext
            print dest
            print src
            os.rename(src, dest)
            i += steps

    return

def cut_tail(path, tail_length = 0):
    # Get file list
    file_list = os.listdir(path)

    # For each file, cut the specified str
    for each in file_list:
        if each == "Thumbs.db":
            print "It's Thumbs.db"
        else:
            src = path + "\\" + each
            dest, ext = split_extension(src)
            dest = dest[:-tail_length] + ext
            os.rename(src, dest)

    return

def split_extension(src):
    ext = ""
    filename, file_extension = os.path.splitext(src)
    if file_extension:
        ext = file_extension
    return filename, ext

def add_ext(path, ext):
    # Get file list
    file_list = os.listdir(path)

    # For each file, cut the specified str
    for each in file_list:
        if each == "Thumbs.db":
            print "It's Thumbs.db"
        else:
            src = path + "\\" + each
            dest = src + "." + ext
            os.rename(src, dest)

    return

#path = r"Y:\Jeffrey's order\Tender_Q9_7_Dec_2016\vendors\tlsurfing\catalog\right_page"
#add_number(path, 2)
#cut_tail(path, 2)
#add_ext(path, "jpg")
