# -*- coding: utf-8 -*-
"""세 종의 32x32 스프라이트를 한 픽셀씩 배치한다. CLI 내장 생성기(sprite_write)는 쓰지 않는다.

행마다 (시작열, 문자열) 스팬을 순서대로 얹으며, 뒤에 오는 스팬이 앞의 것을 덮어쓴다.
광원은 좌상단 하나로 통일했고, 그림자는 차가운 쪽 하이라이트는 따뜻한 쪽으로 색상을 틀었다.
"""
import json, os, sys

N = 32

def canvas(spans_by_row):
    rows = []
    for y in range(N):
        buf = ["."] * N
        for x0, text in spans_by_row.get(y, []):
            for i, ch in enumerate(text):
                if 0 <= x0 + i < N:
                    buf[x0 + i] = ch
        rows.append("".join(buf))
    return rows

def mirror(x0, text):
    """15.5 열을 축으로 좌우를 뒤집은 스팬을 돌려준다."""
    return (N - 1 - (x0 + len(text) - 1), text[::-1])


# ── Pixiel [Fairy] ── 진주빛 치비, 펜촉 볏, 좌우 색상 램프 날개 ──────────────
PIXIEL_PAL = {
    "k": "#2b1d3f", "a": "#7a56ad", "b": "#a97fd4", "c": "#cfb2ef", "d": "#f8f0ff",
    "e": "#241733", "w": "#ffffff", "p": "#ff9ab8",
    "y": "#ffd76e", "m": "#c98f2c",
    "t": "#56b8ff", "g": "#4fd6a0", "o": "#ffb347", "r": "#ff6b8a",
}
PIXIEL = {
    1:  [(15, "k")],
    2:  [(14, "kyk")],
    3:  [(13, "kyyyk")],
    4:  [(12, "kyyyyyk")],
    5:  [(13, "kymyk")],
    6:  [(14, "kmk")],
    7:  [(11, "kkkkkkkkkk")],
    8:  [(9,  "kdddcccccccbk")],
    9:  [(8,  "kddcccccccccbbk")],
    10: [(7,  "kddcccccccccccbbk")],
    11: [(7,  "kdcccccccccccccbk")],
    12: [(7,  "kdcceeecccceeebbk")],
    13: [(7,  "kdccweeccccweebbk")],
    14: [(7,  "kdcceeecccceeebbk")],
    15: [(7,  "kcppcccckkcccppbk")],
    16: [(7,  "kccccccbbbbbbbbak")],
    17: [(8,  "kcccccbbbbbbaak")],
    18: [(9,  "kccbbbbbbaaak")],
    19: [(10, "kcbbbbbaaak"), (7, "ktk"), mirror(7, "ktk")],
    20: [(10, "kcbbbbbbaaak"), (5, "kgttk"), mirror(5, "kgttk")],
    21: [(9,  "kccbbbbbbaaaak"), (3, "kggttk"), mirror(3, "kggttk")],
    22: [(9,  "kcbbbbbbbaaaak"), (1, "kroggttk"), mirror(1, "kroggttk")],
    23: [(9,  "kcbbbbbbbaaaak"), (1, "kroggttk"), mirror(1, "kroggttk")],
    24: [(9,  "kbbbbbbbbaaaak"), (3, "kggttk"), mirror(3, "kggttk")],
    25: [(10, "kbbbbbbaaaak"), (5, "kgttk"), mirror(5, "kgttk")],
    26: [(10, "kbbbbbbaaaak"), (7, "ktk"), mirror(7, "ktk")],
    27: [(10, "kbbbk"), (17, "kaaak")],
    28: [(10, "kaaak"), (17, "kaaak")],
    29: [(10, "kkkkk"), (17, "kkkkk")],
}

# ── Reactyl [Sky] ── 뒤로 젖혀진 볏, 주황 부리, 젖힌 날개, 상태 궤도 점 ──────
REACTYL_PAL = {
    "k": "#0f2a39", "a": "#1c6e86", "b": "#2fa9c4", "c": "#63d8e8", "d": "#d6fbff",
    "e": "#0b1c27", "w": "#ffffff",
    "o": "#ff9f2e", "y": "#ffd07a", "v": "#9b8cff",
}
REACTYL = {
    3:  [(19, "kddk")],
    4:  [(17, "kdddk")],
    5:  [(15, "kddcck")],
    6:  [(13, "kddccck")],
    7:  [(11, "kkkkkkkkkk")],
    8:  [(9,  "kdddcccccccbk")],
    9:  [(8,  "kddcccccccccbbk")],
    10: [(7,  "kddcccccccccccbbk"), (4, "v"), mirror(4, "v")],
    11: [(7,  "kdcccccccccccccbk"), (3, "vv"), mirror(3, "vv")],
    12: [(7,  "kdcceeecccceeebbk"), (4, "v"), mirror(4, "v")],
    13: [(7,  "kdccweeccccweebbk")],
    14: [(7,  "kdcceeecccceeebbk")],
    15: [(7,  "kdcccccccccccccbk"), (13, "kyoook")],
    16: [(7,  "kccccccbbbbbbbbak"), (14, "kyok")],
    17: [(8,  "kcccccbbbbbbaak")],
    18: [(9,  "kccbbbbbbaaak")],
    19: [(10, "kcbbbbbaaak")],
    20: [(10, "kcbbbbbbaaak"), (6, "kcck"), mirror(6, "kcck")],
    21: [(9,  "kccbbbbbbaaaak"), (4, "kdccbk"), mirror(4, "kdccbk")],
    22: [(9,  "kcbbbbbbbaaaak"), (2, "kdcccbbk"), mirror(2, "kdcccbbk")],
    23: [(9,  "kcbbbbbbbaaaak"), (2, "kdcccbbk"), mirror(2, "kdcccbbk")],
    24: [(9,  "kbbbbbbbbaaaak"), (4, "kdcbbk"), mirror(4, "kdcbbk")],
    25: [(10, "kbbbbbbaaaak"), (6, "kcbk"), mirror(6, "kcbk")],
    26: [(10, "kbbbbbbaaaak")],
    27: [(11, "kbbk"), (17, "kaak")],
    28: [(11, "kbbk"), (17, "kaak")],
    29: [(9,  "kyook"), (18, "kooak")],
    30: [(9,  "kkkkk"), (18, "kkkkk")],
}

# ── Hexadrake [Dragon] ── 강철 뿔, 육중한 몸통, 가슴의 용융 육각 코어 ────────
HEXADRAKE_PAL = {
    "k": "#120e1f", "a": "#332a52", "b": "#4d4177", "c": "#6f5fa0", "d": "#a294d1",
    "s": "#95a0bd", "e": "#0d0916",
    "o": "#ff8f26", "y": "#ffd45e", "w": "#fff6d0",
}
HEXADRAKE = {
    3:  [(10, "ks"), mirror(10, "ks")],
    4:  [(10, "ksk"), mirror(10, "ksk")],
    5:  [(11, "ksk"), mirror(11, "ksk")],
    6:  [(11, "kssk"), mirror(11, "kssk")],
    7:  [(11, "kkkkkkkkkk")],
    8:  [(9,  "kdddcccccccbk")],
    9:  [(8,  "kddcccccccccbbk")],
    10: [(7,  "kddcccccccccccbbk")],
    11: [(7,  "kdcccccccccccccbk")],
    12: [(7,  "kdcceyecccceyebbk")],
    13: [(7,  "kdccywyccccywybbk")],
    14: [(7,  "kdcceyecccceyebbk")],
    15: [(7,  "kdcccccccccccccbk")],
    16: [(8,  "kdcccccccccccbak"), (13, "kooook")],
    17: [(9,  "kdcccccccccbak"), (13, "koyyok")],
    18: [(10, "kdcccccccbak"), (14, "kook")],
    19: [(11, "kdcccccbak")],
    20: [(8,  "kdccccccccccccak")],
    21: [(7,  "kdccccccccccccccak"), (3, "kddk"), mirror(3, "kddk")],
    22: [(7,  "kdccccccccccccccak"), (13, "kooook"), (2, "kdcdk"), mirror(2, "kdcdk")],
    23: [(7,  "kdccccccccccccccak"), (12, "koyyyyok"), (1, "kdccdk"), mirror(1, "kdccdk")],
    24: [(7,  "kdccccccccccccccak"), (12, "koywwyok"), (1, "kdccdk"), mirror(1, "kdccdk")],
    25: [(7,  "kdccccccccccccccak"), (12, "koyyyyok"), (2, "kdcdk"), mirror(2, "kdcdk")],
    26: [(7,  "kdccccccccccccccak"), (13, "kooook"), (3, "kddk"), mirror(3, "kddk")],
    27: [(8,  "kdccccccccccccak")],
    28: [(10, "kbbbk"), (17, "kaaak")],
    29: [(9,  "ksssk"), (18, "ksssk")],
    30: [(9,  "kkkkk"), (18, "kkkkk")],
}

SPRITES = {
    "pixiel":    dict(hue=272, body="round",    eyes="sparkle", crest="antenna", pal=PIXIEL_PAL,    spans=PIXIEL),
    "reactyl":   dict(hue=192, body="teardrop", eyes="sharp",   crest="horn",    pal=REACTYL_PAL,   spans=REACTYL),
    "hexadrake": dict(hue=258, body="blocky",   eyes="sharp",   crest="horn",    pal=HEXADRAKE_PAL, spans=HEXADRAKE),
}

def build(spec):
    rows = canvas(spec["spans"])
    used = {ch for r in rows for ch in r if ch != "."}
    unknown = used - set(spec["pal"])
    assert not unknown, unknown
    pal = {k: v for k, v in spec["pal"].items() if k in used}
    return {"size": N, "hue": spec["hue"], "body": spec["body"], "eyes": spec["eyes"],
            "crest": spec["crest"], "palette": pal, "rows": rows}

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for name, spec in SPRITES.items():
        if only and name != only:
            continue
        sp = build(spec)
        print("=" * 34, name)
        for i, r in enumerate(sp["rows"]):
            print("%2d %s" % (i, r))
        out = sys.argv[2] if len(sys.argv) > 2 else None
        if out:
            json.dump(sp, open(os.path.join(out, name + ".json"), "w"), indent=2)
