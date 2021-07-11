'''
Classroom_Assignment

Programme for today’s lab classroom:
Given a list of data containing name of Students, marks in 5 subjects.

Ms. Goofy wants to analyse the data. 
Think and help Ms. Goofy
'''
import numpy as np
import matplotlib.pyplot as plt

# Given data to plot
n_groups = 5
Student_1 = (90, 85, 80, 75, 70)
Student_2 = (85, 75, 65, 55, 45)
Student_3 = (45, 35, 35, 35, 45)

# Creating plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.5

rects1 = plt.bar(index, Student_1, bar_width, alpha=opacity, color='b', label='Divya')

rects2 = plt.bar(index + bar_width, Student_2, bar_width, alpha=opacity, color='m', label='Ankit')

rects3 = plt.bar(index + bar_width+ 0.25, Student_3, bar_width, alpha=opacity, color='g', label='Shubham')

plt.xlabel('\nSubjects')
plt.ylabel('Marks')
plt.title('Graph for Ms. Goofy')
plt.xticks(index + bar_width, ('MCA101', 'MCA102', 'MCA103', 'MCA104','MCA105'))
plt.legend()
plt.show()