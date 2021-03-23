left_hm = {
    "fond":"enamored",
    "wrath":"anger",
    "diligent":"employed",
    "guide":"usher",
    "outfit":"garb",
}

right_hm = {
    "fond":"averse",
    "wrath":"delight",
    "diligent":"idle",
    "guide":"follow",
    "flow":"jam",
}

def left_join(left_hm, right_hm):
    final = []
    for x in left_hm:
        collector = []
        collector.append(x)
        collector.append(left_hm[x])
        for y in right_hm:
            if y == x:
                collector.append(right_hm[y])
        if x not in right_hm:
            collector.append("Null")
        final.append(collector)
    return final

print(left_join(left_hm, right_hm))
