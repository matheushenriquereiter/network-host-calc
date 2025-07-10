ip = input("IP: ").strip()
mask = input("Mask: ").strip()


def getBinary(value):
    dividedValue = value.split(".")

    return ".".join(
        list(map(lambda part: ("00000000" + f"{int(part):b}")[-8:], dividedValue))
    )


ipBinary = getBinary(ip)
maskBinary = getBinary(mask)


def getNetwork(ipBinary, maskBinary):
    network = ""

    for index, ipNumber in enumerate(ipBinary):
        maskNumber = maskBinary[index]

        if ipNumber == ".":
            network += "."
        elif int(ipNumber) & int(maskNumber):
            network += "1"
        else:
            network += "0"

    return network


def getHost(ipBinary, maskBinary):
    host = ""

    for index, ipNumber in enumerate(ipBinary):
        maskNumber = maskBinary[index]

        if ipNumber == ".":
            host += "."
        elif int(ipNumber) == 1 and int(maskNumber) == 0:
            host += "1"
        else:
            host += "0"

    return host


def getConvertedNetworkMask(maskBinary):
    counter = 0

    for maskNumber in maskBinary:
        if maskNumber == "1":
            counter += 1

    return counter


print(f"IP Binário: {ipBinary}")
print(f"IP Máscara: {maskBinary}")

print(f"Network: {getNetwork(ipBinary, maskBinary)}")
print(f"Host: {getHost(ipBinary, maskBinary)}")

print(f"Converted Mask: {getConvertedNetworkMask(maskBinary)}")
