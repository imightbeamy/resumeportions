# take in json stuff and output .tex stuff

import json

def testFn():
    f = open("mark_json.json", "r")
    stuff = json.load(f)

    # stuff is a dictionary
    print generateTextResume(stuff)

    
    print getCategoryList(stuff)

def generateTextResume(jsonDict):
    resume = ""

    # header
    resume += jsonDict["first"] + " " + jsonDict["last"] + "\n"
    resume += jsonDict["title"] + "\n"
    resume += "\n"
    
    emailList = jsonDict["contact"]["emails"]
    for emailEntry in emailList:
        # remember that each emailEntry is a dictionary
        resume += emailEntry["label"] + ": " + emailEntry["adress"]
        resume += "\n"

    phoneList = jsonDict["contact"]["phone_numers"]
    for phoneEntry in phoneList:
        resume += phoneEntry["label"] + ": " + phoneEntry["number"]
        resume += "\n"
    
    addressList = jsonDict["contact"]["addresses"]
    for addrEntry in addressList:
        resume += "\n"
        resume += addrEntry["label"] + ":\n"
        resume += addrEntry["street"] + "\n"
        resume += addrEntry["city"] + " " 
        resume += addrEntry["state"] + " " + addrEntry["zip"] + "\n"
        
    resume += "\n"
    linkList = jsonDict["contact"]["links"]
    for linkEntry in linkList:
        resume += linkEntry["label"] + ": "
        resume += linkEntry["url"] + "\n"


    # body
    resumeList = jsonDict["resume"]

    # this O(n * m * o) operation could probably be done more efficiently.
    # for now, it's easiest to just extract the categories and their 
    # respective titles 
    categories = getCategoryList(jsonDict)
    for cat in categories:
        resume += "\n" + cat.upper() + "\n"

        # walk through the titles that occur under this category, and print
        # each of the entries occuring under this title
        titles = getTitleList(jsonDict, cat)
        for title in titles:
            resume += "\n" + title + "\n"
            
            # now, actually print each entry
            for entry in resumeList:
                if entry["title"] == title and entry["category"] == cat:
                    experienceList = entry["experiences"]
                    for exp in experienceList:
                        resume += exp["organization"] + "\n"
                        resume += exp["title"] + "\n"
                        resume += exp["date"] + "\n"
                        descriptionList = exp["descriptions"]
                        for d in descriptionList:
                            resume += " * " + d + "\n"

    return resume
    
# get a list of all the categories in the json dictionary
def getCategoryList(jsonDict):
    categories = []
    resumeList = jsonDict["resume"]
    
    for entry in resumeList:
        if entry["category"] not in categories:
            categories.append(entry["category"])
                       
    return categories

# given a jsonDict and a category, return a list of all of the titles that
# occur under that category
def getTitleList(jsonDict, category):
    titles = []
    resumeList = jsonDict["resume"]
    for entry in resumeList:
        if entry["category"] == category:
            if entry["title"] not in titles:
                titles.append(entry["title"])
    return titles

testFn()


