import ml
import requests

req = requests.Session()
#"who is batman"
def main():
    print("STARTED")
    while True:
        r = req.get("https://thefury.pythonanywhere.com/qna-backend")
        r=  r.text
        if len(r) != 0:
            print("PROSSESING")
            res = ml.ml_app(r)
            req.get("https://thefury.pythonanywhere.com/res-qna-backend?r="+res)
            print("RESPONDED")
            
main()
