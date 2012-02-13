# generic utility functions for the json resume format


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
