import numpy as np

np.seterr(divide='ignore', invalid='ignore')

_ = np.seterr(divide='warn', invalid='warn')