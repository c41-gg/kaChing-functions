bsyears = int(input("Enter amount of years:"))
yearstart = int(input("Enter first year of the financial statement:"))
column = bsyears+2
index=1

i=0
fsheader = ["",""]
while i<bsyears:
        fsheader.append(yearstart+i)
        i += 1

print(fsheader)

assetheader = ["Asset", ""]
i = 0
while i<bsyears:
    assetheader.append("")
    i += 1

assetbody = []                     
for i in range (0,2):             
    new = ["","test"]                 
    for j in range (2, column):  
        new.append(2)     
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

i=0
for i in range(len(asset)):
    print(asset[i])


#Liability and Equity

#Liability
index += 2

liabilityheader = ["Liability", ""]
i = 0
while i<bsyears:
    liabilityheader.append("")
    i += 1

liabilitybody = []                     
for i in range (0,2):             
    new = ["","test"]                 
    for j in range (2, column):  
        new.append(1)     
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

i=0
for i in range(len(liability)):
    print(liability[i])

#Equity

index += 2

equityheader = ["Equity", ""]
i = 0
while i<bsyears:
    equityheader.append("")
    i += 1

equitybody = []                     
for i in range (0,2):             
    new = ["","test"]                 
    for j in range (2, column):  
        new.append(1)     
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


i=0
for i in range(len(equity)):
    print(equity[i])

totallse=["Total Liabilities and Shareholder's Equity", ""]
for i in range(2, column):
    currenttotal = int(liabilitytotal[i])+int(equitytotal[i])
    totallse.append(currenttotal)
    i += 1

print(totallse)

fsendtotal=["Check", ""]
for i in range(2, column):
    currenttotal = int(assettotal[i])-int(totallse[i])
    fsendtotal.append(currenttotal)
    i += 1

print(fsendtotal)
