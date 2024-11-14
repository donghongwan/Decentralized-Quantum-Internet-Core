import time
import psutil

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()

    def get_memory_usage(self):
        """Get the current memory usage in MB."""
        memory_info = psutil.virtual_memory()
        return memory_info.used / (1024 ** 2)  # Convert bytes to MB

    def get_cpu_usage(self):
        """Get the current CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def elapsed_time(self):
        """Get the elapsed time since the monitor started."""
        return time.time() - self.start_time

# Example usage
if __name__ == "__main__":
    monitor = PerformanceMonitor()
    time.sleep(1)  # Simulate some processing
    print(f"Memory Usage: {monitor.get_memory_usage()} MB")
    print(f"CPU Usage: {monitor.get_cpu_usage()}%")
    print(f"Elapsed Time: {monitor.elapsed_time()} seconds")
