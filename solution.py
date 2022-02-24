import sys

_files_dict = {"a": "a_an_example.in.txt", "b": "b_better_start_small.in.txt", "c": "c_collaboration.in.txt",
               "d": "d_dense_schedule.in.txt", "e": "e_exceptional_skills.in.txt", "f": "f_find_great_mentors.in.txt"}
files_to_run_on = []


def main():
    global files_to_run_on
    if len(sys.argv) == 1:
        files_to_run_on = list(_files_dict.values())
    else:
        for k in sys.argv[1:]:
            files_to_run_on.append(_files_dict[k])
    print(files_to_run_on)


if __name__ == '__main__':
    main()
