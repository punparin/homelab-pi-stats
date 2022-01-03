from StatsResponse import*
import psutil

class Stats:
    def __init__(self, temp_file="/sys/class/thermal/thermal_zone0/temp"):
        self.temp_file = temp_file

    def get_cpu_temp(self):
        with open(self.temp_file, encoding = 'utf-8') as f:
            cpu_temp = f.read()
            f.close()
            return round(float(cpu_temp)/1000, 2)

    def get_cpu_percent(self):
        cpu_percent = psutil.cpu_percent()
        return cpu_percent

    def get_memory_used(self):
        memory = psutil.virtual_memory()
        available = round(memory.available/1024.0/1024.0/1024.0,1)
        total = round(memory.total/1024.0/1024.0/1024.0,1)
        memory_used = round(total - available,1)
        return memory_used

    def get_memory_total(self):
        memory = psutil.virtual_memory()
        memory_total = round(memory.total/1024.0/1024.0/1024.0,1)
        return memory_total

    def get_memory_percent(self):
        memory_percent = round(self.get_memory_used() / self.get_memory_total() * 100,2)
        return memory_percent

    def get_disk_used(self):
        disk = psutil.disk_usage('/')
        free = round(disk.free/1024.0/1024.0/1024.0,1)
        total = round(disk.total/1024.0/1024.0/1024.0,1)
        disk_used = round(total - free,2)
        return disk_used

    def get_disk_total(self):
        disk = psutil.disk_usage('/')
        disk_total = round(disk.total/1024.0/1024.0/1024.0,1)
        return disk_total

    def get_disk_percent(self):
        disk_percent = round(self.get_disk_used() / self.get_disk_total() * 100,2)
        return disk_percent

    def get_stats(self):
        response = StatsResponse(
            cpu_temp=self.get_cpu_temp(),
            cpu_percent=self.get_cpu_percent(),
            memory_used=self.get_memory_used(),
            memory_total=self.get_memory_total(),
            memory_percent=self.get_memory_percent(),
            disk_used=self.get_disk_used(),
            disk_total=self.get_disk_total(),
            disk_percent=self.get_disk_percent()
            )

        return response
