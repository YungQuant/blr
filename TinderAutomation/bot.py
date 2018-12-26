from skimage.io import imread, imsave, imshow, show
import matplotlib.pyplot as plt
import pynder
#from . import helpers
from helpers import get_access_token, get_login_credentials
from io_helper import save_image
from time import sleep
from random import randint
# from messages import messages
from image_processing import extract_faces
import numpy as np
from keras.models import load_model
import sys

def check_swipes(session, total):
    '''
    INPUT:
    ACTION: Will check if I still have swipes
    OUTPUT:
    '''
    swipes_remaining = session.likes_remaining
    print(f'Swipes remaining:{swipes_remaining}, Limit remaining: {total}')
    if swipes_remaining == 0:
        return 'Send messages'
    else:
        return 'Swiping'

def like_or_nope(user, compiled_model, chocolate=0.4):
    '''
    INPUT: Image file
    OUTPUT: Like or Dislike
    '''
    photos = user.get_photos()

    print(f'Fetched {user.name}\'s photos..')
    for photo in photos:
        print(f'photo:{photo}')
        image = imread(photo)
        # imshow(image) # Shows image of person
        # show()
        face = np.array(extract_faces(image))
        if len(face) != 0:
            prediction = compiled_model.predict(face) # Add the model file here instead
            if prediction[0][1] > chocolate:
                return "like"
            else:
                return "dislike"
            break
        else:
            print(f'Felicity isn\'t sure if you\'ll like {user.name}')

def swipe(session,model,n):
    '''
    INPUT: Session object, nearby users object
    ACTION: Will swipe until swipe limit is reached.
        - Currently swiping at random
    OUTPUT:
    '''
    total_swipes = n
    likes = 0
    dislikes = 0
    while total_swipes !=0 :
        users = session.nearby_users()
        try:
            for user in users:
                # print("Checking Swipes remaining.....")
                status = check_swipes(session, total_swipes)
                print(f'Status: {status}')
                if total_swipes == 0 or status == 'Send messages':
                    print("So far I've swiped right on " + str(likes) + " people.")
                    print("I've also swiped left on " + str(dislikes) + " people.")
                    # print("If you'd like that number to be higher or lower adjust the Pickiness Factor in your settings!")
                    # ^ make that a thing
                    print("You've reached your swipe limit, I will now start sending messages to matches!!!")
                    break
                else:
                    action = like_or_nope(user, model)
                    # print("Remaining Swipes: " + str(n))
                    if action == 'like':
                        user.like()
                        total_swipes -= 1
                        likes += 1
                        print('Felicity liked ' + user.name + ' for you! ')
                        print('-------------------------------------------------------')
                        sleep(np.random.uniform(0.666, 6.66))
                    else:
                        user.dislike()
                        total_swipes -= 1
                        dislikes += 1
                        print('Felicity disliked ' + user.name + ' for you!')
                        print('-------------------------------------------------------')
                        sleep(np.random.uniform(0.666, 6.66))
        except:
            print(f'Ooops ;( sorryyy. \n{sys.exc_info()} \nI will try again.')



def send_message(session):
    '''
    INPUT: Session object
    ACTION: Will send an automated message to whomever I match with.
    OUTPUT:
    '''
    matches = session.matches()
    print(f'I\'m going to start sending your matches some messages now! ;D ')
    messages = ['wow', 'ok fine', 'hello!!!', 'sorry i\'m actually only here looking for friends']
    # ^ customize based on names, bio, etc..
    for match in matches:
        try:
            r = randint(0, len(messages)-1)
            print("Sending message: " + messages[r])
            match.message(messages[r])
        except:
            print(f'Ooops ;( sorryyy. \n{sys.exc_info()} \nThey weren\'t very attractive anyways.')

# if __name__=='__main__':
#     print('Hi Jeff. Im the Bae-ta Miner. I know the online dating process is a huge hassle.')
#     print('Im here to help! Im here to automate the process for you.')
#
#     print('-----------------------------------------------------------------------------')
#     print('First, Ill need to get your login credentials from your Facebook account.')
#     ## Get Login Credentials
#     email, password, FBID = get_login_credentials()
#     FBTOKEN = get_access_token(email, password)
#
#     print('-----------------------------------------------------------------------------')
#     print('Now, I will start your Tinder session.')
#     print('Starting Tinder Session........')
#     print('Tinder session started!')
#     ## Start Tinder Session
#     session = pynder.Session(facebook_token=FBTOKEN)
#
#     print('-----------------------------------------------------------------------------')
#     print('Loading model..............')
#     model = load_model("model_V3.h5")
#
#     print('-----------------------------------------------------------------------------')
#     ## Swipe Through users
#     print('How many times would you like me to swipe this session?')
#     total_swipes = input()
#
#     swipe(session, model, total_swipes)
#     print('-----------------------------------------------------------------------------')
#     print('Now, sending automated messages to current matches........')
#
#     ## Send messages to the matches
#     send_message(session)
#
#     print('You have Tindered for the day. Have a great day!')


print('Hello user, welcome to Blr, I am an AI named Felicity built to help you find love, passion, excitment, and more!')
sleep(2)
print('I will be walking you through my process of finding you matches <3')
sleep(2)
print('Enjoy the blur of modern romance!\n')
sleep(1)
print('-----------------------------------------------------------------------------\n')
sleep(1)
print('First I\'ll be getting you logged into those dating app accounts of yours ;)')

email, password, FBID = get_login_credentials()

print(f'I really hope {email} is your email or else..')

# FBTOKEN = "EAAKrij4Q3FIBACSn6kpIZCGfwwrlSYT5hiIx9tfUGwUXPuyZCujPG2c6ko7KevtOhjBZAqNDsroIIAlHZBZAB24cmVO1e0DKxv1YD35ZAEZBALa737QiqpkBT5J13JHBhoZAiuahAaXgKcc3bVZCZATcKxTz7HGZAXVrW5it3L8mHGQsXqDBB5Rdis1UeWOnn5VwxCAvvsJGDRADZCOapfsHp5fU"
FBTOKEN = get_access_token(email, password)
session = pynder.Session(facebook_token=FBTOKEN)

print('\n-----------------------------------------------------------------------------\n')
sleep(1)
print('Now that I\'ve got \"you\" logged in I\'m going to load in the majority of my brain!')
sleep(2)
print('Unlike how humans only ever use 10% of their brains, I\'m about to use 100% of mine to help you <3')

model = load_model("model_V3.h5")
total_swipes = 1
swipe(session, model, total_swipes)
send_message(session)
