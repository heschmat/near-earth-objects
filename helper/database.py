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
