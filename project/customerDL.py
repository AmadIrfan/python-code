class customerDL:
    customerlist = []

    def addCustIntoList(temp):
        customerDL.customerlist.append(temp)
        return True

    def DeleteCustFromList(temp):
        customerDL.customerlist.remove(temp)
        return True
