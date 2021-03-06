from matplotlib import pyplot as plt
import math

def run():
    sequence = list(map(int, input("Enter sequence (must be separated by space): ").split()))
    start = int(input("Enter Head Start: "))
    CYLINDER_MAX = 199
    #INPUTS: 98 183 37 122 14 124 65 67
    def SSTF(sequence, start):
        temp = sequence.copy()

        def next_in_sequence(seq, val):
            diff = 0
            mindiff = math.inf
            nextval = 0
            # print(seq)
            for i in range(0, len(seq)):
                if (seq[i] != val):
                    diff = abs(seq[i] - val)
                    if (diff < mindiff):
                        mindiff = diff
                        nextval = seq[i]
            return nextval

        temp.insert(0, start)
        val = start
        x = []
        y = []
        size = 0
        x.append(start)
        headmovement = 0
        while (len(temp)):
            val = next_in_sequence(temp, val)
            # print(val)
            x.append(val)
            temp.remove(val)
        size = len(x)
        for i in range(0, size):
            y.append(-i)
            if i != (size - 1):
                headmovement = headmovement + abs(x[i] - x[i + 1])
        string = 'Headmovement = ' + str(headmovement) + ' cylinders'
        string2 = str(x)

        plt.plot(x, y, color="violet", markerfacecolor='red', marker='o', markersize=5, linewidth=2, label="SSTF")
        plt.ylim = (0, size)
        plt.xlim = (0, CYLINDER_MAX)
        plt.yticks([])
        plt.title("SHORTEST SEEK TIME FIRST SCHEDULING ALGORITHM")
        plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
        plt.text(182.5, -11.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
        plt.show()

    SSTF(sequence,start)