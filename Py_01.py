'''
Read different types of data from standard input, process them as shown in output format and print the answer to standard output.

Input format:
First line contains integer N. 
Second line contains string S.

Output format: 
First line should contain N x 2. (N between 0-10 & S between 0-15, S = Length of String)
Second line should contain the same string S.
'''
# Write your code here
N =int(input())
S = input()
print(N*2)
print("%s" %S)
