# import fastapi
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
    # """
    # The function `home` returns a dictionary with a message indicating that the user is on the home
    # page.
    # :return: A dictionary with a key "message" and value "Your on home page" is being returned.
    # """
def home():
    return {
        "message": "Your on home page"
    }