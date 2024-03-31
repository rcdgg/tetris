class A:
    a = 1
    #@classmethod
    def change(self):
        self.a = 3
        print("hello")

b = A()
c = A()
