#!/usr/bin/env python3

import sys
from data import Project, Contributer
from datetime import datetime

_files_dict = {"a": "a_an_example.in.txt", "b": "b_better_start_small.in.txt", "c": "c_collaboration.in.txt",
               "d": "d_dense_schedule.in.txt", "e": "e_exceptional_skills.in.txt", "f": "f_find_great_mentors.in.txt"}
files_to_run_on = []

projects = []
contributors = set()

completed_projects = []

"""
Pseudocode:
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

Optimizations:
1. Store for each skill what is the maximal level in the company, this way we can skip undoable projects. 
2. Store for each person what is the highest skill level he has.
"""


def parse_file(file_path):
    global projects, contributors
    contributors.clear()
    projects = []
    with open(file_path, 'r') as f:
        _line = f.readline().split(' ')
        amount_of_contributors = int(_line[0])
        amount_of_projects = int(_line[1])

        for j in range(amount_of_contributors):
            _line = f.readline()
            c = Contributer(_line)
            contributors.add(c)
            for _ in range(c.amount_of_skills):
                c.add_line(f.readline())

        for j in range(amount_of_projects):
            _line = f.readline()
            projects.append(Project(_line))
            for _ in range(projects[j].num_of_roles):
                projects[j].add_line(f.readline())

    # sort projects by score
    projects = sorted(projects, key=lambda proj: proj.score, reverse=True)

    print(f"projects: {', '.join([str(p) for p in projects])}")
    print(f"contributors: {', '.join([str(c) for c in contributors])}")


def get_first_project():
    """
    Return the first project that can be completed.
    """
    global projects
    temp_contributors = contributors

    for p in projects:
        flag = 0
        chosen_people = []
        for skill_name, level in p.needed_skills.items():
            lowest_level = 1000000000
            lowest_name = ""
            for c in temp_contributors:
                current = temp_contributors[c]
                if current not in chosen_people:
                    if current.get_skill_level(skill_name) >= level:
                        if current.get_skill_level(skill_name) < lowest_level:
                            lowest_level = current.get_skill_level(skill_name)
                            lowest_name = current.name
            if lowest_level == 1000000000:
                flag = 1
                break

        if flag == 0:
            chosen_project = p

            break
        chosen_people.append(lowest_name)

    return chosen_project, chosen_people


def _line_prepender(filename: str, line: str):
    """
    Used for outputting.
    """
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line + '\n' + content)


def work_on_file(path: str):
    output_path = path.rstrip(".in.txt") + \
        f"_out_{datetime.now().strftime('%H:%M:%S')}.txt"
    count_projects = 0
    with open(output_path, 'w') as f:
        while True:
            result = get_first_project()
            if result is None:
                break
            # else
            f.write(f"{result[0]}\n{' '.join(result[1])}\n")
            count_projects += 1

    # prepand the amount of projects planned at the begining of the file
    _line_prepender(output_path, str(count_projects))


def main():
    global files_to_run_on
    # if no arguments were passed
    if len(sys.argv) == 1:
        # run on all files
        files_to_run_on = list(_files_dict.values())
    else:
        for k in sys.argv[1:]:
            files_to_run_on.append(_files_dict[k])
    print(files_to_run_on)

    for f_path in files_to_run_on:
        # parse file
        parse_file(f_path)
        # work on file
        # work_on_file(f_path)


if __name__ == '__main__':
    main()
