import numpy as np
from sklearn.linear_model import LinearRegression

# Data: [size, bedrooms, age]
X = np.array([
    [1000, 2, 5],
    [1500, 3, 3],
    [800, 1, 8],
    [2000, 4, 1],
    [1200, 2, 4]
])

# Price lakhs mein
y = np.array([50, 75, 35, 100, 60])

# Model training
model = LinearRegression()
model.fit(X, y)

# User se input lo
print("=== House Price Predictor ===")
size = float(input("Ghar ka size (sqft): "))
bedrooms = float(input("Kitne bedrooms: "))
age = float(input("Ghar ki age (saal): "))

apna_ghar = np.array([[size, bedrooms, age]])
price = model.predict(apna_ghar)
print("Tumhare ghar ki price:", round(price[0], 2), "lakh! hai...")
