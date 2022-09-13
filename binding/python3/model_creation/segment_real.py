from .inertia_parameters_real import InertiaParametersReal
from .marker_real import MarkerReal
from .segment_coordinate_system_real import SegmentCoordinateSystemReal


class SegmentReal:
    def __init__(
        self,
        name,
        parent_name: str = "",
        segment_coordinate_system: SegmentCoordinateSystemReal = None,
        translations: str = "",
        rotations: str = "",
        inertia_parameters: InertiaParametersReal = None,
        mesh: tuple[tuple[float, float, float], ...] = None,
    ):
        self.name = name
        self.parent_name = parent_name
        self.translations = translations
        self.rotations = rotations
        self.markers = []
        self.segment_coordinate_system = segment_coordinate_system
        self.inertia_parameters = inertia_parameters
        self.mesh = mesh

    def add_marker(self, marker: MarkerReal):
        self.markers.append(marker)

    def __str__(self):
        # Define the print function so it automatically format things in the file properly<
        out_string = f"segment {self.name}\n"
        if self.parent_name:
            out_string += f"\tparent {self.parent_name}\n"
        if self.segment_coordinate_system:
            out_string += f"\tRT {self.segment_coordinate_system}\n"
        if self.translations:
            out_string += f"\ttranslations {self.translations}\n"
        if self.rotations:
            out_string += f"\trotations {self.rotations}\n"
        if self.inertia_parameters:
            out_string += str(self.inertia_parameters)
        if self.mesh:
            for m in self.mesh:
                out_string += f"\tmesh {m[0]} {m[1]} {m[2]}\n"
        out_string += "endsegment\n"

        # Also print the markers attached to the segment
        if self.markers:
            for marker in self.markers:
                out_string += str(marker)
        return out_string
