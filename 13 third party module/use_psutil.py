import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

print(psutil.virtual_memory())
print(psutil.swap_memory())

print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())

print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
print(psutil.net_connections())

print(psutil.pids())
p = psutil.Process(4)
print(p.name())
