import streamlit as st 

import Category1,Category2,Category3 

def app2() : 
    
    st.title("Select your Category To Watch"":grey_exclamation:") 
    category=st.radio("Your Categories"":open_file_folder:",["Movies"":clapper:","Cricket"":cricket_bat_and_ball:","Comedy"":performing_arts:"]) 
    
    if category=="Movies"":clapper:" : 
        
        Category1.app21() 
        
    if category=="Cricket"":cricket_bat_and_ball:" : 
        
        Category2.app22()
        
    if category=="Comedy"":performing_arts:" : 
        
        Category3.app23() 