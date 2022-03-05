# Creating an Interactive Stock Brokerage in Python

Project Description: This program will mimic the functions of Robinhood or other stock trading platforms. The key objects that will be interacting with each other through the program will be the account holder, an expert trader, and the account holder’s portfolio/wallet. The account holder will have a plethora of options available to him through the user interface, and each of these options will involve the program classes to communicate with each other and stay up to date given whichever operation is chosen. The available operations will be fairly elementary. The account holder will be able to view their current portfolio, housing which stocks they own, how many shares of each stock, and how much cash is available for them to trade. They will be able to buy or sell stock. They will be able to view and edit their account data (i.e. Name, Phone Number, Bank Account info, etc.). And lastly, they will have the option to ask an expert trader for advice. For the first iteration of the program, this method will simply spit out a random stock from the list of ticker that will be imported and whether they should buy or sell. If time and ability permit, I’d like to implement a second iteration that uses a prediction model to generate a recommendation for whether to buy or sell a particular stock.
Program Interaction:
The following options will be shown to the user for them to interact with the program. Default values will be set for things like current portfolio, cash balance, account information, etc.
1. See Current Portfolio 2. Buy Stock
3. Sell Stock
4. Edit Account Information 5. Ask An Expert Trader
There will be subsequent selection options as the user moves through whichever operation they choose. Options 2-5 will be the primary ones where objects have to interact. If the user selects Buy Stock, they will be shown their current cash balance and asked which stock they would like to purchase and how many shares. To do this, we’ll have to create an instance of stock class and pull in the price from the imported data. After factoring in commission fees, the user will be presented with how much their purchase will cost and notified if they do not have enough cash in their wallet to make the purchase. If they choose to proceed, the portfolio class will have to be updated accordingly. A similar process will occur if sell stock is selected as the option.
Alexandra Drossos
Overview of Classes: 1. Stock
a. Purpose – The Stock class will store major indicators of a particular stock, using the imported data to assign its attributes.
b. Methods
i. Print indicators – If the user requests to see
information about a certain stock, this method will print information like the ticker, price, float, market cap, etc.
c. Inputs/Outputs
i. The Stock Class will take the user inputted
               ticker as an input
ii. Based on the ticker, the program will then search
               from the imported data to return the indicators
               described above
2. Account
a. Purpose – The Account class will store important
account information like name, phone number, and bank account information. Primarily the user will be interacting with this class if they want to edit this information, but it will also be displayed in various ways throughout the program.
b. Methods
i. Print_account_info
ii. Setter methods for the various attributes
c. Inputs/Outputs
i. No inputs. Default values will be set when the user begins the program
ii. Outputs will be the values for name, phone number, etc.
3. Portfolio
a. Purpose – Store portfolio data which includes owned
stocks, how many shares, and gain/loss on each.
b. Methods
i. Update_stock: Will update the stocks that are displayed in portfolio. Only called if a new stock is bought or all shares of a currently owned stock are sold
ii. Update_shares: Will update the shares of a certain stock. This will be called if any buying or selling takes place.
c. Inputs/Outputs
i. No inputs. Default values will be set when the
               user begins the program

ii. Outputs will be the a list of lists containing the values described above
4. Wallet
a. Purpose: Store value of cash for account holder b. Methods
i. Add_funds
ii. Withdraw_funds
iii. Check_funds c. Inputs/Outputs
i. No inputs. Default value will be set when the user begins the program
ii. Output is current cash balance
5. Trader
a. Purpose: Execute trades on behalf of account holder b. Methods –
i. Buy_stock: Will update portfolio according to stock amount and share value purchased
ii. Sell_stock: Will update portfolio according to stock amount and share value sold. Will also update cash balance
iii. Generate_advice: For first iteration this will generate a random value from the stock tickers list and suggest either to buy or sell.
c. Inputs/Outputs:
i. No inputs. Default value for name will be set
ii. No outputs
6. Prediction (for second iteration) – not fully worked out
yet.
Complex Features:
The primary complexity for this project will come from the logic
implementation and frequent communication between classes.
