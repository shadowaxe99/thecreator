```python
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from UserProfileSchema import UserProfileSchema
from ContentDataSchema import ContentDataSchema

userProfile = {}
contentData = {}

def load_user_profile():
    global userProfile
    with open('userProfile.json', 'r') as file:
        userProfile = json.load(file)

def load_content_data():
    global contentData
    with open('contentData.json', 'r') as file:
        contentData = json.load(file)

def educateUser():
    load_user_profile()
    load_content_data()

    user_profile_df = UserProfileSchema().load(userProfile)
    content_data_df = ContentDataSchema().load(contentData)

    X = user_profile_df.drop('education_level', axis=1)
    y = user_profile_df['education_level']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    if accuracy > 0.8:
        print("The AI model is performing well with an accuracy of ", accuracy)
    else:
        print("The AI model needs improvement. Current accuracy is ", accuracy)

    return model

if __name__ == "__main__":
    educateUser()
```