import robobrowser
import re
import json
import os
import random

# MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
MOBILE_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A356 Safari/604.1'
#FB_AUTH = "EAAKrij4Q3FIBACSn6kpIZCGfwwrlSYT5hiIx9tfUGwUXPuyZCujPG2c6ko7KevtOhjBZAqNDsroIIAlHZBZAB24cmVO1e0DKxv1YD35ZAEZBALa737QiqpkBT5J13JHBhoZAiuahAaXgKcc3bVZCZATcKxTz7HGZAXVrW5it3L8mHGQsXqDBB5Rdis1UeWOnn5VwxCAvvsJGDRADZCOapfsHp5fU"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

# def get_access_token(email, password):
#     s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
#     s.open(FB_AUTH)
#     ##submit login form##
#     f = s.get_form()
#     f["pass"] = password
#     f["email"] = email
#     s.submit_form(f)
#     ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app
#     f = s.get_form()
#     s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
#     ##get access token from the html response##
#     access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
#     # print s.response.content.decode()
#     return access_token

def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    f = s.get_form()
    # print(f's:{s}\n f:{f}')
    f["pass"] = password
    f["email"] = email
    # print(f's:{s}\n f:{f}')
    s.submit_form(f)
    f = s.get_form()
    # print(f's:{s}\n f:{f}')
    if f.submit_fields.get('__CONFIRM__'):
        s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    else:
        raise Exception("Couldn't find the continue button. Maybe you supplied the wrong login credentials? Or maybe Facebook is asking a security question?")
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    print("Got facebook access token! (just logging \"you\" in to tinder, calm down)")
    return access_token

# def get_access_token(email, password):
#     class UserAgent:
#         class Mobile:
#             class iOS:
#                 safari = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A356 Safari/604.1'
#
#     class Facebook:
#
#         AUTHAPP_FORM_ACTION = '/v2.8/dialog/oauth/confirm'
#         AUTH_URL = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"
#
#         def __init__(self, username, password, user_agent=None):
#             self.username = username
#             self.password = password
#
#             self.user_agent = user_agent
#             if not self.user_agent:
#                 self.user_agent = UserAgent.Mobile.iOS.safari
#
#             self.browser = robobrowser.RoboBrowser(user_agent=self.user_agent, parser="lxml")
#
#         def get_access_token(self):
#             self.browser.open(self.AUTH_URL)
#
#             # Authentication
#             login_form = self.browser.get_form()
#             login_form["pass"] = self.password
#             login_form["email"] = self.username
#             self.browser.submit_form(login_form)
#
#             # Authorizing App
#             authapp_form = self.browser.get_form(action=self.AUTHAPP_FORM_ACTION)
#             if authapp_form.submit_fields.get('__CONFIRM__'):
#                 self.browser.submit_form(authapp_form, submit=authapp_form.submit_fields['__CONFIRM__'])
#             else:
#                 raise Exception("Couldn't find the continue button. Maybe you supplied the wrong login credentials? Or maybe Facebook is asking a security question?")
#             self.access_token = re.search(r"access_token=([\w\d]+)", self.browser.response.content.decode()).groups()[0]
#             return self.access_token
#
#     username = email
#     password = password
#     facebook = Facebook(username, password)
#     return facebook.get_access_token()

def get_login_credentials():
    print("Checking for credentials..")
    if os.path.exists('auth.json'):
        print("Auth.json existed..")
        with open("auth.json") as data_file:
            data = json.load(data_file)
            if "email" in data and "password" in data and "FBID" in data:
                return (data["email"], data["password"], data["FBID"])
            else:
                print ("Invalid auth.json file")

    print ("Auth.json missing or invalid. Please enter your credentials.")
    return (input("Enter email ..\n"), input("Enter password..\n"))
