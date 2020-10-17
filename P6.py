import numpy as np
import scipy as sp

class P6:
    def __init__(self):
        self.R = self.init_R()
        self.invR = self.init_invR()
        self.detR = self.init_detR()
    def init_R(self):
        return lambda theta: np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0],[0, 0, 1]])
    def init_invR(self):
        return lambda theta: np.linalg.inv(self.R(theta))
    def init_detR(self):
        return lambda theta: np.linalg.det(self.R(theta))

class test_lambda_mat:
    #currently only built to work with exactly 3x3 matrices
    def __init__(self, lambda_mat):
        self.lambda_mat = lambda_mat
        self.run_test()
    def run_test(self):
        ts = ["pi/6", "pi/3", "pi/2"]
        for i in range(3):
            print("---------------------------------------------")
            t = (i+1)*np.pi/6
            print(">>> t = %s" %(ts[i]))
            r = self.lambda_mat.R(t)
            print(">>> r(t) =")
            print(r)
            invr = self.lambda_mat.invR(t) 
            print(">>> inv(r(t)) =")
            print(invr)
            detr = self.lambda_mat.detR(t)
            print(">>> det(r(t)) = %f" %(detr))
            xdoty = np.dot(r[:,0], r[:,1])
            ydotz = np.dot(r[:,1], r[:,2])
            zdotx = np.dot(r[:,2], r[:,0])
            if xdoty+ydotz+zdotx==0:
                print(">>> the columns of r are mutually orthogonal")
            row_norm_test=0
            col_norm_test=0
            for i in range(3):
                if np.linalg.norm(r[i,:])!=1:
                    row_norm_test += 1
                if np.linalg.norm(r[:,i])!=1:
                    col_norm_test += 1
            if row_norm_test==0:
                print(">>> the rows of r are normal")
            if col_norm_test==0:
                print(">>> the columns of r are normal")

ans=P6()
test_lambda_mat(ans)