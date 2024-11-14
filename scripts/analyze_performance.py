import time
import random

def measure_performance():
    """Measure the performance of quantum communication."""
    start_time = time.time()
    
    # Simulate sending and receiving messages
    for _ in range(100):  # Simulate 100 messages
        time.sleep(random.uniform(0.01, 0.1))  # Simulate processing time

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time for 100 messages: {total_time:.2f} seconds")
    print(f"Average time per message: {total_time / 100:.4f} seconds")

if __name__ == "__main__":
    measure_performance()
