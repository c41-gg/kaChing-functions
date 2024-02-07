from datetime import datetime

def financialstatment(fsname, fstitle, fsyears):#Financial Statement Functions
    yearstart = input("Enter first year of the financial statement:")
    fsheader = [ "#" ," "]
    i = 0
    column = fsyears+2
    while i<fsyears:
        fsheader.append(int(yearstart)+i)
        i += 1
    
    fsname = []
    fsname.append(fstitle)
    fsname.append(fsheader)

    index=1

    fsbody = []                     
    for i in range (0,2):
        new = ["",""]  
        for j in range (2, column):  
            new.append(0)     
        fsbody.append(new)
    
    fstotal = [" ", "End Total"]
    i=0
    j=2
    while j<column:
        currenttotal=0
        for i in range(len(fsbody)):
            currenttotal += int(fsbody[i][j])
            fstotal.append(currenttotal)
            j += 1


    fsname = []       
    fsname.append(fsheader)
    i=0
    for i in range(len(fsbody)):
        fsbody[i][0]=index
        index+=1
        fsname.append(fsbody[i])        
    fsname.append(fstotal)

def ktotal(sysSecSource, sysSecName, sysSecTitle):
    sysSecName = [" ", sysSecTitle]
    column=len(sysSecSource[0])
    i=0
    j=2
    while j<column:
        currenttotal=0
        for i in range(len(sysSecSource)):
            currenttotal += int(sysSecSource[i][j])
            sysSecName.append(currenttotal)
            j += 1

def kadd(sysSecStatement, addIndex, addLabel,addList):
    new = ["",addLabel,]
    for i in range(len(addList)):
        addList[i] = abs(addList[i])
    new.append(addList)
    sysSecStatement.insert(addIndex, new) 


def ksub(sysSecStatement, subIndex, subLabel,subList):
    new = ["",subLabel,]
    for i in range(len(subList)):
        subList[i] = 0-abs(subList[i])
    new.append(subList)
    sysSecStatement.insert(subIndex, new) 

def banksystem(bankName, reserveAmmount): #Bank Functions
    class Bank:
        def _init_(self, accNumber=0, accId="", accHolder="",accType=0, accState=0, accRecord=[]):
            accRecord = (["Date", "Account", "Tansaction", "Amount"])
            self.accNumber = "{0:5f}".format(accNumber)
            self.accId = accId
            self.accHolder = accHolder
            self.accType = accType   
            self.accState= accState
            self.accRecord = accRecord
        debitBalance=0
        creditBalance=0#Credit Account Class Attributes
        creditLimit=0
        creditScore=0
        

    bankIterList = []#Bank Account Iterating List
    debitIterList = [] #Bank Account Iterating List
    creditIterList = []
    lockList = []#For Account Freezing or bafreeze()
    activeList = []#For Account currently active or running

    #Bank Account Functions
    def baccount(accountId, accountHolder, accountType):
        bankIterList.append(accountId.accId)
        activeList.append(accountId.accId)
        accountId.accNumber= bankIterList.index(accountId)
        if (accountType == 0):
            creditIterList.append(accountId)
            accountId = Bank(len(bankIterList), accountId, accountHolder, 0, 1 , 0, "acc" + str(len(bankIterList)))
            accountId.creditLimit=50000
        elif (accountType == 1):
            debitIterList.append(accountId)
            accountId = Bank(len(bankIterList), accountId, accountHolder, 1, 1 , 0, "acc" + str(len(bankIterList)))
        
        def bafreeze(accountId):
            accountId.accState=0
            activeList.remove(accountId)
            lockList.add(accountId)
        def baclose(accountId):
            bankReserve.debitBalance += accountId.debitBalance
            bankIterList.remove(accountId)
            if accountId in activeList:
                activeList.remove(accountId)
            elif accountId in lockList:
                lockList.remove(accountId)  
      

        bankReserve= Bank(0,"bankReserve",bankName, 1, 1, "bankMainRecord") #Bank System Reserves
        bankReserve.debitBalance = reserveAmmount
        bankIterList.append("bankReserve")
    

        #Retail Bank Functions
        def brdeposit(currentDate, accountId, cashAmount):
            if(accountId.accountType == 0):
                accountId.creditbalance -= cashAmount
                accountId.accRecord.add[[currentDate, "System", "Payment", cashAmount]]
            elif(accountId.accountType == 1):
                accountId.debitBalance += cashAmount
                bankReserve.debitBalance += cashAmount
                accountId.accRecord.add[[currentDate, "System", "Deposit", cashAmount]]
            
            
        def brwithdraw(currentDate, accountId, cashAmount):
            if(accountId.accountType == 0):
                if(accountId.creditLimit > accountId.creditBalance+cashAmount):
                    accountId.creditbalance += cashAmount
                    accountId.accRecord.add[[currentDate, "System", "Credit", cashAmount]]
                else:
                    print("Credit Limit Reached")            
            elif(accountId.accountType == 1):
                if(accountId.debitBalance-cashAmount > 0):
                    accountId.debitBalance -= cashAmount
                    bankReserve.debitBalance -= cashAmount
                    accountId.accRecord.add[[currentDate, "System", "Withdraw",cashAmount]]
                else:
                    print("Insufficient Balance")    
                
            
        def brtransfer(currentDate, accountSource, accountTarget, cashAmount):
            accountSource.debitBalance -= cashAmount
            accountTarget.debitBalance += cashAmount
            accountSource.accRecord.add([[currentDate, accountTarget, "Transfer-Withdraw", cashAmount]])
            accountTarget.accRecord.add([[currentDate, accountSource, "Transfer-Deposit", cashAmount]])
        
        payrollIterList = []#Payroll Account Iterating List

        class Employee:
            def _init_(self, companyName="", employeeID="", employeeName="", employeePayRate=0, lifeInsurance=0, healthInsurance=0):
                self.companyName= companyName
                self.employeeID= employeeID
                self.employeeName= employeeName
                self.employeePayRate= employeePayRate
                self.lifeInsurance= lifeInsurance
                self.healthInsurance= healthInsurance

        def bcpayroll(companyId, companyName ):
            payrollIterList.append(companyId)
            companyId = Bank(len(bankIterList), companyId, companyName, 1, 0, reserveAmmount, "acc" + str(len(bankIterList)) + "Payroll" + str(len(payrollIterList)))
            companyName = []

            def bcemployee(companyName, employeeId, employeeBank, employeeName, employeePayRate, lifeInsurancerate, healthInsuranceRate):
                employeeId = Employee(companyName, employeeId, employeeName, employeePayRate, lifeInsurancerate, healthInsuranceRate)
                employeeBank = Bank(len(bankIterList), companyId, employeeName, 1, 0, 0, "acc" + str(len(bankIterList)) + "Payroll" + str(len(payrollIterList)))
                companyName.append(employeeId)
            
                def bcrollout(companyId, employeeBank, employeeHours, employeeDeductions, lifeInsuranceBool, healthInsuranceBool):
                    totalSalary = employeeId.employeePayRate * employeeHours
                    totalDeduction = (lifeInsurancerate*totalSalary if lifeInsuranceBool == 1 else 0 ) + (healthInsuranceRate*totalSalary if healthInsuranceBool == 1 else 0 ) + employeeDeductions
                    totalPay= totalSalary - totalDeduction

                    brtransfer(datetime.now(), companyId, employeeBank, totalPay)




    





        