```python
# Importing necessary modules
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data_path):
    """
    This function is used to preprocess the data for the supply chain optimization model.
    It reads the data from the given path, handles missing values, and scales the numerical features.

    Parameters:
    data_path (str): The path to the data file.

    Returns:
    DataFrame: The preprocessed data.
    """

    # Load the data
    data = pd.read_csv(data_path)

    # Handle missing values
    # Here, we simply drop the rows with missing values. Depending on the data, you might want to fill them in a different way.
    data = data.dropna()

    # Scale numerical features
    # Here, we use standard scaling (mean=0, std=1). Depending on the data, you might want to use a different scaler.
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    return data
```
