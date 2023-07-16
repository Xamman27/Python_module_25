class Student():

    def __init__(self, surnname, name, group_num, mark_list):
        self.surnname = surnname
        self.name = name
        self.group_num = group_num
        self.mark_list = list(mark_list)
        self.aver_score = self.average_score()

    def average_score(self):
        return sum(self.mark_list) / len(self.mark_list)

    def info(self):
        print(self.surnname, self.name)


ivanov = Student("Ivanov", 'Ivan', 1, [2, 2, 2, 2, 2])
petrov = Student("Petrov", 'Petr', 2, [3, 4, 3, 3, 3])
kuzmin = Student("Kuzmin", 'Valera', 1, [5, 5, 5, 5, 5])
minin = Student("Minin", 'Aleksei', 1, [5, 5, 5, 5, 5])
svetlova = Student("Svetlova", 'Nina', 2, [5, 5, 5, 5, 5])
romanova = Student("Romanova", 'Elena', 1, [3, 5, 5, 5, 5])
romanov = Student("Romanov", 'Igor', 1, [3, 3, 3, 3, 3])
belova = Student("Belova", 'Svetlana', 2, [5, 3, 3, 5, 3])
sidorov = Student("Sidorov", 'Stanislav', 2, [5, 3, 3, 5, 3])
smirnov = Student("Smirnov", 'Aleksei', 2, [5, 3, 3, 4, 3])

students_list = [ivanov, petrov, kuzmin, minin, svetlova, romanova, romanov, belova, sidorov, smirnov]
students_list.sort(key=lambda x: x.aver_score, reverse=True)
[i.info() for i in students_list]