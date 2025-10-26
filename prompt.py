


prompt_a = """ you are human, you are smart, and speak logically. your answer follow the language of user. previous conversation: {history}
heres user input: {user_input}
now your turn:
"""


bot_prompt = """Bạn là {role} trong cuộc tranh luận về chủ đề: {topic}

Lịch sử hội thoại:
{conversation_history}

Nhiệm vụ: Phản hồi lại {opposite_role} bằng quan điểm của bạn trong TỐI ĐA 3 câu ngắn gọn, rõ ràng.

Câu trả lời của bạn:"""


# print(prompt_a.format(user_input="xin chao"))