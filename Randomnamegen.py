#Define list of male prefixes i.g Lord, Sir, Duke
import random
prem=["Lord","Sir","Duke","Prince","King"]
pref=["Lady","Madam","Duchess","Princess","Queen"]
mn=[" Banana", " Orange", " Apple", " Grape", " Cherry"]
num=[" I"," II"," III"," IV"," V"]
name=[]
#Define list of female prefixes 
#Ask for gender
gender=int(input("Whats your gender(enter 1 for male 0 for female): "))
fn=input("What is your first name(add a space): ")
ln=input("What is your last name(add a space): ")
if gender == 0:
    name.append(random.choice(pref)) 
    name.append(fn) 
    name.append(random.choice(mn))
    name.append(ln)
    name.append(random.choice(num))
    name_str="".join(str(x)for x in name) 
    print(name_str)
else:
    name.append(random.choice(prem)) 
    name.append(fn) 
    name.append(random.choice(mn))
    name.append(ln)
    name.append(random.choice(num))
    name_str="".join(str(x)for x in name) 
    print(name_str)
