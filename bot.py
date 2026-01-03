from prompt import bot_prompt, judge_prompt
from botrole import Role
from call_llm import call_llm
from theflow import Node
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
    
# class AgreeBot(bot):
#     def __init__(self, conversation_history:str, topic: str):
#         super().__init__(conversation_history,topic)
#         self.prompt = bot_prompt.format(role = Role.agree.value, opposite_role = Role.disagree.value, conversation_history = self.conversation_history, topic = self.topic)
shared = {"topic": "working at home is better than working at the office",
          "conversation_history": "no conversation yet"}
class AgreeBot(Node):
    def prep(topic,shared):
        return shared["topic"],shared["conversation_history"]
    def exec(self,prep_res):
        topic,conversation_history = prep_res
        prompt = """Bạn là người đồng tình trong cuộc tranh luận về chủ đề: {topic}

Lịch sử hội thoại:
{conversation_history}

Nhiệm vụ: Phản hồi lại bằng quan điểm của bạn trong TỐI ĐA 3 câu ngắn gọn, rõ ràng.

Câu trả lời của bạn:""".format(topic = topic, conversation_history = conversation_history)
        return call_llm(prompt)
    def post(self, shared, prep_res, exec_res):
        agreebot_dictionary = {"agree_bot": exec_res}
        if isinstance(shared["conversation_history"],str):
            agreebot_dictionary['order'] = 1
            shared["conversation_history"] = []
        else:
            agreebot_dictionary['order'] = len(shared["conversation_history"]) + 1

        shared["agreebot_response"] = exec_res
        shared["conversation_history"].append(agreebot_dictionary)

class DisagreeBot(Node):
    def prep(topic,shared):
        return shared["topic"],shared["conversation_history"]
    def exec(self,prep_res):
        topic,conversation_history = prep_res
        prompt = """Bạn là người không đồng tình trong cuộc tranh luận về chủ đề: {topic}

Lịch sử hội thoại:
{conversation_history}

Nhiệm vụ: Phản hồi lại bằng quan điểm của bạn trong TỐI ĐA 3 câu ngắn gọn, rõ ràng.

Câu trả lời của bạn:""".format(topic = topic, conversation_history = conversation_history)
        return call_llm(prompt)
    def post(self, shared, prep_res, exec_res):
        disagreebot_dictionary = {"disagree_bot": exec_res}
        if isinstance(shared["conversation_history"],str):
            disagreebot_dictionary['order'] = 1
            shared["conversation_history"] = []
        else:
            disagreebot_dictionary['order'] = len(shared["conversation_history"]) + 1

        shared["disagreebot_response"] = exec_res
        shared["conversation_history"].append(disagreebot_dictionary)


# class DisagreeBot(bot):
#     def __init__(self,conversation_history: str, topic: str):
#         super().__init__(conversation_history,topic)
#         self.prompt = bot_prompt.format(role = Role.disagree.value, opposite_role = Role.agree.value, conversation_history = self.conversation_history, topic = self.topic )

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
    

