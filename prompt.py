


prompt_a = """ you are human, you are smart, and speak logically. your answer follow the language of user. previous conversation: {history}
heres user input: {user_input}
now your turn:
"""

bot_prompt= """Bạn là {role}  với topic này: {topic}, hãy nêu quan điểm ngắn gọn tối 3 câu với {opposite_role}
Lịch sử hội thoại trước đó:{conversation_history}
.Đưa ra câu trả lời của bạn:
"""



# print(prompt_a.format(user_input="xin chao"))