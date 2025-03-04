import requests

REQUEST_URL_GET = "https://learningserver.masterschool.com/http-basics/get-me"
REQUEST_URL_POST = "https://learningserver.masterschool.com/http-basics/post-me"
OUTPUT_FILE_NAME = "output.html"

def save_to_file(text, file_name):
    with open(file_name, "w") as file:
        file.write(text)

def get_req():
    usr_name = input("enter your name: ")
    usr_color = input("enter your favourite colour: ")
    params = f"?name={usr_name}&color={usr_color}"
    url = REQUEST_URL_GET + params
    res = requests.get(url)
    save_to_file(res.text, OUTPUT_FILE_NAME)
    print(f"Successfully saved to file {OUTPUT_FILE_NAME}")

def post_req():
    usr_name = input("enter your name: ")
    usr_pass = input("enter your pass: ")
    data = {
        "username" : usr_name,
        "password" : usr_pass
    }
    res = requests.post(REQUEST_URL_POST, data=data)
    print(res.text)


def main():
    #get_req()
    post_req()


if __name__ == "__main__":
    main()
