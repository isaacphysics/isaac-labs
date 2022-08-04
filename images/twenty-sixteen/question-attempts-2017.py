import dateutil
import datetime

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick


dates = ["01/09/2014", "01/10/2014",  "01/11/2014", "01/12/2014",
         "01/01/2015", "01/02/2015", "01/03/2015", "01/04/2015", "01/05/2015", "01/06/2015", "01/07/2015", "01/08/2015", "01/09/2015", "01/10/2015", "01/11/2015", "01/12/2015",
         "01/01/2016", "01/02/2016", "01/03/2016", "01/04/2016", "01/05/2016", "01/06/2016", "01/07/2016", "01/08/2016", "01/09/2016", "01/10/2016", "01/11/2016", "01/12/2016",
         "01/01/2017", "01/02/2017", "01/03/2017", "01/04/2017", "01/05/2017", "01/06/2017", "01/07/2017", "01/08/2017", "01/09/2017", "01/10/2017", "01/11/2017", "01/12/2017"]
counts = [5750, 5652, 9136, 7069,
          6601, 8696, 9396, 32670, 13439, 31133, 33038, 63710, 517642, 321631, 329721, 173757,
          305729, 247510, 234830, 202027, 154171, 109418, 85760, 124473, 945418, 737529, 608279, 313292,
          445216, 356221, 445714, 294867, 197767, 159437, 163274, 228512, 1856179, 1688615, 1639269, 742936]
users = [114, 325, 261, 203,
         275, 386, 319, 733, 359, 890, 768, 774, 5236, 4520, 4449, 3101,
         4337, 3772, 3869, 2861, 2554, 2563, 1923, 1440, 11224, 10733, 9988, 6252,
         7679, 6929, 7891, 4653, 4051, 3340, 3042, 2410, 21195, 21427, 22623, 12501]

assignments = [0, 0, 0, 0,
               0, 0, 5, 143, 148, 221, 232, 70, 1442, 991, 924, 645,
               845, 678, 916, 548, 772, 752, 481, 202, 2751, 2108, 2133, 1216,
               1772, 1668, 2546, 1101, 821, 873, 815, 209, 5368, 4748, 4990, 2494]

password_resets = [0, 0, 0, 0,
                   0, 0, 0, 9, 9, 35, 31, 40, 227, 151, 183, 88,
                   164, 114, 121, 115, 76, 110, 69, 54, 485, 337, 307, 154,
                   263, 201, 261, 140, 144, 126, 149, 126, 963, 891, 931, 426]

registrations = [241, 547, 306, 223,
                 340, 484, 322, 765, 311, 1071, 797, 605, 5582, 1971, 1698, 948,
                 1597, 1609, 1705, 1197, 1039, 1698, 1069, 864, 10298, 3852, 2822, 1530,
                 2428, 2261, 3332, 1844, 1241, 1640, 1953, 1340, 20434, 9545, 9064, 3419]

datetimes = map(lambda x: dateutil.parser.parse(x, dayfirst=True), dates)

d2015 = datetimes[4:16]
d2016 = datetimes[16:28]
d2017 = datetimes[28:40]

c2015 = counts[4:16]
c2016 = counts[16:28]
c2017 = counts[28:40]

u2015 = users[4:16]
u2016 = users[16:28]
u2017 = users[28:40]

a2015 = assignments[4:16]
a2016 = assignments[16:28]
a2017 = assignments[28:40]

p2015 = password_resets[4:16]
p2016 = password_resets[16:28]
p2017 = password_resets[28:40]

r2015 = registrations[4:16]
r2016 = registrations[16:28]
r2017 = registrations[28:40]

plt.xkcd()

#####

plt.figure(figsize=(12, 7))

plt.step(d2017, c2016, linewidth=1, linestyle=':', color='#009acd', where='mid', label='2016')
plt.step(d2017, c2017, linewidth=3, color='#009acd', where='mid', label='2017')

plt.ylim(ymin=0)
plt.xlim((d2017[0], d2017[-1]))

plt.title("Question Attempts per Month", fontsize=22)
plt.gca().title.set_position([0.5, 1.11])

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10, direction='in', bottom=True, top=True)
plt.tick_params(axis='y', which='major', labelsize=20, direction='in', left=True, right=True)

x1 = datetime.datetime(2017, 11, 15)
y1 = (c2017[11] + c2017[10]) / 3.0
#plt.gca().annotate("Things get quiet\nat Christmas!", xy=(x1, y1), xycoords='data',
#                   xytext=(-130, -60), textcoords='offset points',
#                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=-90,angleB=0"))

x2 = datetime.datetime(2017, 8, 15)
y2 = (c2017[7] + c2017[8]) / 1.25
plt.gca().annotate("We saw a huge growth in\nactivity this September!", xy=(x2, y2), xycoords='data',
                   xytext=(-200, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=-90,angleB=30"))

plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2)
plt.tight_layout()

plt.savefig("question-attempts-2017.png")

plt.show()

####

plt.figure(figsize=(12, 7))

plt.step(d2017, u2016, linewidth=1, linestyle=':', color='#fea100', where='mid', label='2016')
plt.step(d2017, u2017, linewidth=3, color='#fea100', where='mid', label='2017')

plt.ylim(ymin=0)
plt.xlim((d2017[0], d2017[-1]))

plt.title("Users Answering Questions per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.11])

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10, direction='in', bottom=True, top=True)
plt.tick_params(axis='y', which='major', labelsize=20, direction='in', left=True, right=True)

x3 = datetime.datetime(2017, 10, 1)
y3 = u2017[9] - 0.01 * u2017[9]
plt.gca().annotate("The number of users answering\nquestions has nearly doubled,\nlikely due to our GCSE book\nwhich launched this year!", xy=(x3, y3), xycoords='data',
                   xytext=(-350, -60), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=90"))

plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2)
plt.tight_layout()
plt.savefig("active-users-2017.png")

plt.show()

#####

plt.figure(figsize=(12, 7))

plt.step(d2017, a2016, linewidth=1, linestyle=':', color='#509e2e', where='mid', label='2016')
plt.step(d2017, a2017, linewidth=3, color='#509e2e', where='mid', label='2017')

plt.ylim(ymin=0)
plt.xlim((d2017[0], d2017[-1]))

plt.title("Assignments Set per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.11])

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10, direction='in', bottom=True, top=True)
plt.tick_params(axis='y', which='major', labelsize=20, direction='in', left=True, right=True)


x4 = datetime.datetime(2017, 8, 1)
y4 = a2017[7]
plt.gca().annotate('Not everyone believes\nin summer holidays!', xy=(x4, y4), xycoords='data',
                   xytext=(-200, 80), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=90"))

x5 = datetime.datetime(2017, 3, 1)
y5 = a2017[2]
plt.gca().annotate("Look out kids!\nMarch seems to be surprise\nextra homework month!", xy=(x5, y5), xycoords='data',
                   xytext=(0, 80), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=90"))

plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2)
plt.tight_layout()
plt.savefig("assignments-set-2017.png")

plt.show()

#####

plt.figure(figsize=(12, 7))

plt.step(d2017, p2016, linewidth=1, linestyle=':', color='#bb2828', where='mid', label='2016')
plt.step(d2017, p2017, linewidth=3, color='#bb2828', where='mid', label='2017')

plt.ylim(ymin=0)
plt.xlim((d2017[0], d2017[-1]))

plt.title("Users Forgetting Their Password per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.11])

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10, direction='in', bottom=True, top=True)
plt.tick_params(axis='y', which='major', labelsize=20, direction='in', left=True, right=True)


plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2)
plt.tight_layout()
plt.savefig("passwords-forgotten-2017.png")

plt.show()

#####

plt.figure(figsize=(12, 7))

plt.step(d2017, r2016, linewidth=1, linestyle=':', color='#944cbe', where='mid', label='2016')
plt.step(d2017, r2017, linewidth=3, color='#944cbe', where='mid', label='2017')

plt.ylim(ymin=0)
plt.xlim((d2017[0], d2017[-1]))

plt.title("Users Registering per Month", fontsize=22)
plt.gca().title.set_position([.5, 1.11])

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10, direction='in', bottom=True, top=True)
plt.tick_params(axis='y', which='major', labelsize=20, direction='in', left=True, right=True)


plt.legend(loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2)
plt.tight_layout()
plt.savefig("users-registering-2017.png")

plt.show()

#####
#
#####

dates2017 = ["01/01/2017", "01/02/2017", "01/03/2017", "01/04/2017", "01/05/2017", "01/06/2017", "01/07/2017", "01/08/2017", "01/09/2017", "01/10/2017", "01/11/2017", "01/12/2017"]
qs_phys_17 = [13.9451211, 16.4428068, 13.9977358, 20.5161394, 20.690382099999997, 19.4518315, 20.2286754, 17.7956914, 13.0886964, 10.7014489, 10.3200048, 11.6579644]
qs_maths_17 = [1.9176764, 3.5873118, 2.1330501, 3.6598047, 3.2233367, 4.5743074, 6.5173814, 4.3698676999999995, 1.7495396, 1.0343934000000001, 0.9522347, 1.9436663]
qs_book_alevel_17 = [79.0467574, 74.1025312, 68.9952172, 55.1203089, 62.5061027, 62.0224239, 53.1373635, 60.4091794, 54.2894829, 46.8999134, 42.7222062, 40.2622786]
qs_book_gcse_17 = [0, 0, 0, 0.0399939, 0.3206693, 2.42012, 11.9507306, 9.1854559, 22.372082, 33.4053667, 39.5801069, 37.9013368]
qs_book_chem_17 = [3.0509201, 3.8628645, 12.5863419, 18.3273827, 12.69917, 6.8821745, 5.0904679, 6.7179312, 6.4021204, 7.3793699, 5.7748334, 7.7976229]

dts2017 = map(lambda x: dateutil.parser.parse(x, dayfirst=True), dates2017)

plt.figure(figsize=(12, 7))
plt.title("Question Attempts by Subject Area in 2017", fontsize=22)
plt.gca().title.set_position([.5, 1.18])

plt.ylim((0, 100))
plt.xlim((dts2017[0], dts2017[-1]))

plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

plt.tick_params(axis='x', which='major', labelsize=18, pad=10, direction='in', bottom=True, top=True)
plt.tick_params(axis='y', which='major', labelsize=20, direction='in', left=True, right=True)

purple_patch = mpatches.Patch(color='#944cbe', label='Physics')
blue_patch = mpatches.Patch(color='#009acd', label='Maths')
burgandy_patch = mpatches.Patch(color='#991846', label='Physics A-Level Book')
light_purple_patch = mpatches.Patch(color='#ff88ff', label='Physics GCSE Book')
red_patch = mpatches.Patch(color='#ef3e36', label='Physical Chemistry A-Level Book')
grey_patch = mpatches.Patch(color='#cccccc', label='Other Questions')

subjects = [qs_phys_17, qs_maths_17, qs_book_alevel_17, qs_book_gcse_17, qs_book_chem_17]
other = [100 - sum([s[i] for s in subjects]) for i in range(12)]
subjects.append(other)

handles = [purple_patch, blue_patch, burgandy_patch, light_purple_patch, red_patch, grey_patch]
colours = ['#944cbe', '#009acd', '#991846', '#ff88ff', '#ef3e36', '#cccccc']

plt.stackplot(dts2017, subjects, colors=colours, edgecolor='#666666')

#x5 = datetime.datetime(2017, 6, 1)
#y5 = 50
#plt.gca().text(x5, y5, "A percentage graph can't show\nthe large increase in number\nof questions in September",
#               bbox=dict(boxstyle="round,pad=0.3", fc="#eeeeee", ec="#eeeeee", lw=1))

plt.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=3)
plt.tight_layout()
plt.savefig("attempts-by-subject-2017.png")

plt.show()
