from substructurepowerspectrum import Grid, Subpk
from pylab import loglog,show
from sys import exit


filename1 = 'testgrid1.txt'
obj = Grid(filename1,9,1)
obj2 = Subpk(Grid.getgrid(obj),Grid.getR(obj),kdim=21)
[k,pk,n] = Subpk.gridtopk(obj2)
loglog(k,pk)
show()

filename2 = 'testgrid2.txt'
obj = Grid(filename2)
obj2 = Subpk(Grid.getgrid(obj),Grid.getR(obj))
[k,pk,n] = Subpk.gridtopk(obj2)
loglog(k,pk)
show()


obj = Grid()
obj2 = Subpk(Grid.getgrid(obj),Grid.getR(obj))
[k,pk,n] = Subpk.gridtopk(obj2)
loglog(k,pk)
show()

