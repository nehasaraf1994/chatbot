from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from urllib.parse import urlencode
# Create your views here.
def hook_list(request):
    #req = request.get_json()
    req = json.loads(request.body.decode('UTF-8'))
    #req = request.body.decode('UTF-8').json()
    #req = req['result']
    # print("Request:")
    # print(json.dumps(req, indent=4))
    res = processRequest(req)
    # res = json.dumps(res, indent=4)
    # print(res)
    # r = get_response(res)
    # r.headers['Content-Type'] = 'application/json'
    # return r

def processRequest(req):
    if req.get("result").get("action") != "appointment":
        return {}
    baseurl = "https://192.168.0.103/api/"
    yql_query = makeYqlQuery(req)
    if yql_query is None:
        return {}
    #yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    yql_url = urllib.parse.urljoin(baseurl, '/' ,yql_query, "/?format=json")
    result = urllib.request.urlopen(yql_url)
    data = json.loads(result.read().decode('UTF-8'))
    res = makeWebhookResult(data)
    return res

def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    types = parameters.get("types")
    if types is None:
        return None

    return types


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    name = result.get("ndoc")
    des = result.get("desgn")

    speech = name + ":" + des 

    #speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
    #         ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "agent"
    }