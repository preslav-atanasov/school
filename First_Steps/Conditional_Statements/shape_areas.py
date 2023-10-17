from math import pi
shape = str(input("Molq vuvedete vid na figura [square, rectangle, circle, triangle] "))

# sigurno moje i po-prosto.
if shape == "square":
    length = float(input("Molq vuvedete duljinata na stranata mu "))
    area_sq = length * length
    print("Liceto na kvadrata e ravno na {:.3f}".format(area_sq))

elif shape == "rectangle":
    l1 = float(input("Molq vuvedete duljinata na ednata strana "))
    l2 = float(input("Molq vuvedete duljinata na drugata strana "))
    area_rec = l1 * l2
    print("Liceto na pravougulnika e ravno na {:.3f}".format(area_rec))

elif shape == "circle":
    rad = float(input("Molq vuvedete radiusa mu "))
    area_cir = pi * (rad * rad)
    print("Liceto na kruga e ravno na {:.3f}".format(area_cir))

elif shape == "triangle":
    b = float(input("Molq vuvedete duljina na stranata mu "))
    h = float(input("Molq vuvedete duljina na visochinata kum neq "))
    area_tri = b/2 * h
    print("Liceto na triugulnika e ravno na {:.3f}".format(area_tri))

else:
    print("Molq vuvedete edna ot dadenite figuri.")
