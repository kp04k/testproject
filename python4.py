# Purchase Quotation
# Program to calculate final price after all discounts and adding tax for the 
# Electronic Luxury items

# initializing Variables Global
fedaralTax = .18
stateTax = .012
discount = 0
delivaryCarges = 30
basePrice = 0
rewardValue = 0
discountValue = 0
taxAmount = 0
totalValue = 0

# Menu Selection for user
print("\n ** TV Tarrifs ** ")
print("\n 1. 32'inch model TV- 20% Discount    : $ 400.00")
print("\n 2. 44'inch model TV- 25% Discount    : $ 600.00")
print("\n 3. 80'inch Plasma TV- 30% Discount   : $ 1500.00")
print("\n 4. 100'inch ULTRA4K TV- 40% Discount : $ 1800.00\n")

# User inputs for items
totalQuantity = int(input("\nHow many TV's do you like to buy ?\t"))
requiredSize = int(input("\nWhat size would you like (select option 1 2 3 4) ?\t"))
rewardPoints = int(input("\nPlease input your existing reward points or Enter 0 if you dont have rewards ? \n or Enter 12345 if you are staff : \t"))
zipcode = input("\nPlease enter your zipcode ?\t")

# Reward calculation
if(rewardPoints > 0 or rewardPoints == 12345) :
    if(rewardPoints == 12345) :
        rewardValue = 50
    else :
        rewardValue = (rewardPoints ** 2)/5           # Reward points into dollars
else :
    rewardValue = 0


# Base price, Discount calculation
if(requiredSize == 1) :
    basePrice = totalQuantity * 400
    discountValue = (basePrice//100) * 20            # consider floor value Discount
elif(requiredSize == 2) :
    basePrice = totalQuantity * 600
    discountValue = (basePrice//100) * 25            # consider floor value only
elif(requiredSize == 3) :
    basePrice = totalQuantity * 1500
    discountValue = (basePrice//100) * 30            # consider floor value only
elif(requiredSize == 4) :
    basePrice = totalQuantity * 1800
    discountValue = (basePrice//100) * 40            # consider floor value only
else :
    basePrice = 0

# Total price
taxAmount = (basePrice * fedaralTax) + (basePrice * stateTax)    # Tax on basePrice only
totalValue = basePrice + taxAmount + delivaryCarges - discountValue - rewardValue    
# Creating a currency farmat
currency = "${:>9,.2f}"

# Quotation details
print("\n\n\t *** Quotaion summary ***")
print("\n Quntity required :\t",totalQuantity)
print("\n Base Price      : ", currency.format(basePrice))
print("\n Sales Tax       : ", currency.format(taxAmount))
print("\n Discount price  : ", currency.format(discountValue))
print("\n Reward Value    : ", currency.format(rewardValue))
print("\n Delivary charge : ", currency.format(delivaryCarges))
print("\n Total Price     : ", currency.format(totalValue))
print("\n\n ** Thank You/Always at your Service **")

# Program End 
# Thank you
