def iou(m1, m2):
    intersection = (m1 & m2).sum()
    union = (m1 | m2).sum()
    return intersection / union

def io1(m1, m2):
    intersection = (m1 & m2).sum()
    return intersection / m1.sum()

def prec(gtruth, retr):
    return io1(retr, gtruth)

def recall(gtruth, retr):
    return io1(gtruth, retr)

def f1(gtruth, retr):
    tp = (gtruth & retr).sum()
    fn_fp = (gtruth ^ retr).sum()
    return 2*tp / (2*tp + fn_fp)

