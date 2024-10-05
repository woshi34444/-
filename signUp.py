
class accountInf:
      def __init__(self,accountID=None,accountPassword=None):
          self.accountID=accountID
          self.accountPassword=accountPassword
      @classmethod
      def signUp(cls):
          tmp = accountInf
          tmp.accountID = input("请输入ID:")
          tmp.accountPassword = input("请输入密码:")

          with open(r"accountID.txt", "r") as checkIn2:
              __listTmp = checkIn2.readlines()
          with open(r"accountID.txt", "a") as checkIn2:
              if ("{:s}\n".format(tmp.accountID) in __listTmp):
                  print("用户名已注册")
              else:
                  checkIn2.write("%s\n" % (tmp.accountID))
                  print_hi(tmp.accountID)
                  with open(r"password.txt", "a") as checkIn1:
                       checkIn1.write("%s\n" % (tmp.accountPassword))
def print_hi(name):
    print(f'Hi, {name}')

def test():
    with open("accountID.txt", "r") as checkIn1:
        listTmp = checkIn1.readlines()
    print(listTmp)

