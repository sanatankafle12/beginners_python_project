def function():
    coefficient_list = []
    n = int(input("Enter the degree of the polynomial: "))
    for i in range(n+1):
        coefficient = int(input(f"Enter the coefficient of x^{i}: "))
        derivative = coefficient*i
        coefficient_list.append(derivative)

    print(coefficient_list)

if __name__ == "__main__":
    function()