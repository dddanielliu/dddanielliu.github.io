def remove_spaces_around_commas(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        # Remove spaces before and after commas
        modified_line = line.replace(' ,', ',').replace(', ', ',')
        modified_lines.append(modified_line)

    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

# Example usage
input_file_path = '112CoursesList.csv'
output_file_path = 'output.txt'

remove_spaces_around_commas(input_file_path, output_file_path)
