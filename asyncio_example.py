import asyncio
async def two ():
    print ('starting two')
    await asyncio.sleep(2)
    print('Hey two')
    return 2

async def four():
    print ('starting four')
    await asyncio.sleep(4)
    print ('hey four')
    return 4

async def main():
    print (await asyncio.gather(two(), four()))

# main()
# RuntimeWarning: coroutine 'main' was never awaited
asyncio.run(main())
