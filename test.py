from substructurepowerspectrum import Grid, subpk
from pylab import loglog,show


filename1 = 'testgrid1.txt'
obj = Grid(filename1,9,1)
obj2 = subpk(Grid.getgrid(obj),Grid.getR(obj))
[k,pk,n] = subpk.gridtopk(obj2)
loglog(k,pk)
show()


filename2 = 'testgrid2.txt'
obj = Grid(filename2)
obj2 = subpk(Grid.getgrid(obj),Grid.getR(obj))
[k,pk,n] = subpk.gridtopk(obj2)
loglog(k,pk)
show()


obj = Grid()
obj2 = subpk(Grid.getgrid(obj),Grid.getR(obj))
[k,pk,n] = subpk.gridtopk(obj2)
loglog(k,pk)
show()