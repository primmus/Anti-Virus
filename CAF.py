import os
filelist = []


def check(path):

    try:
        for i in os.listdir(path):

            try:
               os.listdir(path+"\\" +i)
               check(path +'\\'+ i )
            except:
                i = path +"\\"+ i
                '''if os.access(i, os.X_OK):
                    filelist.append(i)'''
                try:
                    print(i.split(".")[1] == "exe")
                    if "exe" == i.split(".")[1] or "dll" == i.split(".")[1]:
                        filelist.append(i)
                        print(1)

                except:
                    pass


    except:
        pass

def check_mom(MomDir):
    check(MomDir)
    print(filelist)
    return filelist


dir_list = []