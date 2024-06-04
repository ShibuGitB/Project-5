import streamlit as st 
import pickle 
from PIL import Image 
import sklearn 
import tensorflow as tf 
import joblib 

def app22() : 
    
    st.title("Category : Cricket"":cricket_bat_and_ball:") 
    st.video("Category Videos/Cricket.mp4") 
    st.text("Ind VS Sl 2011 World Cup Winning Six") 
    st.caption("Put your Review here"" "":full_moon_with_face:")
    review=st.text_input("Review"":pencil:","type here") 
    st.caption("Rating"" "":star2:")
    
    if review!="type here" : 
        
        input=[review] 
    
        model=tf.keras.models.load_model("NetFlix Review Rating Model-2.h5") 
        vectorizer=joblib.load("NetFlix Vectorizer")
        encoder=joblib.load("NetFlix Encoder") 
    
        rating=model.predict(vectorizer.transform(input)) 
    
        position=rating.argmax(axis=1) 
    
        rating=encoder.inverse_transform(position) 
    
        if rating==1 : 
        
            image=Image.open("rating images/1 star rating.png")
            st.image(image,width=390) 
            st.caption("By your Review to this show, Your rating is 1 for this. Please suggest your type of shows then we can easily gave you the correct one as your taste !!!")
        
        elif rating==2 : 
        
            image=Image.open("rating images/2 star rating.png")
            st.image(image,width=390) 
            st.caption("By your Review to this show, Your rating is 1 for this. Please suggest your type of shows then we can easily gave you the correct one as your taste !!!")
            
        elif rating==3 : 
        
            image=Image.open("rating images/3 star rating.png")
            st.image(image,width=390) 
            st.caption("By your Review to this show, Your rating is 3 for this, ThankYouuuu at the Same time suggest your type to reach you taste !!!")
        
        elif rating==4 : 
        
            image=Image.open("rating images/4 star rating.png")
            st.image(image,width=390,caption="By your Review to this show, Your rating is 4 for this: ThankYouuuuuuuuu !!!")    
        
        elif rating==5 : 
        
            image=Image.open("rating images/5 star rating.png")
            st.image(image,width=500,caption="By your Review to this show, Your rating is 5 for this: Hoooreyyyyyyyyy ThankYouuuuuuuuuuu!!!")    