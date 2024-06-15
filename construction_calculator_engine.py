class ConstructionCalculatorEngine:
    """
    Class to perform calculations for ceilings panels and slabs.

    Methods:
    - calculate_ceiling_panels(width: float, length: float) -> str:
        Calculates the number of ceiling panels needed based on the given width and length.
    - calculate_slab_area(width: float = None, length: float = None, direction: str = None, has_tracks: bool = False, n_tracks: int = None, track_length: float = None) -> str:
        Calculates the slab area based on the provided specifications.
    """

    def calculate_ceiling_panels(self, width, length):
        """
        Calculates the number of ceiling panels needed based on the given width and length.

        Parameters:
        - width (float): The width of the area to be covered by ceiling panels in meters.
        - length (float): The length of the area to be covered by ceiling panels in meters.

        Returns:
        - list of dict: A list of dictionaries containing suggestions for the number of ceiling panels,
        the respective length of each segment, and the total area covered by each suggestion.

        Example:
        ```
        engine = ConstructionCalculatorEngine()
        result = engine.calculate_ceiling_panels(5, 4)
        print(result)
        ```
        """

        panel_width = 0.2

        # Number of ceiling panels per meter of width.
        pieces_per_meter = width / panel_width
        suggestions = []

        # Iterate to suggest different ways to divide the length into segments.
        for lim in range(2, 7):
            # Calculate the suggestion for the number of ceiling panels.
            suggestion = (length / lim) * pieces_per_meter
            # Calculate the total area that will be covered.
            area = round(suggestion + 0.5) * lim * panel_width

            # Check if the suggested number of panels is even (for better aesthetics).
            if int(suggestion) % 2 == 0:
                suggestions.append(
                    {
                        "pieces": round(suggestion, 1),
                        "pieces_length": lim,
                        "area": round(area, 2),
                    }
                )

        # Return the suggestions as a dict
        return suggestions

    def calculate_slab_area(
        self,
        width=None,
        length=None,
        direction=None,
        has_track=False,
        n_track=None,
        track_length=None,
    ):
        """
        Calculates the slab area based on the provided specifications.

        Parameters:
        - width (float, optional): The width of the slab area in meters.
        - length (float, optional): The length of the slab area in meters.
        - direction (str, optional): The direction in which the slab will be aligned ("width" for width or "length" for length).
        - has_track (bool, optional): Indicates if the slab has supporting tracks.
        - n_track (int, optional): The number of supporting tracks, if applicable.
        - track_length (float, optional): The length of each track in meters, if applicable.

        Returns:
        - float or tuple: If `has_track` is True, returns the calculated area of the slab.
        If `has_track` is False, returns a tuple containing the number of tracks (`n_track`),
        the effective length used for calculation (`length_choosen`), and the calculated area of the slab.

        Example:
        ```
        engine = ConstructionCalculatorEngine()
        result = engine.calculate_slab_area(6, 4, 'width')
        print(result)
        ```
        """

        track_width = 0.43

        if has_track:
            # Calculate the area of the slab based on the number of tracks and their length.
            area = n_track * track_width * track_length
            return area
        else:
            # Determine the effective length used for calculation based on the alignment direction.
            length_choosen = width if direction == "width" else length
            # Width of each track in meters
            n_track = length_choosen / track_width
            aligned_length = round(n_track + 0.5) * track_width
            area = width * aligned_length
            return n_track, length_choosen, area


if __name__ == "__main__":
    engine = ConstructionCalculatorEngine()
    print(engine.calculate_ceiling_panels(5, 4))
    print(engine.calculate_slab_area(6, 4, "width"))
