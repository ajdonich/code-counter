#!/usr/bin/env python3

import os, re, argparse

def count_ipynb_code(filename, count_comments):
#{
    line_count = 0
    with open(filename, mode='r') as f_handle:
    #{
        is_source_code = False
        for line in f_handle:
        #{
            if re.match(r"\s*\"source\":\s*\[", line): is_source_code = True
            elif re.match(r"\s*\]", line): is_source_code = False
            elif is_source_code and ((count_comments and re.match(r"\s*\"\s*#", line)) or 
                                     re.match(r"\s*\"\s*\w", line)): line_count += 1 
        #}        
    #}
    
    return line_count
#}

def count_py_code(filename, count_comments):
#{
    line_count = 0    
    with open(filename, mode='r') as f_handle:
        line_count = sum([1 for line in f_handle if (count_comments and re.match(r"\s*#", line)) or re.match(r"\s*\w", line)])
    
    return line_count
#}

def _excluded(path, ex_dirs):
    regex = [r"^\.\w"] + [r"{0}".format(xd) for xd in ex_dirs]
    return sum([1 for d in path.split("/") for rx in regex if re.match(rx, d)]) > 0

def find_code_files(root_path, file_type, inc_subtree, ex_dirs):
#{
    if inc_subtree: return [f"{root}/{filename}" for root, sub_folders, files in os.walk(root_path) for filename in files 
                            if not _excluded(f"{root}/{filename}", ex_dirs) and re.match(r".+\.{0}$".format(file_type), filename)]
    
    else: return [f"{root_path}/{filename}" for filename in [pn for pn in os.listdir(root_path) if os.path.isfile(f"{root_path}/{pn}")] 
                  if not _excluded(f"{root_path}/{filename}", ex_dirs) and re.match(r".+\.{0}$".format(file_type), filename)]
#}

def count_lines(root_dir, count_comments=True, inc_subtree=True, verbose=True, exclude_dirs=[]):
#{
    # Python files
    py_code_counts = []
    if verbose: print(".py files:")
    for fcount, file in enumerate(find_code_files(root_dir, 'py', inc_subtree, exclude_dirs)):
        code_count = count_py_code(file, count_comments)
        if verbose: print("  ", fcount+1, file, ":", code_count)
        py_code_counts.append(code_count)

    # Notebook files
    ipynb_code_counts = []
    if verbose: print("\n.ipynb files:")
    for fcount, file in enumerate(find_code_files(root_dir, 'ipynb', inc_subtree, exclude_dirs)):
        code_count = count_ipynb_code(file, count_comments)
        if verbose: print("  ", fcount+1, file, ":", code_count)
        ipynb_code_counts.append(code_count)
    
    print(f"\nTotal lines of code in directory \'{root_dir}\':", sum(py_code_counts + ipynb_code_counts))
    print("  python file code:", sum(py_code_counts))
    print("  notebook file code:", sum(ipynb_code_counts))
#}

##############################################################################################################
# Commencing with explicitly executed part of script below:

# Defaults
root_directory = '.'
include_coments = True
include_subtree = True
verbose_output = True
exclude_dirs = []

# Initiate the parser with accepted arguments
parser = argparse.ArgumentParser(description = 'Lines of Python Code Counter, includes both .py and .ipynb files.')
parser.add_argument("--root", "-R", help="root directory from which to search, defaults to '.'")
parser.add_argument("--exclude", "-x", help="comma separated directory names to exclude, default excludes ONLY hidden directories")
parser.add_argument("--no_comments", "-nc", help="exclude comment lines, comments included by default", action="store_true")
parser.add_argument("--no_subtree", "-ns", help="exclude subtree files, subtree included by default", action="store_true")
parser.add_argument("--quiet_out", "-q", help="print totals only, default prints file-by-file counts", action="store_true")

# Parse commandline
args = parser.parse_args()
if args.root: root_directory = args.root
print(f"Searching from root directory: '{root_directory}'")

if args.exclude: 
    exclude_dirs = re.compile(r'\s*,\s*').split(args.exclude)
    print(f"Excluding directories: {exclude_dirs}")

if args.no_comments: print(f"Excluding comments"); include_coments = False
if args.no_subtree: print(f"Excluding subtree"); include_subtree = False
if args.quiet_out: print(f"Quiet output"); verbose_output = False


# Count code
print("\nRunning code counter...............")
count_lines(root_directory, 
            count_comments=include_coments,
            inc_subtree=include_subtree, 
            verbose=verbose_output, 
            exclude_dirs=exclude_dirs)
