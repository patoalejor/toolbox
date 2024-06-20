import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

def encode_to_label(input_data, n_bins):
    
    if len(input_data.shape) == 1:
        input_data.shape = (-1,1)
    est = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy='quantile', subsample=200000)
    est.fit(input_data)
    output_data = est.transform(input_data)
    print(f"Bins: {np.unique(output_data, return_counts=True)}")
    unique_groups = np.unique(output_data)
    for each_group in unique_groups:
        idx = np.where(output_data == each_group)
        n_label = input_data[idx]
        print(f"Label: {each_group} N:{len(n_label)} Data: {np.mean(n_label):<5.2f} (+-{np.std(n_label):<5.2f})  max: {np.max(n_label):<5} min: {np.min(n_label):<5}")
    return output_data



input_data = np.random.randint(1, 200, 100)
encode_data = encode_to_label(input_data, 5)
encode_data = encode_to_label(input_data, 10)
