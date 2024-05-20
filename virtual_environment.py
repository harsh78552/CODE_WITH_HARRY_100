"""Create a virtual environment
 pyhon -m venv myenv"""

"""Activate the virtual environment
directory_name\Scripts\activate"""

"""Deactivate the virtual environment
              deactivate"""

"""output the list of installed package in their version of file
   pip freeze > requirements.txt"""

"""Install the package listed in the requirements.txt file
    pip install -r requirements.txt"""

import pandas as pd
print(pd.__version__)
