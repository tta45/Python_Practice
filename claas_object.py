class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{p1.name} {p1.age}"
       
        
p1 = person("Mehedi", 25)

print(p1)
