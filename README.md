# Python Code Counter

This is just a single script for counting lines of code in python class and and notebook files. (It counts **only** the source code components of notebook files.) By default it searches for and counts lines of code, including comment lines but excluding whitespace lines, in all .py/.pynb files in the entire subtree, starting from the root running directory and reporting file-by-file and total code counts. These defaults can be tweaked using script arguments (see below).

This script was written for Python 3, and technically I've only tested using v3.6.7 and v3.7.2, though I believe it should work fine with any v3.

## Example run with just the help output:
```
$codecounter.py -h
usage: codecounter.py [-h] [--root ROOT] [--exclude EXCLUDE] [--no_comments]
                      [--no_subtree] [--quiet_out]

Lines of Python Code Counter, includes both .py and .ipynb files.

optional arguments:
  -h, --help            show this help message and exit
  --root ROOT, -R ROOT  root directory from which to search, defaults to '.'
  --exclude EXCLUDE, -x EXCLUDE
                        comma separated directory names to exclude, default
                        excludes ONLY hidden directories
  --no_comments, -nc    exclude comment lines, comments included by default
  --no_subtree, -ns     exclude subtree files, subtree included by default
  --quiet_out, -q       print totals only, default prints file-by-file counts
```

## Example run on [Rubik's Cube Repository](https://github.com/ajdonich/rubiks-cube):
```
$codecounter.py --root rubiks-cube  --exclude sandbox -nc
Searching from root directory: 'rubiks-cube'
Excluding directories: ['sandbox']
Excluding comments

Running code counter...............
.py files:
   1 rubiks-cube/rubiks/__init__.py : 0
   2 rubiks-cube/rubiks/legacy/Cube3D.py : 147
   3 rubiks-cube/rubiks/legacy/SpiCubeView.py : 89
   4 rubiks-cube/rubiks/legacy/OpticubeSolver.py : 117
   5 rubiks-cube/rubiks/legacy/SpiCubeSolver.py : 130
   6 rubiks-cube/rubiks/legacy/__init__.py : 0
   7 rubiks-cube/rubiks/legacy/Cube3DSolver.py : 60
   8 rubiks-cube/rubiks/legacy/Cube.py : 216
   9 rubiks-cube/rubiks/legacy/Opticube.py : 140
   10 rubiks-cube/rubiks/legacy/Cube3DView.py : 101
   11 rubiks-cube/rubiks/legacy/CubeSolver.py : 18
   12 rubiks-cube/rubiks/legacy/CubeletSolver.py : 101
   13 rubiks-cube/rubiks/legacy/SpiCube.py : 125
   14 rubiks-cube/rubiks/solver/NNSolver.py : 68
   15 rubiks-cube/rubiks/solver/CfopState.py : 131
   16 rubiks-cube/rubiks/solver/__init__.py : 0
   17 rubiks-cube/rubiks/solver/FaceletSolver.py : 225
   18 rubiks-cube/rubiks/solver/DirectSolver.py : 135
   19 rubiks-cube/rubiks/solver/UCTNode.py : 98
   20 rubiks-cube/rubiks/solver/CyclicSolver.py : 117
   21 rubiks-cube/rubiks/solver/CfopSolver.py : 129
   22 rubiks-cube/rubiks/model/Observer.py : 13
   23 rubiks-cube/rubiks/model/VectorCube.py : 133
   24 rubiks-cube/rubiks/model/SMAdapter.py : 133
   25 rubiks-cube/rubiks/model/CubeView.py : 195
   26 rubiks-cube/rubiks/model/__init__.py : 0
   27 rubiks-cube/rubiks/model/CfopCube.py : 21
   28 rubiks-cube/rubiks/model/DirectCube.py : 73

.ipynb files:
   1 rubiks-cube/notebooks/Nb3_CFOP_Algorithm.ipynb : 58
   2 rubiks-cube/notebooks/Nb2_Neural_Networks.ipynb : 101
   3 rubiks-cube/notebooks/Nb1_Intro_Cube_View.ipynb : 174
   4 rubiks-cube/notebooks/Nb4_Cycles_Entropy.ipynb : 111
   5 rubiks-cube/rubiks/legacy/RubiksSpiCube.ipynb : 490
   6 rubiks-cube/rubiks/legacy/RubiksCube3D.ipynb : 733
   7 rubiks-cube/rubiks/legacy/RubiksCube.ipynb : 276

Total lines of code in directory 'rubiks-cube': 4658
  python file code: 2715
  notebook file code: 1943
```
