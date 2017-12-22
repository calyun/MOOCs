
import queue

def HuffmanCodeMaxLength(weights):
    """
    Uses heap to store weights and lengths of Huffman codes

    Stores in q: (frequency, code length, isLeaf, distanceFromLastLeaf/height)
    """
    q = queue.PriorityQueue()
    for w in weights:
        q.put((w, 0, True, 0))

    while True:
        left = q.get()
        right = q.get()

        parent_weight = left[0] + right[0]
        parent_height = max(left[1], right[1]) + 1
        parent_distLeaf = min(left[3], right[3]) + 1
        parent = (parent_weight, parent_height, False, parent_distLeaf)

        # Parent is parent of last two nodes; it is the Top node
        if q.empty():
            break
        else:
            q.put(parent)

    return parent[1], parent[3]



def alg(FNAME):

    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        N = int(lines[0].strip())
        weights = [int(x.strip()) for x in lines[1:]]

    res1, res2 = HuffmanCodeMaxLength(weights)
    return [res1, res2]


print(alg("3.3Huffman.txt"))
