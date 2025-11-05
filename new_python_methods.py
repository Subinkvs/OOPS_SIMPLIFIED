class Operation:

    def add(self, *args): # No extra parameters is required, *args can store any number of arguments
        summ = sum(args)
        print(summ)


obj = Operation()
obj.add(5, 6)
obj.add(4, 5, 6)
obj.add(3, 4, 5, 6, 6, 7, 9)

# method overloading
