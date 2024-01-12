

import pandas as pd


def categorisation_numerique(df, bins, labels, categorie):
    df = df.drop(['charges'], axis=1)
    df['nouvelle_categorie'] = pd.cut(df[categorie], bins=bins, labels=labels, right=False)
    categorie_dummies = pd.get_dummies(df['nouvelle_categorie'], prefix=categorie, drop_first=True)
    df = pd.concat([df, categorie_dummies], axis=1)
    df = df.drop(['nouvelle_categorie'], axis=1)
    return df

df = pd.read_csv('data/df_clean.csv')

df = categorisation_numerique(df, [0, 18.5, 24.9, 28.5, 35, 40, float('inf')],
                               ['maigreur', 'sous_poids', 'poids_normal', 'surpoids', 'obésité', 'obésité_morbide'],
                               'bmi')
print(df)