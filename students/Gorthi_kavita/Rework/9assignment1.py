list_data =[]   #this is donar list adding  to the list
allist =[]   #to keep track how many times the donar name in the list
unique_name = []  # unique donar names
list_sum = []     # donar names and total amount and number of times donated
list_add =[]

class donar():
    def __data(self,name,amount):
        self.donarname = name
        self.donaramount = amount
        alldata = (name,amount,1)
        data = (name)
        list_data.append(alldata)
        allist.append(data)

    def donarname(self):
        self.__data("mike",80)
        self.__data("ketty",175)
        self.__data("john hoop",45)
        self.__data("ravi",780)
        self.__data("david",123)
        self.__data("bratte",45)
        self.__data("mike", 180)
        self.__data("mike", 800)
        self.__data("david",100)

    def  countname(self):
        import collections
        k = allist
        counter = collections.Counter(k)       #how many times the donar name in the donation list
        uniname = set(allist)
        for i in uniname:
            unique_name.append(i)          #this is unique names of the donar

        for i in unique_name:        #this will find the sum of the donation amount and number of times donated
            sum = 0
            times = 0
            for j in list_data:
                 if(i == j[0]):
                    sum = sum+j[1]
                    times = times+j[2]
                    all =(j[0],sum,times)
                    if(counter[i] == times):
                      list_sum.append(all)

    def report(self):
        print("+----------------------------+------------------+-------------------+-------------------+")
        print("|     Donar Name             |  Total given     | Number of gifts   |    Average gift   |")
        print("+----------------------------+------------------+-------------------+--------------------")

        for i in list_sum:
            name = i[0].upper()
            total = '$' + str(i[1])
            avg = i[2]
            k = int(i[1] / i[2])
            avggift = '$' + str(k)
            print("{: >20} {: >20} {: >20} {: >20}".format(name, total, avg, avggift))

    def sendmail(self, listm):
        listd = listm
        for i in listd:
              a = i[0].upper()
              b = '$' + str(i[1])
              file = open("{}"".txt".format(a), 'a+')
              file.write("  Dear  ""{}".format(a))
              file.write("\n")
              file.write(" \n")
              file.write("    Thank you for your very kind donation of ")
              file.write("{}".format(b))
              file.write("\n")
              file.write("\n")
              file.write("    It will be used for very good cause.")
              file.write("\n")
              file.write("           Sincerely, \n")
              file.write("          -The Team  ")
              file.close

class  donarreport(donar):

   def  __init__(self):
        print("Menu:")
        print("1.Send thank you mail")
        print("2.Create report")
        print("3.Add donars")
        print("4.quit")
        i = int(input("enter your choice 1 or 2 or 3 or 4:       "))
        if (i == 2):
            s = donar()
            s.donarname()
            s.countname()
            s.report()
        elif(i == 1):
            s = donar()
            s.donarname()
            s.countname()
            l = list_sum
            s.sendmail(l)
            print("The Thank you mail has been send to the list of donars")
            for i in l:
                print(i[0].upper())


        elif(i == 3):
            self.add_donar()
            s = donar()
            s.donarname()
            s.countname()
            s.report()


   def  add_donar(self):
       n = input("enter name   ")
       m = int(input("enter amount to donate   "))
       c = (n, m, 1)
       d = (n)
       s = donar()
       list_add.append(c)
       list_data.append(c)
       allist.append(d)
       print("do you want to add any donars  ")
       k = input("enter y/n  ")
       if (k == 'y' or k == 'Y'):
           self.add_donar()
       elif(k == 'n' or k == 'N'):
           s.sendmail(list_add)


e = donarreport()

