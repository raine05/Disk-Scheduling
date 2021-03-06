from matplotlib import pyplot as plt
import math
def run():
    sequence = list(map(int, input("Enter sequence (must be separated by space): ").split()))
    start = int(input("Enter Head Start: "))
    CYLINDER_MAX = 199
    #INPUTS: 98 183 37 122 14 124 65 67

    def LOOK(sequence, start, direction):
        temp = sequence.copy()
        left = []
        right = []
        x = []
        y = []
        x_approx = []
        y_approx = []
        headmovement = 0
        headmovement_approx = 0
        x.append(start)
        if (direction == "Left"):
            for i in temp:
                if i < start:
                    left.append(i)
                else:
                    right.append(i)
            left.sort(reverse=True)
            for i in left:
                x.append(i)
            right.sort()
            for i in right:
                x.append(i)
            x_approx.append(start)
            x_approx.append(min(x))
            x_approx.append(max(x))
            headmovement_approx = abs(start - min(x))
            headmovement_approx = headmovement_approx + abs(min(x) - max(x))
            plt.title("LOOK SCHEDULING ALGORITHM (To the left)")
        elif (direction == "Right"):
            for i in temp:
                if i > start:
                    right.append(i)
                else:
                    left.append(i)
            right.sort()
            for i in right:
                x.append(i)
            left.sort(reverse=True)
            for i in left:
                x.append(i)
            x_approx.append(start)
            x_approx.append(max(x))
            x_approx.append(min(x))
            headmovement_approx = abs(start - max(x))
            headmovement_approx = headmovement_approx + abs(max(x) - min(x))
            plt.title("LOOK SCHEDULING ALGORITHM (To the right)")
        y_approx.append(0)
        size = len(x)
        for i in range(0, size):
            y.append(-i)
            if ((x[i] == max(x) or x[i] == min(x)) and (i != size)):
                y_approx.append(-i)
            if i != (size - 1):
                headmovement = headmovement + abs(x[i] - x[i + 1])
        string = 'Headmovement = ' + str(headmovement) + ' cylinders'
        string2 = str(x)

        plt.plot(x, y, color="violet", markerfacecolor='red', marker='o', markersize=5, linewidth=2, label="LOOK")
        """plt.plot(x_approx, y_approx, dashes=[6, 2], color="blue", markerfacecolor='blue', marker='D', markersize=5,
                 linewidth=0.5, label="Approx LOOK")"""
        plt.ylim = (0, size)
        plt.xlim = (0, CYLINDER_MAX)
        plt.yticks([])
        plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
        plt.text(182.5, -12.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
        plt.show()

    LOOK(sequence,start,"Left")
    LOOK(sequence,start,"Right")