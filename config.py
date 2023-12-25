```python
class Config:
    def __init__(self):
        # Path to the data file
        self.data_path = "path/to/your/data.csv"

        # Parameters for the model
        self.model_params = {
            "learning_rate": 0.01,
            "epochs": 100,
            "batch_size": 32
        }

        # Parameters for the optimizer
        self.optimizer_params = {
            "optimization_method": "gradient_descent",
            "max_iterations": 1000,
            "tolerance": 1e-6
        }

        # Parameters for visualization
        self.visualization_params = {
            "plot_type": "line",
            "color": "blue"
        }
```
