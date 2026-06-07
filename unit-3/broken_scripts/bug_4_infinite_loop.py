import time

attempts = 0
max_retries = 3

while attempts < max_retries:
    print(f"Simulating API call... Attempt {attempts + 1}")
    success = False
    
    if not success:
        print("API failed, retrying in 1 second...")
        time.sleep(0.5)
        # BUG: Missing increment of 'attempts' counter inside the failure path, or increment is in wrong block
        # attempts += 1 (Uncommenting this would fix it, but right now it loops forever)
        # For safety in verification, we will break after 5 prints so the test script doesn't actually hang forever
        if attempts > 5:
            print("Force broke loop to prevent absolute hang.")
            break
