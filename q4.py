it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.append("instagram")
print(it_companies)
companies = ["accensor","flipkart","twitter"]
it_companies.extend(companies)
print(it_companies)
it_companies.remove("Facebook")
print(it_companies)
C=A.union(B)
print(C)
D=A.intersection(B)
print(D)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B)&B.union(A))
print(A.symmetric_difference(B))
A.clear()
print(A)
ages=set("age") # conversion of list to set#
print(len(age))
print(len(ages))


