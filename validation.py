from train import *

cv = GroupKFold(n_splits=10)
results = cross_val_score(model, x, y, cv = cv, groups=datas.idade_modelo)
