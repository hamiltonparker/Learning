'''
Created on Jun 23, 2017

@author: prkrj
'''
from __future__ import division

from timeit import default_timer as timer
import copy
import csv

HNF = [[1,0,0],[0,1,0],[0,0,1]]
symHNF = []

def body_ortho_1(size):

    """Generates symmetry preserving HNF's of a given size 
       for a body centered orthogonal basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF =[]
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
    return symHNF

def body_ortho_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a body centered orthogonal basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
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
    return symHNF    
                                                                          
def body_ortho_3 (size):

    """Generates symmetry preserving HNF's of a given size
       for a body centered orthogonal basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    
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
                                                            symHNF.append(copy.deepcopy(HNF))
    return symHNF


def body_ortho_4 (size):

    """Generates symmetry preserving HNF's of a given size
       for a body centered orthogonal basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """
                                                                                    
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
                                                                                    
    return symHNF

def base_mono_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    numValid = 0
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while a * j <= size:
            HNF[1][1] = a * j
            c = HNF[1][1]
            k = 0
            b = 0
            while a * k < c:
                HNF[1][0] = a * k
                b = HNF[1][0]
                if ((-a + (b * b / a)) / c).is_integer():
                    for l in range(size):
                        HNF[2][2] = l + 1
                        f = HNF[2][2]
                        if a * c * f == size:
                            for m in range(f):
                                HNF[2][0] = m
                                d = HNF[2][0]
                                for n in range(f):
                                    HNF[2][1] = n
                                    e = HNF[2][1]
                                    if ((-d + b*d/a - (-a + b*b/a)*e / c) / f).is_integer():
                                        if ((c*d/a - e - b*e/a) / f).is_integer():
                                            symHNF.append(copy.deepcopy(HNF))
                                            numValid += 1
                k += 1
            j += 1
            
    return symHNF

def base_mono_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            for k in range(c):
                HNF[1][0] = k
                b = HNF [1][0]
                if ((a + 2 * b) / c).is_integer():
                    for l in range(size):
                        HNF[2][2] = l + 1
                        f = HNF[2][2]
                        if a * c * f == size:

                            for m in range (f):
                                HNF[2][1] = m
                                e = HNF[2][1]
                                if (2 * e / f).is_integer():
                                    if ((a + 2 * b) * e / (c * f)).is_integer():
                                        for n in range(f):
                                            HNF[2][0] = n
                                            d = HNF[2][0]
                                            symHNF.append(copy.deepcopy(HNF))
    return symHNF

def base_mono_3(size):
    
    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    numValid = 0
    for i in range (size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while a * j <= size:
            HNF[1][1] = a * j
            c = HNF[1][1]
            k = 0
            while a * k < c:
                HNF[1][0] = a * k
                b = HNF[1][0]
                if ((2 * b + (b * b / a)) / c).is_integer():
                    for l in range(size):
                        HNF[2][2] = l + 1
                        f = HNF[2][2]
                        if a * c * f == size:
                            for m in range(f):
                                HNF[2][0] = m
                                d = HNF[2][0]
                                for n in range(f):
                                    HNF[2][1] = n
                                    e = HNF[2][1]
                                    if ((b * d / a - (2 * b + b * b / a) * e / c) / f).is_integer():
                                        if ((c * d / a - 2 * e - b * e / a) / f).is_integer():
                                            symHNF.append(copy.deepcopy(HNF))
                k += 1
            j += 1
    return symHNF

def base_ortho_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while a * j <= size:
            HNF[1][1] = a * j
            c = HNF[1][1]
            k = 0
            while a * k < c:
                HNF[1][0] = a * k
                b = HNF[1][0]
                if ((-a + b * b / a) / c).is_integer():
                    for l in range(size):
                        HNF[2][2] = l + 1
                        f = HNF[2][2]
                        if a * c * f == size:
                            for m in range(f):
                                HNF[2][0] = m
                                d = HNF[2][0]
                                if (2 * d / f).is_integer():
                                    for n in range(f):
                                        HNF[2][1] = n
                                        e = HNF[2][1]
                                        if (2 * e / f).is_integer():
                                            if ((-d + b * d / a - (-a + b * b / a) * e / c) / f).is_integer():
                                                if ((c * d / a - e - b * e / a) / f).is_integer():
                                                    symHNF.append(copy.deepcopy(HNF))
                k += 1
            j += 1
    return symHNF

def base_ortho_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

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
                                HNF[2][1] = m
                                e = HNF[2][1]
                                if (2 * e / f).is_integer():
                                    if ((a + 2 * b) * e / (c * f)).is_integer():
                                        for n in range(f):
                                            HNF[2][0] = n
                                            d = HNF[2][0]
                                            if (2 * d / f).is_integer():
                                                symHNF.append(copy.deepcopy(HNF))
    return symHNF

def base_ortho_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """
    
    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while j * a <= size:
            c = j * a
            HNF[1][1] = c
            k = 0
            while k * a < c:
                b = k * a
                HNF[1][0] = b
                if ((2 * b + b * b / a) / c).is_integer():
                    for l in range(size):
                        HNF[2][2] = l + 1
                        f = HNF[2][2]
                        if a * c * f == size:
                            for m in range(f):
                                HNF[2][0] = m
                                d = HNF[2][0]
                                for n in range(f):
                                    HNF[2][1] = n
                                    e = HNF[2][1]
                                    if ((b * d / a - (2 * b + b * b / a) * e / c) / f).is_integer():
                                        if ((2 * d + b * d / a - (2 * b + b**2 / a) * e / c) / f).is_integer():
                                            if ((c * d / a - 2 * e - b * e / a) / f).is_integer():
                                                if ((c * d / a - b * e / a) / f).is_integer():
                                                    symHNF.append(copy.deepcopy(HNF))
                k += 1
            j += 1
    return symHNF

def body_cubic_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            k = 1
            while a * k <= size:
                HNF[2][2] = a * k
                f = HNF[2][2]
                if a * c * f == size:
                    if (f/c).is_integer():
                        for l in range(c):
                            HNF[1][0] = l
                            b = HNF[1][0]
                            if ((b * f) / (a * c)).is_integer():
                                m = 0
                                while a * m < f:
                                    HNF[2][0] = a * m
                                    d = HNF[2][0]
                                    if ((-a + b - b * d / a) / c).is_integer():
                                        if ((b - d) / c).is_integer():
                                            n = 0
                                            while a * n < f:
                                                HNF[2][1] = a * n
                                                e = HNF[2][1]
                                                if (e / c).is_integer():
                                                    if ((-b + d - (b - d) * e / c) / f).is_integer():
                                                        if ((-a + b + d - d**2 / a - (-a + b - b * d / a) * e / c) / f).is_integer():
                                                            if ((c - d * e / a + b * e**2 / (a * c)) / f).is_integer():
                                                                if ((-c + e**2 / c) / f).is_integer():
                                                                    symHNF.append(copy.deepcopy(HNF))
                                                n += 1
                                    m += 1
                k += 1
    return symHNF

def body_cubic_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while j * a <= size:
            HNF[2][2] = j * a
            f = HNF[2][2]
            for k in range(size):
                HNF[1][1] = k + 1
                c = HNF[1][1]
                if a * c * f == size:
                    for l in range(c):
                        HNF[1][0] = l
                        b = HNF[1][0]
                        if (b * f / a / c).is_integer():
                            if ((-f + b * f / a) / c).is_integer():
                                m = 0
                                while m * a < f:
                                    HNF[2][0] = m * a
                                    d = HNF[2][0]
                                    if ((-b - d) / a).is_integer():
                                        if ((-a + b - (b * (-b -d)) / a) / c).is_integer():
                                            if ((-a - d + b * d / a) / c).is_integer():
                                                n = 0
                                                while n * a < f:
                                                    HNF[2][1] = n * a
                                                    e = HNF[2][1]
                                                    if ((-c - e) / a).is_integer():
                                                        if ((b * (-c - e)) / (a * c)).is_integer():
                                                            if ((-e + (b * e) / a) / c).is_integer():
                                                                if ((2 * a + 2 * d - (-b - d) *d / a - (-a + b - b * (-b - d) / a) * e / c) / f).is_integer():
                                                                    if ((2 * a + 2 * d + d**2 / a - (-a - d + b * d / a) * e / c) / f).is_integer():
                                                                        if ((-d * (-c - e) / a + e + b * (-c - e) * e / (a * c)) / f).is_integer():
                                                                            if ((2 * e + d * e / a - e * (-e + b * e / a) / c) / f).is_integer():
                                                                                symHNF.append(copy.deepcopy(HNF))
                                                    n += 1
                                    m += 1
            j += 1
    return symHNF

def body_cubic_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while j * a <= size:
            HNF[2][2] = j * a
            f = HNF[2][2]
            for k in range (size):
                HNF[1][1] = k + 1
                c = HNF[1][1]
                if a * f * c == size:
                    for l in range(f):
                        HNF [2][1] = l
                        e = HNF[2][1]
                        if ((-c - e) / a).is_integer():
                            for m in range(c):
                                HNF[1][0] = m
                                b = HNF[1][0]
                                if ((2 * f + b * f / a) / c).is_integer():
                                    if (b * f / a / c).is_integer():
                                        if ((-b * (-c - e) / a + 2 * e) / c).is_integer():
                                            if ((b * (-c - e) / a / c)).is_integer():
                                                for n in range(f):
                                                    HNF[2][0] = n
                                                    d = HNF[2][0]
                                                    if ((-b - d) / a).is_integer():
                                                        if ((2 * b - b * (-b - d) / a + 2 * d) / c).is_integer():
                                                            if ((2 * a + 2 * b - b * (-b - d) / a) / c).is_integer():
                                                                if ((-b - (-b - d) * d / a - (2 * b - b * (-b -d) / a + 2 * d) * e / c) / f).is_integer():
                                                                    if ((-a + d - (-b - d) * d / a - (2 * a + 2 * b - b * (-b - d) / a) * e / c) / f).is_integer():
                                                                        if ((-c - d * (-c - e) / a - 2 * e - e * (- b * (-c -e) / a + 2 * e) / c) / f).is_integer():
                                                                            if ((-d * (-c - e) / a - e + b * (-c - e) * e / a / c) / f).is_integer():
                                                                                symHNF.append(copy.deepcopy(HNF))
            j += 1
    return symHNF

def body_cubic_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            if (2 * c / a).is_integer():
                k = 1
                while k * c <= size:
                    HNF[2][2] = k * c
                    f = HNF[2][2]
                    if a * c * f == size:
                        for l in range(c):
                            HNF[1][0] = l
                            b = HNF[1][0]
                            if ((2 * b + 2 * b**2 / a) / c).is_integer():
                                if (2 * b / a).is_integer():
                                    for m in range(f):
                                        HNF[2][0] = m
                                        d = HNF[2][0]
                                        if ((2 * b + 2 * b**2 / a - d) / c).is_integer():
                                            for n in range(f):
                                                HNF[2][1] = n
                                                e = HNF[2][1]
                                                if ((a + b + 2 * d + 2 * b * d / a - (2 * b + 2 * b**2 / a) * e / c) / f).is_integer():
                                                    if ((b + d + 2 * b * d / a - (2 * b + 2 * b**2 / a - d) * e / c) / f).is_integer():
                                                        if ((c + 2 * c * d / a - e - (2 * b * c / a - e) * e /c) / f).is_integer():
                                                            if ((c + 2 * c * d / a - 2 * b * e / a) / f).is_integer():
                                                                symHNF.append(copy.deepcopy(HNF))
                    k += 1

    return symHNF

def body_cubic_5(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while a * j <= size:
            HNF[1][1] = a * j
            c = HNF[1][1]
            k = 1
            while a * k <= size:
                HNF[2][2] = a * k
                f = HNF[2][2]
                if a * c * f == size:
                    for l in range(f):
                        HNF[2][1] = l
                        e = HNF[2][1]
                        m = 0
                        while a * m < c:
                            HNF[1][0] = a * m
                            b = HNF[1][0]
                            if ((b * c / a - e) / c).is_integer():
                                if ((b * c / a + e) / c).is_integer():
                                    for n in range(f):
                                        HNF[2][0] = n
                                        d = HNF[2][0]
                                        if ((2 * b + b**2 / a - d) / c).is_integer():
                                            if ((a + b + b**2 / a + d) / c).is_integer():
                                                if ((b + d + b * d / a - (2 * b + b**2 / a - d) * e / c) / f).is_integer():
                                                    if ((a + d + b * d / a - (a + b + b**2 /a + d) * e / c) / f).is_integer():
                                                        if ((c + c * d / a - e - (b * c / a - e) * e / c) / f).is_integer():
                                                            if ((c + c * d / a - e - (b * c / a - e) * e / c) / f).is_integer():
                                                                if ((c * d / a - e * (b * c / a + e) / c) / f).is_integer():
                                                                    symHNF.append(copy.deepcopy(HNF))
                            m += 1
                k += 1
            j += 1 
    return symHNF

def body_cubic_6(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while j * a <= size:
            HNF[1][1] = j * a
            c = HNF[1][1]
            k = 1
            while a * k <= size:
                HNF[2][2] = a * k
                f = a * k
                if a * c * f == size:
                    l = 0
                    while a * l < c:
                        HNF[1][0] = a * l
                        b = HNF[1][0]
                        if ((2 * b + b**2 / a) / c).is_integer():
                            if (b * f / a / c).is_integer():
                                m = 0
                                while m * a < f:
                                    HNF[2][0] = m * a 
                                    d = HNF[2][0]
                                    if ((a + b - b * d / a) / c).is_integer():
                                        n = 0 
                                        while n * a < f:
                                            HNF[2][1] = n * a
                                            e = HNF[2][1]
                                            if (b * e / a / c).is_integer():
                                                if ((-b + b * d / a - (2 * b + b**2 / a) * e / c) / f).is_integer():
                                                    if ((-a - b + d - d**2 / a - (a + b - b * d / a) * e / c) / f).is_integer():
                                                        if ((-c + c * d / a - 2 * e - b * e / a) / f).is_integer():
                                                            if ((-c - d * e / a + b * e**2 / a / c) / f).is_integer():
                                                                symHNF.append(copy.deepcopy(HNF))
                                            n += 1
                                    m += 1
                        l += 1
                k += 1
            j += 1
    return symHNF

def body_cubic_7(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while a * j <= size:
            HNF[1][1] = a * j
            c = HNF[1][1]
            k = 1
            while a * k <= size:
                HNF[2][2] = a * k
                f = HNF[2][2]
                if (f / c).is_integer():
                    if a * c * f == size:
                        l = 0
                        while l * a < a:
                            HNF[1][0] = l * a
                            b = HNF[1][0]
                            if ((f + b * f / a) / c).is_integer():
                                for m in range(f):
                                    HNF[2][0] = m
                                    d = HNF[2][0]
                                    if ((-b - d) / a).is_integer():
                                        if ((b - b * (-b - d) / a + d) / c).is_integer():
                                            if ((a + 2 * b + b**2 / a + d) / c).is_integer():
                                                for n in range(f):
                                                    HNF[2][1] = n
                                                    e = HNF[2][1]
                                                    if ((-c - e) / a).is_integer():
                                                        if((-b * (-c - e) / a + e) / c).is_integer():
                                                            if ((b * c / a + e) / c).is_integer():
                                                                if (( b + d - (-b - d) * d / a - (b - b * (-b - d) / a + d) * e / c) / f).is_integer():
                                                                    if ((-b + b * d / a - (a + 2 * b + b**2 / a + d) * e / c) / f).is_integer():
                                                                        if ((c - d * (-c - e) / a - e * (-b * (-c - e) / a + e) / c) / f).is_integer():
                                                                            if ((-c + c * d /a - 2 * e - e * (b * c / a + e) / c) / f).is_integer():
                                                                                symHNF.append(copy.deepcopy(HNF))
                            l += 1
                k += 1
            j += 1
    return symHNF

def body_cubic_8(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        j = 1
        while a * j <= size:
            HNF[2][2] = a * j
            f = HNF[2][2]
            for k in range(size):
                HNF[1][1] = k + 1
                c = HNF[1][1]
                if a * c * f == size:
                    for l in range(f):
                        HNF[2][1] = l
                        e = HNF[2][1]
                        if ((-c - e) / a).is_integer():
                            for m in range(c):
                                HNF[1][0] = m
                                b = HNF[1][0]
                                if ((-b * (-c - e) / a - e) / c).is_integer():
                                    if ((-b * (-c - e) / a + e) / c).is_integer():
                                        if ((-f + b * f / a) / c).is_integer():
                                            if ((f + b * f / a) / c).is_integer():
                                                for n in range(f):
                                                    HNF[2][0] = n
                                                    d = HNF[2][0]
                                                    if ((-b - d) / a).is_integer():
                                                        if ((b - b * (-b - d) / a - d) / c).is_integer():
                                                            if ((b - b * (-b - d) / a + d) / c).is_integer():
                                                                if ((b + 2 * d - (-b - d) * d / a - (b - b * (-b - d) / a - d) * e / c) / f).is_integer():
                                                                    if ((a + d - (-b - d) * d / a - (b - b * (-b - d) / a + d) * e / c) / f).is_integer():
                                                                        if ((c - d * (-c - e) / a + e - (-b * (-c - e) / a - e) * e / c) / f).is_integer():
                                                                            if ((-d * (-c - e) / a - e * ( -b * (-c - e) / a + e) / c) / f).is_integer():
                                                                                symHNF.append(copy.deepcopy(HNF))
            j += 1
    return symHNF

def body_tet_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            k = 1
            while a * k <= size:
                HNF[2][2] = a * k
                f = HNF[2][2]
                if (f / c).is_integer():
                    if a * c * f == size:
                        for l in range(c):
                            HNF[1][0] = l
                            b = HNF[1][0]
                            if ((b * f) / (a * c)).is_integer():
                                m = 0
                                while m * a < f:
                                    HNF[2][0] = m * a
                                    d = HNF[2][0]
                                    if ((-a + b + d) / c).is_integer():
                                        if((-a + b - b * d / a) / c).is_integer():
                                            n = 0
                                            while n * a < f:
                                                HNF[2][1] = n * a
                                                e = HNF[2][1]
                                                if ((b * e) / (a * c)).is_integer():
                                                    if (e/c).is_integer():
                                                        if ((-a + b + d - (-a + b + d) * e / c) / f).is_integer():
                                                            if ((-a + b + d - d**2 / a - (-a + b - b * d / a) * e / c) / f).is_integer():
                                                                if ((c - e**2 / c) / f).is_integer():
                                                                    if ((c - d * e / a + b * e**2 / a / c) / f).is_integer():
                                                                        symHNF.append(copy.deepcopy(HNF))
                                                n += 1
                                    m += 1
                k += 1
    return symHNF
                                            
def body_tet_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    for i in range(size):
        HNF[0][0] = i + 1
        a = HNF[0][0]
        for j in range(size):
            HNF[1][1] = j + 1
            c = HNF[1][1]
            k = 1
            while a * k <= size:
                HNF[2][2] = a * k
                f = HNF[2][2]
                if a * c * f == size:
                    for l in range(c):
                        HNF[1][0] = l
                        b = HNF[1][0]
                        if (b * f / a / c).is_integer():
                            if ((-f + b * f / a) / c).is_integer():
                                m = 0
                                while a * m < f:
                                    HNF[2][0] = a * m
                                    d = HNF[2][0]
                                    if ((2 * b + b * d / a) / c).is_integer():
                                        if ((-a - b * (-b - d) / a - d) / c).is_integer():
                                            if ((-b - d) / a).is_integer():
                                                n = 0
                                                while a * n < f:
                                                    HNF[2][1] = a * n
                                                    e = HNF[2][1]
                                                    if ((-c - e) / a).is_integer():
                                                        if (b * e / a / c).is_integer():
                                                            if ((-b * (-c - e) / a - e) / c).is_integer():
                                                                if ((2 * d + d**2 / a - (2 * b + b * d / a) * e / c) / f).is_integer():
                                                                    if ((d - (-b - d) * d / a - (-a - b * (-b - d) / a - d) * e / c) / f).is_integer():
                                                                        if ((d * e / a - b * e**2 / a / c) / f).is_integer():
                                                                            if ((-d * (-c - e) / a + e - (-b * (-c - e) / a - e) * e / c) / f).is_integer():
                                                                                symHNF.append(copy.deepcopy(HNF))
                                                    n += 1
                                    m += 1
                k += 1
    return symHNF

def body_tet_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def body_tet_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def body_tet_5(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def face_cubic_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def hex(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_cubic_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_cubic_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_cubic_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_cubic_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_cubic_5(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_mono(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_ortho(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def s_tet(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def trig_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def trig_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def trig_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def trig_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

def timing (func):

    """Times the function for a set of sizes and wirtes a csv file with results

    Args:
        func (function): The function to be timed

    Returns:
        file (file object): A csv file with the function times
    """

    nums = [10, 100, 1000]
    list = []
    for i in nums:
        start_time = timer()
        func(i)
        end_time = timer()
        time = end_time - start_time
        list.append(time)
    
    file = open('func_time.out', 'w')
    with file as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(list)
