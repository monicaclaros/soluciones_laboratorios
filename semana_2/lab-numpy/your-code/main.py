#1. Import the NUMPY package under the name np.
import numpy as np

#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))

#np.random.rand(2,3,5) --> segunda forma
#np.random.random_sample((2,3,5)) --> tercera forma
#4. Print a.
print("Array a")
print (a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b" 
b = np.ones((5,2,3))

#6. Print b.
print("Array b")
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size == b.size)
print(a.size)
#Ambos tienen 30


#8. Are you able to add a and b? Why or why not?


"""np.add(a,b)"""#Comment the line to let the rest of the code run
#It raises this error: ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 
#We can't add them because they don't have the same shape(number of columns and number of rows) even if they have the same size(amount of data)

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".


c = b.transpose(1,2,0) #This swaps the rows and columns of the matrix
                        # In the argument we specify in wich order the axes are permuted
print("Array b tras np.transpose")
print(c)



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(c,a)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
#When we transpose the "b" matrix to build "c" we end up with two matrix with the same shape. That's why we are able to sum them now.

#It will also work if we use the *.reshape() method, but be careful because this method doesn't change the order of the axis but reorders the values to fit the given shape.


print(d)

#12. Multiply a and c. Assign the result to e.
e = a * c
print("Imprimo a * c")
print(e)


#13. Does e equal to a? Why or why not?
print(e == a)



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print(f"Máximo {d_max}, mínimo {d_min}, media {d_mean}")


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty ((2,3,5))
print(f)

        #Remember that np.empty() returns an array of uninitialized (arbitrary) data of the given shape, dtype, and order.
        #not a matrix filled with zeros. For that we'll use np.zeros()



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for a in range (f.shape[0]):
        for b in range (f.shape[1]):#iterate through the length of axis 1
                for c in range (f.shape[2]):#iterate through the length of axis 2
                        if  d_min < d[a][b][c] < d_mean:
                                f[a][b][c] = 25
                        elif d_mean < d[a][b][c] < d_max:
                                f[a][b][c] = 75
                        elif d[a][b][c] == d_mean:
                                f[a][b][c] = 50
                        elif d[a][b][c] == d_min:
                                f[a][b][c] = 0
                        elif d[a][b][c] == d_max:
                                f[a][b][c] = 100
                   
print(f)
"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],
       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print("My d -------------------------------------------------------------------------------------")
print(d)

print("My f -------------------------------------------------------------------------------------")
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],
       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
# """
f = f.astype('str')
for a in range (f.shape[0]):
        for b in range (f.shape[1]):
                for c in range (f.shape[2]):
                        if  d_mean < d[a][b][c] < d_max:
                                f[a][b][c] = 'D'
                        elif d_min < d[a][b][c] < d_mean:
                                f[a][b][c] = 'B'
                        elif d[a][b][c] == d_mean:
                                f[a][b][c] = 'C'
                        elif d[a][b][c] == d_min:
                                f[a][b][c] = 'A'
                        elif d[a][b][c] == d_max:
                                f[a][b][c] = 'E'

print(f)