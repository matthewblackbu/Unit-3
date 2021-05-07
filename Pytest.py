import pytest
import helper_functions
import pandas as pd
import numpy as np
from helper_functions import Helpers



def test_null_count():
    df1 = pd.DataFrame([[1,2,3,4],[1,2,3,4],[1,2,3,np.nan]])
    df2 = pd.DataFrame([[1,2,3,4],[1,2,np.nan,4],[1,2,3,np.nan]])
    df3 = pd.DataFrame([1,np.nan,3,4,1,2,3,4,1,2,3,np.nan])
    helper1 = Helpers(df1)
    helper2 = Helpers(df2)
    helper3 = Helpers(df3)
    assert helper1.null_count() == 1
    assert helper2.null_count() == 2
    assert helper3.null_count() == 2




