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
        def _init_(self, accNumber, accId, accHolder,accType, accState, accBalance, accRecord):
            accRecord = (["Date", "Account", "Source", "Tansaction", "Amount"])
            self.accNumber = accNumber
            self.accId = accId
            self.accHolder = accHolder
            self.accType = accType   
            self.accState= accState
            self.accBalance= accBalance
            self.accRecord = accRecord

    bankIterList = ["bankReserve"]#Bank Account Iterating List
    lockList = []#For Account Freezing or bafreeze()
    activeList = []#For Account currently active or running

    #Bank Account Functions
    def baccount(accountId, accountHolder, accountType):
        accountId = Bank(accountId, accountHolder, accountType)
        bankIterList.add(accountId.accId)
        activeList.add(accountId.accId)
        accountId.accNumber= bankIterList.index(accountId)

    bankReserve= Bank(0,"bankReserve",bankName, 0, 1,reserveAmmount) #Bank System Reserves

    def bafreeze(accountId):
        accountId.accState=0
        activeList.remove(accountId)
        lockList.add(accountId)
    def baclose(accountId):
        bankReserve.accBalance += accountId.accBalance
        bankIterList.remove(accountId)
        if accountId in activeList:
            activeList.remove(accountId)
        elif accountId in lockList:
            lockList.remove(accountId)

        del accountId
    
    #Retail Bank Functions
    def brdeposit(currentDate, accountId, cashAmount):
        accountId.accBalance += cashAmount
        bankReserve.accBalance += cashAmount
        accountId.accRecord.add[[currentDate, "System", accountId, cashAmount]]
    def brwithdraw(currentDate, accountId, cashAmount):
        accountId.accBalance -= cashAmount
        bankReserve.accBalance -= cashAmount
        accountId.accRecord.add[[currentDate, "System", accountId, "Withdraw",cashAmount]]
    def brtransfer(currentDate, accountSource, accountTarget, cashAmount):
        accountSource.accBalance -= cashAmount
        accountTarget.accBalance += cashAmount
        accountSource.accRecord.add[[currentDate, "System", accountSource, "Transfer-Withdraw",cashAmount]]
        accountTarget.accRecord.add[[currentDate, "System", accountTarget, "Transfer-Deposit",cashAmount]]





        