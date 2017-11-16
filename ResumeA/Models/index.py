work_experience_total = 5

# TODO get data from database


def calculate_experience(value):
    return "{0}%".format((value / work_experience_total) * 100)


# Get my main skill list
def skill_detail():
    return [
        {"text": "C#.Net, Javascript", "value": "4 years", "percentage": calculate_experience(4)},
        {"text": "Oracle", "value": "1.5 year", "percentage": calculate_experience(2)},
        {"text": "Game", "value": "1 year", "percentage": calculate_experience(1.15)}
    ]


# Get my other skill list
def skill_other():
    return [
        "Test", "Windows Server 2008 R2", "Adobe", "MVC", "LINQ"
    ]


# Get language list
def languages_detail():
    return [
        {"text": "Chinese (中文)", "percentage": "100%"},
        {"text": "English (英文)", "percentage": "50%"},
    ]


# Get work experience list
def work_experience():
    return [
        {
            "title": "Engineer", "company": "Test Company",
            "start_date": "10 / 2015", "end_date": "",
            "content": "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
        },
        {
            "title": "Engineer", "company": "GOGOGOTest",
            "start_date": "06 / 2012", "end_date": "03 / 2015",
            "content": "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum.Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
        },
        {
            "title": "Engineer", "company": "HAHAHATest",
            "start_date": "07 / 2009", "end_date": "03 / 2012",
            "content": "Once again, some random text to fedfjiio ididojo jiodfasio ijiojdfasio."
        },
    ]


# Get education list
def education_list():
    return [
        {
            "name": "Test University of Test",
            "date": "2000 - 2009",
            "content": "Bachelor Degree"
        }
    ]


# Get view display context
def context():
    return {
        'title': "No Name's CV",
        # TODO chance color to #008ae6
        'color': "blue-grey",
        'name': "No Name",
        'job_title': "Engineer",
        'location': "Anywhere, Earth",
        'mail': "test@test.com",
        'phone': "09xx-xxx-xxx",
        'skill': {
            'title': "Skills",
            'skills': skill_detail()
        },
        'skill_other': skill_other(),
        'language': {
            'title': "Languages",
            'languages': languages_detail()
        },
        'work_experience': {
            'title': "Work Experience",
            'experience_list': work_experience()
        },
        'education': {
            'title': "Education",
            'education_list': education_list()
        }
    }