import solver
import rubik

start = rubik.I
end = rubik.I

start = rubik.I
middle = rubik.perm_apply(rubik.F, start)
end = rubik.perm_apply(rubik.L, middle)
ans = solver.shortest_path(start, end)
print(ans)