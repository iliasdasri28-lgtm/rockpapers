import streamlit  as st
import random
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
