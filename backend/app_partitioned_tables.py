
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text
import datetime
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:keshav7802@localhost:3306/november_2023_hiring_Keshav7802'
db = SQLAlchemy(app)

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50))
    message = db.Column(db.String(255))
    resourceId = db.Column(db.String(50))
    timestamp = db.Column(db.TIMESTAMP)
    traceId = db.Column(db.String(50))
    spanId = db.Column(db.String(50))
    commit = db.Column(db.String(50))
    parentResourceId = db.Column(db.String(50))

def table_exists(table_name):
    inspector = inspect(db.engine)
    return table_name in inspector.get_table_names()

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

def get_all_partitioned_tables():
    inspector = inspect(db.engine)
    tables = [name for name in inspector.get_table_names()]
    tables.remove('logs', 'log')
    return tables


@app.route('/ingest', methods=['POST'])
def ingest_logs():
    Log.query.delete()

    logs_data = request.get_json()

    tables = get_all_partitioned_tables()
    # Delete existing logs from each partitioned table
    for table in tables:
        delete_query = f"DELETE FROM {table}"
        db.session.execute(text(delete_query))

    db.session.commit()

    # count = {}

    for log_data in logs_data:
        # Convert timestamp to datetime format
        log_data['timestamp'] = datetime.datetime.strptime(log_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')

        # Access parentResourceId from metadata
        log_data['parentResourceId'] = log_data.get('metadata', {}).get('parentResourceId')

        # Remove metadata field from log_data
        if 'metadata' in log_data:
            del log_data['metadata']

        year_month = log_data['timestamp'].strftime('%Y_%m')
        if not table_exists(f'logs_{year_month}'):
            create_table_query = f'''
                CREATE TABLE logs_{year_month} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    level VARCHAR(50),
                    message VARCHAR(255),
                    resourceId VARCHAR(50),
                    timestamp TIMESTAMP,
                    traceId VARCHAR(50),
                    spanId VARCHAR(50),
                    commit VARCHAR(50),
                    parentResourceId VARCHAR(50)
                )
            '''
            db.session.execute(text(create_table_query))

        # Store the log in the corresponding table
        insert_log_query = f'''
            INSERT INTO logs_{year_month} (
                level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId
            ) VALUES (
                :level, :message, :resourceId, :timestamp, :traceId, :spanId, :commit, :parentResourceId
            )
        '''
        params = {
            'level': log_data['level'],
            'message': log_data['message'],
            'resourceId': log_data['resourceId'],
            'timestamp': log_data['timestamp'],
            'traceId': log_data['traceId'],
            'spanId': log_data['spanId'],
            'commit': log_data['commit'],
            'parentResourceId': log_data['parentResourceId']
        }
        # print(params)
        # count[str(year_month)] = count.get(str(year_month), 0) + 1
        db.session.execute(
            text(insert_log_query), params
        )

    # print(count)

    db.session.commit()
    return jsonify({"status": "success"})


def get_logs(level_filter=None, message_filter=None,
             resourceId_filter=None, timestamp_start=None, timestamp_end=None,
             traceId_filter=None, spanId_filter=None, commit_filter=None,
             parentResourceId_filter=None):
    
    # Initialize a list to store the filter conditions
    filters = []

    # Add filters based on the parameters provided

    if level_filter:
        # Filter by level
        filters.append(f"level = :level_filter")

    if message_filter:
        # Filter by message
        filters.append(f"message LIKE :message_filter")

    if resourceId_filter:
        # Filter by level
        filters.append(f"resourceId LIKE :resourceId_filter")

    if traceId_filter:
        # Filter by message
        filters.append(f"traceId LIKE :traceId_filter")

    if spanId_filter:
        # Filter by level
        filters.append(f"spanId LIKE :spanId_filter")

    if commit_filter:
        # Filter by message
        filters.append(f"commit LIKE :commit_filter")

    if parentResourceId_filter:
        # Filter by message
        filters.append(f"parentResourceId LIKE :parentResourceId_filter")

    # Add timestamp range filter
    if timestamp_start and timestamp_end:
        filters.append("timestamp BETWEEN :timestamp_start AND :timestamp_end")

    # Combine the filters into a WHERE clause
    where_clause = "WHERE " + " AND ".join(filters) if filters else ""

    # Initialize an empty list to aggregate results
    aggregated_logs = []
    relevant_tables = get_tables_within_range(timestamp_start, timestamp_end)

    # Iterate over each relevant table and execute the query
    for table_name in relevant_tables:
        # Construct the base query for the current table
        base_query = f"SELECT * FROM {table_name}"

        # Construct the final query
        final_query = f"{base_query} {where_clause}"

        # Prepare the parameters for the query
        params = {
            'level_filter': level_filter,
            'message_filter': f"%{message_filter}%" if message_filter else None,
            'timestamp_start': timestamp_start,
            'timestamp_end': timestamp_end,
            'resourceId_filter': resourceId_filter,
            'spanId_filter': spanId_filter,
            'traceId_filter': traceId_filter,
            'commit_filter': commit_filter,
            'parentResourceId_filter': parentResourceId_filter
        }

        # Execute the query for the current table
        with db.engine.connect() as connection:
            result = connection.execute(text(final_query), params)
    
        # Process the result and add to the aggregated logs
        aggregated_logs.extend([dict(zip(result.keys(), row)) for row in result])

    return aggregated_logs


def get_tables_within_range(timestamp_start, timestamp_end):
    # Assuming tables are named in the format 'logs_YYYY_MM'
    if not timestamp_start or not timestamp_end:
        return get_all_partitioned_tables()
    
    start_year_month = timestamp_start[:7].replace('-', '_')
    end_year_month = timestamp_end[:7].replace('-', '_')

    # Generate a list of year_month strings within the range
    year_months_within_range = []

    current_year_month = start_year_month
    while current_year_month <= end_year_month:
        year_months_within_range.append(current_year_month)

        # Increment to the next month
        year, month = map(int, current_year_month.split('_'))
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        current_year_month = f"{year:04d}_{month:02d}"

    # Generate table names based on the identified year_month values
    relevant_tables = [f'logs_{year_month}' for year_month in year_months_within_range if table_exists(f'logs_{year_month}')]
    return relevant_tables 


def is_table_within_range(table_name, start_date, end_date):
    try:
        # Extract the year and month from the table name
        year_month_str = table_name[5:]
        # print(year_month_str)
        # Convert the year_month string to a datetime object
        year_month = datetime.datetime.strptime(year_month_str, "%Y_%m")
        start_year_month = datetime.datetime.strptime(start_date, '%Y_%m')
        end_year_month = datetime.datetime.strptime(end_date, '%Y_%m')
        return start_year_month <= year_month <= end_year_month
    except (IndexError, ValueError):
        # Handle the case where the table name does not follow the expected pattern
        return False


@app.route('/logs', methods=['GET'])
def get_logs_api():
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

    if timestamp:
        startTimestamp= timestamp
        endTimestamp = timestamp
    
    if not startTimestamp:
        startTimestamp = '2000-01-01T00:00:00Z'
    if not endTimestamp:
        endTimestamp = '2099-12-31T23:59:59Z'

    logs = get_logs(
        level_filter=level,
        message_filter=message,
        timestamp_start=startTimestamp,
        timestamp_end=endTimestamp,
        resourceId_filter=resourceId,
        spanId_filter=spanId,
        traceId_filter=traceId,
        commit_filter=commit,
        parentResourceId_filter=parentResourceId
    )

    return jsonify(logs)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=3000)

