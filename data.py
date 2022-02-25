#!/usr/bin/env python3

class Project:
    def __init__(self, project_line):
        _line = project_line.split(' ')
        self.name = _line[0]
        self.days = int(_line[1])
        self.score = int(_line[2])
        self.best_before = int(_line[3])
        self.num_of_roles = int(_line[4])
        self.needed_skills = {}

    def add_line(self, line):
        line = line.split(' ')
        self.needed_skills[line[0]] = int(line[1])

    def __str__(self):
        return f"{self.name}: days {self.days}, score {self.score}, needed_skills {self.needed_skills}"


class Contributer:
    def __init__(self, contributor_line):
        _line = contributor_line.split(' ')
        self.name = _line[0]
        self.amount_of_skills = int(_line[1])
        self.skills = {}

    def add_line(self, line):
        line = line.split(' ')
        self.skills[line[0]] = int(line[1])

    def get_skill_level(self, skill_name):
        if (skill_name in self.skills):
            return self.skills[skill_name]
        # else
        self.skills[skill_name] = 0
        return 0

    def __str__(self):
        return f"{self.name}: amount of skills {self.amount_of_skills}, skills {self.skills}"
