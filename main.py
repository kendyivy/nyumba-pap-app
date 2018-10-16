from flask import (Flask, render_template, request, jsonify)
from peewee import IntegrityError
import bootstrap
from models.house import House
from models.agent import Agent
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)

bootstrap.initialize()


@app.route('/')
def index():
    avail_houses = House.select()
    return render_template('list_houses.html', houses=avail_houses)


@app.route('/houses/add', methods=['POST'])
def add_house():
    data = dict(request.form.items())
    try:
        House.create(
            plot_no=data.get('plot_no'),
            no_rooms=data.get('no_rooms'),
            rent=data.get('rent'),
            no_bathrooms=data.get('no_bathrooms'),
            location=data.get('location'),
            nearby_amenities=data.get('nearby_amenities'),
            rating=data.get('rating')
        )
        result = {'status': 'success'}
    except IntegrityError:
        result = {'status': 'failed', 'message': 'Plot number not unique'}
    finally:
        return jsonify(result)


@app.route('/agents/see', methods=['POST'])
def see_agent():
    result = {'status': 'success'}
    return jsonify(result)

@app.route('/agents/add',  methods=['POST'])
def add_agent():
    agent_data = dict(request.form.items())
    Agent.create(
        name=agent_data.get('name', 'john doe'),
        business_number=agent_data.get('business_number'),
        email=agent_data.get('email'),
        
    )
    result = {'status': 'success'}
    return jsonify(result)










@app.route('/agents',  methods=['GET'])
def list_saloons():
    agents = Agent.select()
    results = []
    for agent in agents:
        results.append(
            {
                'name': agent.name,
                'business_number': agent.business_number,
                'email': agent.email,
                
             }
            )
    return jsonify(results)








if __name__ == '__main__':
    app.run(**app_start_config)