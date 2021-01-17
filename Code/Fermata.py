# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:29:48 2021

@author: Iga
"""

#importing modules
import streamlit as st
import time

#Creating header and logo
x, y, z, v = st.beta_columns(4)
title = x.title('Fermata')
logo = v.image('./images/logo.png', use_column_width = True)
subtitle = x.markdown('*Helps you focus and work better.*')
with st.beta_expander(''):
    st.write('A fermata (Italian: [fe"ma:ta]); "from fermare, to stay, or stop"; is a symbol of musical notation indicating that the note should be prolonged beyond the normal duration its note value would indicate. The extension time is not predetermined and depends on the interpretation.')

st.subheader(' ')

#Creating mindful breathing session with counter
l, m, r = st.beta_columns(3)
pressed = r.button('Start minduful breathing')
if pressed:
   st.image('./images/gif.gif', use_column_width = True)
   st.subheader('Your progress')
   my_bar = st.progress(0)
   st.button('End mindful breathing')
   for percent_complete in range(100):
       time.sleep(3)
       my_bar.progress(percent_complete + 1)
   st.success('Session completed! Now, start a Pomodoro session.')
   
st.subheader(' ')

#Creating Pomodoro session with counter
pressed_1 = l.button('Start Pomodoro session')
if pressed_1:
   st.subheader('Your progress')
   my_bar_1 = st.progress(0)
   st.button('End Pomodoro session')
   for percent_complete_1 in range(100):
       time.sleep(15)
       my_bar_1.progress(percent_complete_1 + 1)
   st.success('Session completed! Now, take a short break.')
   
#Adding graphics
work = l.image('./images/work.png', width = 200)
breathe = r.image('./images/breathe.png', use_column_width = True)
line = m.image('./images/line.png',  width = 250)
   
st.markdown('-------------------------------------------------------------------------')
st.subheader('')
st.subheader('')

#Creating section with infographics about both techniques
st.header('How it works?')
st.write('Learn about the app features.')
with st.beta_expander('Pomodoro technique'):
    st.image('./images/pomodoro_info.png', use_column_width = True)
with st.beta_expander('Mindful breathing'):
    st.image('./images/breathe_info.png', use_column_width = True)
   
st.subheader(' ')

#Creating section with research articles
st.subheader('Research articles')
st.write('Find out more about the research that supports effectiveness of the Pomodoro and mindful breathing techniques')
with st.beta_expander('Pomodoro technique'):
    st.markdown('[1] Shinoda, K. (2020). Pomodoro technique for improving students reading ability during COVID-19 pandemic. *Jurnal Education and Development*, 8(3), 1.')
    st.markdown('[2] Ariga, A., & Lleras, A. (2011). Brief and rare mental “breaks” keep you focused: Deactivation and reactivation of task goals preempt vigilance decrements. *Cognition*, 118(3), 439-443.')
    st.markdown('[3] Kühnel, J., Zacher, H., De Bloom, J., & Bledow, R. (2017). Take a break! Benefits of sleep and short breaks for daily work engagement. *European Journal of Work and Organizational Psychology*, 26(4), 481-491.')
with st.beta_expander('Mindful breathing'):
    st.write('[1] Silver, A. I., James, L. E., & Small, B. (2020). Word retrieval improves following a mindful breathing exercise but is unrelated to dispositional mindfulness. *Language, Cognition and Neuroscience*, 1-11.')
    st.write('[2] Azam, M. A., Latman, V. V., & Katz, J. (2019). Effects of a 12-Minute Smartphone-Based Mindful Breathing Task on Heart Rate Variability for Students With Clinically Relevant Chronic Pain, Depression, and Anxiety: Protocol for a Randomized Controlled Trial. *JMIR Research Protocols*, 8(12), e14119.')
    st.write('[3] Kurth, L., Engelniederhammer, A., Sasse, H., & Papastefanou, G. (2020). Effects of a short mindful-breathing intervention on the psychophysiological stress reactions of German elementary school children. *School Psychology International*, 41(3), 218-238.')
    st.write('[4] Britton, W. B., Shahar, B., Szepsenwol, O., & Jacobs, W. J. (2012). Mindfulness-based cognitive therapy improves emotional reactivity to social stress: results from a randomized controlled trial. *Behavior therapy*, 43(2), 365-380.')
    st.write('[5] Friese, M., Messner, C., & Schaffner, Y. (2012). Mindfulness meditation counteracts self-control depletion. *Consciousness and cognition*, 21(2), 1016-1022.')
    
#Creating sidebar with log in option
st.sidebar.write('Already have the accunt?') 
option = st.sidebar.button('Log in')
if option:
    st.sidebar.text_input('email / login')
    st.sidebar.text_input('password')
    st.sidebar.button('Done')

#Creating sidebar with sign up option
st.sidebar.write('Create an account')    
option_2 = st.sidebar.button('Sign up')
if option_2:
    st.sidebar.text_input('login')
    st.sidebar.text_input('email')
    st.sidebar.text_input('password')
    st.sidebar.button('Done')



