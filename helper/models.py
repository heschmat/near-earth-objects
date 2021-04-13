""" Represent models for near-Earth objects and their close approaches.
"""

class NearEarthObject:
    """ Represents Near-Earth Object (NEO).

    """
    def __init__(self, info_dict) -> None:
        """
        """
        name = info_dict['name']
        d = info_dict['diameter']
        # Initialize the NEO object.
        self.name = None if len(name) == 0 else name
        self.designation = info_dict['pdes']
        self.diameter = float('nan') if len(d) == 0 else float(d)
        self.hazardous = True if info_dict['pha'] == 'Y' else False
    
    def __repr__(self):
        """Return a computer-readable string representation of the NEO object."""
        return(
            f'NearEarthObject(name={self.name!r}, '
            f'designation={self.designation!r}, diameter={self.diameter:.3f}, '
            f'hazardous={self.hazardous!r})'
        )
