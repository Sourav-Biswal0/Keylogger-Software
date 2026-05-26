# -----------------------------------------------------
# ADVANCED KEYLOGGER SIMULATION (SAFE & EDUCATIONAL)
# -----------------------------------------------------
# Features Added:
# ✔ Timestamp for every key
# ✔ Save logs to a file
# ✔ Typing speed calculation
# ✔ Most used keys report
# -----------------------------------------------------

import time
from collections import Counter

typed_keys = []      # list of (key, timestamp)
start_time = None    # typing session start time


def start_simulation():
    global start_time
    print("----- KEYLOGGER SIMULATION STARTED -----")
    print("Type keys (type 'exit' to stop)\n")

    start_time = time.time()  # record start time

    while True:
        key = input("Enter a key: ")

        if key.lower() == "exit":
            break
        
        timestamp = time.strftime("%H:%M:%S")
        typed_keys.append((key, timestamp))

        print(f"Captured: '{key}' at {timestamp}")

    print("\n----- SIMULATION STOPPED -----")
    show_output()
    save_to_file()


def show_output():
    print("\n----- KEYLOGGER OUTPUT -----")
    
    for key, time_stamp in typed_keys:
        print(f"Key: {key}     Time: {time_stamp}")

    total_keys = len(typed_keys)
    total_time = time.time() - start_time
    kpm = (total_keys / total_time) * 60 if total_time > 0 else 0

    print("\nTotal Keys Captured:", total_keys)
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Typing Speed: {kpm:.2f} keys per minute")

    # Most used keys
    key_list = [k for k, _ in typed_keys]
    freq = Counter(key_list)

    print("\nMost Used Keys:")
    for key, count in freq.most_common():
        print(f"'{key}' used {count} times")

    print("-----------------------------------------")


def save_to_file():
    filename = "simulated_keylog.txt"
    with open(filename, "w") as file:
        file.write("SAFE KEYLOGGER SIMULATION LOG\n\n")
        for key, time_stamp in typed_keys:
            file.write(f"{key} , {time_stamp}\n")

    print(f"\n✔ Logs saved to file: {filename}")


# Run the simulation
start_simulation()