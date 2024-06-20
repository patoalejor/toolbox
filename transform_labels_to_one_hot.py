
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def convert_y_to_keras(y):
    """Convert y to required Keras format."""
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    y = y.reshape(len(y), 1)
    onehot_encoder = OneHotEncoder(sparse_output=False)
    y = onehot_encoder.fit_transform(y)
    return y

y_ordinal = [1,0,1,0,1,0,2,0,1,0,2,3,1,2,1,0,1]
y_one_hot = convert_y_to_keras(y_ordinal)

print(y_ordinal)
print(y_one_hot)