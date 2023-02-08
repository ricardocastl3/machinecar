from datas import *

SEED = 55
np.random.seed(SEED)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.30,
                                                stratify=y)

cf1 = DecisionTreeClassifier(max_depth=3)
cf2 = RandomForestClassifier(n_estimators=10, max_depth=3)

model = VotingClassifier([("decision", cf1), ("random",cf2)], voting="soft")
model.fit(train_x, train_y)
