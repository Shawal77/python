import asyncio

async def main():
    print('Shawal')
    await foo('tim')

async def foo(text):
    print(text)
    await asyncio.sleep(1) #await only in async function
asyncio.run(main())