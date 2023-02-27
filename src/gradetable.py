# This file contains driver code for creating an HTML table of climbing grades
#
# Author: Josh McIntyre
#
import gradetablelib

def main():
    '''
    The main entry point for the program
    '''
    systems = [ gradetablelib.Yosemite, gradetablelib.VScale, gradetablelib.French ]
    grade_table = gradetablelib.GradeTable(systems)
    doc_html = grade_table.generate_table()

    with open("grades.html", "w") as f:
        f.write(doc_html)
	
if __name__ == "__main__":
	main()