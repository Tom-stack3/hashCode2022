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
    with open("./input/" + file_path, 'r') as f:
        _line = f.readline().split(' ')
        amount_of_contributors = int(_line[0])
        amount_of_projects = int(_line[1])

        for i in range(amount_of_contributors):
            _line = f.readline()
            c = Contributer(_line)
            contributors.add(c)
            for _ in range(c.amount_of_skills):
                c.add_line(f.readline())

        for i in range(amount_of_projects):
            _line = f.readline()
            projects.append(Project(_line))
            for _ in range(projects[i].num_of_roles):
                projects[i].add_line(f.readline())

    # sort projects by score
    projects = sorted(projects, key=lambda proj: proj.score, reverse=True)



def find_by_name(list, _name):
    for p in list:
        if p.name == _name:
            return p
    return None


def _get_first_project():
    """
    Return the first project that can be completed.
    """
    global projects
    temp_contributors = contributors.copy()

    for p in projects:
        chosen_contributors = []
        is_good = True

        for skill_name, needed_level in p.needed_skills.items():
            lowest_contributor = None
            lowest_level = None

            for c in temp_contributors:
                # if the contributor is already working on something else in the project
                if c in chosen_contributors:
                    continue

                c_level = c.get_skill_level(skill_name)
                # if qualified
                if c_level >= needed_level:
                    if lowest_contributor is None or lowest_level > c_level:
                        lowest_contributor = c
                        lowest_level = c_level

            # if no matching contributor was found
            if lowest_contributor is None:
                is_good = False
            else:
                # add the chosen contributor to the list of contributors
                chosen_contributors.append(lowest_contributor)

        # if the project is doable
        if is_good:
            i = 0
            for skill_name, needed_level in p.needed_skills.items():
                # only if the contributor has the exact skill level as required
                if chosen_contributors[i].get_skill_level(skill_name) == needed_level:
                    # upgrade his skill level by one
                    chosen_contributors[i].skills[skill_name] += 1
                i += 1
            projects.remove(p)
            return p, chosen_contributors
    return None


def _line_prepender(filename: str, line: str):
    """
    Used for outputting.
    """
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line + '\n' + content)


def work_on_file(path: str):
    output_path = "./output/" + path.rstrip(".in.txt") + \
        f"_out_{datetime.now().strftime('%H:%M:%S')}.txt"
    count_projects = 0
    with open(output_path, 'w') as f:
        while True:
            result = _get_first_project()
            if result is None:
                break
            # else
            out = ''
            for c in result[1]:
                out += c.name + ' '
            f.write(f"{result[0].name}\n{out.rstrip()}\n")
            count_projects += 1

    # prepend the amount of projects planned at the beginning of the file
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
        work_on_file(f_path)


if __name__ == '__main__':
    main()


"""
Today and only today in Martefei Elektronika!
Filter Aquarium
Kirayim Electric
Nurit Kibuy
Mafsek Pahar
Cabel Tlat Fazi
Toaster Meshulashim
Toaster Meshulashim!
Mefatzel Hashmal Meshulash
Timer
Griller Hasmali
Telefon Lahzanim
Lahzanim
Harzanim
Toaster Meshulashim!
Toaster Meshulashim!
Fuzim
Dagei Hashmal
Fiordim
Toaster Meshulashim!
All on massive sale only until monday!
And from tuesday to next week at 2:00 pm
And from 3:00 pm to the rest of the year!
"""
