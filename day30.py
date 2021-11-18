#class employee :
 #   def _int_(self,fname,lname,salary=1000):
 #       self.fname=fname
 #       self.lname=lname
  #      self.salary=salary
 #   def print_emp(self):
  #      print("firstname:"+self.fname+"lastname:"+self.lname+"salary:"+str(self.salary))
#emp1=employee("hassan","dib",2000)
#emp1.print_emp()
    
class bankaccount:
    def _init_(self,accountnb,name,balance):
        self.accountnb=accountnb
        self.name=name
        self.balance=balance
    def print_bankaccount(self):
        print("accnubmer:"+str(self.accountnb)+"accname:"+self.name+"accbalanc:"+str(self.balance))
bankaccount1=(3,"ahmad",2000)
bankaccount1.print_bankaccount()
 
