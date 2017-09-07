
import VirusTotal
import checkWithDB
import Yara
import CAF


def checkFile(path):

    HashRes =  checkWithDB.signature_check(path) # Hash check results
    VT_Res = VirusTotal.mainVT(path) # virus total check results
    Yara_Res = Yara.YARA(path).YARA_check()# yara check results
    #ML_Res = # Machine Learning check result


    return HashRes and VT_Res #and Yara_Res

def main():
    satrtDir = input("Enter Start Directory")
    files = CAF.check_mom(satrtDir)

    for f in files:
        if checkFile(f):
            pass
        else:
            print("Virus: ", f)


if __name__ == '__main__':
    main()