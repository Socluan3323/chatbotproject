from prompt import bot_prompt, judge_prompt
from botrole import Role
from call_llm import call_llm
class bot:
    def __init__(self, input_Role, is_judge):
        self.role = input_Role 
        self.prompt = judge_prompt if is_judge else bot_prompt
        
    def build_prompt(self,topic, history):
        self.prompt = self.prompt.format(role = self.role, topic = topic, history = history )
            
    def respond(self, input,topic, history):
        self.build_prompt(self,topic, history)
        return call_llm(self.prompt)
    
    