# Vincenzo Russotto

# 3rd party libraries

import pandas as pd
df = pd.read_csv("data_words.csv", delimiter= ";")
df.drop(columns= ["N_definito1", "N_definito2", "Numero", "Numero2"], inplace= True)
df.to_csv("words.csv", index=False)


