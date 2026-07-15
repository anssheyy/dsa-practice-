# Problem: Given an integer N, print your name N times
# Source: Striver's DSA Sheet

def print_name_n_times(n, name="Anshi"):
    for i in range(n):
        print(name)

if __name__ == "__main__":
    n = int(input("Enter N: "))
    print_name_n_times(n)