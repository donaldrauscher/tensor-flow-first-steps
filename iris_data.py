import pandas as pd


LARGE = 10000

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

train = pd.read_csv(TRAIN_URL, header=0, names=CSV_COLUMN_NAMES)
test = pd.read_csv(TEST_URL, header=0, names=CSV_COLUMN_NAMES)

x_train = train[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].values
y_train = train[['Species']].values

x_test = test[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].values
y_test = test[['Species']].values