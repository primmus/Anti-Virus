import yara
import os

class YARA:

    def __init__(self, files):

        self.files = files
        self.malwares = []

    def YARA_check(self):
        check = []
        for f in self.files:
            for y in os.listdir(os.getcwd() + "/malware"):
                try:
                    path = os.getcwd() + "/malware/" + y
                    rule = yara.compile(filepath= path)


                    with open(f, 'rb') as fi:
                        matches = rule.match(data=fi.read())
                        for i,k in matches:
                            check.append(k)


                except:
                    pass

        for i in check:
            self.malwares.append(i)

        return len(check) <= 2