import statistics

Garbage_by_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def mean_garbage(Garbage_by_time = Garbage_by_time):
    if statistics.mean(Garbage_by_time) > 10:
        return "Yüksek çöp üretimi!"
    elif statistics.mean(Garbage_by_time) > 2:
        return "Az çöp üretimi ve bu miktar gayet iyi!"
    else:
        return "Bu miktar çok az galiba bana yazmayı untuyorsun!"