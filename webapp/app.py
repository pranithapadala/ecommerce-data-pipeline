
from flask import Flask, render_template, jsonify
import duckdb
import os

# --- Configuration ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(PROJECT_ROOT, 'dbt_project', 'ecommerce.duckdb')
# ---------------------

app = Flask(__name__)

def get_db_connection():
    if not os.path.exists(DB_FILE):
        raise FileNotFoundError(f"Database file not found at {DB_FILE}. Please run 'dbt run' first.")
    con = duckdb.connect(database=DB_FILE, read_only=True)
    return con

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/transactions-over-time')
def get_transactions_over_time():
    con = get_db_connection()
    query = """
        SELECT 
            date_trunc('day', transaction_timestamp)::date AS date,
            count(transaction_id) AS transaction_count
        FROM transactions
        WHERE transaction_timestamp BETWEEN '2015-05-01' AND '2015-09-30'
        GROUP BY 1
        ORDER BY 1;
    """
    data = con.execute(query).fetchall()
    con.close()
    
    labels = [row[0].strftime('%Y-%m-%d') for row in data]
    values = [row[1] for row in data]
    
    return jsonify({'labels': labels, 'data': values})

@app.route('/api/top-users')
def get_top_users():
    con = get_db_connection()
    query = """
        SELECT 
            visitor_id,
            count(transaction_id) AS transaction_count
        FROM transactions
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 10;
    """
    data = con.execute(query).fetchall()
    con.close()
    
    labels = [f"User #{row[0]}" for row in data]
    values = [row[1] for row in data]
    
    return jsonify({'labels': labels, 'data': values})

@app.route('/api/transactions-by-dow')
def get_transactions_by_dow():
    con = get_db_connection()
    query = """
        SELECT 
            dayname(transaction_timestamp) AS day_of_week,
            count(transaction_id) AS transaction_count
        FROM transactions
        GROUP BY dayname(transaction_timestamp), dayofweek(transaction_timestamp)
        ORDER BY dayofweek(transaction_timestamp);
    """
    data = con.execute(query).fetchall()
    con.close()
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    
    return jsonify({'labels': labels, 'data': values})

if __name__ == '__main__':
    app.run(debug=True)
