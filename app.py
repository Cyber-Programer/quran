from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from the JSON file
with open('full_quran.json', 'r', encoding='utf-8') as file:
    surahs_data = json.load(file)

suras = surahs_data  # No need for the loop to create `suras`

@app.route('/')
def home():
    return 'Use /surah/surah number <br>/surah/1'

@app.route('/surah/<int:sura_no>', methods=['GET'])
def get_surah_ayah(sura_no):
    data = None
    if sura_no > 114:
        return 'as a muslim you need to know that there are 114 surah in quran'
    else:
        for sr in suras:
            if sr['id'] == sura_no:
                data = {
                    "No": sura_no,
                    "Name": sr['name'],
                    "Transliteration": sr['transliteration'],
                    "Type": sr['type'],
                    "Total Ayat": sr['total_verses'],
                    "Verses": sr['verses'],
                }
                return data
            

if __name__ == '__main__':
    app.run()
