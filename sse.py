class stats:
	def __init__(self, X, y, model):
		self.data = X
		self.target = y
		self.model = model
		## degrees of freedom population dep. variable variance
		self._dft = X.shape[0] - 1   
		## degrees of freedom population error variance
		self._dfe = X.shape[0] - X.shape[1] - 1 

	def sse(self):
        '''returns sum of squared errors (model vs actual)'''
        squared_errors = (self.target - self.model.predict(self.data)) ** 2
        return np.sum(squared_errors)
		
	def sst(self):
        '''returns total sum of squared errors (actual vs avg(actual))'''
        avg_y = np.mean(self.target)
        squared_errors = (self.target - avg_y) ** 2
        return np.sum(squared_errors)
		
	def r_squared(self):
        '''returns calculated value of r^2'''
        return 1 - self.sse()/self.sst()
		
	def adj_r_squared(self):
        '''returns calculated value of adjusted r^2'''
        return 1 - (self.sse()/self._dfe) / (self.sst()/self._dft)