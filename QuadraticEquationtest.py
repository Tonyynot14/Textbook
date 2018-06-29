from QuadraticEquation import QuadraticEquation
def main():
    a, b, c = eval(input("Input the values for a,b, and c for the quadratic function (put commas between values :"))

    quadratic = QuadraticEquation(a,b,c)

    if quadratic.getDiscriminate()>0:
        print(quadratic.getRoot1(),"is the first root",quadratic.getRoot2(),"is the second root")
    elif quadratic.getDiscriminate()==0:
        print(quadratic.getRoot1(),"is the only root")
    else:
        print("The equation has no roots!!")
main()