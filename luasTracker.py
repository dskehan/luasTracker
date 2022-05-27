import requests
from xml.etree import ElementTree
from flask import Flask, request, render_template, after_this_request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def getLuasData():
    XPATH_STATUS = ".//message"
    XPATH_DIRECTION_INBOUND = ".//direction[@name='Inbound']/tram"
    XPATH_DIRECTION_OUTBOUND = ".//direction[@name='Outbound']/tram"

    _api_endpoint = "http://luasforecasts.rpa.ie/xml/get.ashx"
    luas_params = {'action': 'forecast', 'encrypt': 'false', 'stop': 'CHA'}

    api_response = requests.get(_api_endpoint, params=luas_params)
    tree = ElementTree.fromstring(api_response.content)

    status = tree.find(XPATH_STATUS).text.strip()
    statusx = tree.find(XPATH_STATUS).text
    print(status)

    result_inbound = tree.findall(XPATH_DIRECTION_INBOUND)
    result_outbound = tree.findall(XPATH_DIRECTION_OUTBOUND)
    luasInfo = []
    towardsBroom = []
    towardsBride = [] 

    for tram in result_inbound:
        print(tram.attrib)
        towardsBroom.append(tram.attrib)

    for tram in result_outbound:
        print(tram.attrib)
        towardsBride.append(tram.attrib)

    luasInfo.append(towardsBroom)
    luasInfo.append(towardsBride)
    return luasInfo
    # y = result_outbound.attrib[due]
    print(api_response.content)
    print("done")


@app.route('/getLuasDataJson/',  methods=['GET'])
def getLuasDataJson():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    data = getLuasData()
    data = json.dumps(data)
    return data


if __name__ == '__main__':
    app.run(host='localhost', port=8989)