```python
import json
from TheCreatorAI.content_analysis import analyzeContent
from TheCreatorAI.content_optimization import optimizeContent

userProfile = {}
contentData = {}
analyticsData = {}

def loadUserProfile():
    global userProfile
    with open('userProfile.json', 'r') as file:
        userProfile = json.load(file)

def loadContentData():
    global contentData
    with open('contentData.json', 'r') as file:
        contentData = json.load(file)

def loadAnalyticsData():
    global analyticsData
    with open('analyticsData.json', 'r') as file:
        analyticsData = json.load(file)

def updateProfile(newProfile):
    global userProfile
    userProfile.update(newProfile)
    with open('userProfile.json', 'w') as file:
        json.dump(userProfile, file)

def updateContent(newContent):
    global contentData
    contentData.update(newContent)
    with open('contentData.json', 'w') as file:
        json.dump(contentData, file)

def updateAnalytics(newAnalytics):
    global analyticsData
    analyticsData.update(newAnalytics)
    with open('analyticsData.json', 'w') as file:
        json.dump(analyticsData, file)

def manageWorkflow():
    loadUserProfile()
    loadContentData()
    loadAnalyticsData()

    analyzeContent(contentData, userProfile)
    optimizedContent = optimizeContent(contentData, analyticsData)

    updateContent(optimizedContent)

    return optimizedContent
```