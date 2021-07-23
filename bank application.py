import sys,os

#username,pwd,bal
class Bank:

    def __init__(self):
        
        #self.b = 0
        self.data = {}
        self.fname = 'data.txt'

        if os.path.exists(self.fname):
            self.b = int(self.read_data())
        else:
            self.b = 0

    def read_data(self):
        f1 = open(self.fname,'r')
        d = f1.readlines()
        f1.close()

        return d[-1][0]
        
    def screen(self):
        print('1:create_ac')
        print('2:Login')
        print('3:exit')

        ch = int(input('enter choice:'))
        return ch

    def create_ac(self):

        u = input('enter username:')
        p= input('enter password:')
        #p = getpass.getpass()
        #p = stdiomask.getpass()

        
        self.data[u] = {u:p}           #{1:{u:'q','p':'12',status='active'}}

    def login(self):
        u = input('enter username:')
        p = input('enter password:')
        #p = stdiomask.getpass()
        #p = getpass.getpass()

        for i in self.data:
            
            if u in i:
                if p==self.data[u][u]:
                    self.data[u]['status'] = 'active'
                    return True
                else:
                    print('pwd not match')

            else:
                print('username not found')

    def second_screen(self):
        print('1:deposit')
        print('2:withdraw')
        print('3:balance')
        print('4:logout')

        c = int(input('enter choice:'))
        return c
    
    def save_bal(self,b):
        f = open(self.fname,'a')
        for i in self.data.values():
            if i['status'] =='active':
                p1 = list(i.items())[0]
                #print(p1)
                f.write(p1[0]+','+p1[1]+','+str(b))
                f.write('\n')
        f.close()
        
    def deposit(self):
        a = int(input('enter amount:'))
        self.b = self.b + a

    def withdraw(self):
         a = int(input('enter amount:'))
         self.b = self.b - a

    def check_balance(self):
        print('balance is {}'.format(self.b))
        

bk = Bank()

while True:
    m = bk.screen()

    if m==1:
        bk.create_ac()

    elif m==2:
        k = bk.login()
        if k==True:
            while True:
                z = bk.second_screen()
                if z==1:
                    bk.deposit()
                elif z==2:
                    bk.withdraw()
                elif z==3:
                    bk.check_balance()
                else:
                    bk.save_bal(bk.b)
                    break
    else:
        sys.exit()