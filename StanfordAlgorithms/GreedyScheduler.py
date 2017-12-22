
def Schedule(jobs, mode):
    """
    Inputs:
        jobs: a list of tuples (weight, length)

    """
    # return the indices, sorted by (weight - length)
    if mode == 1:
        order = sorted(range(len(jobs)), key=lambda k: jobs[k][0] - jobs[k][1] + jobs[k][0]*1e-8)
    elif mode == 2:
        order = sorted(range(len(jobs)), key=lambda k: jobs[k][0] / jobs[k][1])

    weighted_sum = 0
    time = 0
    for i in order[::-1]:
        time += jobs[i][1]
        weighted_sum += jobs[i][0]*time

    return weighted_sum


def alg(FNAME):
    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        N = int(lines[0].strip())
        jobs = []
        for line in lines[1:]:
            weight, length = [int(x) for x in line.split()]
            job = (weight, length)
            jobs.append(job)

    res1 = Schedule(jobs, mode=1)
    res2 = Schedule(jobs, mode=2)

    return [res1, res2]

print(alg("3.1Greedy.txt"))
