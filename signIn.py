import signUp,os
def signIn():
    accountID=input("请输入注册的ID:")
    password=input("请输入注册时的密码:")
    with open(r"accountID.txt","r") as checkIn1:
         idTmp=checkIn1.readlines()
    with open(r"password.txt","r") as checkIn2:
         pwTmp=checkIn2.readlines()
    id=False
    pw=False
    if "%s\n"%(accountID) in idTmp:
         position = idTmp.index("{:s}\n".format(accountID))
         id=True
         if "%s\n"%(password) ==pwTmp[position]:
            pw=True
    if id & pw == True:
             print("登陆成功")
    else:
        print("用户名未注册或密码错误")

if __name__ == '__main__':
    while(True):
         choose=input("请输入 'login' 或者 'register' 以进行下一步\n")
         if choose == "login":
            signIn()
            input("按任意键以继续")
         elif choose == "register":
              signUp.accountInf.signUp()
              input("按任意键以继续")
         else:
              print("未知指令")

