from numpy import hamming, outer, log10, absolute,sqrt
from numpy import random, linspace, zeros, pi
from numpy import genfromtxt,transpose,reshape,shape
from sys import exit

__author__ = ("Irshad Mohammed <irshad@physik.uzh.ch>")

#==========================================================
class Grid(object):
	def __init__(self,name=None,head=0,foot=0):
		if name==None:
			print "Please provide name of a file or grid"
			exit()
		else:
			self.name = name

		if type(self.name) is str:
			self.data = genfromtxt(self.name,\
						skip_header=head,skip_footer=foot)
			if len(self.data[0])==3:
				self.dim = int(sqrt(len(self.data)))
				self.R = self.data[0:self.dim,0]
				if self.R[0] == self.R[-1]:
					self.R = self.data[0:dim,1]
				self.grid = reshape(self.data[:,2],\
								(self.dim,self.dim))

			elif len(self.data) == len(transpose(self.data)):
				self.grid = self.data
				self.dim = len(self.grid)
				self.R = linspace(-100,100,self.dim)

			else:
				print "Please provide file with dimension:"
				print "N X 3 or N X N"
				print "current grid shape is:",shape(self.data)
				exit()
		else:
			print "Please provide the name of a file"
			exit()

	def getgrid(self):
		return self.grid

	def getR(self):
		return self.R


#==========================================================
class subpk(object):

	#----------------------------------------------------

	def __init__(self,grid=None,R=None,kdim=None):
		if grid==None:
			self.grid = random.random((100,100))
			print "Grid is random of size 100 X 100"
		else:
			self.grid = grid
		if R==None:
			self.R = linspace(-100,100,len(self.grid))
		else:
			self.R = R

		if kdim==None:
			self.kdim = 11
		else:
			self.kdim = kdim
	#----------------------------------------------------
	
	def fft(self,gg):
		from scipy.fftpack import fftshift,ifftshift,fft2
		gg = fftshift(gg)
		gg_fft = fft2(gg)
		return ifftshift(gg_fft)

	#----------------------------------------------------

	def gridtopk(self):
		
		grid = self.grid
		R = self.R
		kdim = self.kdim

		dim = len(R)
		boxsize = max(R) - min(R)

		smooth = hamming(len(grid))
		grid = grid*outer(smooth,smooth)

		fftgrid = self.fft(grid)

		delta_R = boxsize/dim 
		delta_k = 2.0 * pi / dim / delta_R
		K = linspace(-dim/2*delta_k,(dim-1)/2*delta_k,dim)

		#----------------------------------------------------
		kbins = linspace(log10(K[dim/2+1]),log10(K[-1]),kdim)
		kbins = 10**kbins

		kk = zeros((kdim-1))
		Pk = zeros((kdim-1))
		modes = zeros((kdim-1))
		#----------------------------------------------------

		for i in range(dim):
			for j in range(dim):
			  	distk = (K[i]**2 + K[j]**2)**0.5
				ddk = absolute(fftgrid[i,j])**2
		
				for k in range(kdim-1):
			        	if distk>kbins[k] and distk<kbins[k+1]:
			        		Pk[k] += ddk
			        		modes[k] += 1

		for i in range(kdim-1):
			kk[i] = (kbins[i+1]+kbins[i])/2
			Pk[i] = Pk[i]/modes[i]

		return [kk,Pk,modes]
	
#==========================================================

if __name__=='__main__':

	filename = '/Users/irshad/github/HubbleFrontierField/paper1_substructures/generateplots/grids_all/A2744_HFFv1.gnuplot'
	obj = Grid(filename,9,1)
	obj2 = subpk(Grid.getgrid(obj),Grid.getR(obj))
	[k,pk,n] = subpk.gridtopk(obj2)
#	from pylab import loglog,show
#	loglog(k,pk)
#	show()
