import math
import strformat
let g = 9.8
let y0 = 0.0
let v0 = 0.0
var delta_t = 0.0
var y = 0.0
var y_old = 0.0
var y_new = 0.0
var v = 0.0

iterator countup*(a: float, b: float, step = 1.0): float {.inline.} =
  var res:float = a
  while res <= b:
    yield res
    res += step

proc normal(t: float): float =
    return -0.5*g*pow(t,2) + v0*t

proc euler(delta_t: float, y: float, v: float): seq[float] =
    var y_new = y+v*delta_t
    var v_new = v-g*delta_t
    result = @[]
    result.add(y_new)
    result.add(v_new)

proc verlet(delta_t: float, y: float, y_old: float): float =
    var y_new = 2*y - y_old - g*pow(delta_t, 2)
    return y_new

# Normal analytic solution
echo "Analytic Solution"
for t in countup(0.0, 0.40, 0.10):
    echo fmt"y(t={t})={normal(t)}"


# Euler method
echo "Euler method"
for delta_t in [0.10, 0.050]:
    y = y0
    v = v0
    echo fmt"delta_t={delta_t}"
    for t in countup(0.0, 0.40, delta_t):
        echo fmt"(t={t}) y={y}, v={v}"
        var next = euler(delta_t, y, v)
        y = next[0]
        v = next[1]


# Verlet Method
echo "Verlet method"

delta_t = 0.10
echo fmt"(t={0.0}) y={y0}"
y_old = y0
let y1 = y0 + delta_t * v0 - (g*pow(delta_t, 2))/2
y = y1
for t in countup(0.10, 0.40, 0.10):
    echo fmt"(t={t}) y={y}"
    y_new = verlet(delta_t, y, y_old)
    y_old = y
    y = y_new
