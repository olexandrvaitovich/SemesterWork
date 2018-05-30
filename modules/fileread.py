def reading():
    with open("data.txt", "r") as file:
        file = file.read()
        list_ = file.replace("\n"," ").strip().split(" ")
        dict_ = dict()
        for i in range(len(list_)):
            try:
                if isinstance(int(list_[i]),int):
                    dict_[list_[i]]= (list_[i-1],list_[i-2])
            except IndexError:
                continue
            except ValueError:
                continue
        return dict_
