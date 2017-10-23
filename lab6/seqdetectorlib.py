class seqdetector():

    def __init__(self):
        self.words_list = []
        self.answer = ["here", "are", "the", "solutions", "to", "the", "next", "exam"]

    def evolve(self, input):
        if len(self.words_list) < len(self.answer):
            self.words_list.append(input)
        else:
            self.words_list.remove(self.words_list[0])
            self.words_list.append(input)
        if self.words_list == self.answer:
            return True
        else:
            return False