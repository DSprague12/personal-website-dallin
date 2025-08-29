#English word, type, translation, gender/conjugation
wordInfo = [["he","n","ele","m"],["runs","v","correr",["corro","corremos","corres","correis","corre","correm"]],["store","n","loja","f"]]

class sentenceParsing:
    def __init__(self,ogSentence):
        self.ogSentence=ogSentence
        self.sentence=""
        self.nounList=[]
        self.verbList=[]
        self.subject=""
        self.verb=""
        self.object=""


    def parseSentence(self):
        self.sentence=self.ogSentence.lower().split()
        for word in self.sentence:
            found = None
            for item in wordInfo:
                if word == item[0]:
                    found = item
            if found:
                if found[1]=="n":
                    self.nounList.append(found)
                if found[1]=="v":
                    self.verbList.append(found)
                word=found


    def parseGrammar(self):
        self.subject=self.nounList[0]
        self.object=self.nounList[-1]
        self.verb=self.verbList[0]

    def translate(self):
        if self.subject not in ["you","they","we","i"]:
            self.verb = self.verb[3][4]
        self.sentence=self.subject[2]+" "+self.verb+" "+self.object[2]
        

exampleSentence ="He runs to the store"
parsing = sentenceParsing(exampleSentence)
parsing.parseSentence()
print(parsing.sentence)
print(parsing.nounList)
print(parsing.verbList)
parsing.parseGrammar()
parsing.translate()
print(parsing.sentence)