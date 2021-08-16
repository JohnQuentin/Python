import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 150, size=(20, 4)), 
                                     columns=list("ABCD"))

#standard correlation
df.corr().style.background_gradient(cmap="Blues")

#kendall correlation
df.corr('kendall').style.background_gradient(cmap="Blues")

#spearman correlation
df.corr('spearman').style.background_gradient(cmap="Blues")
