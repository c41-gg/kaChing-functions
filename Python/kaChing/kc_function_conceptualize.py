def financialstatement(fsmode, fsname, fstitle, fsyears):
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
            
    match fsmode:
        case 1:#Balance Sheet 
            #Asset
            assetheader = ["Asset", ""]
            i = 0
            while i<fsyears:
                assetheader.append("")
                i += 1

            assetbody = []                     
            for i in range (0,2):
                new = ["",""]  
                for j in range (2, column):  
                    new.append(0)     
                assetbody.append(new)

            assettotal = [" ", "Total Asset"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(assetbody)):
                    currenttotal += int(assetbody[i][j])
                assettotal.append(currenttotal)
                j += 1


            asset = []       
            asset.append(assetheader)
            i=0
            for i in range(len(assetbody)):
                assetbody[i][0]=index
                index+=1
                asset.append(assetbody[i])        
            asset.append(assettotal)


            index += 2
            #Liability and Equity

            #Liability

            liabilityheader = ["Liability", ""]
            i = 0
            while i<fsyears:
                liabilityheader.append("")
                i += 1

            liabilitybody = []                     
            for i in range (0,2):             
                new = ["",""]                 
                for j in range (2, column):  
                    new.append(0)     
                liabilitybody.append(new)

            liabilitytotal = [" ", "Total Liability"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(liabilitybody)):
                    currenttotal += int(liabilitybody[i][j])
                liabilitytotal.append(currenttotal)
                j += 1

            liability = []       
            liability.append(liabilityheader)
            i=0
            for i in range(len(liabilitybody)):
                liabilitybody[i][0]=index
                index+=1
                liability.append(liabilitybody[i])
            liability.append(liabilitytotal)

            


            #Equity

            index += 2

            equityheader = ["Equity", ""]
            i = 0
            while i<fsyears:
                equityheader.append("")
                i += 1

            equitybody = []                     
            for i in range (0,2):             
                new = ["",""]                 
                for j in range (2, column):  
                    new.append(0)     
                equitybody.append(new)

            equitytotal = [" ", "Total Equity"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(equitybody)):
                    currenttotal += int(equitybody[i][j])
                equitytotal.append(currenttotal)
                j += 1

            equity = []       
            equity.append(equityheader)
            i=0
            for i in range(len(equitybody)):
                equitybody[i][0]=index
                index+=1
                equity.append(equitybody[i])
            equity.append(equitytotal)


            totallse=["Total Liabilities and Shareholder's Equity", ""]
            for i in range(2, column):
                currenttotal = int(liabilitytotal[i])+int(equitytotal[i])
                totallse.append(currenttotal)
                i += 1


            fsendtotal=["Check", ""]
            for i in range(2, column):
                currenttotal = int(assettotal[i])+int(totallse[i])
                fsendtotal.append(currenttotal)
                i += 1


            for i in range(len(asset)):
                fsname.append(asset[i])
                
            for i in range(len(liability)):
                fsname.append(liability[i])

            for i in range(len(equity)):
                fsname.append(equity[i])

            fsname.append(totallse)
            fsname.append(fsendtotal)

            i=0
            for i in range(len(fsname)):
                print(fsname[i])


        case 2:#Income Statement
             #Revenue
            revenueheader = ["Revenue", ""]
            i = 0
            while i<fsyears:
                revenueheader.append("")
                i += 1

            revenuebody = []                     
            for i in range (0,2):
                new = ["","test"]  
                for j in range (2, column):  
                    new.append(0)     
                revenuebody.append(new)

            revenuetotal = [" ", "Total Revenue"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(revenuebody)):
                    currenttotal += int(revenuebody[i][j])
                revenuetotal.append(currenttotal)
                j += 1


            revenue = []       
            revenue.append(revenueheader)
            i=0
            for i in range(len(revenuebody)):
                revenuebody[i][0]=index
                index+=1
                revenue.append(revenuebody[i])        
            revenue.append(revenuetotal)


            index += 2


            #Expense

            expenseheader = ["Expense", ""]
            i = 0
            while i<fsyears:
                expenseheader.append("")
                i += 1

            expensebody = []                     
            for i in range (0,2):             
                new = ["","test"]                 
                for j in range (2, column):  
                    new.append(0)     
                expensebody.append(new)

            expensetotal = [" ", "Total Expense"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(expensebody)):
                    currenttotal += int(expensebody[i][j])
                expensetotal.append(currenttotal)
                j += 1

            expense = []       
            expense.append(expenseheader)
            i=0
            for i in range(len(expensebody)):
                expensebody[i][0]=index
                index+=1
                expense.append(expensebody[i])
            expense.append(expensetotal)


            #Gains

            index += 2

            equityheader = ["Equity", ""]
            i = 0
            while i<fsyears:
                equityheader.append("")
                i += 1

            equitybody = []                     
            for i in range (0,2):             
                new = ["","test"]                 
                for j in range (2, column):  
                    new.append(0)     
                equitybody.append(new)

            equitytotal = [" ", "Total Equity"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(equitybody)):
                    currenttotal += int(equitybody[i][j])
                equitytotal.append(currenttotal)
                j += 1

            equity = []       
            equity.append(equityheader)
            i=0
            for i in range(len(equitybody)):
                equitybody[i][0]=index
                index+=1
                equity.append(equitybody[i])
            equity.append(equitytotal)

            #Gains

            index += 2

            gainsheader = ["Gains", ""]
            i = 0
            while i<fsyears:
                gainsheader.append("")
                i += 1

            gainsbody = []                     
            for i in range (0,2):             
                new = ["","test"]                 
                for j in range (2, column):  
                    new.append(0)     
                gainsbody.append(new)

            gainstotal = [" ", "Total Gains"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(gainsbody)):
                    currenttotal += int(gainsbody[i][j])
                gainstotal.append(currenttotal)
                j += 1

            gains = []       
            gains.append(gainsheader)
            i=0
            for i in range(len(gainsbody)):
                gainsbody[i][0]=index
                index+=1
                gains.append(gainsbody[i])
            gains.append(gainstotal)

            #Losses

            index += 2

            lossesheader = ["Losses", ""]
            i = 0
            while i<fsyears:
                lossesheader.append("")
                i += 1

            lossesbody = []                     
            for i in range (0,2):             
                new = ["","test"]                 
                for j in range (2, column):  
                    new.append(0)     
                lossesbody.append(new)

            lossestotal = [" ", "Total Losses"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(lossesbody)):
                    currenttotal += int(lossesbody[i][j])
                lossestotal.append(currenttotal)
                j += 1

            losses = []       
            losses.append(gainsheader)
            i=0
            for i in range(len(lossesbody)):
                lossesbody[i][0]=index
                index+=1
                losses.append(lossesbody[i])
            losses.append(lossestotal)


            fsendtotal=["Net Income", ""]
            for i in range(2, column):
                currenttotal = int(revenuetotal[i])+int(expensetotal[i])+int(gainstotal[i])+int(lossestotal[i])
                fsendtotal.append(currenttotal)
                i += 1


            for i in range(len(revenue)):
                fsname.append(revenue[i])
                
            for i in range(len(expense)):
                fsname.append(expense[i])

            for i in range(len(gains)):
                fsname.append(gains[i])
            
            for i in range(len(losses)):
                fsname.append(losses[i])

            fsname.append(fsendtotal)

            i=0
            for i in range(len(fsname)):
                print(fsname[i])

        case 3:#Cash Flow Statement
             #Operating 
            operatingheader = ["Operating Cash Flow", ""]
            i = 0
            while i<fsyears:
                operatingheader.append("")
                i += 1

            operatingbody = []                     
            for i in range (0,2):
                new = ["","test"]  
                for j in range (2, column):  
                    new.append(0)     
                operatingbody.append(new)

            operatingtotal = [" ", "Cash From Operations"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(operatingbody)):
                    currenttotal += int(operatingbody[i][j])
                operatingtotal.append(currenttotal)
                j += 1


            operating = []       
            operating.append(operatingheader)
            i=0
            for i in range(len(operatingbody)):
                operatingbody[i][0]=index
                index+=1
                operating.append(operatingbody[i])        
            operating.append(operatingtotal)


            index += 2


            #Investing

            investingheader = ["Investing Cash Flow", ""]
            i = 0
            while i<fsyears:
                investingheader.append("")
                i += 1

            investingbody = []                     
            for i in range (0,2):             
                new = ["","test"]                 
                for j in range (2, column):  
                    new.append(0)     
                investingbody.append(new)

            investingtotal = [" ", "Cash From Investing"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(investingbody)):
                    currenttotal += int(investingbody[i][j])
                investingtotal.append(currenttotal)
                j += 1

            investing = []       
            investing.append(investingheader)
            i=0
            for i in range(len(investingbody)):
                investingbody[i][0]=index
                index+=1
                investing.append(investingbody[i])
            investing.append(investingtotal)


            #Financing

            index += 2

            financingheader = ["Financing Cash Flow", ""]
            i = 0
            while i<fsyears:
                financingheader.append("")
                i += 1

            financingbody = []                     
            for i in range (0,2):             
                new = ["","test"]                 
                for j in range (2, column):  
                    new.append(0)     
                financingbody.append(new)

            financingtotal = [" ", "Cash From Financing"]
            i=0
            j=2
            while j<column:
                currenttotal=0
                for i in range(len(financingbody)):
                    currenttotal += int(financingbody[i][j])
                financingtotal.append(currenttotal)
                j += 1

            financing = []       
            financing.append(financingheader)
            i=0
            for i in range(len(financingbody)):
                financingbody[i][0]=index
                index+=1
                financing.append(financingbody[i])
            financing.append(financingtotal)

            
            fsendtotal=["Closing Cash Balance", ""]
            for i in range(2, column):
                currenttotal = int(operatingtotal[i])+int(investingtotal[i])+int(financingtotal[i])
                fsendtotal.append(currenttotal)
                i += 1


            for i in range(len(operating)):
                fsname.append(operating[i])
                
            for i in range(len(investing)):
                fsname.append(investing[i])

            for i in range(len(financing)):
                fsname.append(financing[i])

            fsname.append(fsendtotal)

            i=0
            for i in range(len(fsname)):
                print(fsname[i])
            
            
            

financialstatement(3,"c41balsheet","C41 Graphics Co. 2023 Bal. Sheet", 5)

print("yadaydaydaydya \t yadadyaydayda")

