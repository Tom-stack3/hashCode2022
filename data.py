class Project:
    def __init__(self, project_line):
        _line = project_line.split(' ')
        self.name = _line[0]
        self.days = _line[1]
        self.best_before = _line[2]
        self.num_of_roles = _line[3]
        self.needed_skills = {}

    def add_line(self, line):
        line = line.split(' ')
        self.needed_skills[line[0]] = line[1]

    def __str__(self):
        return self.name


class Contributer:
    def __init__(self, contributor_line):
        _line = contributor_line.split(' ')
        self.name = _line[0]
        self.amountOfSkills = _line[1]
        self.skills = {}

    def add_line(self, line):
        line = line.split(' ')
        self.skills[line[0]] = line[1]

    def get_skill_level(self, skill_name):
        if (skill_name in self.skills):
            return self.skills[skill_name]
        # else
        self.skills[skill_name] = 0
        return 0

    def __str__(self):
        return self.name
