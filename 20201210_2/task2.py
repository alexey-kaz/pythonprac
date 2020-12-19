import asyncio

src = eval(input())
Futures = {}
all_tasks = []

Tmp = src.copy()


async def merge(from1, to1, to2):
    Futures[from1, to2] = asyncio.Future()
    if to1 - from1 > 1:
        await Futures[from1, to1]
    if to2 - to1 > 1:
        await Futures[to1, to2]
    i1, i2 = from1, to1
    for i in range(from1, to2):
        await asyncio.sleep(0)
        if i1 < to1 and i2 < to2:
            if src[i1] < src[i2]:
                Tmp[i] = src[i1]
                i1 += 1
            else:
                Tmp[i] = src[i2]
                i2 += 1
        elif i1 < to1:
            Tmp[i] = src[i1]
            i1 += 1
        else:
            Tmp[i] = src[i2]
            i2 += 1
    src[from1:to2] = Tmp[from1:to2]
    Futures[from1, to2].set_result(True)


async def main():
    tasks = []
    j, fin = 1, len(src)
    while j <= fin // 2 + 1:
        for i in range(0, fin, j * 2):
            a = -1
            if i + 2 * j < fin and (i, i + 2 * j) not in all_tasks:
                a = i + 2 * j
            elif (i < fin - 1) and (2 * j < fin) and (i, fin) not in all_tasks:
                a = fin
            if a > 0:
                all_tasks.append((i, a))
                tasks.append(asyncio.create_task(merge(i, i + j, a)))
        j *= 2
    tasks.append(asyncio.create_task(merge(0, j if j < fin else j//2, fin)))
    await asyncio.gather(*tasks)


asyncio.run(main())
print(src)
