
'''
Here we generate user data using RandomUser library
Then we store the data in a pandas DataFrame

'''
from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(10)

for user in some_list:
    #print(user.get_full_name()," ",user.get_email())
    print(user.get_picture())


def get_user():
    users = []

    for user in RandomUser.generate_users(5):
        users.append({"name": user.get_full_name(), "email": user.get_email(), "phone": user.get_phone()})
        
    return pd.DataFrame(users)

df1 = pd.DataFrame(get_user())

print(df1)