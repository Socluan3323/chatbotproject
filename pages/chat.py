import streamlit as st
# from call_llm import call_llm
# from prompt import  bot_prompt
from botrole import Role
from bot import JudgeBot, AgreeBot, DisagreeBot

print("start")
st.title("Topic: {topic}".format(topic=st.session_state["topic"] ))
# Initialize chat history
if "is_done" not in st.session_state:
    st.session_state.is_done = False
      
if 'total_round' not in st.session_state:
    st.session_state.total_round = 5
if 'current_round' not in st.session_state:
    st.session_state.current_round = 1
    
if "messages" not in st.session_state:
    print("messages not found")
    st.session_state.messages = []

if "agreebot" not in st.session_state:
    st.session_state.agreebot = AgreeBot(conversation_history = st.session_state.messages, topic= st.session_state["topic"])

if "disagreebot" not in st.session_state:
    st.session_state.disagreebot = DisagreeBot(conversation_history = st.session_state.messages, topic= st.session_state["topic"])
# while not st.session_state.is_done:
#     if  st.session_state.current_round > st.session_state.total_round:
#         st.session_state.is_done = True
#         break
#     #prompts
#     # agree_bot_prompt = bot_prompt.format( topic = st.session_state["topic"], role=Role.agree.value,opposite_role=Role.disagree.value,conversation_history= st.session_state.messages)
    
#     # disagree_bot_prompt = bot_prompt.format( topic = st.session_state["topic"],role=Role.disagree.value,opposite_role=Role.agree.value, conversation_history= st.session_state.messages)
    
    
#     # agree_bot_respone = call_llm(agree_bot_prompt)
    
#     # display aggree bot respone
#     with st.chat_message(Role.agree.value, avatar="🔵"):
#         st.markdown(agree_bot_respone)
        
        
#     st.session_state.messages.append({"role": Role.agree.value, "content": agree_bot_respone})
    
#     # disagree_bot_respone =  call_llm(disagree_bot_prompt)
    
#      # display disaggree bot respone
#     with st.chat_message(Role.disagree.value,avatar="🔴"):
#         st.markdown(disagree_bot_respone)
        
#     st.session_state.messages.append({"role": Role.disagree.value, "content": disagree_bot_respone}) 

#     print(disagree_bot_prompt)
  
            
#     st.session_state.current_round += 1       


# if st.session_state.is_done:
#     pass
                       
           
    
# print("end")

while not st.session_state.is_done:
    if  st.session_state.current_round > st.session_state.total_round:
        st.session_state.is_done = True
        break
    agreebot_response = st.session_state.agreebot.respond(new_conversation_history= st.session_state.messages) 
    st.session_state.messages.append(agreebot_response)
    with st.chat_message(Role.agree.value, avatar="🔵"):
        st.markdown(agreebot_response)
    
    disagreeabot_response = st.session_state.disagreebot.respond(new_conversation_history= st.session_state.messages)
    st.session_state.messages.append(disagreeabot_response)
    with st.chat_message(Role.disagree.value,avatar="🔴"):
        st.markdown(disagreeabot_response)
    

    st.session_state.current_round += 1       


if st.session_state.is_done:
    judgebot = JudgeBot(conversation_history= st.session_state.messages, topic=st.session_state["topic"] )
    judgebot_response = judgebot.respond()
    with st.chat_message(Role.judge.value):
        st.markdown(judgebot_response)                  
           
    
print("end")

