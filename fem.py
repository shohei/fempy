import numpy as np

def simple_fem():
    initialize()
    make_D()
    make_B()
    make_Ke()
    make_K()
    set_boundary_condition()
    solve()
    make_reaction()
    make_strain_element()
    make_stress_element()

def initialize():
    DOF_NODE = 2
    DOF_TOTAL = 12
    DOF_TRIA3 = 6
    ELEMENTS = 4
    NODES = 6
    NODES_TRIA3 = 3
    POISSON  = 0.3
    THICKNESS = 1
    connectivity = np.matrix([[1,2,5],
                              [2,3,4],
                              [2,4,5],
                              [1,5,6]])
    x = np.array([0,1,2,2,1,0])
    y = np.array([0,0,0,1,1,1])

def make_D():
    pass
def make_B():
    pass
def make_Ke():
    pass
def make_K():
    pass
def set_boundary_condition():
    pass
def solve():
    pass
def make_reaction():
    pass
def make_strain_element():
    pass
def make_stress_element():
    pass


if __name__=="__main__":
    simple_fem()

