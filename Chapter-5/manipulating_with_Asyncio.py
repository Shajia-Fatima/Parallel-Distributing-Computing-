import asyncio

# Define factorial as an async function
async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        await asyncio.sleep(1)  # Simulate asynchronous work
        fact *= i
    print(f"Asyncio Task: Compute factorial({number}) = {fact}")
    return fact

# Define fibonacci as an async function
async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(f"Asyncio Task: Compute fibonacci({i}) = {a}")
        await asyncio.sleep(1)  # Simulate asynchronous work
        a, b = b, a + b
    print(f"Asyncio Task: fibonacci({number}) = {a}")
    return a

# Define binomial coefficient as an async function
async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n + 1 - i) // i
    print(f"Asyncio Task: Compute binomial coefficient({n}, {k}) = {result}")
    await asyncio.sleep(1)  # Simulate asynchronous work
    return result

if __name__ == "__main__":
    # Obtain the event loop and run the tasks
    loop = asyncio.get_event_loop()
    task_list = [
        factorial(10),
        fibonacci(10),
        binomial_coefficient(20, 10)
    ]
    loop.run_until_complete(asyncio.gather(*task_list))
    loop.close()
