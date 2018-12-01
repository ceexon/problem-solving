class Additive():
    def __init__(self, additive_string):
        self.additive_string = additive_string

    def additive_func(self):
        seq_list = self.additive_string.split(',')
        # print(seq_list)
        addit_list = []
        for i,num in enumerate(seq_list):
            num = int(num)
            if i > 1:
                if num == (int(seq_list[i-1]) + int(seq_list[i-2])):
                    addit_list.append(str(num))
            else:
                continue
        # print(addit_list)

        # Check if from the third item the addit list matches the initial squence string list
        if addit_list == seq_list[2:]:
            return "String is additive"
        else:
            return "String is not additive"
