import asyncio
import sys

# First coroutine that calculates the sum of integers
async def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += i
        await asyncio.sleep(4)  # Simulating asynchronous work
    future.set_result(f"First coroutine (sum of N ints) results: {count}")

# Second coroutine that calculates the factorial
async def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
        await asyncio.sleep(4)  # Simulating asynchronous work
    future.set_result(f"Second coroutine (factorial) results: {count}")

# Callback function to handle the result from the futures
def got_result(future):
    print(future.result())

if __name__ == "__main__":
    num1 = int(sys.argv[1])  # First number input (for sum)
    num2 = int(sys.argv[2])  # Second number input (for factorial)

    # Create the event loop
    loop = asyncio.get_event_loop()

    # Create two futures
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Create and schedule tasks
    tasks = [
        first_coroutine(future1, num1),
        second_coroutine(future2, num2)
    ]

    # Add done callbacks to each future
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Run the tasks until completion
    loop.run_until_complete(asyncio.gather(*tasks))

    # Close the event loop
    loop.close()
