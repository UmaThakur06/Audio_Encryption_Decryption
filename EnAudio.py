import scipy.io.wavfile
import numpy
import time
import matplotlib.pyplot as plt
import sys

start = time.time()
#time time() Method, The method time() returns the time as a floating point number expressed in seconds since the epoch, in UTC.

#Encryption

fs, data = scipy.io.wavfile.read('8bitaudio.wav')
#scipy.io.wavfile.read(filename, mmap=False)
#Return the sample rate (in samples/sec) and data from a WAV file
print(data)
print(fs)
print(type(data))
#To get the type of a variable in Python, you can use the built-in type() function
dataarray = data
print(type(dataarray))
a, b = dataarray.shape
tup = (a, b)
data = data.astype(numpy.int16)
#astype() method returns a new DataFrame where the data types has been changed to the specified type.
#data = numpy.asarray(data, dtype=numpy.int16)
#print(data.flags)
data.setflags(write=1)
#print(data.flags)
print((a,b))

Time= numpy.linspace(0, len(data)/fs, num=len(data))
plt.figure(1)
plt.title('Signal Wave')
plt.plot(Time, data) 
plt.show()
for i in range(0, tup[0]):
	for j in range(0, tup[1]):
		x = data[i][j] 
		x = ((pow(x,3)) % 25777)
		data[i][j] = x

print(data)
data = data.astype(numpy.int16)
scipy.io.wavfile.write('EN.wav', fs, data)

Time= numpy.linspace(0, len(data)/fs, num=len(data))
plt.figure(2)
plt.title('Encrypted Signal Wave')
plt.plot(Time, data) 
plt.show()

end = time.time()
ElspTime = (end-start)
#print progress bar
print('\n Total time taken from your life: ', +ElspTime, 'sec')


