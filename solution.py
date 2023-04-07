import pandas as pd
import numpy as np


chat_id = 997095449 

def solution(x: np.array) -> float:
    x=(x-(-1+np.exp(1)))/10
    return x.mean() 
