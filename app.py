

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Swordsman',
        'location':'On my Ship',
        'benefits': 'Chance to become the Strongest Swordsman in the World'
    },
{
        'id':2,
        'title':'Navigator',
        'location':'On my Ship',
        'benefits': 'Chance to Draw the Map of the Grand Line'
    },
{
        'id':3,
        'title':'Sniper',
        'location':'On my Ship',
        'benefits': 'Chance to become the Bravest Person on The Sea'
    },
{
        'id':4,
        'title':'Cook',
        'location':'On my Ship',
        'benefits': 'Chance to become the All Blue'
    },
{
        'id':5,
        'title':'Musician',
        'location':'On my Ship',
        'benefits': 'Chance to enjoy the Mighty sea with other Nakamas'
    },
{
        'id':6,
        'title':'Doctor',
        'location':'On my Ship',
        'benefits': 'Chance to become the Best Doctor in the World'
    },
{
        'id':7,
        'title':'Shipwright',
        'location':'On my Ship',
        'benefits': 'Chance to build the Strongest Ship in the World'
    },
{
        'id':8,
        'title':'Archeologist',
        'location':'On my Ship',
        'benefits': 'Chance to know the mystery of the Ponegliphs'
    },
{
        'id':9,
        'title':'Helmsman',
        'location':'On my Ship',
        'benefits': 'Chance to Steer the Strongest Ship in the World'
    }
]


@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Straw Hat')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

