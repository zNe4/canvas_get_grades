# Requirements
- `python 3.x`
### To create the csv file
- `pandas`
- `numpy`
### To insert the grades
- `pyautogui`
- `pynput`

# How to use
- After installing the requirements and preparing some files (scroll down), run the `create_grades.py` program inside its containing folder.
- In case you can not copy-paste the grades, I also made the `insert_grades.py` script. To use it, make sure you ran have the `students_grades.csv` file created by `create_grades.py` in the same folder. Run `insert_grades.py` inside its containing folder, head over to `labmat > course > Ayudante > Ingreso de Notas` and click the pencil icon of the test you want to grade. There, select the first box on where to enter the grades and press the `b` key on your keyboard. It should automatically fill in all the grades one by one.


You need to prepare two files that should be placed in the same folder as the `.py` file:
- `all_students.csv`
- `raw_student_grades.csv`

For `all_students.csv`, go to `labmat > course > Ayudante > Alumnos`, and get the table as a `.csv` file. One way to do this is to `right click > save page as...` and save as html. Then you can use the `csv` library in python to export the desired table, or head to any page that converts html tables to csv, for example `https://www.convertcsv.com/html-table-to-csv.htm` and convert your `.html` file to a `.csv` one. Then rename the downloaded file to `all_students`.

For `raw_student_grades.csv`, go to `Canvas > [Test you want to grade] > Estadísticas del examen` and click on `Análisis de estudiantes` to genereate a report. Download it as a `.csv` and rename it to `raw_student_grades`


# Limitations
- This program will only produce a file when the `raw_student_grades.csv` file contains a column named `name` and other named `score`.
