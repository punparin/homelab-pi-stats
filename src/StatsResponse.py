class StatsResponse:
    def __init__(self, cpu_temp, cpu_percent, memory_used, memory_total, memory_percent, disk_used, disk_total, disk_percent):
        self.cpu_temp = cpu_temp
        self.cpu_percent = cpu_percent
        self.memory_used = memory_used
        self.memory_total = memory_total
        self.memory_percent = memory_percent
        self.disk_used = disk_used
        self.disk_total = disk_total
        self.disk_percent = disk_percent
