def coinChange(coins, amount):
        
    coin_count = 0
    
    coins.sort()
    print(coins)
    index = len(coins)-1
    denomination = coins[index]
    
    while amount > 0:
        if amount >= denomination:
            print("subtracting" ,denomination, amount)
            amount -= denomination
            coin_count += 1
        
        else:
            if index > 0:
                index -= 1
                denomination = coins[index]
            else:
                return -1
        
    return coin_count

coinChange([186,419,83,408], 6249)
    