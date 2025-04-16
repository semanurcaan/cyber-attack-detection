from flask import Flask, request

app = Flask(__name__)

@app.route('/gelen_paket', methods=['POST'])
def gelen_paket():
    veri = request.get_json()
    
    if veri.get('label') == 1:
        print("🚨 Saldırı Paketi Engellendi!")
    else:
        print("✅ Normal Paket Alındı. İçerik:", veri)

    return "Tamam", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

