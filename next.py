s = 'abc'
it = iter(s)
it
next(it)
next(it)
next(it)
next(it) #should throw traceback
StopIteration
