import csv
import random

class MainMenu:
    '''This class presents the main menu to the user'''
    def __init__(self, account, portfolio):
        self.account = account
        self.portfolio = portfolio
        
    def pickCommand(self):
        '''This function is the base of the whole program in that it prints the menu to the account holder and calls the 
        appropriate functions/class creation given user input'''
        print("Welcome to your account!")
        trader_joe = Trader(self.portfolio,self.account)
        while True:
            commandInt = "{:<}\n{:<}\n{:<}\n{:<}\n{:<}\n{:<}".format(
                        "1. See current portfolio",
                        "2. Buy Stock",
                        "3. Sell Stock",
                        "4. Edit Account Information",
                        "5. Ask an Expert Trader",
                        "6. QUIT")
            print(commandInt)
            action = input('What would you like to do next? ')
            if action == '1':
                print(self.portfolio)
                self.portfolio.getStockData()
            elif action == '2':
                tickerToBuy = input("Enter the ticker of the stock you'd like to purchase: ")
                sharesToBuy = float(input("Enter the number of shares you would like to purchase: "))
                trader_joe.buyStock(tickerToBuy,sharesToBuy)
            elif action == '3':
                trader_joe.sellStock()
            elif action == '4': 
                print(self.account)
                self.account.changeAcctInfo()
            elif action == '5':
                trader_joe.giveAdvice()
            elif action == '6':
                break
            else:
                print("This is not a valid input, please try again.")
                
    def __str__(self):
        print_string = ''
        print_string += '''
        1. See current portfolio
        2. Buy Stock
        3. Sell Stock
        4. Edit Account Information
        5. Ask an Expert Trader
        6. Quit'''
        return print_string

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.address = "828 Wilshire Blvd. Los Angeles, CA 90007"
        self.bankaccount = "1010103476"
        self.phone = "2146861003"
        
    def changeAcctInfo(self):
        '''This function presents options to the user to change their account information
        '''
        while True:
            commandNum = input("What would you like to change (1-6)? ")
            if commandNum in '123456':
                if commandNum == '1':
                    nameComm = input("Enter new username: ")
                    self.username = nameComm
                elif commandNum == '2':
                    pwComm = input("Enter new password: ")
                    self.password = pwComm
                elif commandNum == '3':
                    addComm = input("Enter new address: ")
                    self.address = addComm
                elif commandNum == '4':
                    baComm = input("Enter new bank account number: ")
                    self.bankaccount = baComm
                elif commandNum == '5':
                    phoneComm = input("Enter new phone number: ")
                    self.phone = phoneComm
                elif commandNum == '6':
                    break
            else:
                print("Invalid entry. Please try again")    
        
    def __str__(self):
        print_string = ''
        passSecret = '*' * len(self.password)
        bankAccountSecret = '******' + self.bankaccount[6:10]
        print_string += "{:<}\n{:<}\n{:<}\n{:<}\n{:<}\n{:<}\n{:<}".format(
                        "Hi " + self.username + "! Here is what we have on file for you:",
                        "1. Username: " + self.username,
                        "2. Password: " + passSecret,
                        "3. Address: " + self.address,
                        "4. Bank Account Number: " + bankAccountSecret,
                        "5. Phone Number: " + self.phone,
                        "6. Back")
        return print_string

class Stock:
    '''This class pulls data from a static CSV to assign attributes to a stock. 
    The portfolio class is then created from multiple Stock instances
    '''
    def __init__(self, ticker, buyPrice, numShares):
        self.ticker = ticker
        self.buyPrice = float(buyPrice)
        self.numShares = float(numShares)
        self.inSP500 = False

        stocks_csv_read = open('constituents-financials_csv.csv', 'rt')
        csvin = csv.reader(stocks_csv_read)
        for row in csvin:
            if row[0] == ticker:
                self.currPrice = float(row[3])
                self.PE = row[4]
                self.EPS = row[6]
                self.marketCap = row[9]
                self.yrHigh = float(row[8])
                self.yrLow = float(row[7])
                self.inSP500 = True

    def __repr__(self):
        print_string = ''
        print_string += "{Name:<15s} {Price:<15.2f} {PE:<15s} {EPS:<15s} {MarkC:<15s} {yrH:<15.2f} {yrL:<15.2f}\n".format(
                        Name=self.ticker, Price=self.currPrice, PE=self.PE, EPS=self.EPS, MarkC=self.marketCap, yrH=self.yrHigh, 
                        yrL = self.yrLow)
        return print_string

class Portfolio():
    def __init__(self,stocks, cash):
        self.stocks = stocks
        self.cash = cash
           
    def getStockData(self):
        '''This function returns the data in the CVS about a particular stock
        '''
        while True:
            commandNum = input("Type in a ticker to see additional information or type 6 to return to main menu: ")
            if commandNum == '6':
                break
            else:
                testStock = Stock(commandNum, 0, 0)
                tStockBool = testStock.inSP500
                if tStockBool == True:
                    print("{Name:<15s} {Price:<15s} {PE:<15s} {EPS:<15s} {MarkC:<15s} {yrH:<15s} {yrL:<15s}".format(
                    Name='Ticker', Price='Current Price', PE='PE Ratio', EPS='EPS', MarkC='Market Cap', yrH='52W High', 
                    yrL = '52W Low'))
                    print(testStock)
                else:
                    print("Invalid ticker. Please enter a stock symbol that is part of the S&P500")    
            
    def __str__(self):
        print_string = ''
        print_string += "{Name:<8s} {CurrPrice:<15s} {BuyPrice:<11s} {GL:<11s} {Shares:<10s}\n".format(
            Name="Ticker", CurrPrice="Current Price", BuyPrice="Buy Price", 
            GL= "G/L Total", Shares="Shares")
        for stock in self.stocks:
            glCalc = (stock.currPrice - stock.buyPrice) * stock.numShares
            glForm = str(round(glCalc,2))
            print_string += "{Name:<8s} {CurrPrice:<15.2f} {BuyPrice:<11.2f} {GL:<11s} {Shares:<10.2f}\n".format(
            Name=stock.ticker, CurrPrice=stock.currPrice, BuyPrice=stock.buyPrice, 
            GL= ("+" + glForm if float(stock.currPrice) > float(stock.buyPrice) else glForm), Shares=stock.numShares)
        print_string += "Cash Balance: ${cash}".format(cash=round(self.cash,2))
        return print_string 

class Trader():
    def __init__(self, clientPort, clientAcct):
        self.clientPort = clientPort
        self.clientAcct = clientAcct
    
    def buyStock(self,tickerToBuy,sharesToBuy):
        '''This function purchases stock by taking in a ticker and num shares as input'''
        stockToBuy = Stock(tickerToBuy,0,sharesToBuy)
        currCash = self.clientPort.cash
        if stockToBuy.inSP500 == False:
            print("Invalid ticker. Please try again")
        else:
            buyAmount = stockToBuy.currPrice * sharesToBuy
            if buyAmount > currCash:
                print("You don't have enough funds for this purchase. Please try again")
            else:
                for stock in self.clientPort.stocks:
                    tick = stock.ticker
                    if tick == tickerToBuy:
                        totalSharesBought = stock.numShares + sharesToBuy
                        totalAmountBought = (stock.numShares * stock.buyPrice) + (stock.currPrice * sharesToBuy)
                        avgPrice = totalAmountBought/totalSharesBought
                        stock.buyPrice = round(avgPrice,2)
                        stock.numShares += sharesToBuy
                        break
                else:
                    stockToBuy.buyPrice = stockToBuy.currPrice
                    self.clientPort.stocks.append(stockToBuy)
                print(f"Purchase of {sharesToBuy} shares of {tickerToBuy} complete! {round(sharesToBuy * stockToBuy.currPrice,2)} has been deducted from your wallet")
                self.clientPort.cash -= buyAmount

    def sellStock(self):
        '''This function sells stock by asking the use what they would like to sell and how much. 
        It will also tell the user how many shares they have available.'''
        while True:
            commandStr = "{firstline:<}\n{secondline:<}".format(firstline = "Enter the ticker of the stock you would like to sell", 
                        secondline = "OR type 6 to return to the main menu: ")
            tickerToSell = input(commandStr)
            if tickerToSell == '6':
                break
            else:
                tick = ''
                for stock in self.clientPort.stocks:
                    tick = stock.ticker
                    curShares = stock.numShares
                    if tick == tickerToSell:
                        print(f"You have {curShares} shares available to sell")
                        sharesToSell = float(input(f"Enter how many shares of {tick} you would like to sell: "))
                        if sharesToSell > curShares:
                            print("You don't have that many shares to sell. Try again.")
                        else:
                            if sharesToSell == curShares:
                                self.clientPort.stocks.remove(stock)
                            else:
                                self.clientPort.cash += sharesToSell * stock.currPrice
                                stock.numShares -= sharesToSell
                            print(f"Sale of {sharesToSell} shares of {stock.ticker} complete! {round(sharesToSell * stock.currPrice,2)} has been added to your wallet")
                        break
                else:   
                    print("That stock is not in your portfolio. Please enter a valid ticker")
    
    def giveAdvice(self):
        '''This function looks through each of the stocks in the CSV and checks if it meets
        certain conditions. It then selects a random stock from the ones returned and proposes it 
        to the user. The user then has the option to accept the advice or not.
        '''
        reccomendedStocks = []
        stocks_csv_read = open('constituents-financials_csv.csv', 'rt')
        csvin = csv.reader(stocks_csv_read)
        next(csvin)
        for row in csvin:
            if float(row[3]) > float(row[8]) and float(row[3]) < float(row[7]):
                if float(row[4]) < 15:
                    if float(row[6]) > 6:
                        stocktoAdd = Stock(row[0], 0, 0)
                        reccomendedStocks.append(stocktoAdd)
        proposedStock = random.choice(reccomendedStocks)
        availAmount = self.clientPort.cash // proposedStock.currPrice
        print("Calculating recommendation...")

        print(f"Using our proprietay algorithm, I recommend purchasing {proposedStock.ticker}")
        print(f"The current price per share is {proposedStock.currPrice}, so you could purchase {availAmount} shares.")
        while True:
            adviceResp = input("Would you like to like to go ahead with this trade advice? (Y/N): ")
            if adviceResp == 'Y':
                self.buyStock(proposedStock.ticker,availAmount)
                break
            elif adviceResp == 'N':
                print("Returning you to the main menu...")
                break
            else:
                print("Invali input. Please enter Y or N")

    def __str__(self):
        print_string = ''
        print_string += f"Hi! My name is Trader Joe, and I'll be executing trades for {self.clientAcct.username}'s account\n"
        print_string += "Please see the current portfolio below:\n"
        print_string += self.clientPort.__str__()
        return print_string


#def main
currAccount = Account("alexdrossos", "mypassword")
stocks = []
stock1 = Stock('MSFT', '180.72', 10)
stock2 = Stock('ACN', '67.55', 30)
stocks.append(stock1)
stocks.append(stock2)
my_portfolio = Portfolio(stocks, 1000)
mm = MainMenu(currAccount, my_portfolio)
mm.pickCommand()