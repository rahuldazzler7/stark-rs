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


def last_boot():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"


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
