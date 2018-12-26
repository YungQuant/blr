from random import randint
import sys


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