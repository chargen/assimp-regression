import sys
from os.path import dirname
sys.path.append(dirname(__file__))
sys.path.append("assimp_regression")

from assimp_regression.tools import regression_ui
regression_ui.main()
