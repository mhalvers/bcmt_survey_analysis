def change_column_names(df):

    old_labels = df.columns.values

    new_labels = ['timestamp','activities','primary activity','years experience',
                  'activity frequency','activity duration','group size',
                  'membership duration','membership reason','have volunteered',
                  'volunteer activities','used bcmt map','bcmt map frequency',
                  'bcmt.org use reason','mobile apps used','submitted scr',
                  'scr report frequency','gender','age group','location','email']

    df.rename(columns=dict(zip(old_labels, new_labels)), inplace=True)

    return df
