# Requirements
- `python 3.x`
### To create the csv file
- `pandas`
- `numpy`
### To insert the grades
- `pyautogui`
- `pynput`

# How to use
- After installing the requirements and preparing some files (scroll down), run the `create_grades.py` script inside its containing folder.
- In case you cannot copy-paste the grades, I also made the `insert_grades.py` script. To use it, make sure you ran have the `students_grades.csv` file created by `create_grades.py` in the same folder. Run `insert_grades.py` inside its containing folder, head over to `labmat > course > Ayudante > Ingreso de Notas` and click the pencil icon of the test you want to insert the grades on. There, select the first box on where to enter the grades and press the `b` key on your keyboard. It should automatically fill in all the grades one by one. For some reason this only works on linux and not on windows, if you know how to fix that please make a pull request, issue or notify me in any way.


You need to prepare two files that should be placed in the same folder as the `.py` file:
- `all_students.csv`
- `raw_student_grades.csv`

For `all_students.csv`, go to `labmat > course > Ayudante > Alumnos`, and get the table as a `.csv` file. One way to do this is to `right click > save page as...` and save as html. Then you can use the `csv` or the `html2csv` library in python to export the desired table, or head to any page that converts html tables to csv, for example `https://www.convertcsv.com/html-table-to-csv.htm` and convert your `.html` file to a `.csv` one. Then rename the downloaded file to `all_students`.

For `raw_student_grades.csv`, go to `Canvas > Course > Calificaciones` (or head to `/courses/[course_id]/gradebook`)and click on `Exportar > Exportar todo el libro de calificaciones` to genereate a report. Download it as a `.csv` and rename it to `raw_student_grades`

The program will show all possible tests, and you can choose which one to get the grades from.

## EXTRA: How to insert grades quickly in speedgrader
1. Open the browser console by pressing `f12`
2. Paste the following code, replace `NUMBER_OF_STUDENTS` with your number of students and then hit the enter key:
```js
for (let i=0; i<NUMBER_OF_STUDENTS; i++){
	try {
		name = document.querySelector('[data-testid="rubric-total"]').classList[0];
		document.getElementById('grading-box-extended').value = document.getElementsByClassName(name)[3].innerHTML.split(' ')[2];
	    document.getElementById('grading-box-extended').dispatchEvent(new Event('change'));
        document.getElementById('next-student-button').dispatchEvent(new Event('click'));
	}
	catch (error) {
		document.getElementById('next-student-button').dispatchEvent(new Event('click'));
	}
}
```
3. Profit.
