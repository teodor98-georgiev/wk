# OK!
# 3. Check if a user-given username and password match predefined values.
preDefinedUser="elonmusk"
preDefinedPass="pass123"

def userAuthentication(realUser, realPass, pUser,pPass):   #name of parameters must be != from the variables defined at top !!!!
    if pUser == realUser and pPass == realPass:
       #print("requirements respected, move on")
       return True
    else:
        return False
        #print("try to invent something else or you will be fired")

inpUser = input("enter username:")
inpPass = input("enter pass:")

result = userAuthentication(preDefinedUser, preDefinedPass, inpUser,inpPass)
print(result)

