import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask the user for input N (positive integer)
    N = int(input("Enter the number of points (N): "))

    # Initialize arrays to store ground truth (X) and predicted labels (Y)
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    # Read N (x, y) points from the user
    print("Enter the (x, y) points:")
    for i in range(N):
        x = int(input(f"Enter x for point {i + 1}: "))
        y = int(input(f"Enter y for point {i + 1}: "))
        X[i] = x
        Y[i] = y

    # Compute precision and recall
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    # Output precision and recall
    print(f"\nPrecision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()
