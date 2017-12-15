import requests as r
import json as j

def clientproxy(filename,readorwrite,content):
    lockurl = "http://localhost:8188/"
    unlockurl = "http://localhost:8188/unlock/"
    fileurl = "http://localhost:"
    directoryurl = "http://localhost:8186/"
    directoryurl = directoryurl + str(filename)
    reponse = r.get(directoryurl)
    filepath = reponse.text
    print("filepath:",filepath)
    if readorwrite == "r":
        port = filepath[0:4]
        print("port:",port)
        filepath = filepath[4:]
        print("filepath:",filepath)
        fileurl = fileurl + port + "/"+filepath
        print("fileurl:",fileurl)
        fileresponse = r.get(fileurl)
        print("file content : ",fileresponse.text)
    else:
        lockurl = lockurl + str(filename)
        print("lockurl:",lockurl)
        lockreponse = r.get(lockurl)
        print(lockreponse.text)
        if lockreponse.text == 'The file is not locked...':
            lock1response = r.post(lockurl)
            print("lock1response: ",lock1response)
            port = filepath[0:4]
            filepath = filepath[4:]
            fileurl = fileurl + port + "/"+filepath
            fileresponse = r.post(fileurl,data=content)
            print(fileresponse.text)
            unlockurl = unlockurl + filename
            unlock1response = r.get(unlockurl)
            print(unlock1response.text)

if __name__ == "__main__":
    filename = input("Enter the name of the file: ")
    readorwrite = input("Enter read or write? (r/w): ")
    content = 0
    if readorwrite == "w":
        content = input("Enter the file content: ")

    clientproxy(filename,readorwrite,content)
