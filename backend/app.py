from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:keshav7802@localhost:3306/november_2023_hiring_Keshav7802'
db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50), index = True)
    message = db.Column(db.String(255), index = True)
    resourceId = db.Column(db.String(50), index = True)
    timestamp = db.Column(db.DateTime, index = True)
    traceId = db.Column(db.String(50), index = True)
    spanId = db.Column(db.String(50), index = True)
    commit = db.Column(db.String(50), index = True)
    parentResourceId = db.Column(db.String(50), index = True)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/testdb')
def test_db():
    try:
        # Query all logs
        all_logs = Log.query.all()
        return jsonify([log.__dict__ for log in all_logs])
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/ingest', methods=['POST'])
def ingest_logs():
    Log.query.delete()

    logs_data = request.get_json()

    for index, log_data in enumerate(logs_data):
        # Convert timestamp to datetime format
        log_data['timestamp'] = datetime.datetime.strptime(log_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')

        # Access parentResourceId from metadata
        log_data['parentResourceId'] = log_data.get('metadata', {}).get('parentResourceId')

        # Remove metadata field from log_data
        if 'metadata' in log_data:
            del log_data['metadata']

        # Store the index value as a new field with key 'id'
        log_data['id'] = index + 1
        new_log = Log(**log_data)
        db.session.add(new_log)

    db.session.commit()
    return jsonify({"status": "success"})


def apply_filter(query, key, value):
    if value:
        return query.filter(getattr(Log, key) == value)
    return query

def apply_text_search(query, key, search_query):
    if search_query:
        return query.filter(getattr(Log, key).ilike(f"%{search_query}%"))
    return query

def apply_date_range(query, start_timestamp, end_timestamp, timestamp):
    if timestamp:
        start_timestamp = timestamp
        end_timestamp = timestamp
    if start_timestamp and end_timestamp:
        start_datetime = datetime.datetime.strptime(start_timestamp, '%Y-%m-%dT%H:%M:%SZ')
        end_datetime = datetime.datetime.strptime(end_timestamp, '%Y-%m-%dT%H:%M:%SZ')
        query = query.filter(Log.timestamp.between(start_datetime, end_datetime))
    return query

@app.route('/logs', methods=['GET'])
def get_logs():
    # Extract filter parameters from the request
    level = request.args.get('level')
    message = request.args.get('message')
    resourceId = request.args.get('resourceId')
    timestamp = request.args.get('timestamp')
    traceId = request.args.get('traceId')
    spanId = request.args.get('spanId')
    commit = request.args.get('commit')
    parentResourceId = request.args.get('parentResourceId')
    startTimestamp = request.args.get('startTimestamp')
    endTimestamp = request.args.get('endTimestamp')

    # Start building the SQLAlchemy query
    query = Log.query
    query = apply_filter(query, 'level', level)
    query = apply_text_search(query, 'message', message)
    query = apply_filter(query, 'resourceId', resourceId)
    query = apply_filter(query, 'traceId', traceId)
    query = apply_filter(query, 'spanId', spanId)
    query = apply_filter(query, 'commit', commit)
    query = apply_filter(query, 'parentResourceId', parentResourceId)
    query = apply_date_range(query, startTimestamp, endTimestamp, timestamp)

    # Execute the query
    filtered_logs = query.all()

    log_list = [{"id" : log.id, "level": log.level, "message": log.message, 
                 "resourceId" : log.resourceId, "timestamp" : log.timestamp, 
                 "traceId" : log.traceId, "spanId" : log.spanId, "commit" : log.commit, 
                 "parentResourceId" : log.parentResourceId} for log in filtered_logs]

    return jsonify(log_list)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=3000)
