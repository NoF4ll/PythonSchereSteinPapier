import requests


def send_request(username, countScissors, countRock, countPaper, countSpock, countLizard,
                 apiIP="http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl += "?username=" + str(username) + "&voteScissors=" + str(countScissors)
    reqUrl += "&voteRock=" + str(countRock) + "&votePaper=" + str(countPaper)
    reqUrl += "&voteSpock=" + str(countSpock) + "&voteLizard=" + str(countLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode
