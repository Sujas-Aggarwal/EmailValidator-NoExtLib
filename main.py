def checkEmail(x):
    '''It checks whether email is correct or not using string functions'''
    if len(x)<6: #1) Length should be atleast 6 as g@g.in
        return("Inavlid")
    if x.count("@")!=1 and x.count(".")==0: #2) Count of @ and . in Email 
        return("Inavlid")

    for i in range(len(x)):
        if x[i]!="@" and x[i]!="." and x[i]!="#" and x[i]!="-":
            if x[i]==x[i].upper():
                return("Invalid")
            count=0
        else:
            if i==0 or i==len(x):
                return("Invalid")
            if count==1:
                return("Invalid")
            count=1

            
    return("Valid")
            
    
email = input("Enter Your E-Mail:\n")
print(checkEmail(email))
