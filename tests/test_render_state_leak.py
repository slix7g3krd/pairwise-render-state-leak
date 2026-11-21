import pytest
import math
from render import render_state_leak as mod

CASES = [
    ("opaque", 'm.blend_for("opaque") == "none"'),
    ("fx", 'm.blend_for("fx") == "add"'),
    ("depth", 'm.depth_write(True) is False'),
    ("stencil", 'm.reset_stencil(0) == 0'),
    ("scissor", 'm.push_scissor(1, 2, 3, 4) == (1, 2, 3, 4)'),
    ("uniform", 'm.bind_uniform("rough", 0.5) == "rough=0.5"'),
    ("offset", 'm.vb_offset(16, 12, 2) == 40'),
    ("viewport", 'm.viewport(800, 600) == (0, 0, 800, 600)'),
    ("cull", 'm.cull_for(True) == "front"'),
    ("mask", 'm.color_mask(False) == (0, 0, 0, 0)'),
    ("stack", 'm.stack_key(3) == "stack:3"'),
    ("leak", 'm.is_leak("alpha", "add") is True'),
    ("clamp", 'm.clamp_state(5, 0, 3) == 3'),
    ("pass", 'm.pass_key("depth") == "pass:depth"'),
    ("bits", 'm.mask_bits(True) == 15')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
