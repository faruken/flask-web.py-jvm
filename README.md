# Flask and web.py meet JVM (or how to use Apache Shiro with them)

This is a small proof-of-concept project that mixes Flask, web.py and Apache Shiro.

[Apache Shiro](http://shiro.apache.org/) is a Java security framework that performs authentication, authorization, cryptography, and session management. You may also be interested in reading [this article](http://www.infoq.com/articles/apache-shiro) as well.

This is a demonstration of [Flask](http://flask.pocoo.org/) and [web.py](http://webpy.org/) with [WTForms](http://wtforms.simplecodes.com/) running on [Jython](http://www.jython.org/) and uses [Apache Shiro](http://shiro.apache.org/).

## Installation

1. Please refer to `requirements.txt` in each folder to install mandatory Python libraries. I have created a virtualenv, you may want to do as well.

2. Then add Apache Shiro libraries to your `CLASSPATH`.

3. Install Jython (I have tested on Jython 2.7a2).

4. Run the program: `jython -Dpython.path=$PYTHONPATH main.py`

## Default Login

This demonstration uses `ini` files. A sample ini file is provided (`shiro.ini`). Default login details are:

- Username: shiro, Password: shiro
