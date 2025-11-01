from prompt import bot_prompt, judge_prompt
from botrole import Role
from call_llm import call_llm
class bot:
    def __init__(self, conversation_history, topic):
        self.conversation_history = conversation_history
        self.topic = topic
        
    # def build_prompt(self,topic, history):
    #     self.prompt = self.prompt.format(role = self.role, topic = topic, history = history )
            
    # def respond(self,topic, history):
    #     self.build_prompt(self,topic, history)
    #     return call_llm(self.prompt)
    
class AgreeBot(bot):
    def __init__(self, conversation_history,topic):
        super.__init__(conversation_history,topic)
        self.prompt = bot_prompt.format(role = Role.agree, opposite_role = Role.disagree, conversation_history = self.conversation_history, topic = self.topic)


if __name__ == "__main__":
    a = AgreeBot("","working at home is better than working at the office")
    print(a.prompt)