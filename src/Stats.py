from StatsResponse import*

class Stats:
    def __init__(self, temp_file="/sys/class/thermal/thermal_zone0/temp"):
        self.temp_file = temp_file

    def get_cpu_temp(self):
        with open(self.temp_file, encoding = 'utf-8') as f:
            cpu_temp = f.read()
            return round(float(cpu_temp)/1000, 2)

    def get_stats(self):
        cpu_temp = self.get_cpu_temp()
        response = StatsResponse(
            cpu_temp=cpu_temp
            )

        return response
