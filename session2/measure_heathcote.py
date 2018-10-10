def calculate_distance(A, B):
    #Calculates the euclidean difference between n-dimentional points A and B
    distance = 0

    if len(A) == len(B):
        for i in range(len(A)):
            #Sum the difference in squares for each dimension
            distance += (A[i]-B[i])**2

        #Square root sum of difference of squares to get true distance
        distance = distance**0.5
        if distance == 0:
            print('Warining: Coordinates are the same, hence distance is zero.')
        else:
            print(distance)
    else:
        print('A and B have different dimensions.')

        
if __name__ == '__main__':
    #Set point A and B coordinates
    point_A = (0,0)
    point_B = (1,1)    

    calculate_distance(point_A, point_B)