def perfectnumber(inputnumber):
    factorsum = 0   # sledim za deliteli
    for factor in range(1, inputnumber + 1):
        if inputnumber % factor == 0 and factor != inputnumber:     # ako namerim delitel deto ne e raven na chisloto
            factorsum += factor                                     # go dobavqme kum sbora deliteli
    if inputnumber == factorsum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfectnumber(inputnumber=int(input()))
