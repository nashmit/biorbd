from .inertia_parameters import InertiaParameters
from .marker import Marker
from .segment_coordinate_system import SegmentCoordinateSystem


class Segment:
    def __init__(
        self,
        name,
        parent_name: str = "",
        translations: str = "",
        rotations: str = "",
        segment_coordinate_system: SegmentCoordinateSystem = None,
        inertia_parameters: InertiaParameters = None,
    ):
        """
        Create a new generic segment.

        Parameters
        ----------
        name
            The name of the segment
        parent_name
            The name of the segment the current segment is attached to
        translations
            The sequence of translation
        rotations
            The sequence of rotation
        inertia_parameters
            The inertia parameters of the segment
        """

        self.name = name
        self.parent_name = parent_name
        self.translations = translations
        self.rotations = rotations
        self.markers = []
        self.segment_coordinate_system = segment_coordinate_system
        self.inertia_parameters = inertia_parameters

    def add_marker(self, marker: Marker):
        """
        Add a new marker to the segment

        Parameters
        ----------
        marker
            The marker to add
        """
        self.markers.append(marker)
