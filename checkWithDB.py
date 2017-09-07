
import os
import hashlib




def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()






def signature_check(path):
    # check the hash with our virus db

    hash = md5(path)


    with open(os.getcwd() + "/sigs") as f:

        sig_file = f.read()

        list_of_sigs = sig_file.split("\n")
        check = True
        for i in list_of_sigs:
            if i == hash:
                check = False
            else:
                pass
        return check
