# Vincenzo Russotto

# librerie terze parti
import pandas as pd
df = pd.read_csv("polarita_dataset.csv", delimiter= ";")
df.drop(columns= ["N_definito1", "N_definito2", "Numero", "Numero2"], inplace= True)
df.to_csv("dataset/pulito.csv", index=False)


