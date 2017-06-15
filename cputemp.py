class CpuTemp:
    def read(self):
       f = open("/sys/class/thermal/thermal_zone0/temp", "r")
       val = float(f.read())
       val = val / 1000.0
       return "{0:.2f}".format(val)
