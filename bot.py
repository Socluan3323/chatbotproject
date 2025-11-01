from prompt import bot_prompt, judge_prompt
from botrole import Role
from call_llm import call_llm
class bot:
    def __init__(self, conversation_history, topic):
        self.conversation_history = conversation_history
        self.topic = topic

    def respond(self, new_conversation_history):
        """pass in new conversation history to update the conversation history"""
        self.conversation_history = new_conversation_history
        
        response = call_llm(self.prompt)
        return response
    
        
    # def build_prompt(self,topic, history):
    #     self.prompt = self.prompt.format(role = self.role, topic = topic, history = history )
            
    # def respond(self,topic, history):
    #     self.build_prompt(self,topic, history)
    #     return call_llm(self.prompt)
    
class AgreeBot(bot):
    def __init__(self, conversation_history:str, topic: str):
        super().__init__(conversation_history,topic)
        self.prompt = bot_prompt.format(role = Role.agree.value, opposite_role = Role.disagree.value, conversation_history = self.conversation_history, topic = self.topic)
    

class DisagreeBot(bot):
    def __init__(self,conversation_history: str, topic: str):
        super().__init__(conversation_history,topic)
        self.prompt = bot_prompt.format(role = Role.disagree.value, opposite_role = Role.agree.value, conversation_history = self.conversation_history, topic = self.topic )

class JudgeBot(bot):
    def __init__(self,conversation_history: str, topic:str):
        super().__init__(conversation_history,topic)
        self.prompt = judge_prompt.format(role_a = Role.agree.value, role_b = Role.disagree.value, conversation_history = self.conversation_history, topic = self.topic)
    def respond(self):
        response = call_llm(self.prompt)
        return response

if __name__ == "__main__":
    # a = AgreeBot("","working at home is better than working at the office")
    # print(a.respond())
    # b = DisagreeBot("","working at home is better than working at the office")
    # print(b.respond(new_conversation_history= None))
    c = JudgeBot("No conversation yet", "Working at home is better than working at the office")
    print(c.respond())
    

