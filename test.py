import math
u = True


def trying():
    for x in range(0, 90, 1):
        term1 = float(math.sin(float(math.radians(float(x)))) * float(0.49))
        term2 = float(math.cos(float(math.radians(float(x)))) * float(0.49))
        term3 = 0.05625
        pterm1 = term1 - term3
        miu = pterm1 / term2
        return miu

print(trying())