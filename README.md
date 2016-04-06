# ThingsPro: Simple log upload server

## Prequest
- Python 2.7 with pip
> sudo apt-get update && sudo apt-get install python2.7 python-pip

- Linux-based environment
- Internet connection (for install dependencies from pypi)

## Install
- `pip install https://github.com/Sanji-IO/pyuploadserver/archive/master.zip` (You may need root privilege)

## Usage

```
moxa@Moxa:~$ pyuploadserver
```
Then, the server will startup and serving HTTP POST method on `http://0.0.0.0:5000`

```
CWD: /tmp/
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
All HTTP POST with content-type:`multipart/form-data` and a file field named `file` will save the uploaded file to current working directory.

### Advanced
By passing environments, you could set the following variables:
- `DEBUG=yes` enable debug console
- `PORT=1234` change listening port to 1234
