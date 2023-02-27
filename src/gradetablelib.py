# This file contains code for generating a climbing grade table
#
# Author: Josh McIntyre
#

class GradeSystem:
    '''
    An individual grade system
    '''
    # Override
    name = ""
    ratings = {}

    # Internal metrics
    _max_level = 34

class Yosemite(GradeSystem):
    '''
    Yosemite decimal system
    '''
    name = "Yosemite Decimal System"
    ratings = { 0: '5.0', 
                1: '5.1',
                2: '5.2',
                3: '5.3',
                4: '5.4',
                5: '5.5',
                6: '5.6',
                7: '5.7',
                8: '5.8',
                9: '5.9',
                10: '5.10a',
                11: '5.10b',
                12: '5.10c',
                13: '5.10d',
                14: '5.11a',
                15: '5.11b',
                16: '5.11c',
                17: '5.11d',
                18: '5.12a',
                19: '5.12b',
                20: '5.12c',
                21: '5.12d',
                22: '5.13a',
                23: '5.13b',
                24: '5.13c',
                25: '5.13d',
                26: '5.14a',
                27: '5.14b',
                28: '5.14c',
                29: '5.14d',
                30: '5.15a',
                31: '5.15b',
                32: '5.15c',
                33: '5.15d'
              }

class VScale(GradeSystem):
    '''
    V-scale bouldering system
    '''
    name = "V-scale"
    ratings = { 0: 'V-easy/VB', 
                9: 'V0-',
                10: 'V0',
                11: 'V0+',
                12: 'V1',
                14: 'V2',
                16: 'V3',
                18: 'V4',
                19: 'V5',
                21: 'V6',
                22: 'V7',
                24: 'V8',
                25: 'V9',
                26: 'V10',
                27: 'V11',
                28: 'V12',
                29: 'V13',
                30: 'V14',
                31: 'V15',
                32: 'V16',
                33: 'V17'
              }


class French(GradeSystem):
    '''
    French grading system
    '''
    name = "French grading system"
    ratings = { 2: '1',
                3: '1',
                4: '3',
                5: '4a',
                6: '4b',
                7: '4c',
                8: '5a',
                9: '5b',
                10: '5c',
                11: '6a',
                12: '6a+',
                13: '6b',
                14: '6b+',
                15: '6c',
                16: '6c+',
                17: '7a',
                18: '7a+',
                19: '7b',
                20: '7b+',
                21: '7c',
                22: '7c+',
                23: '8a',
                24: '8a+',
                25: '8b',
                26: '8b+',
                27: '8c',
                28: '8c+',
                29: '9a',
                30: '9a+',
                31: '9b',
                32: '9b+',
                33: '9c'
              }


class GradeTable:
    '''
    Methods for generating an HTML-formatted table of climbing grades
    '''

    def __init__(self, grade_systems):
        '''
        Initialize the table generator with the provided grade system
        '''
        self.grade_systems = grade_systems

    def generate_table(self):
        '''
        Generate an HTML-formatted table using the internal grade system
        '''
        doc_html_fmt = "<!doctype html><html>{}</html>"
        table_html_fmt = "<table border=\"1\">{}</table>"
       
        data = ""
        
        table_headers = "<tr>"
        for system in self.grade_systems:
            table_headers += f"<th>{system.name}</th>"
        table_headers += "</tr>"
        data += table_headers
        
        table_data = ""
        for i in range(0, GradeSystem._max_level):
            row = "<tr>"
            for system in self.grade_systems:
                item = system.ratings.get(i, "")
                row += f"<td>{item}</td>"
            row += "</tr>"
            table_data += row
        data += table_data

        table_html = table_html_fmt.format(data)
        doc_html = doc_html_fmt.format(table_html)
       
        return doc_html
       

