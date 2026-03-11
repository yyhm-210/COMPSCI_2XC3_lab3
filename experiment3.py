from lab3 import XC3Tree

def experiment3():
    results = []

    for i in range(26):  # degree 0 to 25
        tree = XC3Tree(i)
        height = tree.getHeight()
        results.append((i, height))
        print(f"Degree {i}: Height = {height}")

    return results


if __name__ == "__main__":
    experiment3()