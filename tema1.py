#V1 - hardcodat
#Ex 1.
a = [1, 2, 3, 4, 5]
print("Input array:",a)
a.reverse()
print("Result:",a)

#Ex 2.
#Example:
a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
b = 2
print("Input array: ",a)
print("Searched value:",b)
print("Result:",a.count(b))
#Ex 3.
a = 'ana are mere si nu are pere'
print("Input string",a)
print("Result",len(a.split(" ")))

#V2 - input tastarura
#Ex.1
n=0
a=[]
print("Introduceti numarul de elemente din sir: ")
n=int(input())

for i in range(n):
    print("Introuceti elemntul: ",i)
    a.append(int(input()))
print("Input array: ",a)
a.reverse()
print("Result:",a)


#Ex. 2
print("Alegeti numarul cautat:")
i=int(input())
print("Result:",a.count(i))


#Ex. 3
print("Introduceti propozitia:")
st=input()
print("Result:",len(st.split(" ")))