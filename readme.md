# Requirements
- `python 3.x`
### To create the csv file
- `pandas`
- `numpy`
### To insert the grades
- `pyautogui`
- `pynput`

# How to use
- After installing the requirements and preparing some files (scroll down), run the `create_grades.py` program inside it's containing folder.
- In case you can not copy-paste the grades, I also made the `insert_grades.py` script. To use it, make sure you ran have the `students_grades.csv` file created by `create_grades.py` in the same folder. Run `insert_grades.py` inside its containing folder, head over to `labmat > course > Ayudante > Ingreso de Notas` and click the pencil icon of the test you want to grade. There, select the first box on where to enter the grades and press the `b` key on your keyboard. It should automatically fill in all the grades one by one.


You need to prepare three files that should be placed in the same folder as the `.py` file:
- `all_students.csv`
- `raw_student_grades.csv`
- `last_name_exceptions.txt`

For `all_students.csv`, go to `labmat > course > Ayudante > Alumnos`, and get the table as a `.csv` file. One way to do this is to `right click > save page as...` and save as html. Then head to any page that converts html tables to csv, for example `https://www.convertcsv.com/html-table-to-csv.htm` and convert your `.html` file to a `.csv` one. Then rename the downloaded file to `all_students`.

For `raw_studenr_grades.csv`, go to `Canvas > [Test you want to grade] > Estadísticas del examen` and click on `Análisis de estudiantes` to genereate a report. Download it as a `.csv` and rename it to `raw_student_grades`

The `last_name_exceptions.txt` has to be generated manually. It's used to handle students with last names longer than two words (for example, I had three studens with last names `first_name_1 second_name 1 (maybe_third_name) last_name_1 San Martín`). You need to store, line by line the equivalent of the `San` from `San Martín`.

# Limitations
- This program can not handle students whose last names have a two-word name as a first last name, i.e., if you have an student named `name name Del saz last_name_2` so that the first last name is `Del saz`, the program will most likely throw a score of `0`.

- The same would happen with last names of more than three words (compound last names are fine as long as they are hyphenated).
