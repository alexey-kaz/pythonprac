import asyncio

src = eval(input())
tmp = src.copy()
futures = {}


async def merge(from1, to1, to2):
    futures[from1, to2] = asyncio.Future()
    if to1-from1 > 1:
        await futures[from1, to1]
    if to2-to1 > 1:
        await futures[to1, to2]
    i1, i2 = from1, to1
    for i in range(from1, to2):
        await asyncio.sleep(0)
        if i1 < to1 and i2 < to2:
            if src[i1] < src[i2]:
                tmp[i] = src[i1]
                i1 += 1
            else:
                tmp[i] = src[i2]
                i2 += 1
        elif i1 < to1:
            tmp[i] = src[i1]
            i1 += 1
        else:
            tmp[i] = src[i2]
            i2 += 1
    src[from1:to2] = tmp[from1:to2]
    futures[from1, to2].set_result(True)


async def main():
    tasks = []
    j = 1
    while j <= 4:
        for i in range(0, 16, j * 2):
            tasks.append(asyncio.create_task(merge(i, i + j, i + j * 2)))
        j *= 2
    tasks = [asyncio.create_task(merge(0, 8, 16))]
    await asyncio.gather(*tasks)


asyncio.run(main())
print(src)
