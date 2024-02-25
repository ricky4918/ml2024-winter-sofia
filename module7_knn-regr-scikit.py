import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def main():
    # Ask for input N
    N = int(input("Enter the number of points (N): "))
    
    # Ask for input k
    k = int(input("Enter the value of k for k-NN Regression: "))

    # Initialize arrays to store X and Y values
    X = np.zeros(N)
    Y = np.zeros(N)

    # Read N (x, y) points
    print("Enter the coordinates of the points (x, y):")
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        X[i] = x
        Y[i] = y

    # Ask for input X
    x_pred = float(input("Enter the value of X for prediction: "))

    if k <= N:
        # Reshape X to 2D array for scikit-learn input
        X_2d = X.reshape(-1, 1)

        # Fit k-NN Regression model
        knn_reg = KNeighborsRegressor(n_neighbors=k)
        knn_reg.fit(X_2d, Y)

        # Predict Y for input X
        y_pred = knn_reg.predict([[x_pred]])

        # Compute coefficient of determination (R-squared)
        y_pred_all = knn_reg.predict(X_2d)
        r_squared = r2_score(Y, y_pred_all)

        print(f"The predicted value of Y for X = {x_pred} is: {y_pred[0]}")
        print(f"Coefficient of determination (R^2): {r_squared}")
    else:
        print("Error: k must be less than or equal to N.")

if __name__ == "__main__":
    main()
