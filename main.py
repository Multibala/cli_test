import typer
import validators
import requests

app = typer.Typer()

@app.command()
def urlcheck(url:str):
    valid = validators.url(url)
    methods = {url:{}}
    def check_method(r,method_name):
        if r.status_code != 405:
            methods[url][method_name] = str(r.status_code)

    if valid:
        check_method(requests.get(url),method_name='GET') 
        check_method(requests.post(url),method_name='POST')
        check_method(requests.patch(url),method_name='PATCH')
        check_method(requests.delete(url),method_name='DELETE')
        check_method(requests.put(url=url),method_name='PUT')
        print(methods)
    else:
        print(f'Строка "{url}" не является ссылкой')




if __name__ == '__main__':
    app()
