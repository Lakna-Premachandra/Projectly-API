import os
from flask import Flask, jsonify
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

app = Flask(__name__)

# Initialize Supabase client
#test commit
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        # Query all users with their name and age from the 'users' table
        response = supabase.table('users').select('name, age').execute()
        
        # Extract data from response
        users = response.data
        
        return jsonify({
            'success': True,
            'data': users
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
