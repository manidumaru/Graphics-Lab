
#BRTUE FORCE
def _01knapsackBrute(length, data, size, init):
    if init == length or size <= 0:
        return 0
    # recursive calculation of profit
    if data[init]["weight"] <= size:
        profit_including_data = data[init]["profit"] + _01knapsackBrute(len(data), data, size - data[init]["weight"], init+1)
        profit_excluding_data = _01knapsackBrute(len(data), data, size, init+1)

        return max(profit_including_data, profit_excluding_data)
    else:
        profit_excluding_data = _01knapsackBrute(len(data), data, size, init+1)
        return profit_excluding_data

