def accumulate(seq,op):
    res = []
    for i in seq:
        res.append(op(i))
    return res