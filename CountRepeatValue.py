class RepeatValue:
    def __init__(self):
        self.length_of_list = int(input("Enter the number of elements: "))
        self.my_list = []
        for i in range(self.length_of_list):
            element = input(f"Enter element {i+1}: ")
            self.my_list.append(element)
        self.countRepeatValue()

    def countRepeatValue(self):
        self.max_count = 0
        self.max_element = []
        for element in self.my_list:
            self.count = self.my_list.count(element)
            if self.count > self.max_count:
                self.max_count = self.count
                self.max_element = [element]
            elif self.count == self.max_count and element not in self.max_element:
                self.max_element.append(element)
        print(f"The maximum number of repetitions is {self.max_count} for the element(s): {self.max_element}")

obj = RepeatValue()