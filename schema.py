import math


class TriangleAngle(float):
    def sin(self):
        return math.sin(self)

    def cos(self):
        return math.cos(self)

    def degree(self):
        return math.pi * self

    @staticmethod
    def from_A_B(A: float, B: float):
        A = TriangleAngle(A)
        B = TriangleAngle(B)
        return TriangleAngle(math.pi - A - B)


class TriangleArea(float):
    @staticmethod
    def from_a_b_C(a: float, b: float, C: float):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        C = TriangleAngle(C)
        return TriangleArea(0.5 * a * b * C.sin())

    @staticmethod
    def from_a_ha(a: float, ha: float):
        a = TriangleEdge(a)
        ha = TriangleHeight(ha)
        return TriangleArea(0.5 * a * ha)

    @staticmethod
    def from_a_b_c_p(a: float, b: float, c: float, p: float):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        c = TriangleEdge(c)
        p = TriangleHalfPerimeter(p)
        return TriangleArea(math.sqrt(p * (p - a) * (p - b) * (p - c)))

    @staticmethod
    def from_p_r(p: float, r: float):
        p = TriangleHalfPerimeter(p)
        r = TriangleIncircleRadius(r)
        return TriangleAngle(p * r)


class Edge(float):
    pass


class TriangleEdge(Edge):
    @staticmethod
    def from_a_b_C(a: float, b: float, C: float):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        C = TriangleAngle(C)

        c_square = a**2 + b**2 - 2 * a * b * C.cos()
        c = math.sqrt(c_square)
        return TriangleEdge(c)

    @staticmethod
    def from_ha_S(ha: float, S: float):
        ha = TriangleHeight(ha)
        S = TriangleArea(S)
        return TriangleEdge(2 * S / ha)

    @staticmethod
    def from_hc_B(hc: float, B: float):
        hc = TriangleHeight(hc)
        B = TriangleAngle(B)
        return TriangleEdge(hc / B.sin())


class TriangleHeight(Edge):
    @staticmethod
    def from_a_C(a: float, C: float):
        a = TriangleEdge(a)
        C = TriangleAngle(C)
        return a * C.sin()

    @staticmethod
    def from_a_S(a: float, S: float):
        a = TriangleEdge(a)
        S = TriangleArea(S)
        return TriangleHeight(2 * S / a)


class TrianglePerimeter(float):
    def to_triangle_half_perimeter(self):
        return TriangleHalfPerimeter(self * 0.5)

    @staticmethod
    def from_a_b_c(a: float, b: float, c: float):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        c = TriangleEdge(c)
        return TrianglePerimeter(a + b + c)


class TriangleHalfPerimeter(float):
    def to_triangle_perimeter(self):
        return TrianglePerimeter(self * 2)

    @staticmethod
    def from_a_b_c(a: float, b: float, c: float):
        return TrianglePerimeter.from_a_b_c(a, b, c).to_triangle_half_perimeter()


class Radius(float):
    pass


class TriangleIncircleRadius(float):
    @staticmethod
    def from_p_S(p: float, S: float):
        p = TriangleHalfPerimeter(p)
        S = TriangleArea(S)
        return Radius(S / p)
