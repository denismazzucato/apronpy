# apronpy

Python Interface for the 
[APRON Numerical Abstract Domain Library](http://apron.cri.ensmp.fr/library/).

## Getting Started 

### Prerequisites

* Install [**APRON**](https://github.com/antoinemine/apron)

* Install [**Python 3.x**](http://www.python.org/)

### Installation

* Create a virtual Python environment:

    | Linux or Mac OS X                   |
    | ----------------------------------- |
    | `virtualenv --python=python3 <env>` |

* Install apronpy in the virtual environment:

    | Linux or Mac OS X                 |
    | --------------------------------- |
    | `./<env>/bin/pip install apronpy` | 

## Troubleshooting

For Mac OS X users, if you get an OSError when CDLL tries to load the apron
libraries, try setting the APRON_LD_PATH environment variable to the
directory where the libraries are located.
