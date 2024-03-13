from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database to store user accounts and balances
user_accounts = {
    "user1": {"balance": 1000.0},
    "user2": {"balance": 2000.0},
}

# Mock payment gateway (replace with a real payment gateway in production)
def process_payment(amount, user_id):
    if user_id not in user_accounts:
        return False, "User not found"
    
    if user_accounts[user_id]["balance"] < amount:
        return False, "Insufficient balance"
    
    user_accounts[user_id]["balance"] -= amount
    return True, "Payment successful"

@app.route('/payment', methods=['POST'])
def make_payment():
    data = request.get_json()
    
    user_id = data.get("user_id")
    amount = data.get("amount")
    
    if not user_id or not amount:
        return jsonify({"status": "error", "message": "Invalid request"}), 400
    
    success, message = process_payment(amount, user_id)
    
    if success:
        return jsonify({"status": "success", "message": "Payment successful"}), 200
    else:
        return jsonify({"status": "error", "message": message}), 400

if __name__ == '__main__':
    app.run(debug=True)
