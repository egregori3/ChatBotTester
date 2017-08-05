class yourChatbot:

    def __init__(self,key):
        self.key = key
        self.session = None

    def startSession(self):
        # init session variables here
        return {'command':'continue'}

    def Chatbot(self,session,msg):
        # msg is text to chatbot
        return session,'msg sent to chatbot: '+msg
