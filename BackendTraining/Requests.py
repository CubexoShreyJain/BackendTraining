import requests
from requests.exceptions import HTTPError

"""requests return an Response class instance"""
x = requests.get("https://v2.jokeapi.dev/joke/Any") # Return Resonse instance

print("Status Code of req: ", x.status_code)


if (x): # return True if status code between 200 - 400, else False
    print("Request sucessfull, but not sure if content returned or not.")
else:
    print("Request fail to at some point")
    
    
# Happy and negative testing
for url in ["https://v2.jokeapi.dev/joke/Any", "https://v2.jokeapi.dev/jofe/Any"]:
    try:
        res = requests.get(url, timeout=1)
        res.raise_for_status() # Raises HTTPError for unsuccessful status code.else do nothing
    except HTTPError:
        print("Request unsuccessful: invalid request")
    except Exception:
        print("other exception")
    else:
        print("Success")
        
        
# Payload: useful info in response is called payload
print(x.content) # Print raw content, data in binary form
print(x.text)    # convert data to string format -- only this method keeps the indentation intact
print(x.json())  # Convert json format to dictonary -- **important\
print()

# Header: Gives useful info about the payload like, time/date of arrival, time took to get response,etc.
print(x.headers) # It's not a function, but a dictonary

# It's case INsensitive, i.e.it provide us to access elements through both below methods
print(x.headers['content-type'])
print(x.headers['Content-TYpe']) # Returns data type of response


# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+