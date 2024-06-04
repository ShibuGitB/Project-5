import streamlit as st 

from streamlit_option_menu import option_menu 

import Home,Categories,Thanks

st.set_page_config(
        page_title="NetFlix Review Rating",
)

class MultiApp: 
    
    def __init__(self) : 
        
        self.apps=[] 
        
    def add_app(self,title,func) : 
        
        self.apps.append({
            "Title": title,
            "Function": func 
        })
        
    def run() : 
        
        with st.sidebar:
            app=option_menu (menu_title="NetFlix",
                             options=["Home","Categories","Thanks"],
                             icons=["house","collection-play","chat-heart"],
                             menu_icon="display",
                             default_index=0, 
                styles={"container":{"padding": "5!important","background-color":"black"},
        "nav-link":{"color":"white","font_size":"20px","text align":"left","margin":"0px"},
        "nav-link-selected":{"background-color": "#ff2b2b"},}
                
                ) 
            
        if app=="Home" : 
            Home.app1()
                
        if app=="Categories" : 
            Categories.app2() 
            
        if app=="Thanks" : 
            
            Thanks.app3() 
                
    run() 