def writing(thing):
    try:
        f = open('data.txt','a')
    except IOError:
        f = open('data.txt','w')
    string = thing[0] + " " + thing[1] + " " + str(thing[2])
    f.write(string)
    f.close()

