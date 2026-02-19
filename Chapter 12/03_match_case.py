def http_status(status):
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 500:
            return "Internal server error"
        case 502 | 503 | 504:
            return "Server is down"
        case _:
            return "Something's wrong with the internet" # default case 
        

print(http_status(200))
print(http_status(400))
print(http_status(418))
print(http_status(500))
print(http_status(502))
print(http_status(999))
