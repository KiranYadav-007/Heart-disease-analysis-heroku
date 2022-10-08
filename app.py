import pickle
import streamlit as st 
st.title("HEART DISEASE ANALYSIS")
col1,col2,col3 = st.columns([1.3,5,0.2])

age = st.slider("Age:",0,100,50)
sex = st.slider("Sex: Male=1,Female=0",0,1,1)
cp = st.slider("Chest pain:",0,3,2)
bp = st.slider("Resting Bp in mm Hg:",100,400,250)
chol = st.slider("Cholesterol in mg/dl:",100,400,250)
fbs = st.slider("Fasting blood sugar > 120 mg/dl: True=1,False=0",0,1,0)
rest = st.slider("Resting ECG results:",0,2,1)
hrate = st.slider("Maximum heart rate:",60,200,130)
exang = st.slider("Exercize induced angina Yes=1,No=0:",0,1,0)
old = st.slider("Oldpeak,ST depression induced by exercise relative to rest:",0,10,5)
slope = st.slider("Slope of peak exercise ST segment, 1=unsloping,2=flat,3=downsloping:",1,3,2)
ca = st.slider("No. of major vessels(0-3):",0,3,2)
thal = st.slider("Thal normal=1,fixed defect=2,reversable defect=3",1,3,2)

target = ['Less chance of heart attack','More chance of heart attack']
new = pickle.load(open('model.pkl','rb'))
y_pred = new.predict([[age,sex,cp,bp,chol,fbs,rest,hrate,exang,old,slope,ca,thal]])
y_pred = target[y_pred[0]]
clicked = st.button("Submit")
if(clicked):
	if(y_pred):
		st.success('Prediction Successful')
		y_pred
		st.balloons()
	else:
		st.error('Error running analysis')
