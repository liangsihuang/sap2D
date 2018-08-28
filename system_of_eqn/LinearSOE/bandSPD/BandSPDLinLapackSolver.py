from system_of_eqn.LinearSOE.bandSPD.BandSPDLinSolver import BandSPDLinSolver
from scipy.linalg import solveh_banded
class BandSPDLinLapackSolver(BandSPDLinSolver):
    SOLVER_TAGS_BandSPDLinLapackSolver = 3

    def __init__(self):
        super().__init__(self.SOLVER_TAGS_BandSPDLinLapackSolver)
    
    def solve(self):
        if(self.theSOE==None):
            print('WARNING BandSPDLinLapackSolver::solve() - No LinearSOE object has been set. \n')
            return -1
        
        n = self.theSOE.size()
        kd = self.theSOE.half_band - 1
        ldA = kd + 1
        nrhs = 1
        ldB = n
        A = self.theSOE.A
        X = self.theSOE.X
        B = self.theSOE.B

        # first copy B into X
        for i in range(0, n):
            X[i] = B[i]

        # now solve AX = B
		
        
        
        
        
    def setSize(self):
        pass
        n = self._theSOE._size
        kd = self._half_band - 1
        ldA = kd + 1
        nrhs = 1
        ldB = n 
        A = self._theSOE._A
        X = self._theSOE._X
        B = self._theSOE._B

        # first copy B into X
        for i in range(0, n):
            