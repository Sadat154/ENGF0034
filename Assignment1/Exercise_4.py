import random

def estimate_pi(precision):
    in_circle = 0
    out_circle = 0

    for i in range(10**precision):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        if ((0.5-x)**2 + (0.5-y)**2)**0.5 <= 0.5:
            in_circle += 1
        else:
            out_circle += 1

    estimation = 4*(in_circle / (in_circle + out_circle))
    return estimation


print(estimate_pi(8))