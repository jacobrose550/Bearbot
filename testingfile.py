import time, sys
print("You run to the vent, and grab a ladder")
for i in range(6):
    time.sleep(0.2)
    x = i % 2
    sys.stdout.write("." * x)
    sys.stdout.flush()
