#!/usr/bin/env python3

import sys
from data import Project, Contributer

_files_dict = {"a": "a_an_example.in.txt", "b": "b_better_start_small.in.txt", "c": "c_collaboration.in.txt",
               "d": "d_dense_schedule.in.txt", "e": "e_exceptional_skills.in.txt", "f": "f_find_great_mentors.in.txt"}
files_to_run_on = []

projects = []
contributors = []

completed_projects = []

"""
sort all projects by score
while True:
    1. pop out the first project that can be completed
    2. for each skill desired:
       2.1. assign the worst fitting person (later on can track who is available and who is not and prefer free contributors)
    3. add project to completed projects list
    4. update skills of the contributors
    5. go back to 1.
    6. if got to the end of the projects list:
       6.1 break
"""


def parse_file(file_path):
    global projects, contributors
    contributors = []
    projects = []
    with open(file_path, 'r') as f:
        _line = f.readline().split(' ')
        amountOfContributors = int(_line[0])
        amountOfProjects = int(_line[1])

        for j in range(amountOfContributors):
            _line = f.readline()
            contributors.append(Contributer(_line))
            for _ in range(contributors[j].amount_of_skills):
                contributors[j].add_line(f.readline())

        for j in range(amountOfProjects):
            _line = f.readline()
            projects.append(Project(_line))
            for _ in range(projects[j].num_of_roles):
                projects[j].add_line(f.readline())

    # sort projects by score
    projects = sorted(projects, key=lambda proj: proj.score, reverse=True)

    =========

    print(f"projects: {', '.join([str(p) for p in projects])}")
    print(f"contributors: {', '.join([str(c) for c in contributors])}")


def main():
    global files_to_run_on
    if len(sys.argv) == 1:
        files_to_run_on = list(_files_dict.values())
    else:
        for k in sys.argv[1:]:
            files_to_run_on.append(_files_dict[k])
    print(files_to_run_on)

    for f_path in files_to_run_on:
        # work on file
        parse_file(f_path)


if __name__ == '__main__':
    main()
