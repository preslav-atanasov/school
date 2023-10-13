import math
shape = str(input("Molq vuvedete vid na figura [square, rectangle, circle, triangle] "))

# sigurno moje i po-prosto.
if shape == "square":
    length = float(input("Molq vuvedete duljinata na stranata mu "))
    print("Liceto na kvadrata e ravno na {0:.3f}".format(length * length))

elif shape == "rectangle":
    l1 = float(input("Molq vuvedete duljinata na ednata strana "))
    l2 = float(input("Molq vuvedete duljinata na drugata strana "))
    print("Liceto na pravougulnika e ravno na {0:.3f}".format(l1 * l2))

elif shape == "circle":
    rad = float(input("Molq vuvedete radiusa mu "))
    print("Liceto na kruga e ravno na {0:.3f}".format(math.pi * (rad * rad)))

elif shape == "triangle":
    b = float(input("Molq vuvedete duljina na stranata mu "))
    h = float(input("Molq vuvedete duljina na visochinata kum neq "))
    print("Liceto na triugulnika e ravno na {0:.3f}".format(b/2 * h))

else:
    print("Molq vuvedete edna ot dadenite figuri.")
