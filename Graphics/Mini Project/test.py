
a = {
    "mass": 1,
    "rad": 4
}

def test(obj):
    obj["mass"] = 100
    obj["rad"] = 500
    return

print(a)
test(a)
print(a)