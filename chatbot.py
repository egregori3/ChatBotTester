"""
Simple console chatbot tester - by Eric Gregori.

Usage: chatbot.py -h | --help
       chatbot.py -v | --version
       chatbot.py --key key
       chatbot.py --log filename

Options:
  -h,--help         : This help text
  -v,--version      : Version
  --key <key>       : key
  --log <filename>  : Log to file
"""
import sys
import os
import yourChatbot
from docopt import docopt

def main(arguments):
    print __doc__.split('.')[0]
    try:
        chatbot = yourChatbot.yourChatbot(arguments['--key'])
    except KeyError:
#        print arguments
        print "Could not find key in argument."
        return 1

    Logging = arguments['--log']
    if Logging:
        print "Loggin to file: "+Logging
        logFile = open(Logging,"a")

    # Start chatbot session
    session = chatbot.startSession()

    # loop
    while(1):
        try:
            userInput = raw_input('Input: ')
        except KeyboardInterrupt:
            # User hit ctrl-c
            if Logging:
                logFile.close()
            return 1

        # We open and close the file to avoid loosing data if we crash
        if Logging:
            logFile = open(Logging,"a")

        session,response = chatbot.Chatbot(session,userInput)
        if Logging:
            logFile.write("\nInput: "+userInput)
            logFile.write("\nResponse: "+response)
            logFile.write("\nSession: "+str(session))
            logFile.write("\n")
            logFile.close()

        print
        print "Response: "+response
        if session['command'] == 'clear':
            os.system('cls' if os.name=='nt' else 'clear')
        print
        print

# NOTE: main() will not be called if doctype catches -v or -h
if __name__ == '__main__':
    sys.exit(main(docopt(__doc__, version='08052017')))
