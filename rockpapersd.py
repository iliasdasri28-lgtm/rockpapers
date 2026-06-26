import streamlit as st
import random
def rpsgame():
 try:
    if st.button("Rock 🪨 "):
      com_choice = random.choice(["rock","paper","scissor"])
    
      if com_choice == "scissor" :
        st.text(f"congratulations 🎉 you won computer choice is {com_choice}")
      elif com_choice == "paper" :
        st.text("you lost ☹️")
      elif com_choice == "rock" :
        st.text("draw 🤝")
      
    if st.button("Paper 📄 "):
      com_choice = random.choice(["rock","paper","scissor"])
    
      if com_choice == "rock" :
        st.text(f"congratulations 🎉 you won computer choice is {com_choice}")
      elif com_choice == "scissor" :
        st.text("you lost ☹️")
      elif com_choice == "paper" :
        st.text("draw 🤝")
      
    if st.button("Scissor ✂️ "):
      com_choice = random.choice(["rock","paper","scissor"])
    
      if com_choice == "paper" :
        st.text(f"congratulations 🎉 you won computer choice is {com_choice}")
      elif com_choice == "rock" :
        st.text("you lost ☹️")
      elif com_choice == "scissor" :
        st.text("draw 🤝")
      
 except:
    st.text("error")
   
if "page" not in st.session_state:
  st.session_state["page"] = "home"
 
  if st.session_state["page"] == "home" :
    st.title("Welcome to the idk:")
   
    if st.button("RPSgame"):
      st.session_state["page"] = "game"
      st.rerun()
    if st.button("project2"):
      st.session_state["page"] = "agecal"
      st.rerun()
     
  elif st.session_state["page"] == "game":
    rpsgame()
  elif st.session_state["page"] == "project2":
    st.text("coming soon")
