import numpy as np
import pandas as pd
from package_test.config import config
import importlib
# Reload the module if changes have been made in mymodule
importlib.reload(config)


def plus(dataframe):
    dataframe['addition'] = dataframe[config.DF_COLUMNS[0]] + dataframe[config.DF_COLUMNS[1]] 
    return dataframe
    



# Example of using the function
if __name__ == "__main__":
    np.random.seed(config.RANDOM_SEED)
    df = pd.DataFrame(np.random.randint(10, size = config.DF_SHAPE), columns=config.DF_COLUMNS)
    df = plus(df)
    df.head()