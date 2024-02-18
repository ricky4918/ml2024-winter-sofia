import numpy as np

class KNNRegression:
    def __init__(self):
        self.points = []

    def read_points(self, n):
        for i in range(n):
            x = float(input("Enter x-coordinate for point {}: ".format(i + 1)))
            y = float(input("Enter y-coordinate for point {}: ".format(i + 1)))
            self.points.append((x, y))

    def knn_regression(self, k, x):
        if k > len(self.points):
            return "Error: k is greater than the number of points provided."
        
        distances = np.array([abs(point[0] - x) for point in self.points])
        sorted_indices = np.argsort(distances)
        k_nearest_indices = sorted_indices[:k]
        
        sum_y = sum(self.points[i][1] for i in k_nearest_indices)
        return sum_y / k

def main():
    n = int(input("Enter the number of points (N): "))
    knn_reg = KNNRegression()
    knn_reg.read_points(n)

    k = int(input("Enter the value of k: "))
    x = float(input("Enter the value of X: "))

    result = knn_reg.knn_regression(k, x)

    print("Result of k-NN Regression:", result)


if __name__ == "__main__":
    main()
