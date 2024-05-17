import re, time
file_path = 'gamestate'
print("请输入两个星系的id来交换它们的位置，你可以通过群星自带的observe模式以及debugtooltip来查找id。")
print("Please input the id for the two systems that you want to swap locations. You can find the id by using observe mode and debugtooltip function.")
original_system = int(input("请输入第一个id/Please input the first id："))
target_system = int(input("请输入第二个id/Please input the second id："))



def find_text(file_path, target_text, start,end,indent_level=None):
    last_line_number = None
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if start <= line_number <= end:
                    if target_text in line:
                        index = line.find(target_text)
                        if indent_level is None:
                            last_line_number = line_number
                        elif index >= 0 and line[:index].strip() == "" and line[:index].count('\t') == indent_level:
                            last_line_number = line_number
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    return last_line_number

def find_next(file_path, target_text, start,end,indent_level=None):
    last_line_number = None
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if start <= line_number <= end:
                    if target_text in line:
                        index = line.find(target_text)
                        if indent_level is None:
                            last_line_number = line_number
                            break
                        elif index >= 0 and line[:index].strip() == "" and line[:index].count('\t') == indent_level:
                            last_line_number = line_number
                            break
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    return last_line_number


def swap_paragraphs(file_path, start1, end1, start2, end2):
    with open(file_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()

    if start1 < 0 or end1 >= len(lines) or start2 < 0 or end2 >= len(lines):
        raise ValueError("Line numbers out of range")

    paragraph1 = lines[start1:end1]
    paragraph2 = lines[start2:end2]

    lines = lines[:start1] + paragraph2 + lines[end1:start2] + paragraph1 + lines[end2:]

    with open(file_path, 'w',encoding='utf-8') as file:
        file.writelines(lines)

def modify_text_file_in_place(file_path, start_line, end_line, indent_level, target_text_1, target_text_2):
    with open(file_path, 'r+',encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()

        for i, line in enumerate(lines):
            if start_line <= i+1 <= end_line:
                pattern = rf'^\t{{{indent_level}}}(to={re.escape(target_text_1)})$'
                match = re.search(pattern, line)
                if match:
                    line = line.replace(match.group(1), f'to={target_text_2}')
                else:
                    pattern = rf'^\t{{{indent_level}}}(to={re.escape(target_text_2)})$'
                    match = re.search(pattern, line)
                    if match:
                        line = line.replace(match.group(1), f'to={target_text_1}')
            f.write(line)


ori_beg = str(original_system) + '='
ori_end = str(original_system+1) + '='
tag_beg = str(target_system) + '='
tag_end = str(target_system+1) + '='


galaxy_begin = find_text(file_path, 'galactic_object=',1,1000000,0)
galaxy_end = find_text(file_path, 'starbase_mgr=',1,1000000,0)


original_system_begin = find_text(file_path, ori_beg,galaxy_begin,galaxy_end,1)
original_system_end = find_text(file_path, ori_end,galaxy_begin,galaxy_end,1)
target_system_begin = find_text(file_path, tag_beg,galaxy_begin,galaxy_end,1)
target_system_end = find_text(file_path, tag_end,galaxy_begin,galaxy_end,1)

original_system_coordinate_begin = find_next(file_path, 'coordinate=',original_system_begin,original_system_end,2)
original_system_coordinate_end = find_next(file_path, '}',original_system_begin,original_system_end,2)
target_system_coordinate_begin = find_next(file_path, 'coordinate=',target_system_begin,target_system_end,2)
target_system_coordinate_end = find_next(file_path, '}',target_system_begin,target_system_end,2)
swap_paragraphs(file_path, original_system_coordinate_begin, original_system_coordinate_end, target_system_coordinate_begin, target_system_coordinate_end)

original_system_hyperline_begin = find_next(file_path, 'hyperlane=',original_system_begin,original_system_end,2)
original_system_hyperline_end = find_next(file_path, '}',original_system_hyperline_begin,original_system_end,2)
target_system_hyperline_begin = find_next(file_path, 'hyperlane=',target_system_begin,target_system_end,2)
target_system_hyperline_end = find_next(file_path, '}',target_system_hyperline_begin,target_system_end,2)
swap_paragraphs(file_path, original_system_hyperline_begin, original_system_hyperline_end, target_system_hyperline_begin, target_system_hyperline_end)


oo=str(original_system)
tt=str(target_system)
modify_text_file_in_place(file_path, galaxy_begin, galaxy_end, 4, oo, tt)



print('finish')


time.sleep(5)
