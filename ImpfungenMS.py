from pandas import DataFrame, DatetimeIndex, read_csv, to_datetime
from datetime import timedelta
import numpy as np
import altair as alt
import pandas as  pd
#alt.data_transformers.disable_max_rows()
#alt.renderers.enable('notebook')

df_impfung=pd.read_csv("https://raw.githubusercontent.com/robert-koch-institut/COVID-19-Impfungen_in_Deutschland/master/Aktuell_Deutschland_Landkreise_COVID-19-Impfungen.csv")


df_impfung_muenster=df_impfung.loc[df_impfung['LandkreisId_Impfort'].isin([5515])]
datum = df_impfung_muenster['Impfdatum'].iat[-1]
#df_impfung_muenster['Impfdatum'] =pd.to_datetime(df_impfung_muenster['Impfdatum'], format='%Y-%m-%d')
einwohnerzahlMuenster=316403
#Größen der Altersgruppen nach https://www-genesis.destatis.de
df_Münster_Anteilig=pd.DataFrame({'Altersgruppen': ['Gesamtbevölkerung',
                                                   '12-17',
                                                    '18-59',
                                                    '60+'
                                                   ],
                                            'Erste Dosis Absolut':[
                                                df_impfung_muenster.loc[df_impfung_muenster['Impfschutz'] == 1, 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 1) & (df_impfung_muenster['Altersgruppe'] == '12-17') , 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 1) & (df_impfung_muenster['Altersgruppe'] == '18-59') , 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 1) & (df_impfung_muenster['Altersgruppe'] == '60+') , 'Anzahl'].sum(),
                                              ],
                                            'Erste Dosis Anteilig':[
                                                df_impfung_muenster.loc[df_impfung_muenster['Impfschutz'] == 1, 'Anzahl'].sum()/einwohnerzahlMuenster*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 1) & (df_impfung_muenster['Altersgruppe'] == '12-17') , 'Anzahl'].sum()/14941*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 1) & (df_impfung_muenster['Altersgruppe'] == '18-59') , 'Anzahl'].sum()/164726*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 1) & (df_impfung_muenster['Altersgruppe'] == '60+') , 'Anzahl'].sum()/73802*100,
                                            ],
                                            'Zweite Dosis Absolut':[
                                                df_impfung_muenster.loc[df_impfung_muenster['Impfschutz'] == 2, 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 2) & (df_impfung_muenster['Altersgruppe'] == '12-17') , 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 2) & (df_impfung_muenster['Altersgruppe'] == '18-59') , 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 2) & (df_impfung_muenster['Altersgruppe'] == '60+') , 'Anzahl'].sum(),
                                            ],
                                            'Zweite Dosis Anteilig':[
                                            df_impfung_muenster.loc[df_impfung_muenster['Impfschutz'] == 2, 'Anzahl'].sum()/einwohnerzahlMuenster*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 2) & (df_impfung_muenster['Altersgruppe'] == '12-17') , 'Anzahl'].sum()/14941*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 2) & (df_impfung_muenster['Altersgruppe'] == '18-59') , 'Anzahl'].sum()/164726*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 2) & (df_impfung_muenster['Altersgruppe'] == '60+') , 'Anzahl'].sum()/73802*100,
                                            ],
                                             'Dritte Dosis Absolut':[
                                                df_impfung_muenster.loc[df_impfung_muenster['Impfschutz'] == 3, 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 3) & (df_impfung_muenster['Altersgruppe'] == '12-17') , 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 3) & (df_impfung_muenster['Altersgruppe'] == '18-59') , 'Anzahl'].sum(),
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 3) & (df_impfung_muenster['Altersgruppe'] == '60+') , 'Anzahl'].sum(),
                                            ],
                                            'Dritte Dosis Anteilig':[
                                            df_impfung_muenster.loc[df_impfung_muenster['Impfschutz'] == 3, 'Anzahl'].sum()/einwohnerzahlMuenster*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 3) & (df_impfung_muenster['Altersgruppe'] == '12-17') , 'Anzahl'].sum()/14941*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 3) & (df_impfung_muenster['Altersgruppe'] == '18-59') , 'Anzahl'].sum()/164726*100,
                                                df_impfung_muenster.loc[(df_impfung_muenster['Impfschutz'] == 3) & (df_impfung_muenster['Altersgruppe'] == '60+') , 'Anzahl'].sum()/73802*100,
                                            ]})

erst=alt.Chart(df_Münster_Anteilig).mark_bar(color='red').encode(
    alt.X('Erste Dosis Anteilig', title='Einfach geimpft (rot)',scale=alt.Scale(domain=[0,100])),
    y="Altersgruppen:O",
    tooltip=['Erste Dosis Anteilig']
)
zweit=alt.Chart(df_Münster_Anteilig).mark_bar(color='green').encode(
    #x='Zweite Dosis Anteilig',
    alt.X('Zweite Dosis Anteilig', title='Doppelt geimpft (grün)'),
    y="Altersgruppen:O",
    tooltip=['Zweite Dosis Anteilig']
)
drei=alt.Chart(df_Münster_Anteilig).mark_bar(color='blue').encode(
    #x='Zweite Dosis Anteilig',
    alt.X('Dritte Dosis Anteilig', title='Dreifach geimpft (blau)'),
    y="Altersgruppen:O",
    tooltip=['Dritte Dosis Anteilig']
)
final=(erst + zweit+drei).properties(
    title={
    'text':'Impfquote in Münster nach Altersgruppen Datum:'+datum,
    'subtitle':['Datenqulle: RKI',]
          }, width=800,height=200)
#final.encode(X('Erste Dosis Anteilig', scale=Scale(domain=[0, 100])))
final.save('website/ImpfQuoteMuenster.html')
