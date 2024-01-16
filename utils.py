def bmi_transform(df):
    df.loc[df['bmi'] < 18.5 , 'bmi'] = 0
    df.loc[df['bmi'].between(18.5, 25, 'both'), 'bmi'] = 1
    df.loc[df['bmi'].between(25, 30, 'right'), 'bmi'] = 2
    df.loc[df['bmi'] > 30 , 'bmi'] = 3
    df.bmi = df.bmi.astype('category')
    return df