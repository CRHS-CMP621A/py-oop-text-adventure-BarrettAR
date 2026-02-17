class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self,char_conversation):
        self.conversation=char_conversation

    def talk(self):
        print(self.name,"says",self.conversation)


    def describe(self):
        print(self.name,"is here!")
        print(self.description)



class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)