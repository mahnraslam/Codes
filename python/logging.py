import math
m = math.pi
print(m)
import time 
import logging 
fmt = "%(levelname)s== %(asctime):%(message)"
logging.basicConfig( filename="app.log" ,filemode ="a" ,format=fmt, level = logging.INFO,datefmt="%H:%M:%S" )
logging.info("start:%d",2023)
logging.warning("end:%d",2024)