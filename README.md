# xxe-fileUpload 

 A minimalistic application vulnerable to XXE through File Upload
This application insecurely processes the XML document!!<br>

## XXE - XML External Entity Injection
An XML injection attacks happens when XML input containing a reference to an external entity is parsed using a weakly configured XML parser. This may lead to disclosure of sensitive data, DoS, SSRF and other major system impacts.<br>
An external entity that is used to access local or remote content via declared system identifier, which is then dereferenced by the XML parser when processing the entity.  The parser then replaces the named external entities with the contents derefenced by the identifier.<br>
Attack vectors apply the usage of external DTDs, stylesheets, schemas, etc.

## Application Setup
### Requirements
* Python3
### Installation
* Clone and move into the repository
```sh
git clone https://github.com/gokul-ramesh/xxe-fileUpload.git
cd xxe-fileUpload/
```
#### Using Docker
* Ensure docker engine is installed
  ```sh
  docker --version
  ```

* Build the image
```sh
docker build -t xxe-fileupload:latest .
```
Run the docker image
```
docker run -p 8000:8000 xxe-fileupload:latest
```
#### Without Docker
* Populate the DB
```python
python manage.py makemigratations
python manage.py migrate
```
* Run server
```
python manage.py runserver
```


* App is available at port 8000 by default
