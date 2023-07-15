def move(disk_num, from_peg, to_peg):
    print("Move disk " + str(disk_num) + " from peg " \
            + str(from_peg) + " to peg " + str(to_peg) + ".")
    
def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        move(n, start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        solve_hanoi(n-1, start_peg, spare_peg)
        move(n, start_peg, end_peg)
        solve_hanoi(n-1, spare_peg, end_peg)

