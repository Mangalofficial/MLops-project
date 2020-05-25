programfile = open('/myenv/testing.py','r')	  # Opening python file 
code = programfile.read()				              # Reading the code

if 'keras' or 'tensorflow' in code:						# Keras or Tensorflow libraries are must for Deep Learning program
	if 'Conv2D' in code:				                # CNN codes must have conv2D library
		print('CNN model')
	else:
		print('NO CNN model')
else:
	print('Not a CNN program')
