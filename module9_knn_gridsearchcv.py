import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Function to read input pairs
def read_pairs(num_pairs):
    pairs = []
    for _ in range(num_pairs):
        x = float(input("Enter x value: "))
        y = int(input("Enter y value: "))
        pairs.append((x, y))
    return pairs

# Read training set
N = int(input("Enter the number of pairs in the training set (N): "))
train_set = read_pairs(N)
X_train = np.array([pair[0] for pair in train_set])
y_train = np.array([pair[1] for pair in train_set])

# Read test set
M = int(input("Enter the number of pairs in the test set (M): "))
test_set = read_pairs(M)
X_test = np.array([pair[0] for pair in test_set])
y_test = np.array([pair[1] for pair in test_set])

# Perform kNN classification for different values of k and find the best k
best_accuracy = 0
best_k = 1
for k in range(1, 11):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train.reshape(-1, 1), y_train)
    y_pred = knn_classifier.predict(X_test.reshape(-1, 1))
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy for k =", k, ":", accuracy)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

print("Best k for kNN Classification:", best_k)
print("Corresponding test accuracy:", best_accuracy)
