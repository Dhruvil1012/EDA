# -*- coding: utf-8 -*-
"""dsa_load_data.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ff2hEr-8RTZ4zmNSBaenzjul8W7CD51O
"""

import pandas as pd
import numpy as np

def load_data(position):
  df = pd.read_csv(position)
  return(df)



