import androidhelper
import time

droid = androidhelper.Android()
dt = 100 #100ms between sensings
endTime = 3000 #sample for 3000ms
timeSensed=0
droid.startSensingTimed(2,dt) 
print("Hello User")
while timeSensed <= endTime:
    print(droid.sensorsReadAccelerometer().result)
    time.sleep(dt/1000.0)
    timeSensed+=dt
droid.stopSensing()