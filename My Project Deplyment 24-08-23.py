#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pnd  
import numpy as nmp  
import pickle as pkl  
import streamlit as smt  
from PIL import Image as img  
    
# loading in the model to predict on the data  
pickle_in1 = open('recommendations.pkl', 'rb')  
recommendations = pkl.load(pickle_in1)  
    
def welcome():  
    return 'welcome you all'  
    
# here, we will define the function which will make the prediction using the      
# data which the user have imported  
def recommend_food_by_location(state,region,flavor,diet):
# Filter foods based on the provided region and state
    recommending_foods = data2[(data2["state"] == state) 
                               & (data2["region"] == region) 
                               & (data2["flavor"] == flavor_profile) 
                               & ((data2["diet"] == diet))]
        
    
# Here, this is the main function in which we will be defining our webpage   
def main():  
      # Now, we will give the title to out web page  
    smt.title("Food Recommendation System")  
        
    # Now, we will be defining some of the frontend elements of our web            # page like the colour of background and fonts and font size, the padding and    # the text to be displayed  
    html_temp = """  
    <div style = "background-colour: #FFFF00; padding: 16px">  
    <h1 style = "color: #000000; text-align: centre; "> Streamlit Food Recommendation ML App   
     </h1>  
    </div>  
    """  
        
    # Now, this line will allow us to display the front-end aspects we have   
    # defined in the earlier  
    smt.markdown(html_temp, unsafe_allow_html = True)  
        
    # Here, the following lines will create the text boxes in which the user can     # enter the data which is required for making the prediction  
    user_state = smt.text_input ("state ", " Type Here")  
    user_region = smt.text_input ("region ", " Type Here")  
    user_flavor = smt.text_input ("flavor_profile ", " Type Here")  
    user_diet = smt.text_input ("diet ", " Type Here")  
    result = " " 
    
        
    # here, the below line will ensure that whenever the button named 'Recommend' 
    # is clicked, the prediction function that is defined earlier is called for making   
    # the recommendation and it will also store it in the variable result  
    if smt.button ("Recommend"):  
        result = recommend_food_by_location(state,region,flavor,diet) 
    smt.success ('The output of the above is {}'.format(result))  
if __name__== '__main__':  
    main()  


# In[ ]:




