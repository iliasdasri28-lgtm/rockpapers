import streamlit as st
import random
def rpsgame():
 
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
def agecal():

 born = st.text_input("what time have you born:\n")
 date = st.text_input("what today date:\n")

 if st.button("Calculate"):
    try:
        
        daydate,monthdate,yeardate = date.split("/")
        
        today = int(daydate)
        tomonth = int(monthdate)
        toyear = int(yeardate)
        
        born_day,born_month,born_year=born.split("/")
        
        day = int(born_day)
        month = int(born_month)
        year = int(born_year)
        
        if month > tomonth or (month == tomonth and day > today) : 
            ageyear = toyear - year - 1
            
        else:
            ageyear = toyear - year
            
        if day > today :
            agemonth = (tomonth - month - 1)%12
            ageday = (today + 30) - day
            
        else:
            agemonth = (tomonth - month)%12
            ageday = today - day
            
        st.write(f"your age is {ageyear} year and {agemonth} month and {ageday} day")
    except:
          st.error("enter the date as number in that form: xx/yy/zzzz")
 
if "page" not in st.session_state:
  st.session_state["page"] = "menu"
if st.session_state["page"] != "menu":
  if st.button("⬅️ back to menu"):
        st.session_state["page"] = "menu"
        st.rerun()
if st.session_state["page"] == "menu" :
    st.title("Welcome to the idk:")
   
    if st.button("RPSgame"):
      st.session_state["page"] = "rpsgame"
      st.rerun()
    if st.button("agecal"):
      st.session_state["page"] = "agecal"
      st.rerun()
     
elif st.session_state["page"] == "rpsgame":
    rpsgame()
elif st.session_state["page"] == "agecal":
    agecal()
