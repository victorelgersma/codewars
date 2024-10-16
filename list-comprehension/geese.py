# list comprehension
# https://stackoverflow.com/questions/5640630/array-filter-in-python

def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [bird for bird in birds if bird not in geese]



if __name__ == "__main__":
    print(goose_filter(["Mallard", "Hook Bill", "African", "Crested",
    "Pilgrim", "Toulouse", "Blue Swedish"]))

