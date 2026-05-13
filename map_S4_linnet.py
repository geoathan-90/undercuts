import numpy as np


XLIM = (100, 500)
YLIM = (100, 650)

boundaries = {
    0: [(145, 100), (450, 370), (450, 650)],
    1: [(105, 100), (150, 132.5), (400, 355), (400, 650)],
    2: [(100, 147.5), (282.5, 280), (350, 340), (350, 650)],
    3: [(100, 200), (300, 345), (300, 650)],
    4: [(100, 250), (250, 360), (250, 650)],
    5: [(100, 302.5), (200, 375), (200, 650)],
    6: [(100, 355), (150, 390), (150, 650)],
}


tower = (310, 345, 1.23)

def boundary_x(boundary_id, y):
    """
        Return the x-limit of one boundary at vertical coordinate y.
        Points to the right or bottom of this limit are considered no-go.
    """

    points = boundaries[boundary_id]

    xs = np.array([p[0] for p in points])
    ys = np.array([p[1] for p in points])

    return np.interp(y, xs, ys)



boundaries = {
    0: [(145, 100), (450, 370), (450, 650)],
    1: [(105, 100), (150, 132.5), (400, 355), (400, 650)],
    2: [(100, 147.5), (282.5, 280), (350, 340), (350, 650)],
    3: [(100, 200), (300, 345), (300, 650)],
    4: [(100, 250), (250, 360), (250, 650)],
    5: [(100, 302.5), (200, 375), (200, 650)],
    6: [(100, 355), (150, 390), (150, 650)],
}

def max_angle(tower, boundaries):
    """
        Return the maximum line angle (in degrees)
    """

    H, V, angle = tower
    print(H)

    max_angle = 6

    for boundary_id in boundaries:
        min_Vert = boundary_y(boundary_id, H)   
        print(min_Vert)

    return H, V, angle


def boundary_y_at_x(boundary_points, x):
    """
        Return the y-value where one boundary crosses a given x-value.

        Vertical segments are ignored, because for x = constant they do not
        correspond to one unique y-value.
    """

    for p1, p2 in zip(boundary_points[:-1], boundary_points[1:]):
        x1, y1 = p1
        x2, y2 = p2

        # Ignore vertical segments
        if x1 == x2:
            continue

        # Check whether x lies inside this segment's x-range
        xmin = min(x1, x2)
        xmax = max(x1, x2)

        if xmin <= x <= xmax:
            t = (x - x1) / (x2 - x1)
            y = y1 + t * (y2 - y1)
            return y

    return None


def all_boundary_y_values_at_x(x):
    """
    Return all valid boundary y-values for a given x.
    """

    results = []

    for boundary_id, points in boundaries.items():
        y = boundary_y_at_x(points, x)

        if y is not None:
            results.append((boundary_id, y))

    return results

values = all_boundary_y_values_at_x(x)

    for boundary_id, y in values:
        print(f"Boundary {boundary_id}: y = {y:.2f}")

def main():
    #a = max_angle(tower, boundaries)
    a = boundary_y(0, 310)
    print(a)

if __name__ == "__main__":
    main()