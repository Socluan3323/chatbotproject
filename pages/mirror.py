import streamlit as st
from call_llm import call_llm
from prompt import prompt_a
print("start")
st.title("LLM app")
# Initialize chat history
if "messages" not in st.session_state:
    print("messages not found")
    
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    print("messsage found:",message)
    with st.chat_message(message["role"]):
        print("write message to UI")
        st.markdown(message["content"])
        
    
# React to user input
if user_input := st.chat_input("What is up?"):
    print("get user input")
    
    # Display user message in chat message container
    with st.chat_message("user"):
        print("display user input")
        st.markdown(user_input)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    response = call_llm(prompt_a.format(user_input = user_input, history = st.session_state.messages))
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
print("end")