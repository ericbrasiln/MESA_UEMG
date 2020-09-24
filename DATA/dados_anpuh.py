import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv('/home/ebn/Documentos/GitHub/MESA_UEMG/DATA/anais-anpuh-infos.csv')

print(len(df))

pb = df[df['Título'].str.contains('pós-abolição')]
print(len(pb))
ditadura = df[df['Título'].str.contains("ditadura")]
print(len(ditadura))
educacao = df[df['Título'].str.contains("educação")]
emancipacoes = df[df['Título'].str.contains("cidadania")]
print(len(emancipacoes))
#
#pb.to_csv('pb.csv')
#ditadura.to_csv('ditadura.csv')
