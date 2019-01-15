import pandas as pd
import numpy as np
#from tabulate import tabulate
# Read Json File
data=pd.read_json("searches.json",lines=True)
print("Loaded JSON")
print()
print(data.head())
#Removing the 234 instructors from the dataset
data.drop(data[data.is_instructor==True].index, inplace=True) #446 users left
print()
print("Removed Instructors from Dataset")
print()
print(data.head())
#drop Instructors column
data=data.drop(columns=['is_instructor'])
print()
print("Dropped Instructors Column")
print()

print(data.head())

#Design A

even=data.loc[data['uid']%2==0]

#re arrange index
#even=even.sort_index(axis=1,ascending=False)
even=even.reset_index()
even=even.drop(columns=['index'])

#sum
l_count= sum(even.login_count)
s_count= sum(even.search_count)
#ratio=l_count/s_count

#last index value = even user
#index.getlevelvalues(0)
total_A=even.index
UsersA=total_A[-1]

#total sum
sums = even.select_dtypes(pd.np.number).sum().rename('Total')
even=even.append(sums)
#even.loc['total'] = even.select_dtypes(pd.np.number).sum()
print()
print("A design Users with even Uid")
print()

print(even.tail())
print()
#print(l_count,s_count)
#print('Ratio : Login/Search',ratio)
#Design B
odd=data.loc[data['uid']%2==1]
#re arrange index
odd=odd.reset_index()
odd=odd.drop(columns=['index'])

#odd_users=odd['index']
total_B=odd.index
UsersB=total_B[-1]

l_count1= sum(odd.login_count)
s_count1= sum(odd.search_count)
#ratio1=s_count1/l_count1
sum2 = odd.select_dtypes(pd.np.number).sum().rename('Total')
odd=odd.append(sum2)
print()
print("B design Users")
print()

print(odd.tail())
#print(l_count1,s_count1)
#print('Ratio',ratio1)
print()

d={'index':pd.Series(['User A','User B']),
    'Total Users':pd.Series([UsersA,UsersB]),
   'Login counts':pd.Series([l_count,l_count1]),
   'Search counts':pd.Series([s_count,s_count1])}
df=pd.DataFrame(d)
df=df.set_index('index')
sum3 = df.select_dtypes(pd.np.number).sum().rename('Total')
df=df.append(sum3)
print('A/B Testing Results')
print()
print(df)
print()
print("Did more users use the search feature in the new design (B)?")
if UsersB>UsersA and s_count>s_count1: 
    print("No")
else:
    print("Yes")
print("Did users search more often in the new design (B)?")
if l_count1>l_count and s_count1<s_count: #l_count,s_count=A,l_count1,s_count1=B 
    print("No")
else:
    print("Yes")
df.to_json("AB Result.json")


