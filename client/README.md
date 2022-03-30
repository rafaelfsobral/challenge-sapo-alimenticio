# Coding challenge

Sapo Alimentício

## Getting Started

### Instalation

Install the dependency to run this project

- [Python](https://www.python.org/downloads/)

# Clone the repository

```
$ git clone git://github.com/rafaelfsobral/challenge-sapo-alimenticio.git


```
# Running the Python server - Execute the steps below in a terminal

```

$ cd challenge-sapo-alimenticio
$ cd flask-server
$ cd venv
$ cd flask-server
$ cd Scripts
$ Execute the command activate
$ cd..
$ cd..
$ Execute the command python server.py

```
# Install project dependencies located in package.json and run the React project in other terminal

```
$ cd challenge-sapo-alimenticio
$ cd client
$ npm install

```

# Project structure - Folders and Files

```
├── client
│   ├── node_modules
│   ├── public
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src
│   │   ├── component
│   │   │   └── Navibar.css
│   │   │   └── Navibar.js
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── reset.css 
│   ├── .gitignore
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
└── flask-server
    ├── data
    │   ├── arquivo_01.txt
    │   ├── arquivo_02.txt
    │   ├── arquivo_03.txt
    │   ├── arquivo_04.txt
    │   ├── arquivo_05.txt
    │   ├── arquivo_06.txt
    │   ├── arquivo_07.txt
    │   ├── arquivo_08.txt
    │   ├── arquivo_09.txt
    ├── venv
    └── server.py
```

### Component operation

Sapo Alimentícios customers want to view the products of the chain classified by
majority of its macronutrients, to facilitate the elaboration of a diet of the
fashion, according to the exemplified specifications in txt files. An api with three routes will be used.

# Route 1

* GET /produtosproteinas
* Data params: prodprot.produtos


``` Example: 
// http://localhost:3000/produtosproteinas
[
    {
        "Nome":"Picadinho",
        "Quantidade":"100",
        "Proteínas":"53",
        "Carboidratos":"2",
        "Gorduras":"5"
    }
]
```

---
# Route 2

* GET /produtoscarboidratos
* Data params: prodcarb.produtos

``` Example: 
// http://localhost:3000/produtoscarboidratos
[
    {
        "Nome":"Cará Inhame ou mandioquinha",
        "Quantidade":"100",
        "Proteínas":"5",
        "Carboidratos":"32",
        "Gorduras":"5"
    }
]
```
# Route 3

* GET /produtosgorduras
* Data params: prodgord.produtos

``` Example: 
// http://localhost:3000/produtosgorduras
[
    {
        "Nome":"Azeite",
        "Quantidade":"100",
        "Proteínas":"4",
        "Carboidratos":"2",
        "Gorduras":"54"
    }
]
```