import math


class TriangleAngle(float):
    def sin(self):
        return math.sin(self)

    def cos(self):
        return math.cos(self)

    def degree(self):
        return math.pi * self

    @staticmethod
    def from_A_B(A: float, B: float, *args, **kwargs):
        A = TriangleAngle(A)
        B = TriangleAngle(B)
        return TriangleAngle(math.pi - A - B)

    @staticmethod
    def from_A_C(A: float, C: float, *args, **kwargs):
        return TriangleAngle.from_A_B(A, C)

    @staticmethod
    def from_B_C(B: float, C: float, *args, **kwargs):
        return TriangleAngle.from_A_B(B, C)


class TriangleArea(float):
    @staticmethod
    def from_a_b_C(a: float, b: float, C: float, *args, **kwargs):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        C = TriangleAngle(C)
        return TriangleArea(0.5 * a * b * C.sin())

    @staticmethod
    def from_a_c_B(a: float, c: float, B: float, *args, **kwargs):
        return TriangleArea.from_a_b_C(a, c, B)

    @staticmethod
    def from_b_c_A(b: float, c: float, A: float, *args, **kwargs):
        return TriangleArea.from_a_b_C(b, c, A)

    @staticmethod
    def from_a_ha(a: float, ha: float, *args, **kwargs):
        a = TriangleEdge(a)
        ha = TriangleHeight(ha)
        return TriangleArea(0.5 * a * ha)

    @staticmethod
    def from_b_hb(b: float, hb: float, *args, **kwargs):
        return TriangleArea.from_a_ha(b, hb)

    @staticmethod
    def from_c_hc(c: float, hc: float, *args, **kwargs):
        return TriangleArea.from_a_ha(c, hc)

    @staticmethod
    def from_a_b_c_p(a: float, b: float, c: float, p: float, *args, **kwargs):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        c = TriangleEdge(c)
        p = TriangleHalfPerimeter(p)
        return TriangleArea(math.sqrt(p * (p - a) * (p - b) * (p - c)))

    @staticmethod
    def from_p_r(p: float, r: float, *args, **kwargs):
        p = TriangleHalfPerimeter(p)
        r = TriangleIncircleRadius(r)
        return TriangleAngle(p * r)


class Edge(float):
    pass


class TriangleEdge(Edge):
    @staticmethod
    def from_a_b_C(a: float, b: float, C: float, *args, **kwargs):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        C = TriangleAngle(C)

        c_square = a**2 + b**2 - 2 * a * b * C.cos()
        c = math.sqrt(c_square)
        return TriangleEdge(c)

    @staticmethod
    def from_a_c_B(a: float, c: float, B: float, *args, **kwargs):
        return TriangleEdge.from_a_b_C(a, c, B)

    @staticmethod
    def from_b_c_A(b: float, c: float, A: float, *args, **kwargs):
        return TriangleEdge.from_a_b_C(b, c, A)

    @staticmethod
    def from_ha_S(ha: float, S: float, *args, **kwargs):
        ha = TriangleHeight(ha)
        S = TriangleArea(S)
        return TriangleEdge(2 * S / ha)

    @staticmethod
    def from_hb_S(hb: float, S: float, *args, **kwargs):
        return TriangleEdge.from_ha_S(hb, S)

    @staticmethod
    def from_hc_S(hc: float, S: float, *args, **kwargs):
        return TriangleEdge.from_ha_S(hc, S)

    @staticmethod
    def from_hc_B(hc: float, B: float, *args, **kwargs):
        hc = TriangleHeight(hc)
        B = TriangleAngle(B)
        return TriangleEdge(hc / B.sin())

    @staticmethod
    def from_hb_C(hc: float, C: float, *args, **kwargs):
        return TriangleEdge.from_hc_B(hc, C)

    @staticmethod
    def from_ha_C(ha: float, C: float, *args, **kwargs):
        return TriangleEdge.from_hc_B(ha, C)

    @staticmethod
    def from_hc_A(hc: float, A: float, *args, **kwargs):
        return TriangleEdge.from_hc_B(hc, A)

    @staticmethod
    def from_ha_B(ha: float, B: float, *args, **kwargs):
        return TriangleEdge.from_hc_B(ha, B)

    @staticmethod
    def from_hb_A(hb: float, A: float, *args, **kwargs):
        return TriangleEdge.from_hc_B(hb, A)


class TriangleHeight(Edge):
    @staticmethod
    def from_a_C(a: float, C: float, *args, **kwargs):
        a = TriangleEdge(a)
        C = TriangleAngle(C)
        return a * C.sin()

    @staticmethod
    def from_a_B(a: float, B: float, *args, **kwargs):
        return TriangleHeight.from_a_C(a, B)

    @staticmethod
    def from_b_C(b: float, C: float, *args, **kwargs):
        return TriangleHeight.from_a_C(b, C)

    @staticmethod
    def from_c_B(c: float, B: float, *args, **kwargs):
        return TriangleHeight.from_a_C(c, B)

    @staticmethod
    def from_a_S(a: float, S: float, *args, **kwargs):
        a = TriangleEdge(a)
        S = TriangleArea(S)
        return TriangleHeight(2 * S / a)

    @staticmethod
    def from_b_S(b: float, S: float, *args, **kwargs):
        return TriangleHeight.from_a_S(b, S)

    @staticmethod
    def from_c_S(c: float, S: float, *args, **kwargs):
        return TriangleHeight.from_a_S(c, S)


class TrianglePerimeter(float):
    def to_triangle_half_perimeter(self):
        return TriangleHalfPerimeter(self * 0.5)

    @staticmethod
    def from_a_b_c(a: float, b: float, c: float, *args, **kwargs):
        a = TriangleEdge(a)
        b = TriangleEdge(b)
        c = TriangleEdge(c)
        return TrianglePerimeter(a + b + c)


class TriangleHalfPerimeter(float):
    def to_triangle_perimeter(self):
        return TrianglePerimeter(self * 2)

    @staticmethod
    def from_a_b_c(a: float, b: float, c: float, *args, **kwargs):
        return TrianglePerimeter.from_a_b_c(a, b, c).to_triangle_half_perimeter()


class Radius(float):
    pass


class TriangleIncircleRadius(float):
    @staticmethod
    def from_p_S(p: float, S: float, *args, **kwargs):
        p = TriangleHalfPerimeter(p)
        S = TriangleArea(S)
        return Radius(S / p)
