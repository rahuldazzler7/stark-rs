import platform
import psutil
from datetime import datetime
from common.system_analyser.memomry_byte_scaling import get_size


class System_Information:
    def __init__(self):
        self.uname = platform.uname()

    def operating_sys(self):
        os_type = self.uname.system
        os_release = self.uname.release
        os_version = self.uname.version
        return f"{os_type}{os_release} - {os_version}"

    def machine(self):
        return self.uname.machine

    def hardware_type(self):
        return self.uname.node

    def processor_version(self):
        return self.uname.processor

    def all_info(self):
        os = self.operating_sys()
        mc = self.machine()
        ht = self.hardware_type()
        pv = self.processor_version()
        return {"operating_system": os, "machine": mc, "hardware_type": ht, "processor_version": pv}


class CPU_usage:
    def __init__(self):
        self.cpufreq = psutil.cpu_freq()

    def physical_cores(self):
        return psutil.cpu_count(logical=False)

    def total_cores(self):
        return psutil.cpu_count(logical=True)

    def max_freq(self):
        return f"{self.cpufreq.max:.2f}Mhz"

    def min_freq(self):
        return f"{self.cpufreq.min:.2f}Mhz"

    def current_freq(self):
        return f"{self.cpufreq.current:.2f}Mhz"

    def total_cpu_usage_percentage(self):
        return f"{psutil.cpu_percent()}%"

    def all_info(self):
        pc = self.physical_cores()
        tc = self.total_cores()
        maxf = self.max_freq()
        minf = self.min_freq()
        currentf = self.current_freq()
        percent = self.total_cpu_usage_percentage()
        return {"physical_cores": pc, "total_cores": tc, "max_freq": maxf, "min_freq": minf, "current_freq": currentf, "usage_percent": percent}


def last_boot():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return {"Boot_Time": f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"}


class Virtual_memory:
    def __init__(self):
        self.svmem = psutil.virtual_memory()

    def total_memory(self):
        return get_size(self.svmem.total)

    def available_memory(self):
        return get_size(self.svmem.available)

    def memory_in_use(self):
        return get_size(self.svmem.used)

    def usage_percentage(self):
        return get_size(self.svmem.percent)

    def all_info(self):
        tm = self.total_memory()
        am = self.available_memory()
        mu = self.memory_in_use()
        upercent = self.usage_percentage()
        return {"total_memory": tm, "available_memory": am, "memory_in_use": mu, "usage_percentage": upercent}


class Swap_memory:
    def __init__(self):
        self.swap = psutil.swap_memory()

    def total_memory(self):
        return get_size(self.swap.total)

    def available_memory(self):
        return get_size(self.swap.free)

    def memory_in_use(self):
        return get_size(self.swap.used)

    def usage_percentage(self):
        return get_size(self.swap.percent)

    def all_info(self):
        tm = self.total_memory()
        am = self.available_memory()
        mu = self.memory_in_use()
        upercent = self.usage_percentage()
        return {"total_memory": tm, "available_memory": am, "memory_in_use": mu, "usage_percentage": upercent}


def read_write_stats_of_disk():
    disk_io = psutil.disk_io_counters()
    total_read = f"{get_size(disk_io.read_bytes)}"
    total_write = f"{get_size(disk_io.write_bytes)}"
    return total_read, total_write


class Disk_info:
    all_partitions: list = []

    def __init__(self):
        self.partitions = psutil.disk_partitions()

    def partitiones_usage_info(self):
        for partition in self.partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                p_size = { "mountpoint": partition.device, "type": partition.fstype,
                          "total_size": f"{get_size(partition_usage.total)}",
                          "used": f"{get_size(partition_usage.used)}",
                           "free": f"{get_size(partition_usage.free)}",
                           "percentage": f"{get_size(partition_usage.percent)}",
                          }
                self.all_partitions.append(p_size)
            except PermissionError :
                print("Unable to access the disk")
                continue
        return self.all_partitions

