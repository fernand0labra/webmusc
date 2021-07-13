########################################################################
#                      DEPENDENCY INSTALLATION FILE                    #                             
########################################################################

# Define UTF-8 Encoding
chcp 65001

# Create the Virtual Environment
py -3 -m venv myVirtualEnvironment

# Activate it on the system
.\myVirtualEnvironment\Scripts\activate

# Install Dependencies
pip install flask

# Run Server
flask run