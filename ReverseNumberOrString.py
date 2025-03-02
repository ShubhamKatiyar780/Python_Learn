class Reverse:
    def __init__(self):
        self.var = input("Enter a Name or Number: ")
        self.methods()

    def methods(self):
# -------------------using for loop-----------------------
        string = ""
        for i in self.var:
            # print(i)
            string = i + string
        print(string)
# ----------------using reversed() function--------------------
        string1 = "".join(reversed(self.var))
        print(string1)
# --------------Using Slicing[start, stop, step]--------------
        reversed_string = self.var[::-1]
        print(reversed_string)
# --------------Using Recursion--------------
    def reverse_string(self, s = None):
        if s is None:
            s = self.var
        if len(s) == 0:
            return s
        return s[1] + self.reverse_string(s[ : -1])
        
obj = Reverse()
