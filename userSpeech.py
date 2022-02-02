import androidhelper
import time

# import android
droid = androidhelper.Android()
(id, result, error) = droid.recognizeSpeech("Say something")
print(result, error) 


