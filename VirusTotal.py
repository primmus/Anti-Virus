
from __future__ import print_function
import json
from virus_total_apis import PublicApi as VirusTotalPublicApi
import hashlib
import time



class VT:

    def __init__(self, h, path = ""):
        self.hash = h
        self.path = path
    def get_info(self):

        API_KEY = '70f9022751728d5829c8e636a66ca686b9e2aec4b81f838337b55d5e13371c11'

        EICAR_MD5 = self.hash

        vt = VirusTotalPublicApi(API_KEY)

        response = vt.get_file_report(EICAR_MD5)


        print (response)
        time.sleep(30)

        if ('"response_code": 1' in json.dumps(response) and "detected': True" in str(response) and (not ("detected': False" in str(response)))):
            return False
        else:
            return True



def getHash_sha256(path):
    hash_sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def mainVT(path):
    vtCheck = VT(getHash_sha256(path))

    return(vtCheck.get_info())


