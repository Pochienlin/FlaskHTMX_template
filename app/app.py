'''
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from flask import Flask, request, render_template
from requests.models import Response

app = Flask(__name__)
    
@app.route("/", methods=['GET'])
def startEndpoint():
    print("started successfully!")

    return render_template('home.html')

@app.route("/<page>", methods=['GET'])
def getPath(page):
    # DO SOME VALIDATIONS
    return render_template(page)

@app.route('/postmethod', methods=['POST'])
def samplePOST():
    req_body = request.json.get('body')
    if not req_body or len(req_body) == 0:
        response = Response()
        response.status_code=400
        response._content='{"error": Bad request: {0}}'.format(req_body)
        return response
    try:
        return ""
    except Exception as e:
        return {
            'status': 500,
            'error': f'Error calling API: {str(e)}'
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2025, debug=True)