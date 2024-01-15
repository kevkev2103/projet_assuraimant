import warnings
warnings.simplefilter(action='ignore', category=Warning)

import pickle
import streamlit as st
import pandas as pd

# chargement du model et du preprocessor
# En variables:
#   numérique : ['age', 'bmi', 'children']
#   catégorielle : ['region'] (southwest, southeast, northeast, northwest)
#   label : ['smoker'] (yes, no)

#model_path = 'data/model_cv.pickle'
model_path = 'data/model_grid.pickle'

m = pickle.load(open(model_path, 'rb'))
model = m['model']

smokerVal = {
            'Oui': 'yes', 
            'Non': 'no'
        }
sexVal = {
            'Homme': 'male', 
            'Femme': 'female'
        }
regionVal = {
    'Nord-est': 'northeast',
    'Nord-ouest': 'northwest',
    'Sud-est': 'southeast',
    'Sud-ouest': 'southwest'
}

with st.form("my_form"):
    st.title("Calculez votre prime d'assurance")
    
    sex_val = st.radio(
            "Sexe",
            [key for key, val in sexVal.items()],
            key="sex", horizontal=True)
    smoker_val = st.radio(
            "Fumeur",
            [key for key, val in smokerVal.items()],
            key="smoker", horizontal=True)
    poids_val = st.number_input('Poids', step=1)
    taille_val = st.number_input('Taille en cm', step=1)
    age_val = st.number_input('Age', min_value=18, step=1)
    #bmi_val = st.number_input('IMC', min_value=15., max_value=65., step=.1)
    children_val = st.number_input('Enfants', min_value=0, step=1)
    
    region_val = st.selectbox('Région',
                         [key for key, val in regionVal.items()],
                        )
    
    submitted = st.form_submit_button("Prédire !")
    if submitted:
        t = taille_val / 100
        bmi = poids_val / t**t
        columns = ['sex', 'smoker', 'age', 'bmi', 'children', 'region']

        df =  pd.DataFrame([[
                        sexVal[sex_val],
                        smokerVal[smoker_val],
                        age_val,
                        bmi,
                        children_val,
                        regionVal[region_val]
                    ]], columns=columns)
        
        print(df.head())
        predict = model.predict(df)
        
        st.write(f'{round(predict[0], 2)}€')
