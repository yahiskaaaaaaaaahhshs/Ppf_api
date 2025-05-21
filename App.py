from flask import Flask, request, jsonify
import re
import time

app = Flask(__name__)

API_KEY = "yashikaaa"  # The required API key

@app.route('/key=<key>/cc=<card_data>', methods=['GET'])
def check_card(key, card_data):
    """Endpoint to check credit card - Always returns Declined after 12 seconds"""
    if key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401
    
    # Validate card format
    if not re.match(r'^\d{13,16}\|\d{2}\|\d{2,4}\|\d{3,4}$', card_data):
        return jsonify({"error": "Invalid card format. Use CC|MM|YYYY|CVV"}), 400
    
    # Wait exactly 12 seconds
    time.sleep(12)
    
    # Generate decline response without donation_id
    response = {
        "cc": card_data,
        "response": {
            "errors": ["Your card was declined."],
            "success": False
        },
        "status": "Declined"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
