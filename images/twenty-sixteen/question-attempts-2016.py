import dateutil
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


dates = ["01/09/2014", "01/10/2014",  "01/11/2014", "01/12/2014",
         "01/01/2015", "01/02/2015", "01/03/2015", "01/04/2015", "01/05/2015", "01/06/2015", "01/07/2015", "01/08/2015", "01/09/2015", "01/10/2015", "01/11/2015", "01/12/2015",
         "01/01/2016", "01/02/2016", "01/03/2016", "01/04/2016", "01/05/2016", "01/06/2016", "01/07/2016", "01/08/2016", "01/09/2016", "01/10/2016", "01/11/2016", "01/12/2016"]
counts = [10440, 13489, 16402, 12713, 10492, 12879, 13627, 38474, 17720, 35447, 36546, 67262, 528996, 336703, 355140, 197784, 325298, 260543, 251778, 228602, 176054, 124626, 92342, 130041, 975544, 769895, 638281, 336903]
users = [117, 326, 263, 205, 279, 390, 322, 740, 363, 896, 774, 778, 5262, 4535, 4466, 3113, 4349, 3793, 3887, 2876, 2563, 2570, 1929, 1445, 11257, 10750, 10004, 6264]

assignments = [0, 0, 0, 0, 0, 0, 5, 143, 148, 223, 232, 70, 1442, 991, 924, 648, 845, 680, 924, 548, 775, 757, 484, 204, 2763, 2113, 2148, 1227]

datetimes = map(lambda x: dateutil.parser.parse(x, dayfirst=True), dates)

d2015 = datetimes[4:16]
d2016 = datetimes[16:]

c2015 = counts[4:16]
c2016 = counts[16:]

u2015 = users[4:16]
u2016 = users[16:]

a2015 = assignments[4:16]
a2016 = assignments[16:]

plt.xkcd()

#####

plt.figure(figsize=(12, 6))

plt.step(d2016, c2016, linewidth=3, color='#009acd', where='mid', label='mid')

plt.title("Question Attempts per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.03])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10)
plt.tick_params(axis='y', which='major', labelsize=20)

x1 = datetime.datetime(2016, 11, 15)
y1 = (c2016[11] + c2016[10]) / 2.0
plt.gca().annotate("Things get quiet\nat Christmas!", xy=(x1, y1), xycoords='data',
                   xytext=(-130, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=-90,angleB=0"))

x2 = datetime.datetime(2016, 8, 15)
y2 = (c2016[7] + c2016[8]) / 1.25
plt.gca().annotate("Can you tell it's the\nstart of term again?", xy=(x2, y2), xycoords='data',
                   xytext=(-200, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=-90,angleB=30"))

plt.tight_layout()

plt.savefig("question-attempts-2016.png")

plt.show()

####

plt.figure(figsize=(12, 6))

plt.step(d2016, u2016, linewidth=3, color='#fea100', where='mid', label='mid')

plt.title("Users Answering Questions per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.03])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10)
plt.tick_params(axis='y', which='major', labelsize=20)

x3 = datetime.datetime(2016, 10, 1)
y3 = u2016[9] - 0.01 * u2016[9]
plt.gca().annotate("Number of users answering\nquestions doesn't drop,\nnumber of attempts does!", xy=(x3, y3), xycoords='data',
                   xytext=(-350, -100), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=90"))

plt.tight_layout()
plt.savefig("active-users-2016.png")

plt.show()

#####

plt.figure(figsize=(12, 6))

plt.step(d2016, a2016, linewidth=3, color='#509e2e', where='mid', label='mid')

plt.title("Assignments Set per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.03])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10)
plt.tick_params(axis='y', which='major', labelsize=20)


x4 = datetime.datetime(2016, 8, 1)
y4 = a2016[7]
plt.gca().annotate('"Summer holidays?\nNever heard of them!"', xy=(x4, y4), xycoords='data',
                   xytext=(-200, 80), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=90"))

x5 = datetime.datetime(2016, 5, 15)
y5 = a2016[9]
plt.gca().annotate("\"Are you sure this isn't just\nexactly the same graph again?\"", xy=(x5, y5), xycoords='data',
                   xytext=(-250, 40), textcoords='offset points',
                   )

plt.tight_layout()
plt.savefig("assignments-set-2016.png")

plt.show()
