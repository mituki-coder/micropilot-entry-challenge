import math

#take the coefficients a,b,c as user inputs
a = input("Enter the coefficient a:")
b = input("Enter the coefficient b:")
c = input("Enter the coefficient c:")

#convert inputs into integers
a = int (a)
b = int (b)
c = int (c)

#getX function to compute and compare the roots of the equation defined by the given coefficients
def getX(a,b,c):
    #calculating the discriminant i.e b*b - 4*a*c
    dis = b*b - 4*a*c
    if dis > 0:
        print("Roots real and not equal:")
        sq_rt_dis = math.sqrt(dis)

        #root 1
        root_1 = (-b + sq_rt_dis) / (2 * a)

        #root 2
        root_2 = (-b - sq_rt_dis) / (2 * a)

        print("Root 1: " + str(root_1))
        print("Root 2: " + str(root_2))

        #compare the roots and return the largest
        print(max(root_1,root_2), "is the largest:")


    elif dis == 0:
        print("Roots are real and equal: ")
        root = -b/2*a
        print("Roots of the equation:" + str(root))

    else:
        print("Error on your coefficients: ")

getX(a,b,c)