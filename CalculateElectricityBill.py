from tabulate import tabulate
class Electricity:
    def __init__(self, customertype, units):
        self.customertype = customertype
        self.units = units
    
    def calculateBill(self):
        billDetails = []
        if self.customertype == "domestic":
            fixrate = 250
            rpu = 8
            exemption = 600
            if self.units <= exemption:
                bill = fixrate
            else:
                bill = fixrate + (self.units - exemption)*rpu
            if bill >= 10000:
                bill = bill - ((bill*5)/100)
            billDetails = ["Domestic", self.units, fixrate, rpu, bill]
                    
        elif self.customertype == "commercial":
            fixrate = 1000
            rpu = 15
            bill = fixrate + self.units*rpu
            if bill >= 10000:
                bill = bill - ((bill*10)/100)
            billDetails = ["Commercial", self.units, fixrate, rpu, bill]
                  
        return billDetails  

def main():
    customers = [
        Electricity("domestic", 1100),
        Electricity("commercial", 900),
        Electricity("domestic", 500),
        Electricity("commercial", 1200),
    ]   
    header = [["Customer Type", "Units Consumed", "Fixed Rate", "Rate per Unit", "Total Bill (Rs)"]]

    for i in customers:
        header.append(i.calculateBill())

    print(tabulate(header, headers="firstrow", tablefmt="grid"))    

if __name__ == "__main__":
    main()