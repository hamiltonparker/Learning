'''
Created on Jun 23, 2017

@author: prkrj
'''
from __future__ import division

from timeit import default_timer as timer
import copy
import csv

symHNF = []

def find_HNF_diagonal(size):

    """Generats allowable values for the diagonal of an HNF
       given a particular size

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        diags_list (list, int): a list of allowable values for a given size
    """

    diags_list = []
    for i in range(size):
        a = i + 1
        if (size / a) % 1 == 0:
            for j in range(size // a):
                c = j + 1
                if (size / a / c) % 1 == 0:
                    f = size // a // c
                    diags_list.append([a,c,f])
    return diags_list

def body_ortho_1(size):

    """Generates symmetry preserving HNF's of a given size 
       for a body centered orthogonal basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF =[]
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / c) % 1 == 0:
            if (f / a) % 1 == 0:
                for j in range(f):
                    e = j
                    if ((e - c) / a) % 1 == 0:
                        if (e / c) % 1 == 0:
                            if ((c - e * e / c) / f) % 1 == 0:
                                for k in range(c):
                                    b = k 
                                    if ((e - b * (e -c) / a) / c) % 1 == 0:
                                        if ((f - b * f / a) / c) % 1 == 0:
                                            for l in range(f):
                                                d = l
                                                if ((b - d) / a) % 1 == 0:
                                                    if ((b + d - a) / c) % 1 == 0:
                                                        if ((d - a - b * (d - b) / a) / c) % 1 == 0:
                                                            if ((b - a + d - (b - a + d) * e / c) /f) % 1 == 0:
                                                                if ((d - d * (d - b) / a - (d - a - b * (d - b) / a) * e / c) / f) % 1 == 0:
                                                                    if ((e - d * (e - c) / a - e * (e - b * (e - c) / a) / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f/a) % 1 == 0:
            for j in range(f):
                d = j
                if (d/a) % 1 == 0:
                    for k in range(f):
                        e = k
                        if (e/a) % 1 == 0:
                            for l in range(c):
                                b = l
                                if ((-d + b*d/a) / c) % 1 == 0:
                                    if ((2*b + b*d/a) / c) % 1 == 0:
                                        if ((-e + b*e/a)/c) % 1 == 0:
                                            if (b*e / (a*c)) % 1 == 0:
                                                if ((-f + b*f/a)/c) % 1 == 0:
                                                    if (b*f / (a*c)) % 1 == 0:
                                                        if ((2*d + d*d/a - (-d + b*d/a)*e/c) / f) % 1 == 0:
                                                            if ((2*d + d*d/a - (2*b + b*d/a)*e/c) / f) % 1 == 0:
                                                                if ((2*e +d*e/a - e*(-e + b*e/a)/c)/f) % 1 == 0:
                                                                    if ((d*e/a - b*e*e/a/c)/f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c/a) % 1 == 0:
            for j in range(c):
                b = j 
                if (b/a) % 1 == 0:
                    if ((2*b + b*b/a)/c) % 1 == 0:
                        for k in range(f):
                            d = k
                            for l in range(f):
                                e = l
                                if ((-b + b*d/a - (2*b + b*b/a) * e / c) / f) % 1 == 0:
                                    if ((2*d + b*d/a - (2*b + b*b/a) * e / c) / f) % 1 == 0:
                                        if ((-c + c*d/a - 2*e - b*e/a) / f) % 1 == 0:
                                            if ((c*d/a - b*e/a)/f) % 1 == 0:
                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        for j in range(c):
            b = j
            if ((a + 2 * b) / c) % 1 == 0:
                for k in range(f):
                    d = k
                    if ((a + 2 * d) / f) % 1 == 0:
                        for l in range(f):
                            e = l
                            if (2 * e / f) % 1 == 0:
                                if (((a + 2 * b) * e) / (c * f)) % 1 == 0:
                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]    
        j = 0
        b = 0
        if (c / a) % 1 == 0:
            while a * j < c:
                b = a * j
                j += 1
                if ((-a + (b * b / a)) / c) % 1 == 0:
                    for k in range(f):
                        d = k
                        for l in range(f):
                            e = l
                            if ((-d + b*d/a - (-a + b*b/a)*e / c) / f) % 1 == 0:
                                if ((c*d/a - e - b*e/a) / f) % 1 == 0:
                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        for j in range(c):
            b = j
            if ((a + 2 * b) / c) % 1 == 0:
                for k in range (f):
                    e = k
                    if (2 * e / f) % 1 == 0:
                        if ((a + 2 * b) * e / (c * f)) % 1 == 0:
                            for l in range(f):
                                d = l
                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            j = 0
            while a * j < c:
                b = a * j
                j += 1
                if ((2 * b + (b * b / a)) / c) % 1 == 0:
                    for k in range(f):
                        d = k
                        for l in range(f):
                            e = l
                            if ((b * d / a - (2 * b + b * b / a) * e / c) / f) % 1 == 0:
                                if ((c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            j = 0
            while a * j < c:
                b = a * j
                j += 1
                if ((-a + b * b / a) / c) % 1 == 0:
                    for k in range(f):
                        d = k
                        if (2 * d / f) % 1 == 0:
                            for l in range(f):
                                e = l
                                if (2 * e / f) % 1 == 0:
                                    if ((-d + b * d / a - (-a + b * b / a) * e / c) / f) % 1 == 0:
                                        if ((c * d / a - e - b * e / a) / f) % 1 == 0:
                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        for j in range(c):
            b = j
            if ((a + 2 * b) / c) % 1 == 0:
                for k in range(f):
                    e = k
                    if (2 * e / f) % 1 == 0:
                        if ((a + 2 * b) * e / (c * f)) % 1 == 0:
                            for l in range(f):
                                d = l
                                if (2 * d / f) % 1 == 0:
                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            j = 0
            while j * a < c:
                b = j * a
                j += 1
                if ((2 * b + b * b / a) / c) % 1 == 0:
                    for k in range(f):
                        d = k
                        for l in range(f):
                            e = l
                            if ((b * d / a - (2 * b + b * b / a) * e / c) / f) % 1 == 0:
                                if ((2 * d + b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                    if ((c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                        if ((c * d / a - b * e / a) / f) % 1 == 0:
                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / c) % 1 == 0:
            if (f / a) % 1 == 0:
                for j in range(c):
                    b = j
                    if ((b * f) / (a * c)) % 1 == 0:
                        k = 0
                        while a * k < f:
                            d = a * k
                            k += 1
                            if ((-a + b - b * d / a) / c) % 1 == 0:
                                if ((b - d) / c) % 1 == 0:
                                    l = 0
                                    while a * l < f:
                                        e = a * l
                                        l += 1
                                        if (e / c) % 1 == 0:
                                            if ((-b + d - (b - d) * e / c) / f) % 1 == 0:
                                                if ((-a + b + d - d**2 / a - (-a + b - b * d / a) * e / c) / f) % 1 == 0:
                                                    if ((c - d * e / a + b * e**2 / (a * c)) / f) % 1 == 0:
                                                        if ((-c + e**2 / c) / f) % 1 == 0:
                                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(c):
                b = j
                if (b * f / a / c) % 1 == 0:
                    if ((-f + b * f / a) / c) % 1 == 0:
                        k = 0
                        while k * a < f:
                            d = k * a
                            k += 1
                            if ((-b - d) / a) % 1 == 0:
                                if ((-a + b - (b * (-b -d)) / a) / c) % 1 == 0:
                                    if ((-a - d + b * d / a) / c) % 1 == 0:
                                        l = 0
                                        while l * a < f:
                                            e = l * a
                                            l += 1
                                            if ((-c - e) / a) % 1 == 0:
                                                if ((b * (-c - e)) / (a * c)) % 1 == 0:
                                                    if ((-e + (b * e) / a) / c) % 1 == 0:
                                                        if ((2 * a + 2 * d - (-b - d) *d / a - (-a + b - b * (-b - d) / a) * e / c) / f) % 1 == 0:
                                                            if ((2 * a + 2 * d + d**2 / a - (-a - d + b * d / a) * e / c) / f) % 1 == 0:
                                                                if ((-d * (-c - e) / a + e + b * (-c - e) * e / (a * c)) / f) % 1 == 0:
                                                                    if ((2 * e + d * e / a - e * (-e + b * e / a) / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(f):
                e = j
                if ((-c - e) / a) % 1 == 0:
                    for k in range(c):
                        b = k
                        if ((2 * f + b * f / a) / c) % 1 == 0:
                            if (b * f / a / c) % 1 == 0:
                                if ((-b * (-c - e) / a + 2 * e) / c) % 1 == 0:
                                    if ((b * (-c - e) / a / c)) % 1 == 0:
                                        for l in range(f):
                                            d = l
                                            if ((-b - d) / a) % 1 == 0:
                                                if ((2 * b - b * (-b - d) / a + 2 * d) / c) % 1 == 0:
                                                    if ((2 * a + 2 * b - b * (-b - d) / a) / c) % 1 == 0:
                                                        if ((-b - (-b - d) * d / a - (2 * b - b * (-b -d) / a + 2 * d) * e / c) / f) % 1 == 0:
                                                            if ((-a + d - (-b - d) * d / a - (2 * a + 2 * b - b * (-b - d) / a) * e / c) / f) % 1 == 0:
                                                                if ((-c - d * (-c - e) / a - 2 * e - e * (- b * (-c -e) / a + 2 * e) / c) / f) % 1 == 0:
                                                                    if ((-d * (-c - e) / a - e + b * (-c - e) * e / a / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (2 * c / a) % 1 == 0:
            if (f / c) % 1 == 0:
                for j in range(c):
                    b = j
                    if ((2 * b + 2 * b**2 / a) / c) % 1 == 0:
                        if (2 * b / a) % 1 == 0:
                            for k in range(f):
                                d = k
                                if ((2 * b + 2 * b**2 / a - d) / c) % 1 == 0:
                                    for l in range(f):
                                        e = l
                                        if ((a + b + 2 * d + 2 * b * d / a - (2 * b + 2 * b**2 / a) * e / c) / f) % 1 == 0:
                                            if ((b + d + 2 * b * d / a - (2 * b + 2 * b**2 / a - d) * e / c) / f) % 1 == 0:
                                                if ((c + 2 * c * d / a - e - (2 * b * c / a - e) * e /c) / f) % 1 == 0:
                                                    if ((c + 2 * c * d / a - 2 * b * e / a) / f) % 1 == 0:
                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / c) % 1 == 0:
                for j in range(f):
                    e = j
                    k = 0
                    while a * k < c:
                        b = a * k
                        k += 1
                        if ((b * c / a - e) / c) % 1 == 0:
                            if ((b * c / a + e) / c) % 1 == 0:
                                for l in range(f):
                                    d = l
                                    if ((2 * b + b**2 / a - d) / c) % 1 == 0:
                                        if ((a + b + b**2 / a + d) / c) % 1 == 0:
                                            if ((b + d + b * d / a - (2 * b + b**2 / a - d) * e / c) / f) % 1 == 0:
                                                if ((a + d + b * d / a - (a + b + b**2 /a + d) * e / c) / f) % 1 == 0:
                                                    if ((c + c * d / a - e - (b * c / a - e) * e / c) / f) % 1 == 0:
                                                        if ((c + c * d / a - e - (b * c / a - e) * e / c) / f) % 1 == 0:
                                                            if ((c * d / a - e * (b * c / a + e) / c) / f) % 1 == 0:
                                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / a) % 1 == 0:
                j = 0
                while a * j < c:
                    b = a * j
                    j += 1
                    if ((2 * b + b**2 / a) / c) % 1 == 0:
                        if (b * f / a / c) % 1 == 0:
                            k = 0
                            while k * a < f:
                                d = k * a
                                k += 1
                                if ((a + b - b * d / a) / c) % 1 == 0:
                                    l = 0 
                                    while l * a < f:
                                        e = a * l
                                        l += 1
                                        if (b * e / a / c) % 1 == 0:
                                            if ((-b + b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                                if ((-a - b + d - d**2 / a - (a + b - b * d / a) * e / c) / f) % 1 == 0:
                                                    if ((-c + c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                                        if ((-c - d * e / a + b * e**2 / a / c) / f) % 1 == 0:
                                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / a) % 1 == 0:
                if (f / c) % 1 == 0:
                    j = 0
                    while j * a < a:
                        b = j * a
                        j += 1
                        if ((f + b * f / a) / c) % 1 == 0:
                            for k in range(f):
                                d = k
                                if ((-b - d) / a) % 1 == 0:
                                    if ((b - b * (-b - d) / a + d) / c) % 1 == 0:
                                        if ((a + 2 * b + b**2 / a + d) / c) % 1 == 0:
                                            for l in range(f):
                                                e = l
                                                if ((-c - e) / a) % 1 == 0:
                                                    if((-b * (-c - e) / a + e) / c) % 1 == 0:
                                                        if ((b * c / a + e) / c) % 1 == 0:
                                                            if (( b + d - (-b - d) * d / a - (b - b * (-b - d) / a + d) * e / c) / f) % 1 == 0:
                                                                if ((-b + b * d / a - (a + 2 * b + b**2 / a + d) * e / c) / f) % 1 == 0:
                                                                    if ((c - d * (-c - e) / a - e * (-b * (-c - e) / a + e) / c) / f) % 1 == 0:
                                                                        if ((-c + c * d /a - 2 * e - e * (b * c / a + e) / c) / f) % 1 == 0:
                                                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(f):
                e = j
                if ((-c - e) / a) % 1 == 0:
                    for k in range(c):
                        b = k
                        if ((-b * (-c - e) / a - e) / c) % 1 == 0:
                            if ((-b * (-c - e) / a + e) / c) % 1 == 0:
                                if ((-f + b * f / a) / c) % 1 == 0:
                                    if ((f + b * f / a) / c) % 1 == 0:
                                        for l in range(f):
                                            d = l
                                            if ((-b - d) / a) % 1 == 0:
                                                if ((b - b * (-b - d) / a - d) / c) % 1 == 0:
                                                    if ((b - b * (-b - d) / a + d) / c) % 1 == 0:
                                                        if ((b + 2 * d - (-b - d) * d / a - (b - b * (-b - d) / a - d) * e / c) / f) % 1 == 0:
                                                            if ((a + d - (-b - d) * d / a - (b - b * (-b - d) / a + d) * e / c) / f) % 1 == 0:
                                                                if ((c - d * (-c - e) / a + e - (-b * (-c - e) / a - e) * e / c) / f) % 1 == 0:
                                                                    if ((-d * (-c - e) / a - e * ( -b * (-c - e) / a + e) / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / c) % 1 == 0:
            if (f / a) % 1 == 0:
                for j in range(c):
                    b = j
                    if ((b * f) / (a * c)) % 1 == 0:
                        k = 0
                        while k * a < f:
                            d = k * a
                            k += 1
                            if ((-a + b + d) / c) % 1 == 0:
                                if((-a + b - b * d / a) / c) % 1 == 0:
                                    l = 0
                                    while l * a < f:
                                        e = l * a
                                        l += 1
                                        if ((b * e) / (a * c)) % 1 == 0:
                                            if (e/c) % 1 == 0:
                                                if ((-a + b + d - (-a + b + d) * e / c) / f) % 1 == 0:
                                                    if ((-a + b + d - d**2 / a - (-a + b - b * d / a) * e / c) / f) % 1 == 0:
                                                        if ((c - e**2 / c) / f) % 1 == 0:
                                                            if ((c - d * e / a + b * e**2 / a / c) / f) % 1 == 0:
                                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

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
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(c):
                b = j
                if (b * f / a / c) % 1 == 0:
                    if ((-f + b * f / a) / c) % 1 == 0:
                        k = 0
                        while a * k < f:
                            d = a * k
                            k += 1
                            if ((2 * b + b * d / a) / c) % 1 == 0:
                                if ((-a - b * (-b - d) / a - d) / c) % 1 == 0:
                                    if ((-b - d) / a) % 1 == 0:
                                        l = 0
                                        while a * l < f:
                                            e = a * l
                                            l += 1
                                            if ((-c - e) / a) % 1 == 0:
                                                if (b * e / a / c) % 1 == 0:
                                                    if ((-b * (-c - e) / a - e) / c) % 1 == 0:
                                                        if ((2 * d + d**2 / a - (2 * b + b * d / a) * e / c) / f) % 1 == 0:
                                                            if ((d - (-b - d) * d / a - (-a - b * (-b - d) / a - d) * e / c) / f) % 1 == 0:
                                                                if ((d * e / a - b * e**2 / a / c) / f) % 1 == 0:
                                                                    if ((-d * (-c - e) / a + e - (-b * (-c - e) / a - e) * e / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def body_tet_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            j = 0
            while a * j < c:
                b = a * j
                j += 1
                if ((2 * b + b**2 / a) / c) % 1 == 0:
                    if ((2 * a + 2 * b + b**2 / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            for l in range(f):
                                e = l
                                if ((-b + b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                    if ((2 * d + b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                        if ((-a - b + b * d / a - (2 * a + 2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                            if ((-c + c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                                if ((c * d / a - b * e / a) / f) % 1 ==0:
                                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def body_tet_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (2 * c / a) % 1 == 0:
            for j in range(c):
                b = j
                if (2 * b / a) % 1 == 0:
                    if ((2 * b + 2 * b**2 / a) / c) % 1 == 0:
                        if ((a + 2 * b + 2 * b**2 / a) / c) % 1 == 0:
                            for k in range(f):
                                d = k
                                for l in range(f):
                                    e = l
                                    if ((b + 2 * b * d / a - (a + 2 * b + 2 * b**2 / a) * e / c) / f) % 1 == 0:
                                        if ((c + 2 * c * d / a - 2 * e - 2 * b * e / a) / f) % 1 == 0:
                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def body_tet_5(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            if (f / c) % 1 == 0:
                for j in range(c):
                    b = j
                    if ((f + b * f / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            if ((-b - d) / c) % 1 == 0:
                                if ((-a + d + b * (-b - d) / a) / c) % 1 == 0:
                                    if ((b + d) / c) % 1 == 0:
                                        for l in range(f):
                                            e = l
                                            if ((-c - e) / a) % 1 == 0:
                                                if ((e + b * (c + e) / a) / c) % 1 == 0:
                                                    if (e / c) % 1 == 0:
                                                        if ((b + d - (b + d) * e / c) / f) % 1 == 0:
                                                            if ((-d - d * (-b - d) / a - (-a - b * (-b - d) / a + d) * e / c) / f) % 1 == 0:
                                                                if ((c - e**2 / c) / f) % 1 == 0:
                                                                    if ((-e - d * (-c - e) / a - e * (-b * (-c - e) / a + e) / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / a) % 1 == 0:
                j = 0
                while j * a < c:
                    b = a * j
                    j += 1
                    if ((-a + b**2 / a) / c) % 1 == 0:
                        if ((f + b * f / a) / c) % 1 == 0:
                            for k in range(f):
                                d = k
                                if ((-b - d) / a) % 1 == 0:
                                    if ((b - b * (-b - d) / a + d) / c) % 1 == 0:
                                        for l in range(f):
                                            e = l
                                            if (-c - e) % 1 == 0:
                                                if ((-b * (-c - e) / a + e) / c) % 1 == 0:
                                                    if ((b + d - (-b - d) * d / a - (b - b * (-b - d) / a + d) * e / c) / f) % 1 == 0:
                                                        if ((a + b + d + b * d / a - (-a + b**2 / a) * e / c) / f) % 1 == 0:
                                                            if ((c - d * (-c - e) / a - e * (-b * (-c - e) / a + e) / c) / f) % 1 == 0:
                                                                if ((c + c * d / a + e - b * e / a) / f) % 1 == 0:
                                                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / a) % 1 == 0:
                j = 0
                while a * j < c:
                    b = a * j
                    j += 1
                    if (b * f / a / c) % 1 == 0:
                        if ((2 * b + b**2 / a) / c) % 1 == 0:
                            k = 0
                            while a * k < f:
                                d = a * k
                                k += 1
                                if ((-b - d) / a) % 1 == 0:
                                    if (b * d / a / c) % 1 == 0:
                                        if ((2 * b - b * (-b - d) / a) / c) % 1 == 0:
                                            l = 0
                                            while a * l < f:
                                                e = l * a
                                                l += 1
                                                if ((-c - e) / a) % 1 == 0:
                                                    if (-b * (-c - e) / a / c) % 1 == 0:
                                                        if (b * e / a / c) % 1 == 0:
                                                            if ((2 * d - (-b - d) * d / a - (2 * b - b * (-b - d) / a) * e / c) / f) % 1 == 0:
                                                                if ((b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                                                    if ((2 * d + d**2 /a - b * d * e / a / c) / f) % 1 == 0:
                                                                        if ((-d * (-c - e) / a + b * (-c - e) * e / a / c) / f) % 1 == 0:
                                                                            if ((c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                                                                if ((2 * e + d * e / a - b * e**2 / a / c) / f) % 1 == 0:
                                                                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF
                                                                                                  
def face_ortho_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(c):
                b = j
                if (b * f / a / c) % 1 == 0:
                    k = 0
                    while a * k < f:
                        d = a * k
                        k += 1
                        if ((-b - d) / a) % 1 == 0:
                            if (b * (-b - d) / a / c) % 1 == 0:
                                if ((2 * b + b * d / a) / c) % 1 == 0:
                                    l = 0
                                    while l * a < f:
                                        e = a * l
                                        l += 1
                                        if ((-c - e) / a) % 1 == 0:
                                            if (b * (-c - e) / a / c) % 1 == 0:
                                                if (b * e / a / c) % 1 == 0:
                                                    if ((2 * b + 2 * d - (-b - d) * d / a + b * (-b - d) * e / a / c) / f) % 1 == 0:
                                                        if ((2 * d + d**2 / a - (2 * b + b * d / a) * e / c) / f) % 1 == 0:
                                                            if ((2 * c - d * (-c - e) / a + 2 * e + b * (-c - e) * e / a / c) / f) % 1 == 0:
                                                                if ((d * e / a - b * e**2 / a / c) / f) % 1 == 0:
                                                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / a) % 1 == 0:
                j = 0
                while a * j < c:
                    b = a * j
                    j += 1
                    if ((2 * b + b**2 / a) / c) % 1 == 0:
                        if ((2 * f + b * f / a) / c) % 1 == 0:
                            for k in range(f):
                                d = k
                                if ((b + d) / a) % 1 == 0:
                                    if ((2 * b - b * (-b - d) / a + 2 * d) / c) % 1 == 0:
                                        for l in range(f):
                                            e = l
                                            if ((c + e) / a) % 1 == 0:
                                                if ((-b * (-c - e) / a + 2 * e) / c) % 1 == 0:
                                                    if ((-(-b - d) * d / a - (2 * b - b * (-b - d) / a + 2 * d) * e / c) / f) % 1 == 0:
                                                        if ((2 * d + b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                                            if ((-d * (-c - e) / a - 2 * e - e * (-b * (-c - e) / a + 2 * e) / c) / f) % 1 == 0:
                                                                if ((c * d / a - b * e / a) / f) % 1 == 0:
                                                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_5(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / c) % 1 == 0:
            for j in range(c):
                b = j
                if ((-a + 2 * b) / c) % 1 == 0:
                    for k in range(f):
                        d = k
                        if ((-a - d) / c) % 1 == 0:
                            l = 0
                            while c * l < f:
                                e = c * l
                                l += 1
                                if ((2 * e + e**2 / c) / f) % 1 == 0:
                                    if ((2 * a + 2 * d - (-a - d) * e / c) / f) % 1 == 0:
                                        if ((2 * a + 2 * d - (-a + 2 * b) * e / c) / f) % 1 == 0:
                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_6(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / c) % 1 == 0:
            for j in range(c):
                b = j
                if ((a + 2 * b) / c) % 1 == 0:
                    k = 0
                    while c * k < f:
                        d = c * k
                        k += 1
                        l = 0
                        while c * l < f:
                            e = c * l
                            l += 1
                            if ((2 * d + d * e / c) / f) % 1 == 0:
                                if ((2 * d - (a + 2 * b) * e / c) / f) % 1 == 0:
                                    if ((2 * e + e**2 / c) / f) % 1 == 0:
                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
    return symHNF

def face_ortho_7(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (2 * f / a) % 1 == 0:
            for j in range(c):
                b = j
                if ((f + 2 * b * f / a) / c) % 1 == 0:
                    for k in range(f):
                        d = k 
                        if (2 * d / a) % 1 == 0:
                            if ((d + 2 * b * d / a) / c) % 1 == 0:
                                if ((a + 2 * b + d + 2 * b * d / a) / c) % 1 == 0:
                                    for l in range(f):
                                        e = l
                                        if (2 * e / a) % 1 == 0:
                                            if((e + 2 * b * e / a) / c) % 1 == 0:
                                                if ((2 * d + 2 * d**2 / a - (d + 2 * b * d / a) * e / c) / f) % 1 == 0:
                                                    if ((2 * d + 2 * d**2 / a - (a + 2 * b + d + 2 * b * d / a) * e / c) / f) % 1 == 0:
                                                        if ((2 * e + 2 * d * e / a - e * (e + 2 * b * e / a) / c) / f) % 1 == 0:
                                                            if ((2 * d * e / a - e * (e + 2 * b * e / a) / c) / f) % 1 == 0:
                                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_8(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        for j in range(c):
            b = j
            if ((2 * a + 2 * b) / c) % 1 == 0:
                for k in range(f):
                    d = k
                    if ((b + 2 * d) / f) % 1 == 0:
                        for l in range(f):
                            e = l
                            if ((-a - b - (2 * a + 2 * b) * e / c) / f) % 1 == 0:
                                if ((c + 2 * e) / f) % 1 == 0:
                                    if ((-c - 2 * e) / f) % 1 == 0:
                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_9(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (2 * c / a) % 1 == 0:
            for j in range(c):
                b = j
                if (2 * b / a) % 1 == 0:
                    if ((2 * b + 2 * b**2 / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            for l in range(f):
                                e = l
                                if ((b + 2 * b * d / a - (2 * b + 2 * b**2 / a) * e / c) / f) % 1 == 0:
                                    if ((a + b + 2 * d + 2 * b * d / a - (2 * b + 2 * b**2 / a) * e / c) / f) % 1 == 0:
                                        if ((c + 2 * c * d / a - 2 * e - 2 * b * e / a) / f) % 1 == 0:
                                            if ((c + 2 * c * d / a - 2 * b * e / a) / f) % 1 == 0:
                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def face_ortho_10(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        for j in range(c):
            b = j
            if (2 * b / c) % 1 == 0:
                for k in range(f):
                    d = k
                    if ((a + b + 2 * d) / f) % 1 == 0:
                        for l in range(f):
                            e = l
                            if ((-b - 2 * b * e / c) / f) % 1 == 0:
                                if ((c + 2 * e) / f) % 1 == 0:
                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def s_cubic_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            if (f / c) % 1 == 0:
                for j in range(c):
                    b = j
                    if (b * f / a / c) % 1 == 0:
                        k = 0
                        while a * k < f:
                            d = a * k
                            k += 1
                            if ((b - d) / c) % 1 == 0:
                                if ((-a - b * d / a) / c) % 1 == 0:
                                    l = 0
                                    while a * l < f:
                                        e = a * l
                                        l += 1
                                        if (e / c) % 1 == 0:
                                            if (b * e / a / c) % 1 == 0:
                                                if ((-b + d - (b - d) * e / c) / f) % 1 == 0:
                                                    if ((b - d**2 / a - (-a - b * d / a) * e / c) / f) % 1 == 0:
                                                        if ((-c + e**2 / c) / f) % 1 == 0:
                                                            if ((c - d * e / a + b * e**2 / a / c) / f) % 1 == 0:
                                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def s_cubic_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / c) % 1 == 0:
                j = 0
                while a * j < c:
                    b = a * j
                    j += 1
                    if ((2 * b + b**2 / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            if ((a + b + d) / c) % 1 == 0:
                                for l in range(f):
                                    e = l
                                    if ((b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                        if ((-a - b + d - (a + b + d) * e / c) / f) % 1 == 0:
                                            if ((c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                                if ((-c - e**2 / c) / f) % 1 == 0:
                                                    symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def s_cubic_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            if (f / c) % 1 == 0:
                for j in range(c):
                    b = j
                    if (b * f / a / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            if ((-b - d) / a) % 1 == 0:
                                if ((-a + b - b * (-b - d) / a) / c) % 1 == 0:
                                    if ((a + d) / c) % 1 == 0:
                                        for l in range(f):
                                            e = l
                                            if ((c + e) / a) % 1 == 0:
                                                if (-b * (-c - e) / a / c) % 1 == 0:
                                                    if (e / c) % 1 == 0:
                                                        if ((2 * a + 2 * d - (-b - d) * d / a - (-a + b + b * (-b - d) / a) * e / c ) / f) % 1 == 0:
                                                            if ((2 * a + 2 * b + 2 * d - (-a - d) * e / c) / f) % 1 == 0:
                                                                if ((-d * (-c - e) / a + e + b * (-c - e) * e / a / c) / f) % 1 == 0:
                                                                    if ((2 * c + 2 * e + e**2 / c) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def s_cubic_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / c) % 1 == 0:
                j = 0
                while a * j < c:
                    b = a * j
                    j += 1
                    if ((2 * b + b**2 / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            if ((a + 2 * b + d) / c) % 1 == 0:
                                for l in range(f):
                                    e = l
                                    if (e / c) % 1 == 0:
                                        if ((-2 * b + b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                            if ((-2 * a - 2 * b - (a + 2 * b + d) * e / c) / f) % 1 == 0:
                                                if ((-2 * c + c * d / a - 2 * e - b * e / a) / f) % 1 == 0:
                                                    if ((-2 * c - 2 * e - e**2 / c) / f) % 1 == 0:
                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def s_cubic_5(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (2 * c / a) % 1 == 0:
            if (f / a) % 1 == 0:
                for j in range(c):
                    b = j
                    if (2 * b / a) % 1 == 0:
                        if ((a + 2 * b + 2 * b**2 / a) / c) % 1 == 0:
                            if ((f + b * f / a) / c) % 1 == 0:
                                for k in range(f):
                                    d = k 
                                    if ((b + d) / a) % 1 == 0:
                                        if ((b - b * (-b - d) / a + d) / c) % 1 == 0:
                                            for k in range(f):
                                                e = k
                                                if ((-c - e) / a) % 1 == 0:
                                                    if ((-b * (-c - e) / a + e) / c) % 1 == 0:
                                                        if ((-b + d - (-b - d) * d / a - (b - b * (-b - d) / a + d) * e / c) / f) % 1 == 0:
                                                            if ((2 * d + 2 * b * d / a - (a + 2 * b + 2 * b**2 / a) * e / c) / f) % 1 == 0:
                                                                if ((-c - d * (-c - e) / a - e * (-b * ( -c - e) / a + e) / c) / f) % 1 == 0:
                                                                    if ((2 * c * d / a - 2 * b * e / a) / f) % 1 == 0:
                                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF
                                            

def trig_1(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            if (f / c) % 1 == 0:
                for j in range(c):
                    b = j
                    if (b * f / a / c) % 1 == 0:
                        k = 0
                        while a * k < f:
                            d = a * k
                            k += 1
                            if ((b - d) / c) % 1 == 0:
                                if ((-a + b * d / a) / c) % 1 == 0:
                                    l = 0
                                    while a * l < f:
                                        e = a * l 
                                        l += 1
                                        if (e / c) % 1 == 0:
                                            if (b * e / a / c) % 1 == 0:
                                                if ((-b + d - (b - d) * e / c) / f) % 1 == 0:
                                                    if ((-b + d**2 / a - (-a + b * d / a) * e / c) / f) % 1 == 0:
                                                        if ((-c + e**2 / c) / f) % 1 == 0:
                                                            if ((-c + d * e / a - b * e**2 / a / c) / f) % 1 == 0:
                                                                symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def trig_2(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (c / a) % 1 == 0:
            if (f / c) % 1 == 0:
                j = 0
                while a * j < c:
                    b = a * j
                    j += 1
                    if ((2 * b + b**2 / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            if ((a + 2 * b + b**2 / a - d) / c) % 1 == 0:
                                for l in range(f):
                                    e = l
                                    if ((b * c / a - e) / c) % 1 == 0:
                                        if ((b * d / a - (2 * b + b**2 / a) * e / c) / f) % 1 == 0:
                                            if ((-a + d + b * d / a - (a + 2 * b + b**2 / a - d) * e / c) / f) % 1 == 0:
                                                if (( c * d / a - 2 * e - b * e * a) / f) % 1 == 0:
                                                    if ((c * d - e - (b * c / a - e) * e / c) / f) % 1 == 0:
                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
                    
    return symHNF

def trig_3(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(c):
                b = j
                if ((a + 2 * b) / c) % 1 == 0:
                    if ((-f - b * f / a) / c) % 1 == 0:
                        for k in range(f):
                            d = k
                            if ((-b + d) / a) % 1 == 0:
                                if ((b - d - b * (-b + d) / a) / c) % 1 == 0:
                                    for l in range(f):
                                        e = l
                                        if ((-e - b * (-c + e) / a) / c) % 1 == 0:
                                            if ((-c + e) / a) % 1 == 0:
                                                if ((-b + d - d*(-b + d) / a - (b - d - b * (-b + d) / a) * e / c) / f) % 1 == 0:
                                                    if ((2 * d - (a + 2 * b) * e / c) / f) % 1 == 0:
                                                        if ((-c - d * (-c + e) / a - e * (-e - b * ( -c + e) / a) / c) / f) % 1 == 0:
                                                            symHNF.append([[a,0,0], [b,c,0], [d,e,f]])

    return symHNF

def trig_4(size):

    """Generates symmetry preserving HNF's of a given size
       for a base centered monoclinic basis

    Args:
        size (int): The determinate of the HNF matricies

    Returns:
        list (int): The generated HNF matricies
    """

    symHNF = []
    diags = find_HNF_diagonal(size)
    for i in diags:
        a = i[0]
        c = i[1]
        f = i[2]
        if (f / a) % 1 == 0:
            for j in range(c):
                b = j
                if (2 * b / c) % 1 == 0:
                    if ((f + b * f / a) / c) % 1 == 0:
                        k = 0
                        while a * k < f:
                            d = a * k
                            k += 1
                            if ((-a + b + d + b * d / a) / c) % 1 == 0:
                                l = 0
                                while a * l < f:
                                    e = a * l
                                    l += 1
                                    if ((e + b * e / a) / c) % 1 == 0:
                                        if ((-b - 2 * b * e / c) / f) % 1 == 0:
                                            if ((-b - d + d**2 / a - (-a + b + d + b * d / a) * e / c) / f) % 1 == 0:
                                                if ((-c - 2 * e) / f) % 1 == 0:
                                                    if ((-c - 2 * e + d * e / a - e * ( e + b * e / a) / c) / f) % 1 == 0:
                                                        symHNF.append([[a,0,0], [b,c,0], [d,e,f]])
                                                        
    return symHNF

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

    return list
