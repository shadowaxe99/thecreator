```python
import requests
from TheCreatorAI.content_analysis import analyzeContent
from TheCreatorAI.content_security import secureContent

def integrateThirdParty(userProfile, contentData, thirdPartyAPI):
    """
    Function to integrate with third-party tools.
    """
    # Analyze the content
    analyzedContent = analyzeContent(contentData)

    # Secure the content
    securedContent = secureContent(analyzedContent)

    # Prepare the data to be sent to the third-party API
    data = {
        'userProfile': userProfile,
        'contentData': securedContent
    }

    # Send a POST request to the third-party API
    response = requests.post(thirdPartyAPI, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        print('Integration with third-party tool successful.')
    else:
        print('Integration with third-party tool failed.')

    return response
```