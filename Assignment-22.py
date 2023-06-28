class BankAccount:

    @property
    def Acc_num(self):

        print("Account number")

        return self.__acc_num

    @Acc_num.setter
    def Acc_num(self, acc_num):

        self.__acc_num = acc_num

    @property
    def Acc_name(self):

        print("Account holder name")

        return self.__acc_name

    @Acc_name.setter
    def Acc_name(self, acc_name):

        self.__acc_name = acc_name


obj = BankAccount()
obj.Acc_name = "Jain"
obj.Acc_num = 12345
print(obj.Acc_name)
print(obj.Acc_num)
