import pickle
import streamlit as st
import pandas as pd

# chargement du model et du preprocessor
# En variables:
#   numérique : ['age', 'bmi', 'children']
#   catégorielle : ['region'] (southwest, southeast, northeast, northwest)
#   label : ['smoker'] (yes, no)

model_path = 'data/model.pickle'
m = pickle.load(open(model_path, 'rb'))
model = m['model']
preprocessor = m['preprocessor']

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

columns = ['smoker', 'age', 'bmi', 'children', 'region']

with st.form("my_form"):
    st.title("Calculez votre prime d'assurance")
    
    smoker_val = st.radio(
            "Fumeur",
            [key for key, val in smokerVal.items()],
            key="smoker", horizontal=True)
    age_val = st.number_input('Age', min_value=18, step=1)
    bmi_val = st.number_input('IMC', min_value=15., max_value=65., step=.1)
    children_val = st.number_input('Enfants', min_value=0, step=1)
    
    region_val = st.selectbox('Région',
                         [key for key, val in regionVal.items()],
                        )
    
    submitted = st.form_submit_button("Prédire !")
    if submitted:
        print([
                    [smokerVal[smoker_val]],
                    [age_val],
                    [bmi_val],
                    [children_val],
                    [regionVal[region_val]]
                ])
        df =  pd.DataFrame([[
                        smokerVal[smoker_val],
                        age_val,
                        bmi_val,
                        children_val,
                        regionVal[region_val]
                    ]], columns=columns)
        
        df_process = preprocessor.transform(df)
        print(df)
        print(df_process)
        predict = model.predict(df_process)
        
        st.write(f'{round(predict[0], 2)}€')
