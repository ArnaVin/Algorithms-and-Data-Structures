def binary_search(data, target, low, high):
# Return True if target is found in indicated portion of a Python list.

    if low > high:
        # interval is empty: No match
        return False

    else:
        mid = (low+high)//2
        if target == data[mid]:
            # Found a match
            return True

        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)

if __name__ == "__main__":

    test = [2,18,41,55,53,70,99]
    target = 41
    print(binary_search(test, target, 0, len(test)-1))
