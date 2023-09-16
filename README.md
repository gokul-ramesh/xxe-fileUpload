<h1> xxe-fileUpload </h1>

<p> A minimalistic application vulnerable to XXE through File Upload </p>
This application insecurely processes the XML document!!<br>

<h2> XXE - XML External Entity Injection</h2>
An XML injection attacks happens when XML input containing a reference to an external entity is parsed using a weakly configured XML parser. This may lead to disclosure of sensitive data, DoS, SSRF and other major system impacts.<br>
An external entity that is used to access local or remote content via declared system identifier, which is then dereferenced by the XML parser when processing the entity.  The parser then replaces the named external entities with the contents derefenced by the identifier.<br>
Attack vectors apply the usage of external DTDs, stylesheets, schemas, etc.

<h2> Application Setup</h2>
<h3>Requirements</h3>
  Python3

<h3>Installation using Docker</h3>
Clone the repository
```git clone https://github.com/gokul-ramesh/xxe-fileUpload.git```
