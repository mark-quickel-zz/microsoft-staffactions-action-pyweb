from flask import Flask, render_template
import urllib.request, json

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/staffactions')
def hello():
    # Render the page
    url = "https://constoso-apim.azure-api.net/staffaction-actions-fn/actions"
    headers = {'Ocp-Apim-Subscription-Key': ''}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    #return data;
    dict = json.loads(data)
    
    return render_template ("staffactions.html", actions=dict)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)