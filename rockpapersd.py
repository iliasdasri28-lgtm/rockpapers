import streamlit  as st
import random
try:
  if st.button("Rock 🪨 "):
    com_choice = random.choice(["rock","paper","scissor"])
    if com_choice == "rock" :
      st.text(f"congratulations 🎉 you won computer choice is {com_choice}")
    else:
      st.text(f"you lost the computer chose {com_choice}")
  if st.button("Paper 📄 "):
    com_choice = random.choice(["rock","paper","scissor"])
    if com_choice == "paper" :
      st.text(f"congratulations 🎉 you won computer choice is {com_choice}")
    else:
      st.text(f"you lost the computer chose {com_choice}")
  if st.button("Scissor ✂️ "):
    com_choice = random.choice(["rock","paper","scissor"])
    if com_choice == "scissor" :
      st.text(f"congratulations 🎉 you won computer choice is {com_choice}")
    else:
      st.text(f"you lost the computer chose {com_choice}")
except:
  st.text("error")
