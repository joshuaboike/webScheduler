from flask import render_template, request, session
from app import app
from schedule_api import get_schools, get_terms, get_subjects, get_catalogNbrs, get_sectionNbrs

@app.route('/')
def index():
    options = {}

    '''TermCode = 'Empty'
    SchoolCode = 'Empty'
    SubjectCode = 'Empty'
    CatalogNumber = 'Empty'
    SectionNumber = 'Empty'
    ClassNumber = 'Empty'''

    try:
        options['terms'] = get_terms()
        
    except:
        options['api_error'] = True

    return render_template('index.html', **options)

@app.route('/<termCode>')
def schools(termCode):
    options = {}
    TermCode = termCode
    try:
        options['schools'] = get_schools(TermCode)
        options['term'] = TermCode
        
    except:
        options['api_error'] = True

    return render_template('schools.html', **options)

@app.route('/<termCode>/<schoolCode>')
def subjects(termCode, schoolCode):
    options = {}
    TermCode = termCode
    SchoolCode = schoolCode
    try:
        options['term'] = TermCode
        options['school'] = SchoolCode
        options['subjects'] = get_subjects(TermCode, SchoolCode)
        
    except:
        options['api_error'] = True

    return render_template('subjects.html', **options)

@app.route('/<termCode>/<schoolCode>/<subjectCode>')
def catalog(termCode, schoolCode, subjectCode):
    options = {}
    TermCode = termCode
    SchoolCode = schoolCode
    SubjectCode = subjectCode
    try:
        options['term'] = TermCode
        options['school'] = SchoolCode
        options['subject'] = SubjectCode
        options['catalogNbers'] = get_catalogNbrs(TermCode, SchoolCode, SubjectCode)
    except:
        options['api_error'] = True

    return render_template('courses.html', **options)

@app.route('/<termCode>/<schoolCode>/<subjectCode>/<catalogNumber>/', methods=['GET', 'POST', 'REMOVE'])
def backpack(termCode, schoolCode, subjectCode, catalogNumber):
    options = {}
    TermCode = termCode
    SchoolCode = schoolCode
    SubjectCode = subjectCode
    CatalogNumber = catalogNumber
    try:
        options['term'] = TermCode
        options['school'] = SchoolCode
        options['subject'] = SubjectCode
        options['catalogNbers'] = CatalogNumber
        options['sectionNbers'] = get_sectionNbrs(TermCode, SchoolCode, SubjectCode, CatalogNumber)
        if 'backpack' not in session:
             session['backpack'] = []
 
        if request.method == 'POST':
             session['backpack'].append(request.form['course'])

        if request.method == 'REMOVE':
            session['backpack'].remove(request.form['course'])
 
        options['backpack'] = session['backpack']
    except:
        options['api_error'] = True

    return render_template('sections.html', **options)

@app.route('/mybackpack')
def myBackpack():
    options = {}
    try:
        if 'backpack' not in session:
            session['backpack'] = []
 
        if request.method == 'POST':
            session['backpack'].append(request.form['course'])

        if request.method == 'REMOVE':
            session['backpack'].remove(request.form['course'])

        options['backpack'] = session['backpack']
    except:
        options['api_error'] = True
 
    return render_template('mybackpack.html', **options)

@app.route('/editbackpack')
def editBackpack():
    options = {}
    try:
        if 'backpack' not in session:
            session['backpack'] = []

        if request.method == 'REMOVE':
            for value in backpack:
                value['backpack'].pop(request.form['removeCourse'])

            return render_template('mybackpack.html', ** options)

        options['backpack'] = session['backpack']
    except:
        options['api_error'] = True
 
    return render_template('editbackpack.html', **options)
