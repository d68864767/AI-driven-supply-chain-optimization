```python
# Importing necessary modules
from data_preprocessing import preprocess_data
from model import Model
from optimizer import optimize
from visualizer import visualize
from config import Config

def main():
    # Load configuration
    config = Config()

    # Preprocess the data
    data = preprocess_data(config.data_path)

    # Initialize the model
    model = Model(config)

    # Train the model
    model.train(data)

    # Optimize the supply chain
    optimized_data = optimize(model, data)

    # Visualize the results
    visualize(optimized_data)

if __name__ == "__main__":
    main()
```
