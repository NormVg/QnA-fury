from ml import ml_app
import time
print("STARTED")

while True:
  s = time.time()
  ans = ml_app("parents of Bruce Wayne ?")

  e = time.time()
  print(e-s)
  print(ans)
