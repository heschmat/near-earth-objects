""" A database encapsulating collections of near-Earth objects
and their close approaches.


"""


class NEODatabase:
    def __init__(self, neos, approaches) -> None:
        """
        """
        self._neos = neos
        self._approaches = approaches

        self._names_neo = {neo.name: neo for neo in self._neos}
        self._designations_neo = {neo.designation: neo for neo in self._neos}

        # Link the `NearEarthObject` & `CloseApproach`.
        # They connection is per their `designations`.
        for app in self._approaches:
            # Find the `NEO` associated with the `CloseApproach`.
            neo = self._designations_neo[app.designation]
            app.neo = neo
            # Append the current `CloseApproach` to the list of
            # close-approaches associated with the `NEO`.
            neo.close_approaches.append(app)

    def get_neo_by_name(self, neo_name):
        """ Return NEO by its name. If no match is found, return `None`.

        Arguments:
        :neo_name {str}

        Returns:
        : {NearEarthObject} NEO that corresponds to the asked name.
        """
        return self._names_neo.get(neo_name, None)

    def get_neo_by_designation(self, neo_desig):
        """ Return NEO by its primary designation.
        If no match is found, return `None`.

        Arguments:
        :neo_desig {str}

        Returns:
        : {NearEarthObject} NEO that corresponds to the asked designation.
        """
        return self._designations_neo.get(neo_desig, None)
