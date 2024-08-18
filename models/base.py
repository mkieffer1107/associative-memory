class BaseModel:
    def __init__(self):
        self.parameters = {}

    def train(self, data):
        """Train the model on the provided data."""
        raise NotImplementedError

    def predict(self, data):
        """Make predictions based on the provided data."""
        raise NotImplementedError

    def save_model(self, file_path: str):
        """Save the model parameters to a file."""
        with open(file_path, 'w') as f:
            f.write(str(self.parameters))
        print(f"Model saved to {file_path}")

    def load_model(self, file_path: str):
        """Load the model parameters from a file."""
        with open(file_path, 'r') as f:
            self.parameters = eval(f.read())
        print(f"Model loaded from {file_path}")

    def __repr__(self):
        return f"{self.__class__.__name__} with parameters: {self.parameters}"