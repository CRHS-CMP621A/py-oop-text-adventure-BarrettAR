class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self,char_conversation):
        self.conversation=char_conversation

    def talk(self):
        if self.conversation is not None:
            print("["+self.name,"says]:"+self.conversation)
        else:
            print(self.name +" doesn't want to talk to you")

    def describe(self):
        print(self.name,"is here!")
        print(self.description)
    
    def fight(self, combat_item):
        print(self.name+" doesn't want to fight you")
        return True



class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness= None
    
    def set_weakness(self,char_weakness):
        self.weakness=char_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you!")
            return False
