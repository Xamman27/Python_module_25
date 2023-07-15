class Student():

    def __init__(self, surnname, name, group_num, mark_list):
        self.surnname = surnname
        self.name = name
        self.group_num = group_num
        self.mark_list = list(mark_list)

    def average_score(self):
        return sum(self.mark_list) / len(self.mark_list)


ivanov = Student("ivanob", 'Ivan', 1, [5, 4, 3, 5, 3])
petrov = Student("petrov", 'petr', 1, [3, 4, 3, 3, 3])
print(ivanov.average_score())
