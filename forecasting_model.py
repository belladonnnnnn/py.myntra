import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class TrendDemandForecast:
    def _init_(self, data):
        self.data = data
        self.model = LinearRegression()
        self._train_model()

    def _train_model(self):
        # Simple example: using features and target from data
        X = self.data[['feature1', 'feature2']]  # Add your actual features here
        y = self.data['demand']
        self.model.fit(X, y)

    def predict(self, product_id):
        # This is a simplified example
        # Replace with actual logic to get features for the product
        features = np.array([[1, 2]])  # Example features
        prediction = self.model.predict(features)
        return {"product_id": product_id, "predicted_demand": prediction[0]}
