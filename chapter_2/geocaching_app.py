#coding utf-8
from utils.geo_functions import open_vector_file
from utils.geo_functions import transform_geometries

import numpy as np
import math

class GeocachingApp(object):
    def __init__(self, data_file=None)
        """
        Application Class
        :param data_file: An OGR compatible file with geocaching points
        """

    #Part 1
    self._datasource = None
    self._transformed_geoms = None

    #Part 2
    if data_file:
        self.open_file(data_file)
    


if __name__ == '__main__':
    main()