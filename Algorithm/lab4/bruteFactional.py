
#FRACTIONAL KNAPSACK with brute force
def FractionalBrute(length, data, size, init):
    if init == length or size <= 0:
        return 0
    
    if data[init]["weight"] <= size:
        profit_including_data = data[init]["profit"] + FractionalBrute(len(data), data, size - data[init]["weight"], init+1)
        profit_excluding_data = FractionalBrute(len(data), data, size, init+1)
    else:
        profit_including_data = data[init]["profit"] * (size / data[init]["weight"])
        profit_excluding_data = FractionalBrute(len(data), data, size, init+1)
    return max(profit_including_data, profit_excluding_data)
