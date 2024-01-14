
import streamlit as st
import pandas as pd

st.title(body="Assur...aimant")

st.write('''
         Cher client,\n
         Nous vous remercions de faire confiance à assur'aimant, afin de pouvoir vous accompagner de la 
         meilleure des manières, nous vous proposons de renseigner certaines informations sur cet interface.  \n
         A vous de jouer.
         ''')

st.title('Formulaire de saisie')



genre  = ['male','female']
sex = st.radio('Quel est votre sexe ?',genre)

age = st.slider("quel est votre âge ?",0,100)

tabac=['yes','no']
smoker = st.radio('Etes vous fumeur(euse)?',tabac)

r= ['southwest', 'southeast', 'northwest', 'northeast']
region = st.radio('Quelle est votre région',r )

children = st.slider("Combien d'enfant(s) avez-vous ?",0,10)

taille = st.slider('Quelle est votre taille (en cm)?',1,250)

poids = st.slider('Quel est votre poids (en kg) ?',1,200)

bmi = poids/(taille/100)**2

st.write(f'votre bmi est : {bmi}')

data={
    'age':age,
    'sex':sex,
    'bmi':bmi,
    'children':children,
    'smoker':smoker,
    'region': region


}

input_parametres = pd.DataFrame(data,index=[0])
print(input_parametres)

  
st.subheader('Voici les élements renseignés:')

st.write(input_parametres)


import pickle

input_parametres.loc[input_parametres['bmi'] < 18.5 , 'grade'] = 'underweight'
input_parametres.loc[input_parametres['bmi'].between(18.5, 25, 'both'), 'grade'] = 'good'
input_parametres.loc[input_parametres['bmi'].between(25, 30, 'right'), 'grade'] = 'overweight'
input_parametres.loc[input_parametres['bmi'] > 30 , 'grade'] = 'obesity'
input_parametres.drop('bmi',axis=1, inplace=True)

with open ('best_model.pkl','rb') as model_file:
    loaded_model = pickle.load(model_file)

prediction = loaded_model.predict(input_parametres)

st.write(f'''
Nous avons analysé votre dossier, nous avons {round(prediction[0],2)} €  
''')
