#participants=[{"first":"tom","last":"white","age":35},{"first":"tedd","last":"smith","age":21},{"first":"sarah","last":"lewis","age":40}]
#for participant in participants:
#    print(participant["first"],"\t",participant["last"],"\t",participant["age"])


f=set(("acer","thomson"))
e=set(("lenovo","del","hp","accent","asus"))
g=set(())
def union1(f,e):
    for x in f:
        g.add(x)
    for y in e:
        g.add(y)
    return g
print(union1(f,e))
