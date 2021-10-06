import numpy as np
class frame:

    def __init__(self):
        self.measures_list = []

    def add_measure(m_i):
        self.measures_list.append(m_i)
        self.len += 1
    
    def get_measures():
        arr = np.array(measures)
        m = np.mean(arr)
        r = sqrt(measures.var(ddof=1) / measures.size)
        c = 1 - 2*r
        return(m, c)
    