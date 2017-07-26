'''
Created on Jun 23, 2017

@author: prkrj
'''
from __future__ import division

import timeit
import copy

HNF = [[1,0,0],[0,1,0],[0,0,1]]
symHNF = []

# Generate symmetry preserving HNF's for
# for body centered orthogonal lattice using 2nd basis
def bodyOrtho1(size):
    start = timeit.timeit()
    symHNF =[]
    numValid = 0
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[2][2] = j + 1
            f = HNF[2][2]
            if (f / a).is_integer():
                for k in range(size):
                    HNF[1][1] = k + 1
                    c = HNF[1][1]
                    if (f / c).is_integer():
                        if (a * f * c) == size:
                            for l in range(f):
                                HNF[2][1] = l
                                e = HNF[2][1]
                                if ((e - c) / a).is_integer():
                                    if (e / c).is_integer():
                                        if ((c - e * e / c) / f).is_integer():
                                            for m in range(c):
                                                HNF[1][0] = m 
                                                b = HNF[1][0]
                                                if ((e - b * (e -c) / a) / c).is_integer():
                                                    if ((f - b * f / a) / c).is_integer():
                                                        for n in range(f):
                                                            HNF[2][0] = n
                                                            d = HNF[2][0]
                                                            if ((b - d) / a).is_integer():
                                                                if ((b + d - a) / c).is_integer():
                                                                    if ((d - a - b * (d - b) / a) / c).is_integer():
                                                                        if ((b - a + d - (b - a + d) * e / c) /f).is_integer():
                                                                            if ((d - d * (d - b) / a - (d - a - b * (d - b) / a) * e / c) / f).is_integer():
                                                                                if ((e - d * (e - c) / a - e * (e - b * (e - c) / a) / c) / f).is_integer():
                                                                                    symHNF.append(copy.deepcopy(HNF))
    end = timeit.timeit()
    print (end - start)
    return symHNF

# Generate symmetry preserving HNF's for
# for body centered orthogonal lattice using 2nd basis

def bodyOrtho2(size):
    start = timeit.timeit()
    symHNF = []
    numValid = 0
    for i in range(size):
        HNF [0][0] = i +1
        a = HNF[0][0]
        for j in range(size):
            HNF[2][2] = j +1
            f = HNF[2][2]
            if (f/a).is_integer():
                for k in range(f):
                    HNF[2][0] = k 
                    d = HNF[2][0]
                    if (d/a).is_integer():
                        for l in range(f):
                            HNF[2][1] = l
                            e = HNF[2][1]
                            if (e/a).is_integer():
                                for m in range(size):
                                    HNF[1][1] = m + 1
                                    c = HNF[1][1]
                                    for n in range(c):
                                        HNF[1][0] = n
                                        b = HNF[1][0]
                                        if ((-d + b*d/a) / c).is_integer():
                                            if ((2*b + b*d/a) / c).is_integer():
                                                if ((-e + b*e/a)/c).is_integer():
                                                    if (b*e / (a*c)).is_integer():
                                                        if ((-f + b*f/a)/c).is_integer():
                                                            if (b*f / (a*c)).is_integer():
                                                                if ((2*d + d*d/a - (-d + b*d/a)*e/c) / f).is_integer():
                                                                    if ((2*d + d*d/a - (2*b + b*d/a)*e/c) / f).is_integer():
                                                                        if ((2*e +d*e/a - e*(-e + b*e/a)/c)/f).is_integer():
                                                                            if ((d*e/a - b*e*e/a/c)/f).is_integer():
                                                                                if (a * c * f) == size:
                                                                                    symHNF.append(copy.deepcopy(HNF))
                                                                                    numValid += 1
    end = timeit.timeit()
    print (end - start)
    return symHNF    
                                                                          
# Generate symmetry preserving HNF's for
# for body centered orthogonal lattice using 3rd basis
def bodyOrtho3 (size):
    start = timeit.timeit()
    symHNF = []
    numValid = 0
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            if (c/a).is_integer():
                for k in range(c):
                    HNF[1][0] = k 
                    b = HNF[1][0]
                    if (b/a).is_integer():
                        if ((2*b + b*b/a)/c).is_integer():
                            for l in range(size):
                                HNF[2][2] = l + 1
                                f = HNF[2][2]
                                if (a*c*f) == size:
                                    for m in range(f):
                                        HNF[2][0] = m
                                        d = HNF[2][0]
                                        for n in range(f):
                                            HNF[2][1] = n
                                            e = HNF[2][1]
                                            if ((-b + b*d/a - (2*b + b*b/a) * e / c) / f).is_integer():
                                                if ((2*d + b*d/a - (2*b + b*b/a) * e / c) / f).is_integer():
                                                    if ((-c + c*d/a - 2*e - b*e/a) / f).is_integer():
                                                        if ((c*d/a - b*e/a)/f).is_integer():
                                                            numValid += 1
                                                            symHNF.append(copy.deepcopy(HNF))
    end = timeit.timeit()
    print (end - start)
    return symHNF

# Generate symmetry preserving HNF's for
# for body centered orthogonal lattice using 4th basis
def bodyOrtho4 (size):
    start = timeit.timeit()
    numValid = 0
    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            for k in range(size):
                HNF[2][2] = k + 1
                f = HNF[2][2]
                if a * c * f == size:
                    for l in range(c):
                        HNF[1][0] = l 
                        b = HNF[1][0]
                        if ((a + 2 * b) / c).is_integer():
                            for m in range(f):
                                HNF[2][0] = m 
                                d = HNF[2][0]
                                if ((a + 2 * d) / f).is_integer():
                                    for n in range(f):
                                        HNF[2][1] = n
                                        e = HNF[2][1]
                                        if (2 * e / f).is_integer():
                                            if (((a + 2 * b) * e) / (c * f)).is_integer():
                                                symHNF.append(copy.deepcopy(HNF))
                                                numValid += 1
    end = timeit.timeit()
    print (end - start)
    return symHNF
