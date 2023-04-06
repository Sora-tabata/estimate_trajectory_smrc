import numpy as np
import yaml
from trim import TrimImages
import io


class EditYaml():
    def __init__(self):
        self.size = TrimImages().createTrimedImages()[1:-1].split(',')

    def pass2yaml(self):
        right = int(self.size[0])
        bottom = int(self.size[1])
        with open ('./calib.yaml', 'r') as file:
            yml = yaml.safe_load(file)
            yml["Camera.width"] = right
            yml["Camera.height"] = bottom
            yml["Camera.type"] = str("PinHole")
        with io.open('./calib.yaml', 'w') as newfile:
            newfile.write("%YAML:1.0\n")
            yaml.dump(yml, newfile)
EditYaml().pass2yaml()

