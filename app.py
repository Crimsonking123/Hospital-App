from flask import Flask, render_template
data = {'Central Newfoundland Regional Health Centre': [80, 46, 32, 400, 29], 'Health Sciences Centre': [80, 78, 42, 253, 70], 'Western Memorial Regional Hospital': [80, 46, 38, 305, 72], 
'Waterford Hospital, Eastern Health': [139, 32, 49, 297, 100], "St. Clare's Mercy Hospital": [103, 62, 37, 281, 84], 'Dr. G. B. Cross Memorial Hospital': [140, 41, 48, 491, 27], 'Sir Thomas Roddick Hospital': [122, 29, 35, 421, 85], 'Bonavista Peninsula Health Centre': [120, 15, 45, 288, 44], 'James Paton Memorial Regional Health Centre': [140, 40, 49, 420, 93], "St Clare's Hospital Chaplain": [139, 17, 38, 249, 22],
'Carbonear General Hospital': [98, 58, 45, 363, 21], 'Baie Verte Peninsula Health Centre': [110, 28, 38, 343, 72], 'Fogo Island Health Centre': [129, 65, 30, 223, 48], 'Notre Dame Bay Memorial Health Centre': [113, 53, 34, 301, 53], 'Bonne Bay Health Centre': [135, 13, 30, 384, 24], 'Burin Peninsula Health Care Centre': [98, 29, 38, 268, 86], 'Labrador Health Centre': [81, 12, 46, 473, 22], 
'Labrador West Health Centre': [124, 77, 32, 379, 52], 'Dr. Charles S. Curtis Memorial Hospital': [87, 30, 45, 339, 33], 'U S Memorial Health Centre': [102, 36, 39, 415, 70], 'Brookfield Hospital Dr': [129, 79, 40, 463, 76], 'Dr. A.A. Wilkinson Memorial Health Centre': [135, 57, 46, 310, 28], 'Labrador South Health Centre - Labrador-Grenfell Health': [134, 6, 31, 309, 48], 'Strait of Belle Isle Health Centre': [83, 31, 40, 212, 82], "Janeway Children's Health and Rehabilitation Centre": [91, 5, 30, 425, 49], 'Labrador Health Svc': [103, 27, 47, 413, 88], 'Brookfield Hospital': [82, 24, 41, 226, 53], 'Corner Brook Acute Care Hospital': [98, 9, 50, 344, 64], 'Eastern Health Long Term Care': [86, 59, 49, 484, 44], 'Dr. Hugh Twomey Health Centre': [133, 42, 32, 374, 54], 'Corner Brook Long Term Care Centre': [103, 4, 47, 250, 27], 
'Calder Health Centre - Western Health': [140, 53, 48, 396, 81], 'Janeway Childrens Hospital': [117, 71, 42, 231, 44], 'st.marry': [84, 19, 44, 202, 93], 'Brookfield Health Centre': [110, 50, 33, 480, 27], 'Dr.Charles L.Legrow Health Centre': [100, 56, 47, 414, 71], 'Dr. S Beckley Health Center': [136, 49, 45, 337, 40], 'Green Bay Community Health Centre': [131, 28, 47, 206, 62], 
'Dr. Walter Templeman Health Care Centre': [121, 63, 36, 439, 56], 'Eastport Community Health Center': [102, 46, 45, 337, 31]}

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("prac.html")

@app.route('/data')
def pythondata():
   return data


if __name__ == '__main__':
   app.run(debug = True)