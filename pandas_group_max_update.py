import pandas as pd
data = {
    'group': ['A', 'B', 'A','B'],
    'odds' : [85, 75, 60, 65]
}

data = pd.DataFrame(data)
data['max'] = data.groupby('group')['odds'].transform('max')
data['min'] = data.groupby('group')['odds'].transform('min')
print(data)