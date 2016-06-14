# You are given two sequences. Write a program to determine the longest common subsequence between the two strings 

def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # Intializing (m+1) cross (n+1) matrix
    T = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i][j-1], T[i-1][j])
    return T

def backTrack(T, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return backTrack(T, X, Y, i-1, j-1) + X[i-1]
    else:
        if T[i][j-1] > T[i-1][j]:
            return backTrack(T, X, Y, i, j-1)
        else:
            return backTrack(T, X, Y, i-1, j)

X = raw_input("Enter the 1st String: ")
Y = raw_input("Enter the 2nd String: ")
m = len(X)
n = len(Y)
T = LCS(X, Y)

print "LCS: '%s'" % backTrack(T, X, Y, m, n)
